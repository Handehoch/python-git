import pandas as pd


class SalaryParser:
	def __init__(self, file_name: str) -> None:
		self.__currencies = pd.read_csv('../currencyparser/data.csv')
		self.__available = list(self.__currencies.keys()[2:])
		self.__filename = file_name
	
	def parse_salary(self) -> None:
		"""
		Срздаёт обработанный CSV файл
		:return: None
		"""
		salaries = []
		to_remove = []
		dataframe = pd.read_csv(self.__filename)
		
		for row in dataframe.itertuples():
			s_from = str(row[2])
			s_to = str(row[3])
			
			if s_from != 'nan' and s_to != 'nan':
				salary = float(s_from) + float(s_to)
			elif s_from != 'nan' and s_to == 'nan':
				salary = float(s_from)
			elif s_from == 'nan' and s_to != 'nan':
				salary = float(s_to)
			else:
				to_remove.append(int(row[0]))
				continue
				
			if row[4] == 'nan' or row[4] not in self.__available:
				to_remove.append(int(row[0]))
				continue
				
			if row[4] != 'RUR':
				date = row[6][:7]
				coefficient = self.__currencies[self.__currencies['date'] == date][row[4]].iat[0]
				salary *= coefficient
				
			salaries.append(salary)
			
		dataframe.drop(labels=to_remove, axis=0, inplace=True)
		dataframe.drop(labels=['salary_to', 'salary_from', 'salary_currency'], axis=1, inplace=True)
		dataframe['salary'] = salaries
		dataframe.to_csv('res.csv')


SalaryParser('../../../vacancies_dif_currencies.csv').parse_salary()
