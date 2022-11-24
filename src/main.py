from version.first import InputConnect as InputConnectOld
from version.second import InputConnect


def main():
	version = input('Ведите версию:')
	
	if int(version) == 1:
		InputConnectOld()
	elif int(version) == 2:
		InputConnect()
		
	print('Hello develop')
	
	print('Hello main')
	
	
if __name__ == '__main__':
	main()
	