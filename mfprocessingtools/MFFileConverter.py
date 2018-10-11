
import os, re
import pandas as pd
import numpy as np

class MFRawFileToCSVConverter:
	
	def __init__(self, fileLocation):
		self.fileLocation = fileLocation


	def convert(self):
		if os.path.isdir(self.fileLocation):
			files = os.listdir(self.fileLocation)
			for file in files:
				file = self.fileLocation + file
				self.rawFileToCSV(file)
		else:
			self.rawFileToCSV(self.fileLocation)


	def rawFileToCSV(self, file):
		lines = []
		with open(file, 'r', encoding="utf8", errors='ignore') as f:
			for line in f:
				if not re.match(r'^\s*$', line):
					if len(line.split(';')) == 6:
						lines.append(line.strip())

		for line in lines:
			print(line)
		fileName, file_extension = os.path.splitext(file)
		csvFileName = fileName +'.csv'
		print(csvFileName)
		print('Writing File {} to {}'.format(file, csvFileName))
		with open(csvFileName, 'w', encoding='utf-8') as csvFile:
			for line in lines:
				csvFile.write(line)
				csvFile.write('\n')



class TextFileToDataFrame:

	def __init__(self, fileLocation):
		self.fileLocation = fileLocation
		self.data = pd.DataFrame(columns=['Scheme_Code','Scheme_Name','Net_Asset_Value','Repurchase_Price','Sale_Price','Date'])


	def fileToDataFrame(self):
		if os.path.isdir(self.fileLocation):
			files = os.listdir(self.fileLocation)
			data = []
			for file in files:
				print('Converting File {} to DataFrame'.format(self.fileLocation + file))
				data.append(self.createDataFrame(self.fileLocation + file))
				
			self.data = pd.concat(data)
			print(type(self.data))
			print(self.data.head())
			return self.data
		else:
			print('Converting File {} to DataFrame'.format(self.fileLocation))
			self.data = self.createDataFrame(self.fileLocation)
			print(type(self.data))
			print(self.data.head())
			return self.data


	def createDataFrame(self, fileName):
		lines = []
		with open(fileName, 'r', encoding='utf-8') as file:
			for line in file:
				if not re.match(r'^\s*$', line): #To remove blank lines in the file
					if len(line.split(';')) == 6:
						tempLine = line.replace(',','').strip().split(';') #To remove (,) in NAV values Ex: 1,763.09123
						lines.append(tuple(tempLine))

		columns = [column for column in lines[0]]
		columns = [column.replace(' ','_') for column in columns]
		print(columns)
		data = lines[1:]
		print(type(data))

		dataframe = pd.DataFrame(data=data, columns=columns)
		dataframe.head()

		dataframe['Scheme_Code'] = pd.to_numeric(dataframe['Scheme_Code'])
		dataframe['Scheme_Name'] = dataframe['Scheme_Name'].astype('str')
		dataframe['Net_Asset_Value'] = pd.to_numeric(dataframe['Net_Asset_Value'], errors='coerce')
		dataframe['Repurchase_Price'] = pd.to_numeric(dataframe['Repurchase_Price'], errors='coerce')
		dataframe['Sale_Price'] = pd.to_numeric(dataframe['Sale_Price'], errors='coerce')
		dataframe['Date'] = pd.to_datetime(dataframe['Date'], errors='coerce')

		print(dataframe.dtypes)

		return dataframe


class CreateDataFrameFromCSV:

	def __init__(self, fileLocation):
		self.fileLocation = fileLocation
		self.dataframe = pd.DataFrame(columns=['Scheme_Code','Scheme_Name','Net_Asset_Value','Repurchase_Price','Sale_Price','Date'])


	def getDataFrame(self):
		if os.path.isdir(self.fileLocation):
			files = os.listdir(self.fileLocation)
			data = []
			files = [file for file in files if not file.startswith('.') and re.search('\.csv', file)]
			for file in files:
				file = self.fileLocation + file
				print('Building DataFrame from File {}'.format(file))
				data.append(pd.read_csv(file, sep=';'))
				
			self.dataframe = pd.concat(data)
			print(type(self.dataframe))
			return self.dataframe
		else:
			print('Building DataFrame from File {}'.format(file))
			data.append(pd.read_csv(file))
			return self.dataframe










