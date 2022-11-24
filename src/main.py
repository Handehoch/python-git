from version.first import InputConnect as InputConnectOld
from version.second import InputConnect


def main():
	version = input('Ведите версию:')
	
	if int(version) == 2:
		InputConnectOld()
	elif int(version) == 2:
		InputConnect()
	
	
if __name__ == '__main__':
	main()
	