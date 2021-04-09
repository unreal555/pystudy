# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 上午 9:37
# Tool ：PyCharm

import win32com.client as win32
import os

class excelFile():

	def __init__(self,filePath):
		self.excel = win32.DispatchEx("Excel.Application")
		self.excel.Visible = True
		self.excel.DisplayAlerts = False
		self.filePath = os.path.abspath(filePath)
		self.file=self.excel.Workbooks.Open(filePath)

	def __del__(self):
		self.file.Save()
		self.file.Close()
		self.excel.Quit()

	def readCell(self,rowN,colN,sheet='sheet1'):
		sht=self.file.Worksheets(sheet)
		data = sht.Cells(rowN,colN).Value
		return data

	def writeCell(self,rowN,colN,text,sheet='sheet1'):
		sht=self.file.Worksheets(sheet)
		sht.Cells(rowN,colN).Value=text

	def getAll(self,sheet='sheet1'):
		sht=self.file.Worksheets(sheet)
		result=[row for row in sht.UsedRange.Value]
		return result

	def getSheets(self):
		return [sheet.Name for sheet in self.file.Worksheets]

	def unlockSheet(self, sheet,password):
		sht = self.file.Worksheets(sheet)
		sht.Unprotect(password)

	def lockSheet(self,sheet,password):
		sht = self.file.Worksheets(sheet)
		sht.Protect(password)

	def copyCellsTo(self, copy_cells, to_cells,sheet='sheet1'):
		# to_cells,如:"A2:B2"
		sht = self.file.Worksheets(sheet)
		sht.Range(copy_cells).Copy()
		sht.Range(to_cells).PasteSpecial()

	def readCells(self,cells,sheet='sheet1'):
		sht=self.file.Worksheets(sheet)
		data=sht.Range(cells).Value
		return data

	def writeCells(self,cells,text,sheet='sheet1'):
		sht=self.file.Worksheets(sheet)
		sht.Range(cells).Value=text

	def haveComment(self, rowN,colN,sheet='sheet1'):
		sht = self.file.Worksheets(sheet)
		if sht.Cells(rowN,colN).Comment:
			return sht.Cells(rowN,colN).Comment.Text()
		else:
			return False

	def delComment(self, rowN,colN,sheet='sheet1'):
		sht = self.file.Worksheets(sheet)
		if s:=self.haveComment(rowN,colN,sheet):
			print('{}{}'.format(rowN,colN),'已有批注，删除内容:',s)
			sht.Cells(rowN, colN).Delete()
			return s
		else:
			print('{}{}'.format(rowN,colN),'无批注')
			return None

	def addComment(self, rowN,colN,text,sheet='sheet1'):
		if self.haveComment(rowN,colN,sheet):
			self.delComment(rowN,colN,sheet)
		sht = self.file.Worksheets(sheet)
		sht.Cells(rowN,colN).AddComment(text)

	def addPicture(self, pictureName, Left, Top, Width, Height,sheet='sheet1'):

		sht = self.file.Worksheets(sheet)
		sht.Pictures.Insert (pictureName)





if __name__ == '__main__':
	'''
	cells,如:A1:B1
	cells,如:rowN=6,colN=B
	'''
	sourcedir = os.path.abspath(r'C:\2018')

	for  file in os.listdir(sourcedir):
		path=os.path.join(sourcedir,file)
		print(path)
		f=excelFile(path)
		f.unlockSheet(sheet='sheet1',password='1234')
		f.writeCells('A1:a11','test')
		f.delComment(rowN='6',colN='b')
		f.copyCellsTo('b4','b6')
		f.addPicture(pictureName=r'D:\PyCharm2019.3.1\pystudy\pic\2.jpg',Left=1,Top=1,Width=400,Height=40)

