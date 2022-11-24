from version.first import InputConnect as InputConnectOld3
from version.second import InputConnect


def main():
	version = input('Ведите версию:')
	
	if int(version) == 1:
		InputConnectOld3()
	elif int(version) == 2:
		InputConnect()
	
	
if __name__ == '__main__':
	main()
	