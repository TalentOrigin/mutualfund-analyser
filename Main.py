
from mfprocessingtools.MFFileConverter import TextFileToDataFrame, MFRawFileToCSVConverter, CreateDataFrameFromCSV
from mfprocessingtools.MFNavDownloader import HistoricDataDownloader

if __name__ == '__main__':
	# downloader = HistoricDataDownloader()
	# downloader.downloadAllData()
	# print(downloader.fundHouseMapping)
	fundHouseMapping = {2: 'Standard_Chartered_Mutual_Fund', 3: 'Aditya_Birla_Sun_Life_Mutual_Fund', 4: 'Baroda_Pioneer_Mutual_Fund', 6: 'DSP_Mutual_Fund', 9: 'HDFC_Mutual_Fund', 10: 'PRINCIPAL_Mutual_Fund', 13: 'Quant_Mutual_Fund', 14: 'ING_Mutual_Fund', 16: 'JM_Financial_Mutual_Fund', 17: 'Kotak_Mahindra_Mutual_Fund', 18: 'LIC_Mutual_Fund', 19: 'Morgan_Stanley_Mutual_Fund', 20: 'ICICI_Prudential_Mutual_Fund', 21: 'Reliance_Mutual_Fund', 22: 'SBI_Mutual_Fund', 25: 'Tata_Mutual_Fund', 26: 'Taurus_Mutual_Fund', 27: 'Franklin_Templeton_Mutual_Fund', 28: 'UTI_Mutual_Fund', 31: 'DBS_Chola_Mutual_Fund', 32: 'Canara_Robeco_Mutual_Fund', 33: 'Sundaram_Mutual_Fund', 35: 'Sahara_Mutual_Fund', 36: 'Benchmark_Mutual_Fund', 37: 'HSBC_Mutual_Fund', 38: 'Deutsche_Mutual_Fund', 39: 'ABN__AMRO_Mutual_Fund', 40: 'Fidelity_Mutual_Fund', 41: 'Quantum_Mutual_Fund', 42: 'Invesco_Mutual_Fund', 43: 'JPMorgan_Mutual_Fund', 44: 'PineBridge_Mutual_Fund', 45: 'Mirae_Asset_Mutual_Fund', 46: 'BOI_AXA_Mutual_Fund', 47: 'Edelweiss_Mutual_Fund', 48: 'IDFC_Mutual_Fund', 49: 'Goldman_Sachs_Mutual_Fund', 51: 'Fortis_Mutual_Fund', 52: 'Shinsei_Mutual_Fund', 53: 'Axis_Mutual_Fund', 54: 'Essel_Mutual_Fund', 55: 'Motilal_Oswal_Mutual_Fund', 56: 'L&T_Mutual_Fund', 57: 'IDBI_Mutual_Fund', 58: 'DHFL_Pramerica_Mutual_Fund', 59: 'BNP_Paribas_Mutual_Fund', 60: 'Daiwa_Mutual_Fund', 61: 'Union_Mutual_Fund', 62: 'IIFL_Mutual_Fund', 63: 'Indiabulls_Mutual_Fund', 64: 'PPFAS_Mutual_Fund', 65: 'IL&FS_Mutual_Fund_(IDF)', 67: 'Shriram_Mutual_Fund', 68: 'IIFCL_Mutual_Fund_(IDF)', 69: 'Mahindra_Mutual_Fund'}
	print(len(fundHouseMapping))

	# converter = TextFileToDataFrame('/Users/talentorigin/workspace/datasets/mutualfunds/sample/')
	# data = converter.fileToDataFrame()
	# print(data.head(20))

	# writer = MFRawFileToCSVConverter('/Users/talentorigin/workspace/datasets/mutualfunds/sample/')
	# writer.convert()

	data = CreateDataFrameFromCSV('/Users/talentorigin/workspace/datasets/mutualfunds/sample/')
	dataframe = data.getDataFrame()
	print(dataframe.head(10))
