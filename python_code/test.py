<<<<<<< HEAD
import statistiCuM
from suffix_statistics import Suffix_Stat

def test_statistic_class():
	"""Тестирование .so обёртки для C++ структуры данных""" 
	p = statistiCuM.statistic_counter()
	p.add('The is the link to the python package')
	p.add('is the link to the python package I ')
	p.add('the link to the python package I am')
	
=======
import StatistiCuM
from prefix_statistics import Prefix_Stat

def test_statistic_class():
	"""Тестирование .so обёртки для C++ структуры данных""" 
	p = StatistiCuM.statistic_counter()
	p.add('The is ')
	p.add('is the link')
	p.add('the ')
	p.add('the is')
	p.add('the	')

>>>>>>> c4bc0d0d0024554c93a8a65cbe96e370219a5ad7
	# Тестирование обхода заколненной структуры методов get_next
	s = p.get_next()
	while(s != ''):
		assert(s != '')
		assert(s != None)
		print(s)
		s = p.get_next()
	
	if p.get_by_number(2) != "is the link":
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
<<<<<<< HEAD
		test_name = "suffix_statistic"; test_suffix_statistic(); print_test_passed(test_name)
=======
		# test_name = "prefix_statistic"; test_prefix_statistic(); print_test_passed(test_name)
>>>>>>> c4bc0d0d0024554c93a8a65cbe96e370219a5ad7
	except AssertionError as error:
		print("Test "+test_name+' '+'\033[101m'+"ERROR"+'\033[0m')
		print(error)
		print()