# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from core import BlogManager

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.insertUser)
        self.ui.pushButton_2.clicked.connect(self.deleteUser)
        self.ui.pushButton_3.clicked.connect(self.insertPage)
        self.ui.pushButton_4.clicked.connect(self.deletePage)
        self.ui.pushButton_5.clicked.connect(self.getUserCom)
        self.ui.pushButton_6.clicked.connect(self.getMaPlate)
        self.ui.pushButton_7.clicked.connect(self.getDocCount)
        self.ui.pushButton_8.clicked.connect(self.getUserDoC)
        self.blogDB = BlogManager()

    def printData(self, name, data):
        self.ui.textBrowser.append("*"*30)
        self.ui.textBrowser.append(name)
        self.ui.textBrowser.append("*"*30)
        for i in data:
            self.ui.textBrowser.append(str(i))
        self.ui.textBrowser.append("\n")
    
    def getUserCom(self):
        status, info = self.blogDB.getUserCom()
        if status:
            self.ui.textBrowser.clear()
            self.printData(info[0],info[1])
        else:
            self.ui.textBrowser.append("[GET UserCom FAILED] {}".format(info))
    
    def getUserDoC(self):
        value, ok = QInputDialog.getMultiLineText(self, "查看某位用户某种情绪的评论", "请按行分别输入信息\n\n用户编号\n情绪", "22\nHATE")
        if ok:
            value = value.split("\n")
            status, info = self.blogDB.getUserDoC(value[0],value[1])
            if status:
                self.ui.textBrowser.clear()
                self.printData(info[0],info[1])
            else:
                self.ui.textBrowser.append("[GET UserCom FAILED] {}".format(info))
    
    def getDocCount(self):
        value, ok = QInputDialog.getMultiLineText(self, "查看某篇文章的评论", "请按行分别输入信息\n\n文章编号", "7")
        if ok:
            value = value.split("\n")
            status, info = self.blogDB.getDocCount(value[0])
            if status:
                self.ui.textBrowser.clear()
                self.printData(info[0],info[1])
            else:
                self.ui.textBrowser.append("[GET DocCount FAILED] {}".format(info))
    
    def getMaPlate(self):
        status, info = self.blogDB.getPlatePerInfo()
        if status:
            self.ui.textBrowser.clear()
            self.printData(info[0],info[1])
        else:
            self.ui.textBrowser.append("[GET UserCom FAILED] {}".format(info))    
    
    def insertUser(self):
        value, ok = QInputDialog.getMultiLineText(self, "新增用户", "请按行分别输入信息\n\n用户昵称\n联系方式", "xingqwq\n17689776180")
        if ok:
            value = value.split("\n")
            status, info = self.blogDB.insertUser(value[0],value[1])
            if status:
                self.ui.textBrowser.append("[Insert User SUCCESS] {} {}".format(value[0],value[1]))
            else:
                self.ui.textBrowser.append("[Insert User FAILED] {}".format(info))

    def deleteUser(self):
        value, ok = QInputDialog.getMultiLineText(self, "删除用户", "请按行分别输入信息\n\n用户编号", "22")
        if ok:
            value = value.split("\n")
            if value[0].isdigit:
                status, info = self.blogDB.deleteUser(value[0])
                if status:
                    self.ui.textBrowser.append("[DELETE User SUCCESS] {}".format(info))
                else:
                    self.ui.textBrowser.append("[DELETE User FAILED] {}".format(info))

    def insertPage(self):
        value, ok = QInputDialog.getMultiLineText(self,
        "新增文章", "请按行分别输入信息\n\n文章昵称\n存储地址\n参与话题（多个话题用,分割）\n板块编号\n创作组编号\n时间\n\n",
        "DBMS实验二要验收啦！\n./xingqwq\n6,4\n100\n3\n2023-03-27\n")
        if ok:
            value = value.split("\n")
            name = value[0]
            addr = value[1]
            topic = value[2].split(",")
            plateID = value[3]
            creationID = value[4]
            date = value[5]
            status, info = self.blogDB.insertPage(name, addr, topic, plateID, creationID, date)
            if status:
                self.ui.textBrowser.append("[Insert User SUCCESS] 文章昵称：{} 存储地址：{}".format(name, addr))
            else:
                self.ui.textBrowser.append("[Insert User FAILED] {}".format(info))
    
    def deletePage(self):
        value, ok = QInputDialog.getMultiLineText(self,
        "删除文章", "请按行分别输入信息\n文章编号\n",
        "7")
        if ok:
            value = value.split("\n")
            docID = value[0]
            status, info = self.blogDB.deletePage(docID)
            if status:
                self.ui.textBrowser.append("[DELETE User SUCCESS] {}".format(info))
            else:
                self.ui.textBrowser.append("[DELETE User FAILED] {}".format(info))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
