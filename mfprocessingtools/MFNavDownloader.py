
from bs4 import BeautifulSoup
import requests, datetime, sys
import traceback

class HistoricDataDownloader:

	def __init__(self, startDate=None, endDate=None, schemeType=1, defaultLocation=None):
		startDt = "01-Jan-1990"
		endDt = datetime.datetime.now().strftime('%d-%b-%Y')
		if defaultLocation is None:
			self.defaultLocation = '/Users/talentorigin/workspace/datasets/mutualfunds/{fund_name}_{fund_type}.txt'
		self.fundHouseMapping = {}
		if startDate is None:
			self.startDate = startDt
		if endDate is None:
			self.endDate = endDt
		self.schemeType = schemeType
		self.baseUrl = "http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf={mf_house_num}&tp={mf_type}&frmdt={start_date}&todt={end_date}"
		print(self.startDate)


	def downloadData(self, url):
		print('Downloading data from: ', url)
		htmlResponse = requests.get(url)
		rawData = BeautifulSoup(htmlResponse.content, 'lxml')
		mfHouseData = rawData.get_text()
		return mfHouseData


	def downloadAllData(self):
		try:
			for fundHouse in range(1, 100):
				print(fundHouse)
				for mfType in range(1, 4):
					url = self.baseUrl.format(mf_house_num=fundHouse, mf_type=mfType, start_date=self.startDate, end_date=self.endDate)
					data = self.downloadData(url)
					fundHouseName = data.split('\n')[5].strip().replace(' ','_')
					print('Fund Name: ', fundHouseName)
					if fundHouseName != '':
						self.fundHouseMapping[fundHouse] = fundHouseName
						print('Saving {} Fund House Data.'.format(fundHouseName))
						print('Fund House Name: ', fundHouseName)
						self.saveData(data, fundHouseName, self.getFundType(mfType))
		except:
			print("Exception Caught: ", traceback.print_exc())


	def saveData(self, data, fundHouseName, mfType):
		with open(self.defaultLocation.format(fund_name=fundHouseName, fund_type=mfType), 'w', encoding="utf-8") as file:
			file.write(data)


	def getFundType(self, typeNo):
		ft = {
			1: 'Open',
			2: 'Closed',
			3: 'Interval'
		}
		return ft.get(typeNo, 'None')






















