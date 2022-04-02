from fileinput import filename
from PyQt5.QtWidgets import (QApplication,QWidget,QHBoxLayout,QPushButton,QGridLayout, QVBoxLayout, QTabWidget, QPlainTextEdit, QTableWidget, QFileDialog, QTableWidgetItem)
from PyQt5.QtCore import pyqtSlot, QDir
from PyQt5 import QtGui, Qt 
import sys
import os
import csv




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
                self.browseFiles = QPushButton("--")

                layout = QHBoxLayout()
                layout.addWidget(self.table_widget, 2)
                layout.addWidget(self.browseFiles, 1)
                layout.addWidget(QPushButton(":DD"))
                self.setLayout(layout)

                self.initUI()
      def initUI(self):
                self.setMinimumSize(self.width,self.height)
                self.setWindowTitle(self.title)
                self.setGeometry(self.left,self.top,self.width,self.height)
                self.show()

      
      

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

            self.pushButtonLoad = QPushButton(self)
            self.pushButtonLoad.setText("Load file")
            self.pushButtonLoad.clicked.connect(self.getTextData)
            self.pushButtonLoad.setFixedWidth(60)


            self.tab1.layout = QGridLayout(self)
            self.tab1.layout.setSpacing(1)
            self.tab1.layout.setContentsMargins(0, 0,0, 0)
            self.tab1.layout.addWidget(self.pushButtonLoad, 0,0)
            self.tab1.layout.addWidget(self.textBox, 1, 0, 1, 10)
            self.tab1.setLayout(self.tab1.layout)

    def secondTab(self):
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(100)
            self.tableWidget.setColumnCount(100)
            self.tableWidget.setShowGrid(True)

            self.pushButtonLoad = QPushButton(self)
            self.pushButtonLoad.setText("Load file")
            self.pushButtonLoad.clicked.connect(self.getTableData)
            self.pushButtonLoad.setFixedWidth(60)


            self.tab2.layout = QGridLayout(self)
            self.tab2.layout.setSpacing(1)
            self.tab2.layout.setContentsMargins(0, 0,0, 0)
            self.tab2.layout.addWidget(self.pushButtonLoad, 0, 0)
            self.tab2.layout.addWidget(self.tableWidget, 1, 0, 1, 10)
            self.tab2.setLayout(self.tab2.layout)
    
    def getTableData(self):
            self.tableWidget.clear()
            self.fileDir = QFileDialog.getOpenFileName(self, 'Single File', os.getcwd() , '*.csv')
            if self.fileDir[0] != '':
                dir = self.fileDir[0]
                basename_without_ext = os.path.splitext(os.path.basename(dir))[0]
                print(os.path.basename(dir))

                self.tabs.setTabText(1,basename_without_ext)
                #does this closes the file? or just leaves it opened :D
                data = list(csv.reader(open(dir, encoding='utf-8')))
                
                rowcount = 0
                for row in open(dir):
                    rowcount+= 1

                self.tableWidget.setRowCount(rowcount+2)
                for i in range(0,rowcount): 
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(data[i][0]))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(data[i][1]))
   
    def getTextData(self):
        self.textBox.clear()
        self.fileDir = QFileDialog.getOpenFileName(self, 'Single File', os.getcwd() , '*.txt')
        if self.fileDir[0] != '':
            #open text file in read mode
            text_file = open(self.fileDir[0], "r")
        
            #read whole file to a string
            data = text_file.read()
            self.textBox.insertPlainText(data)
            #close file
            text_file.close()


if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex=App()
        sys.exit(app.exec_())   