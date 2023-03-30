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
            print("执行成功")
        except Exception as e:
            print("执行失败")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def insertPage(self, name, doc):
        try:
            sql = "INSERT INTO `doc` (`名称`, `存储地址`) VALUES ('{}', '{}')".format(name, doc)
            self.printSQL(sql)
            cur = self.dbms.newCur()
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功")
        except Exception as e:
            print("执行失败")
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
            print("执行成功")
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
            print("执行成功")
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
            print("执行成功")
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
            print("执行成功")
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
            print("执行成功")
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
            print("执行成功")
        except Exception as e:
            print("执行失败")
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前用户/活动编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
    def joinTopic(self, docID, topicID, date):
        try:
            cur = self.dbms.newCur()
            sql = "INSERT INTO `join_topic` (`文章编号t`, `话题编号t`, `发布时间`) VALUES ('{}', '{}','{}')".format(docID, topicID, date)
            self.printSQL(sql)
            cur.execute(sql)
            self.dbms.db.commit()
            print("执行成功")
        except Exception as e:
            print("执行失败",e)
            if "a foreign key constraint fails" in repr(e):
                print("[外键错误] 当前文章/话题编号不存在")
            if "Duplicate entry" in repr(e):
                print("[唯一性约束] 当前新加入元组存在重复")
            self.dbms.db.rollback()
        finally:
            cur.close()
    
blogDB = BlogManager()
blogDB.showDatabase("acti")
# blogDB.insertPlate("微积分", "微积分（Calculus），数学概念，是高等数学中研究函数的微分（Differentiation）、积分（Integration）以及有关概念和应用的数学分支。它是数学的一个基础学科，内容主要包括极限、微分学、积分学及其应用。")
# blogDB.insertCreationPer("450009199812134567", "周一宁", "12793456523", "8", "2020-03-20", "2035-03-19")
# blogDB.insertUser("xingqwq","19872553809")
# blogDB.insertCreation("8","DBMS","数据库管理系统")            
# blogDB.insertPage("ChatGPT4最新综述","./xingqwq")
# blogDB.insertPlatePer("238880200212180387", "王笑笑", "12793456523")
# blogDB.insertPlateMa("238880200212180387", "3","2020-03-20", "2035-03-19")
blogDB.joinActi("6","3","2022-06-19")
blogDB.joinTopic("4", "6","2022-06-19") 