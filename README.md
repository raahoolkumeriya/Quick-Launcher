# Quick-Launcher


Python app to perform day-to-day task on single click 

![screenshot from 2019-01-04 23-54-06](https://user-images.githubusercontent.com/31859032/50704240-b3cc2380-107c-11e9-92f1-b33fedb23efd.png)

## Requirement (Python Packages added in script): 
Package|Version
-----|-----
PyQt5| 5.9.2
xlsxwriter|1.1.2
sqlalchemy|1.2.15
cx_Oracle| 7.0.0
pyperclip|1.7.0

### Flow of Tool Development: 
- Design the tool using qt 4 Designser
- Convert ui file into py using below command
```    
    pyuic5 -x quicklaunch.ui -o quicklaunch.py
```

## Code Snippets:

### To Launch Terminal 

```
    os.system("gnome-terminal 'sudo apt-get update'")
```
### To Launch Favorite Sites
```
        import webbrowser

        favoriteSite = [
        'https://github.com/',
        'https://www.youtube.com/',
        'https://duckduckgo.com/',
        'https://openai.com/'
        ]
        for url in favoriteSite:
            webbrowser.open(url)

```
### To Trigger any script 
```
        reply = qt.QMessageBox.question(self, "Send automate mail", qt.QMessageBox.Yes | qt.MessageBox.Cancel)
        if reply == qt.QMessageBox.Yes:
            subprocess.call("python python_Script_name.py")
        else:
            print("Mission Aborted")

```
### To send automated mail 
```
        reply = qt.QMessageBox.question(self, "Send automate mail", qt.QMessageBox.Yes | qt.MessageBox.Cancel)
        if reply == qt.QMessageBox.Yes:
            print("Sending autoamte mail")

            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = 'rahulkumeriya@gmail.com,rahulkumeriya@gmail.com'
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
```
### To wrap database data into Excel sheet
```
        import xlsxwriter

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
        user='XXXXXXXXXXXXX'
        password='XXXXXXXXXXXX'
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
        worksheet.write('A1', 'ID',cell_format)
        worksheet.write('B1', 'NAME',cell_format)
        worksheet.write('C1', 'AGE',cell_format)
        worksheet.write('D1', 'LOACTION', cell_format)
        worksheet.write('E1', 'PROFESSION', cell_format)

        result = engine.execute('select * from CUSTOMERS')
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

```

### To launch Putty from Windows OS
```
       # For windows to launch Putty 
        from pywinauto.application import Application
        import time

        app = Application().start(cmd_line=u'putty.exe username@hostname -pw %s' % sys.argv[2])
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

```
These are few things added in the script. 

# The app can be scale to large extend to use mutiple python utilities

![screenshot from 2019-01-05 00-12-39](https://user-images.githubusercontent.com/31859032/50704809-b3348c80-107e-11e9-8fc5-170d98e6963a.png)
