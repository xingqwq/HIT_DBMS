import pymysql

class mysqlConnector:
    def __init__(self, addr = "localhost", port = 3306):
        self. db = pymysql.connect(
            host="localhost",
            port=port,
            user='root',
            password='111',
            charset='utf8mb4'
        )

    def newCur(self):
        new = self.db.cursor()
        new.execute('use lab1')
        return new

    def getData(self, cur):
        data = cur.fetchall()
        return data

class BlogManager:
    def __init__(self):
        self.dbms = mysqlConnector()
    
    def printSQL(self, sql):
        print("当前执行的SQL语句为：{}".format(sql))
    
    def printData(self, name, data):
        print("*"*30)
        print(name)
        print("*"*30)
        for i in data:
            print(i)
        print("\n")
    
    def showDatabase(self, table):
        try:
            cur = self.dbms.newCur()
            cur.execute('select * from '+table)
            data = self.dbms.getData(cur)
            self.printData("活动数据",data)
        except Exception as e:
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def insertUser(self, name, phoneNum):
        if len(name) >= 10:
            print("error name")
            return False
        
        if phoneNum.isdigit() == False:
            print("error phoneNum")
            return False
        
        try:
            sql = "INSERT INTO `user` (`名称`, `联系方式`) VALUES ('{}', '{}')".format(name, phoneNum)
            self.printSQL(sql)
            cur = self.dbms.newCur()
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
        
    def insertCreation(self, plateID, name, text):
        try:
            sql = "INSERT INTO `creation` (`板块编号`, `名称`, `简介`) VALUES ('{}', '{}','{}')".format(plateID, name, text)
            self.printSQL(sql)
            cur = self.dbms.newCur()
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前板块编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def insertPlate(self, name, text):
        try:
            sql = "INSERT INTO `plate` (`名称`, `简介`) VALUES ('{}', '{}')".format(name, text)
            self.printSQL(sql)
            cur = self.dbms.newCur()
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def insertCreationPer(self, ID, name, phoneNum, creationID, sDate, eData):
        if phoneNum.isdigit() == False:
            print("error phoneNum")
            return False
        try:
            cur = self.dbms.newCur()
            # 插入负责人
            sql = "INSERT INTO `creation_per` (`身份证号`, `姓名`, `联系方式`) VALUES ('{}', '{}','{}')".format(ID, name, phoneNum)
            self.printSQL(sql)
            cur.execute(sql)
            # 构建联系
            sql = "INSERT INTO `ma_creation` (`身份证号t`, `创作组编号t`, `开始时间`, `结束时间`) VALUES ('{}', '{}','{}','{}')".format(ID, creationID, sDate, eData)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前创作组/负责人编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def insertPlatePer(self, ID, name, phoneNum):
        if phoneNum.isdigit() == False:
            print("error phoneNum")
            return False
        try:
            cur = self.dbms.newCur()
            sql = "INSERT INTO `plate_per` (`身份证号`, `姓名`, `联系方式`) VALUES ('{}', '{}','{}')".format(ID, name, phoneNum)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def insertPlateMa(self, ID, plateID, sDate, eDate):
        try:
            cur = self.dbms.newCur()
            sql = "INSERT INTO `ma_plate` (`身份证号t`, `板块编号t`, `开始时间`, `结束时间`) VALUES ('{}', '{}','{}','{}')".format(ID, plateID, sDate, eDate)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前板块/负责人编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
        
    def joinActi(self, userID, actiID, date):
        try:
            cur = self.dbms.newCur()
            sql = "INSERT INTO `join_acti` (`用户编号t`, `活动编号t`, `参与时间`) VALUES ('{}', '{}','{}')".format(userID, actiID, date)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前用户/活动编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def insertPage(self, name, doc, topicList, plateID, creationID, date):
        try:
            # 新建文章
            sql = "INSERT INTO `doc` (`名称`, `存储地址`) VALUES ('{}', '{}');".format(name, doc)
            self.printSQL(sql)
            cur = self.dbms.newCur()
            cur.execute(sql)
            cur.execute("SELECT LAST_INSERT_ID();")
            docID = cur.fetchone()[0]
            # 添加话题
            for i in topicList:
                sql = "INSERT INTO `join_topic` (`文章编号t`, `话题编号t`, `发布时间`) VALUES ('{}', '{}','{}')".format(docID, i, date)
                self.printSQL(sql)
                cur.execute(sql)
            # 创作组发布文章联系
            sql = "INSERT INTO `pub_doc` (`板块编号t`, `创作组编号t`, `文章编号t`, `发表时间`) VALUES ('{}', '{}', '{}', '{}');".format(plateID, creationID, docID, date)
            cur.execute(sql)
            self.printSQL(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前文章/话题编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
            
    def comDoc(self, userID, docID, date, like):
        try:
            cur = self.dbms.newCur()
            sql = "INSERT INTO `com_doc` (`用户编号t`, `文章编号t`, `评论时间`, `情绪`) VALUES ('{}', '{}','{}','{}')".format(userID, docID, date, like)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
        except Exception as e:
            print("执行失败")
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前用户/文章编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
            
    def deleteUser(self, userID):
        try:
            cur = self.dbms.newCur()
            sql = "delete from user where 用户编号 = '{}'".format(userID)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
            print("[成功出发删除前触发器]已同步删除用户参与活动记录和用户评论记录")
        except Exception as e:
            print("执行失败",e)
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前文章/话题编号不存在")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def deletePage(self, docID):
        try:
            cur = self.dbms.newCur()
            sql = "delete from doc where 文章编号 = '{}'".format(docID)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功\n")
            print("[成功出发删除前触发器]已同步删除其他表项中的该文章记录")
        except Exception as e:
            print("执行失败",e)
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 无法删除")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def getPlatePerInfo(self):
        try:
            cur = self.dbms.newCur()
            sql = "select * from plate_info"
            self.printSQL(sql)
            cur.execute(sql)
            self.printData("板块与板块负责人联系表",cur.fetchall())
            print("执行成功\n")
        except Exception as e:
            print("执行失败",e)
        finally:
            cur.close()
    
    def getUserCom(self):
        try:
            cur = self.dbms.newCur()
            sql = "select * from user_com"
            self.printSQL(sql)
            cur.execute(sql)
            self.printData("板块与板块负责人联系表",cur.fetchall())
            print("执行成功\n")
        except Exception as e:
            print("执行失败",e)
        finally:
            cur.close()
    
    def getUserDoC(self, userID, status):
        try:
            cur = self.dbms.newCur()
            sql = "select in_user.文章名, in_user.评论时间 from (select * from user_com where 情绪 = '{}') as in_user where 用户编号 = '{}'".format(status,userID)
            self.printSQL(sql)
            cur.execute(sql)
            self.printData("用户编号为 {} {}的文章列表".format(userID, status),cur.fetchall())
            print("执行成功\n")
        except Exception as e:
            print("执行失败",e)
        finally:
            cur.close()
    
    def getDocCount(self, docID):
        try:
            cur = self.dbms.newCur()
            sql = "select in_user.文章名, in_user.情绪, count(*) from (select * from user_com where 文章编号 = '{}') as in_user group by in_user.情绪".format(docID)
            self.printSQL(sql)
            cur.execute(sql)
            self.printData("文章编号为 {} 的情绪分布".format(docID),cur.fetchall())
            print("执行成功\n")
        except Exception as e:
            print("执行失败",e)
        finally:
            cur.close()

    
    
blogDB = BlogManager()
# blogDB.showDatabase("acti")
# blogDB.insertPlate("微积分", "微积分（Calculus），数学概念，是高等数学中研究函数的微分（Differentiation）、积分（Integration）以及有关概念和应用的数学分支。它是数学的一个基础学科，内容主要包括极限、微分学、积分学及其应用。")
# blogDB.insertCreationPer("450009199812134567", "周一宁", "12793456523", "8", "2020-03-20", "2035-03-19")
# blogDB.insertUser("玉院士","19872553809")
# blogDB.insertCreation("8","DBMS","数据库管理系统")            
# blogDB.insertPage("ChatGPT4可以联网计算数学","./xingqwq",[6,4], 100, 3, "2023-03-05")
# blogDB.insertPlatePer("238880200212180387", "王笑笑", "12793456523")
# blogDB.insertPlateMa("238880200212180387", "3","2020-03-20", "2035-03-19")
# blogDB.joinActi("22","3","2022-06-19")
# blogDB.comDoc("22", "4", "2023-03-27", "SUB")
# blogDB.comDoc("22", "1", "2023-03-27", "NO LIKE")
# blogDB.comDoc("22", "2", "2023-03-27", "HATE")
# blogDB.comDoc("5", "4", "2023-03-27", "SUB")
# blogDB.comDoc("1", "3", "2023-03-27", "HATE")
# blogDB.comDoc("4", "3", "2023-03-22", "LIKE")
# blogDB.comDoc("12", "3", "2023-03-29", "HATE")
# blogDB.joinTopic("4", "6","2022-06-19") 
# blogDB.deleteUser("6")

# blogDB.getPlatePerInfo()
# blogDB.getUserCom()
blogDB.getUserDoC(3, "HATE")
blogDB.getDocCount(3)
# blogDB.deletePage(2)
# blogDB.getUserDoC(22, "HATE")
