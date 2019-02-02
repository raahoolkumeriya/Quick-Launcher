# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmvapp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import os
from PyQt5 import QtGui as qt
import subprocess
#import win32com.client as win32   #Enable this for Windows platform
#import external python scripts if you are calling from subprocess

# To write data from database into excle import xlsxwriter
import xlsxwriter
#For Putty login import below package
#from pywinauto.application import Application      #Enable this for Windows platform
import time
        


class Ui_QuickLaunch(QWidget):
    def setupUi(self, QuickLaunch):
        QuickLaunch.setObjectName("QuickLaunch")
        QuickLaunch.setEnabled(True)
        QuickLaunch.resize(284, 373)
        self.gridLayout = QtWidgets.QGridLayout(QuickLaunch)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(QuickLaunch)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 4, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 5, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 6, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 7, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 8, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 9, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(QuickLaunch)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 10, 0, 1, 1)

        self.retranslateUi(QuickLaunch)
        QtCore.QMetaObject.connectSlotsByName(QuickLaunch)

        self.initevents()

    def initevents(self):
        self.pushButton_7.clicked.connect(self.launchFavouriteSites)
        self.pushButton_6.clicked.connect(self.triggerPythonScript)
        self.pushButton_12.clicked.connect(self.puttyLaunch)
        self.pushButton_11.clicked.connect(self.browserLaunch)
        self.pushButton_10.clicked.connect(self.sendReportFromDatabase)
        self.pushButton_9.clicked.connect(self.sendAutomatedMail)
        self.pushButton_8.clicked.connect(self.triggerShellScript)
        self.pushButton_3.clicked.connect(self.UATPuttyLogin)
        self.pushButton_2.clicked.connect(self.PRODputtyLogin)
        self.pushButton_5.clicked.connect(self.writeDatabaseDataToExcel)
    
    def PRODputtyLogin(self):
        # For windows to launch Putty 
        #app = Application().start(cmd_line=u'putty.exe <USERNAME>@<HOSTNAME> -pw <PASSWORD>') # password hardcoded
        app = Application().start(cmd_line=u'putty.exe raahool@localhost -pw %s' % sys.argv[2])  # password provided as CLI positional parameter
        putty  = app.Putty()
        putty.Wait('ready')
        time.sleep(5)
        putty.TypeKeys("export TMOUT=0", with_spaces = True)
        putty.TypeKeys("{ENTER}")
        putty.TypeKeys("cd /path/to/desire/location")
        putty.TypeKeys("{ENTER}")
        time.sleep(1)
        putty.TypeKeys("./execute_script.sh")
        putty.TypeKeys("{ENTER}")
        
    def writeDatabaseDataToExcel(self):
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('Dashboard_Report.xlsx')
        worksheet = workbook.add_worksheet()

        # Widen the first column to make the text clearer.
        worksheet.set_column('A:A', 25)

        # Add a cell_format format to use to highlight cells.
        cell_format = workbook.add_format({'bold': True, 'border':1, 'align':'center','font_size':'10','font_name':'Calibri'})
        cell_FRMT = workbook.add_format({'bold': False, 'border':1, 'align':'center','font_size':'10','font_name':'Calibri'})

        worksheet.set_column(0,5,25,cell_FRMT)

        from sqlalchemy import create_engine
        import cx_Oracle

        host='127.0.0.1'
        port=1521
        sid='XE'
        user='databaseuser'
        password='Password#1'
        sid = cx_Oracle.makedsn(host, port, sid=sid)

        cstr = 'oracle://{user}:{password}@{sid}'.format(
            user=user,
            password=password,
            sid=sid
        )

        engine =  create_engine(
            cstr,
            convert_unicode=False,
            pool_recycle=10,
            pool_size=50,
            echo=True
        )


        worksheet.write('A1', 'OWNER',cell_format)
        worksheet.write('B1', 'TABLESPACE_NAME',cell_format)
        worksheet.write('C1', 'TABLE_NAME',cell_format)
        worksheet.write('D1', 'STATUS', cell_format)
        worksheet.write('E1', 'NUM_ROWS', cell_format)

        result = engine.execute('select OWNER,TABLESPACE_NAME,TABLE_NAME,STATUS,NUM_ROWS from all_tables where NUM_ROWS=100')
        row=1
        col=0
        for i,j,k,l,m in (result):
            worksheet.write(row,col,i)
            worksheet.write(row,col+1,j)
            worksheet.write(row,col+2,k)
            worksheet.write(row,col+3,l)
            worksheet.write(row,col+4,m)
            row+=1
        # Write some simple text.
        worksheet.write('A10', 'TABLE NAMES',cell_format)

        # Text with formatting.
        worksheet.write('B10', 'Table', cell_format)

        # Write some numbers, with row/column notation.
        result = engine.execute('select * from tab')
        row=10
        col=0
        for i,j,k in (result):
            worksheet.write(row,col,i)
            worksheet.write(row,col+1,j)
            worksheet.write(row,col+2,k)
            row+=1
        conn = engine.connect()
        conn.close()
        workbook.close()



    def UATPuttyLogin(self):
        pass
        """	
        # FOR MULTIPLE SERVER DETAILS
        app = Application().start(cmd_line=u'putty.exe %s@%s -pw %s' % (username,hostname,sys.argv[2]))
        putty  = app.Putty()
        putty.Wait('ready')
        """

    def triggerShellScript(self):
        """this fuction use under linux system"""	
        os.system("sh /path/to/script/laoction/script_name.sh")

    def sendAutomatedMail(self):
        pass
        '''		
        reply = QMessageBox.question(self, 'Action Require', "Do you want to send mail?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            print("Sending autoamte mail")

            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = 'rahulkumeriya@gmail.com'
            mail.CC = 'rahulkumeriya@gmail.com'
            mail.Subject = 'Automate mail'
            mail.HTMLBody = """
            <html>
                <head></head>
                    <style>
                        body {
                                background-color: #f0f0f0;
                        }
                        h1 {
                                color: white;
                        }
                    </style>
                    <body>
                    <pre>
Hi World,

This is automate mail sent from python Quick launcher app.

<strong>Quick launcher</strong> is live now !!!!
                    </pre>
                    </body>
                    </html>
                    """
            mail.Send()
            print("Mail sent successfully!!!!")
        else:
            print("AAAArrrr!!! Mission Aborted!!!!")
        '''
        
    def sendReportFromDatabase(self):
        from sqlalchemy import create_engine
        import cx_Oracle

        host='127.0.0.1'
        port=1521
        sid='XE'
        user='databaseuser'
        password='Password#1'
        sid = cx_Oracle.makedsn(host, port, sid=sid)
        cstr = 'oracle://{user}:{password}@{sid}'.format(
            user=user,
            password=password,
            sid=sid
        )

        engine =  create_engine(
            cstr,
            convert_unicode=False,
            pool_recycle=10,
            pool_size=50,
            echo=True
        )
        result = engine.execute('SELECT SYSDATE FROM DUAL')

        for row in result:
            print(row)
            
        conn = engine.connect()
        conn.close()

    def browserLaunch(self):
        import webbrowser, sys, pyperclip
        if len(sys.argv) > 1:
            # Get address from comandline
            address = sys.argv[2]
        else:
            #Get address from clipboard
            address = pyperclip.paste()
            
        webbrowser.open('https://www.google.com/maps/place/' + address)

    def puttyLaunch(self):
        '''This fuction will work with Linux'''
        print("""os.system("gnome-terminal 'sudo apt-get update'")""") 

    def triggerPythonScript(self):
        reply = QMessageBox.question(self, "Send automate mail", QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            subprocess.call("python python_Script_name.py")
        else:
            print("Mission Aborted")

    def launchFavouriteSites(self):
        import webbrowser

        favoriteSite = [
        'https://github.com/',
        'https://www.youtube.com/',
        'https://www.youtube.com/',
        'https://duckduckgo.com/',
        'https://openai.com/'
        ]
        for url in favoriteSite:
            webbrowser.open(url)


    def retranslateUi(self, QuickLaunch):
        _translate = QtCore.QCoreApplication.translate
        QuickLaunch.setWindowTitle(_translate("QuickLaunch", "Quick Launcher"))
        self.label_2.setText(_translate("QuickLaunch", "Quick Launcher"))
        self.pushButton_7.setText(_translate("QuickLaunch", "Launch Favourite sites"))
        self.pushButton_6.setText(_translate("QuickLaunch", "Trigger Python script"))
        self.pushButton_12.setText(_translate("QuickLaunch", "Putty launch"))
        self.pushButton_11.setText(_translate("QuickLaunch", "Browser launch"))
        self.pushButton_10.setText(_translate("QuickLaunch", "Send Report from database"))
        self.pushButton_9.setText(_translate("QuickLaunch", "Send automate mail"))
        self.pushButton_8.setText(_translate("QuickLaunch", "Trigger the shell script"))
        self.pushButton_3.setText(_translate("QuickLaunch", "UAT putty Login"))
        self.pushButton_2.setText(_translate("QuickLaunch", "PROD putty Login"))
        self.pushButton_5.setText(_translate("QuickLaunch", "Report write to Excel "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QuickLaunch = QtWidgets.QWidget()
    ui = Ui_QuickLaunch()
    ui.setupUi(QuickLaunch)
    QuickLaunch.show()
    sys.exit(app.exec_())

