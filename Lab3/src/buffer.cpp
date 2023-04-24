/**
 * @file buffer.cpp
 * @author 7203610316_符兴
 * @brief
 * @version 0.1
 * @date 2023-04-23
 *
 * @copyright Copyright (c) 2023
 *
 */

#include <memory>
#include <iostream>
#include "buffer.h"
#include "exceptions/buffer_exceeded_exception.h"
#include "exceptions/page_not_pinned_exception.h"
#include "exceptions/page_pinned_exception.h"
#include "exceptions/bad_buffer_exception.h"
#include "exceptions/hash_not_found_exception.h"

namespace badgerdb
{

    BufMgr::BufMgr(std::uint32_t bufs)
        : numBufs(bufs)
    {
        bufDescTable = new BufDesc[bufs];

        for (FrameId i = 0; i < bufs; i++)
        {
            bufDescTable[i].frameNo = i;
            bufDescTable[i].valid = false;
        }

        bufPool = new Page[bufs];

        int htsize = ((((int)(bufs * 1.2)) * 2) / 2) + 1;
        hashTable = new BufHashTbl(htsize); // allocate the buffer hash table

        clockHand = bufs - 1;
    }

    /**
     * @brief Destroy the Buf Mgr:: Buf Mgr object（需要对脏页进行处理。）
     *
     */
    BufMgr::~BufMgr()
    {
        for (FrameId i = 0; i < numBufs; i++)
        {
            if (bufDescTable[i].dirty)
            {
                bufDescTable[i].file->writePage(bufPool[i]);
            }
        }
        delete[] bufDescTable;
        delete[] bufPool;
        delete hashTable;
    }

    /**
     * @brief 每个时间节点，移进时钟指针
     *
     */
    void BufMgr::advanceClock()
    {
        clockHand = (clockHand + 1) % numBufs;
    }

    /**
     * @brief 使用时钟算法分配一个空闲帧（如果是脏页需要写回磁盘）
     *
     * @param frame
     */
    void BufMgr::allocBuf(FrameId &frame)
    {
        int cnt = 0;
        while (cnt <= numBufs)
        {
            advanceClock();
            if (!bufDescTable[clockHand].valid)
            {
                frame = clockHand;
                return;
            }
            else if (bufDescTable[clockHand].refbit)
            {
                bufDescTable[clockHand].refbit = false;
            }
            else if (bufDescTable[clockHand].pinCnt != 0)
            {
                cnt += 1;
            }
            else if (bufDescTable[clockHand].pinCnt == 0 && bufDescTable[clockHand].dirty == true)
            {
                bufDescTable[clockHand].file->writePage(bufPool[clockHand]);
                bufDescTable[clockHand].dirty = false;
                frame = clockHand;
                hashTable->remove(bufDescTable[clockHand].file, bufDescTable[clockHand].pageNo);
                bufDescTable[clockHand].Clear();
                return;
            }
            else if (bufDescTable[clockHand].pinCnt == 0 && bufDescTable[clockHand].dirty == false)
            {
                frame = clockHand;
                hashTable->remove(bufDescTable[clockHand].file, bufDescTable[clockHand].pageNo);
                bufDescTable[clockHand].Clear();
                return;
            }
        }
        throw BufferExceededException();
    }

    /**
     * @brief 读取数据，如果改页在缓冲池中直接返回Page指针；如果不存在，需要调用allocBuf()获取新的帧用于读入页数据。
     *
     * @param file
     * @param pageNo
     * @param page
     */
    void BufMgr::readPage(File *file, const PageId pageNo, Page *&page)
    {
        FrameId id;
        try
        {
            hashTable->lookup(file, pageNo, id);
            bufDescTable[id].refbit = true;
            bufDescTable[id].pinCnt += 1;
        }
        catch (HashNotFoundException e)
        {
            allocBuf(id);
            bufPool[id] = file->readPage(pageNo);
            hashTable->insert(file, pageNo, id);
            bufDescTable[id].Set(file, pageNo);
        }
        page = bufPool + id;
    }

    /**
     * @brief 减少特定帧的PinCnt；如果dirty==true，则设置dirty位；如果引脚计数已经为0，则扔出异常；
     *        如果在哈希表查找中没有找到page，则什么都不做；
     *
     * @param file
     * @param pageNo
     * @param dirty
     */
    void BufMgr::unPinPage(File *file, const PageId pageNo, const bool dirty)
    {
        FrameId id;
        try
        {
            hashTable->lookup(file, pageNo, id);
            if (bufDescTable[id].pinCnt == 0)
            {
                throw PageNotPinnedException(file->filename(), pageNo, id);
            }
            bufDescTable[id].pinCnt -= 1;
            if (dirty == true)
            {
                bufDescTable[id].dirty = true;
            }
        }
        catch (HashNotFoundException e)
        {
            std::cerr << e.what() << '\n';
        }
    }

    /**
     * @brief 在哈希表中查找属于该文件的页；对于遇到的每个文件，如果页面是脏的，则需要将页面写回，
     *        然后将脏位设置为false；从哈希表中删除该页面；调用BufDesc的clear()方法。如果某些
     *        页面被Pin则抛出异常；如果遇到无效页，则抛出BadBufferException异常。
     * @param file
     */
    void BufMgr::flushFile(const File *file)
    {
        for (uint32_t i = 0; i < numBufs; i++)
        {
            if (bufDescTable[i].file == file)
            {
                if (!bufDescTable[i].valid)
                {
                    throw BadBufferException(i, bufDescTable[i].dirty, bufDescTable[i].valid, bufDescTable[i].refbit);
                }
                if (bufDescTable[i].pinCnt > 0)
                {
                    throw PagePinnedException(file->filename(), bufDescTable[i].pageNo, i);
                }
                if (bufDescTable[i].dirty)
                {
                    bufDescTable[i].file->writePage(bufPool[i]);
                }
                bufDescTable[i].dirty = false;
                hashTable->remove(file, bufDescTable[i].pageNo);
                bufDescTable[i].Clear();
            }
        }
    }

    /**
     * @brief 为指定页面分配一个空页；然后获取缓冲池帧，并在哈希表中插入条目，并通过page参数向调用者返回指向该页分配的缓冲帧指针。
     *
     * @param file
     * @param pageNo
     * @param page
     */
    void BufMgr::allocPage(File *file, PageId &pageNo, Page *&page)
    {
        FrameId id;
        allocBuf(id);
        bufPool[id] = file->allocatePage();
        pageNo = bufPool[id].page_number();
        hashTable->insert(file, pageNo, id);
        bufDescTable[id].Set(file, pageNo);
        page = &bufPool[id];
    }

    /**
     * @brief 从文件中删除特定页面；在删除之前，如果在缓冲池中分配了一个帧则该帧需要被释放，并相应地从散列表中删除条目。
     *
     * @param file
     * @param PageNo
     */
    void BufMgr::disposePage(File *file, const PageId PageNo)
    {
        FrameId id;
        try
        {
            hashTable->lookup(file, PageNo, id);
            hashTable->remove(file, PageNo);
            file->deletePage(PageNo);
            bufDescTable[id].Clear();
        }
        catch (HashNotFoundException e)
        {
        }
        file->deletePage(PageNo);
    }

    void BufMgr::printSelf(void)
    {
        BufDesc *tmpbuf;
        int validFrames = 0;

        for (std::uint32_t i = 0; i < numBufs; i++)
        {
            tmpbuf = &(bufDescTable[i]);
            std::cout << "FrameNo:" << i << " ";
            tmpbuf->Print();

            if (tmpbuf->valid == true)
                validFrames++;
        }

        std::cout << "Total Number of Valid Frames:" << validFrames << "\n";
    }

}
