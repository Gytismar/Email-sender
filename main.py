# from PyQt5.QtWidgets import (QApplication,QWidget,QHBoxLayout,QPushButton,QGridLayout,QLineEdit, QLabel,QVBoxLayout, QTabWidget, QPlainTextEdit, QTableWidget, QFileDialog, QTableWidgetItem)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QDir
from PyQt5 import QtGui, Qt 
import sys
import os
import csv
import json
import Script

f = open('config.json')
data = json.load(f)
f.close()

class App(QWidget):
        def __init__(self):
                super().__init__()
                screen_rect = app.desktop().screenGeometry()

                self.title='Email sender'
                self.width=900
                self.height=600
                self.left = int(screen_rect.width()/2-self.width/2)
                self.top = int(screen_rect.height()/2-self.height/2)


                self.table_widget = TableWidget(self)
               

                self.usless = QLabel(' ', self)
                self.txtLabel = QLabel('Txt file:', self)
                self.txtDirLabel = QLabel(" ", self)
                self.csvLabel = QLabel('Csv file:', self)
                self.csvDirLabel = QLabel(" ", self)


                self.txtLoad = QPushButton(self)
                self.txtLoad.setText("Load file")
                self.txtLoad.clicked.connect(self.getTextData)
                self.txtLoad.setFixedWidth(60)
                
                self.csvLoad = QPushButton(self)
                self.csvLoad.setText("Load file")
                self.csvLoad.clicked.connect(self.getTableData)
                self.csvLoad.setFixedWidth(60)

                self.layout2 = QGridLayout()

                self.layout2.addWidget(self.usless, 0, 0, 10, 1)
                self.layout2.addWidget(self.txtLabel, 1, 0, 1, 1)
                self.layout2.addWidget(self.txtLoad, 1, 1, 1, 1)
                self.layout2.addWidget(self.txtDirLabel, 2, 0, 1, 1)

                self.layout2.addWidget(self.csvLabel, 3, 0, 1, 1)
                self.layout2.addWidget(self.csvLoad, 3, 1, 1, 1)
                self.layout2.addWidget(self.csvDirLabel, 4, 0, 1, 1)
                self.layout2.addWidget(self.usless, 5, 0, 10, 1)

        
                
                self.layout2.addWidget(QLabel("Log in "), 6,0, 1, 1)
                self.logInLineEdit = QLineEdit(data["Prisijungimas"])
                self.layout2.addWidget(self.logInLineEdit, 6,1, 1, 1)
                
                self.layout2.addWidget(QLabel("Password"), 7,0, 1, 1)
                self.passwordLineEdit = QLineEdit(data["Slaptazodis"])
                self.layout2.addWidget(self.passwordLineEdit, 7,1, 1, 1)
        
                self.layout2.addWidget(QLabel("Email theme"), 8,0, 1, 1)
                self.themeLineEdit = QLineEdit(data["Theme"])
                self.layout2.addWidget(self.themeLineEdit, 8,1, 1, 1)
        
                self.layout2.addWidget(QLabel("Attachment"), 9,0, 1, 1)
                self.attachmentLineEdit = QLineEdit(data["Attachment"])
                self.layout2.addWidget(self.attachmentLineEdit, 9,1, 1, 1)
        
                self.layout2.addWidget(QLabel("Port"), 10,0, 1, 1)
                self.portLineEdit = QLineEdit(str(data["Port"]))
                self.layout2.addWidget(self.portLineEdit, 10,1, 1, 1)
        
                self.layout2.addWidget(QLabel("SMTP"), 11,0, 1, 1)
                self.SMTPLineEdit = QLineEdit(str(data["SMTP"]))
                self.layout2.addWidget(self.SMTPLineEdit, 11,1, 1, 1)
        
                self.saveButton = QPushButton(self)
                self.saveButton.setText("Save")
                self.saveButton.clicked.connect(self.saveInfo)
                self.saveButton.setFixedWidth(60)

                self.sendButton = QPushButton(self)
                self.sendButton.setText("Yeet it")
                self.sendButton.clicked.connect(self.sendScript)
                self.sendButton.setFixedWidth(200)
                self.sendButton.hide()
                self.layout2.addWidget(self.saveButton, 12, 0,1,10)

                self.layout2.addWidget(self.sendButton, 13, 0,1,10)

                layout = QHBoxLayout()
                layout.addWidget(self.table_widget,2)
                layout.addLayout(self.layout2, 1)
                
                self.setLayout(layout)

                self.initUI()
        def initUI(self):
                self.setMinimumSize(self.width,self.height)
                self.setWindowTitle(self.title)
                self.setGeometry(self.left,self.top,self.width,self.height)
                self.show()

        def saveInfo(self):
                if  self.logInLineEdit.text() != "XXXX@gmail.com":
                        temp = {
                                "Prisijungimas":self.logInLineEdit.text(),
                                "Slaptazodis":self.passwordLineEdit.text(),
                                "Theme":self.themeLineEdit.text(),
                                "Attachment":self.attachmentLineEdit.text(),
                                "Port":self.portLineEdit.text(),
                                "SMTP":self.SMTPLineEdit.text()
                         }
                        updateConfig(temp)
                        self.sendButton.show()

        def sendScript(self):
                self.sendButton.hide()
                Script.mainScript()


        def getTextData(self):
                self.table_widget.textBox.clear()
                self.fileDir = QFileDialog.getOpenFileName(self, 'Single File', os.getcwd() , '*.txt')
                if self.fileDir[0] != '':

                        #open text file in read mode
                        self.txtDir = os.path.basename(self.fileDir[0])

                        temp = {"txtDir": self.fileDir[0]}
                        updateConfig(temp)
                        
                        self.txtDirLabel.setText(self.txtDir)
                        basename_without_ext = os.path.splitext(self.txtDir)[0]
                        self.table_widget.tabs.setTabText(0,basename_without_ext)

                        temp = self.txtDirLabel.font()
                        temp.setItalic(True)
                        self.txtDirLabel.setFont(temp)

                        text_file = open(self.fileDir[0], "r")

                        #read whole file to a string
                        data = text_file.read()
                        self.table_widget.textBox.insertPlainText(data)
                        #close file
                        text_file.close()
        
        def getTableData(self):
                self.table_widget.tableWidget.clear()
                self.fileDir = QFileDialog.getOpenFileName(self, 'Single File', os.getcwd() , '*.csv')
                if self.fileDir[0] != '':
                        dir = self.fileDir[0]
                        basename_without_ext = os.path.splitext(os.path.basename(dir))[0]
                        temp = {"csvDir": self.fileDir[0]}
                        updateConfig(temp)
                        self.csvDir = os.path.basename(self.fileDir[0])
                        self.csvDirLabel.setText(self.csvDir)

                        temp = self.csvDirLabel.font()
                        temp.setItalic(True)
                        self.csvDirLabel.setFont(temp)

                        self.table_widget.tabs.setTabText(1,basename_without_ext)
                        #does this closes the file? or just leaves it opened :D
                        data = list(csv.reader(open(dir, encoding='utf-8')))
                        
                        rowcount = 0
                        for row in open(dir):
                            rowcount+= 1

                        self.table_widget.tableWidget.setRowCount(rowcount+2)
                        for i in range(0,rowcount): 
                                self.table_widget.tableWidget.setItem(i, 0, QTableWidgetItem(data[i][0]))
                                self.table_widget.tableWidget.setItem(i, 1, QTableWidgetItem(data[i][1]))

class TableWidget(QWidget):
    
    def __init__(self, parent):
            super(QWidget, self).__init__(parent)     

            self.layout = QVBoxLayout(self)       
            # Initialize tab screen
            self.tabs = QTabWidget()
            self.tab1 = QWidget()
            self.tab2 = QWidget()
          
            self.tabs.addTab(self.tab1,"E-mail")
            self.tabs.addTab(self.tab2,"Table")
        
            self.firstTab()
            self.secondTab()

            self.layout.addWidget(self.tabs)
            self.setLayout(self.layout)

    def firstTab(self):
            self.textBox = QPlainTextEdit()

        
            self.tab1.layout = QGridLayout(self)
            self.tab1.layout.setSpacing(1)
            self.tab1.layout.setContentsMargins(0, 0,0, 0)
            self.tab1.layout.addWidget(self.textBox, 1, 0, 1, 10)
            self.tab1.setLayout(self.tab1.layout)

    def secondTab(self):
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(100)
            self.tableWidget.setColumnCount(100)
            self.tableWidget.setShowGrid(True)

            
            self.tab2.layout = QGridLayout(self)
            self.tab2.layout.setContentsMargins(0, 0,0, 0)
            self.tab2.layout.addWidget(self.tableWidget, 0, 0, 1, 10)
            self.tab2.setLayout(self.tab2.layout)
    
    
   
def updateConfig(temp):
        data.update(temp)
        with open("config.json", "w") as outfile:
                json.dump(data, outfile)
                        

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex=App()
        sys.exit(app.exec_())   