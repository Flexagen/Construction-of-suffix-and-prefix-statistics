import statistiCuM
from suffix_statistics import Suffix_Stat

def test_statistic_class():
	"""Тестирование .so обёртки для C++ структуры данных""" 
	p = statistiCuM.statistic_counter()
	p.add('The is the link to the python package')
	p.add('is the link to the python package I ')
	p.add('the link to the python package I am')
	
	# Тестирование обхода заколненной структуры методов get_next
	s = p.get_next()
	while(s != ''):
		assert(s != '')
		assert(s != None)
		s = p.get_next()
	
	if p.get_by_number(11) != "is the link":
		raise AssertionError("Тест поиска префикса/суффикса по номеру")

	if p.get_by_pref('package') != 0:
		raise AssertionError("Тест поиска префикса/суффикса")


def test_suffix_statistic():
	"""Тестирование модуля подсчёта статистики префиксов"""
	p = Suffix_Stat('The is the link to the python package', 2)


def test_suffix_statistic():
	None


def print_test_passed(test_name):
	print("Test "+test_name+" "+'\033[42m'+"PASSED"+'\033[0m')


if __name__ == "__main__":
	test_name = ""
	try:
		test_name = "statistic_class"; test_statistic_class(); print_test_passed(test_name)
		test_name = "suffix_statistic"; test_suffix_statistic(); print_test_passed(test_name)
	except AssertionError as error:
		print("Test "+test_name+' '+'\033[101m'+"ERROR"+'\033[0m')
		print(error)
		print()