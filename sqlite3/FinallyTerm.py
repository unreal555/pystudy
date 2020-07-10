import sqlite3

from tkinter import messagebox

class Values(object):
    conn=''
    cursor=''
    def __init__(self):
        self.conn = sqlite3.connect("data.sqlite3")

        self.cursor = self.conn.cursor()

    def addFinalExamDatabaseVersion2(self, value):

        sql = "INSERT INTO testData (testValues)  VALUES (%d)"%value
        self.cursor.execute(sql)
        print(self.cursor.fetchall())
        self.conn.commit()



    def getsum(self, testValues='testValues'):
        # sql = "SELECT SUM(testValues) FROM testData WHERE testValues = '"+ testValues + "'"
        sql = "SELECT SUM ({}) FROM testData".format(testValues)
        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        print(records)
        sum = records[0][0]
        return sum

    def removeValue(self, index):
        print("index value: ", index, "|")
        sql = "DELETE FROM testData WHERE id = " + str(self.ids[index[0]])
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

def cmdSumit():
    try:
        Value = float(inputValue.get())
    except Exception as e:
        messagebox.showinfo('消息框', e)
        return False

    myData.addFinalExamDatabaseVersion2(Value)
    # SumText.config(text=myData.getsum())

def cmdDelete():
    myData.removeValue(index)

from tkinter import *
from tkinter import ttk

myData = Values()

root = Tk()
root.title("(Energy)")
root.geometry("350x200")


Label(root, text="Input Value:").grid(row=0, column=0, sticky=W)

inputValue = Entry(root, width=20)
inputValue.grid(row=0, column=1, sticky=W)

Button(root, text="Sumit", command = cmdSumit).grid(row=0, column=2, sticky=W)
Label(root, text="Count of Records: ").grid(row=2, column=0, sticky=W)
Label(root, text="Sum of Values: ").grid(row=3, column=0, sticky=W)

CountText = Label(root, text="0")
CountText.grid(row=2, column=1, sticky=E)

SumText = Label(root, text=myData.getsum())
SumText.grid(row=3, column=1, sticky=E)

Button(root, text="Delete All Values", command = cmdDelete).grid(row=4, column=0, sticky=W)

root.mainloop()
