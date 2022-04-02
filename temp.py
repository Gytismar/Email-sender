from PyQt5.QtWidgets import (QApplication,QWidget,QHBoxLayout,QPushButton, QVBoxLayout, QTabWidget, QPlainTextEdit, QTableWidget, QFileDialog, QTableWidgetItem)
from PyQt5.QtCore import pyqtSlot, QDir
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
                self.browseFiles = QPushButton("Browse files")
                self.browseFiles.clicked.connect(self.getTableData)

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

      def getTableData(self):
                fileName = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.csv')

                dir = fileName[0]
                basename_without_ext = os.path.splitext(os.path.basename(dir))[0]
                self.table_widget.tab1Name(basename_without_ext, dir)
      

class TableWidget(QWidget):
    
    def __init__(self, parent):
            super(QWidget, self).__init__(parent)     

            self.layout = QVBoxLayout(self)       
            # Initialize tab screen
            self.tabs = QTabWidget()
            self.tab1 = QWidget()
            self.tab2 = QWidget()
          
            self.tabs.addTab(self.tab1,"")
            self.tabs.addTab(self.tab2,"")
        
            #first tab  
            self.textBox = QPlainTextEdit(parent)
            self.tab1.layout = QVBoxLayout(self)
            self.tab1.layout.setContentsMargins(0, 0,0, 0)
            self.tab1.layout.addWidget(self.textBox)
            self.tab1.setLayout(self.tab1.layout)

            #second tab
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(100)
            self.tableWidget.setColumnCount(100)
            self.tab2.layout = QVBoxLayout(self)
            self.tab2.layout.setContentsMargins(0, 0,0, 0)
            self.tab2.layout.addWidget(self.tableWidget)
            self.tab2.setLayout(self.tab2.layout)
            
            self.layout.addWidget(self.tabs)
            self.setLayout(self.layout)
            
    def tab1Name(self,name, dir):
            self.tabs.setTabText(1,name)

            data = list(csv.reader(open(dir, encoding='utf-8')))

            rowcount = 0
            for row in open(dir):
                rowcount+= 1

            for i in range(0,rowcount): 
                self.tableWidget.setItem(i, 0, QTableWidgetItem(data[i][0]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(data[i][1]))
                

                

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex=App()
        sys.exit(app.exec_())