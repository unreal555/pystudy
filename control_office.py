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

	def readCell(self,rowN,colN,sheet='sheet1'):
		sheet=self.file.Worksheets(sheet)
		data = sheet.Cells(rowN,colN).Value
		return data

	def writeCell(self,rowN,colN,content,sheet='sheet1'):
		sheet=self.file.Worksheets(sheet)
		sheet.Cells(rowN,colN).Value=content

	def getAll(self,sheet='sheet1'):
		sheet=self.file.Worksheets(sheet)
		result=[row for row in sheet.UsedRange.Value]
		return result

	def getSheets(self):
		return [sheet.Name for sheet in self.file.Worksheets]

	def unlockSheet(self, sheet,password):
		sheet = self.file.Worksheets(sheet)
		sheet.Unprotect(password)

	def lockSheet(self,sheet,password):
		sheet = self.file.Worksheets(sheet)
		sheet.Protect(password)

	def copyCells(self, copy_cells, to_cells,sheet='sheet1'):
		# to_cells,如:"A2:B2"
		sheet = self.file.Worksheets(sheet)
		sheet.Range(copy_cells).Copy()
		sheet.Range(to_cells).PasteSpecial()

	def readCells(self,cells,sheet='sheet1'):
		sheet=self.file.Worksheets(sheet)
		data=sheet.Range(cells).Value
		return data

	def writeCells(self,cells,content,sheet='sheet1'):
		sheet=self.file.Worksheets(sheet)
		sheet.Range(cells).Value=content

	def __del__(self):
		self.file.Save()
		self.file.Close()
		self.excel.Quit()

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

