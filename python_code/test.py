import StatistiCuM
from prefix_statistics import PrefixStat
from suffix_statistics import SuffixStat

# Settings
text = """Advertisers study how people learn so that they can 'teach' them to respond 
		  to their advertising. They want us to be interested, to try something, and 
	      then to do it again. These are the elements of to learning: interest, experience 
		  and repetition. If an advert can achieve this, it is successful. If an advert 
		  works well, the same technique can be used to advertise different things. So, 
		  for example, in winter if the weather is cold and you see a family having a 
		  warming cup of tea and feeling cosy, you may be interested and note the name 
		  of the tea ... Here the same technique is being used as with the cool, 
		  refreshing drink."""
n_prefix = 2
n_suffux = 1

def test_statistic_class():
	"""Тестирование .so обёртки для C++ структуры данных""" 
	p = StatistiCuM.statistic_counter()
	p.add('The is ')
	p.add('is the link')
	p.add('the ')
	p.add('the is')
	p.add('the ')

	# Тестирование обхода заколненной структуры методов get_next
	s = p.get_next()
	while(s != ''):
		assert(s != '')
		assert(s != None)
		# print(s)
		s = p.get_next()
	if p.get_by_number(2) != "is the link":
		raise AssertionError("Тест поиска префикса/суффикса по номеру")

	if p.get_by_pref('package') != 0:
		raise AssertionError("Тест поиска префикса/суффикса")


def test_prefix_statistic():
	p = PrefixStat(text, n_prefix)
	# print(p.most_common_in_text(2))


def test_suffix_statistic():
	"""Тестирование модуля подсчёта статистики суффиксов"""
	p = SuffixStat(text, n_suffux)
	# Тест самых часто встречающихся суффиксов в данном тексте
	if p.most_common_in_text_suffux(-10**20) != []:
		raise AssertionError("Тест самых часто встречающихся суффиксов в данном тексте 1")
	if p.most_common_in_text_suffux(-10) != []:
		raise AssertionError("Тест самых часто встречающихся суффиксов в данном тексте 2")
	if p.most_common_in_text_suffux(0) != []:
		raise AssertionError("Тест самых часто встречающихся суффиксов в данном тексте 3")
	if p.most_common_in_text_suffux(1) != [['to', 'the']]:
		raise AssertionError("Тест самых часто встречающихся суффиксов в данном тексте 4")
	if p.most_common_in_text_suffux(10) != [['if', 'can', 'be', 'of', 'is'],
											['they', 'it', 'so', 'advert', 'a', 'an', 'you',
											 'interested', 'tea', 'same', 'technique', 'used'],
											['people', 'then', 'do', 'study', 'again', 'these',
											 'are', 'teach', 'elements', 'advertising', 'learning',
											 'interest', 'experience', 'repetition', 'that', 'how',
											 'learn', 'achieve', 'this', 'respond', 'successful',
											 'works', 'well', 'us', 'try', 'something', 'advertise',
											 'different', 'things', 'for', 'example', 'in', 'winter',
											 'weather', 'cold', 'want', 'see', 'their', 'family', 'having',
											 'warming', 'cup', 'them', 'feeling', 'cosy', 'may', 'note',
											 'name', 'here', 'being', 'as', 'with', 'cool', 'refreshing', 'drink']]:
		raise AssertionError("Тест самых часто встречающихся суффиксов в данном тексте 5")
	if p.most_common_in_text_suffux(10**20) != [['if', 'can', 'be', 'of', 'is'],
											['they', 'it', 'so', 'advert', 'a', 'an', 'you',
											 'interested', 'tea', 'same', 'technique', 'used'],
											['people', 'then', 'do', 'study', 'again', 'these',
											 'are', 'teach', 'elements', 'advertising', 'learning',
											 'interest', 'experience', 'repetition', 'that', 'how',
											 'learn', 'achieve', 'this', 'respond', 'successful',
											 'works', 'well', 'us', 'try', 'something', 'advertise',
											 'different', 'things', 'for', 'example', 'in', 'winter',
											 'weather', 'cold', 'want', 'see', 'their', 'family', 'having',
											 'warming', 'cup', 'them', 'feeling', 'cosy', 'may', 'note',
											 'name', 'here', 'being', 'as', 'with', 'cool', 'refreshing', 'drink']]:
		raise AssertionError("Тест самых часто встречающихся суффиксов в данном тексте 6")


def print_test_passed(test_name):
	print("Test "+test_name+" "+'\033[42m'+"PASSED"+'\033[0m')


if __name__ == "__main__":
	test_name = ""
	try:
		test_name = "statistic_class"; test_statistic_class(); print_test_passed(test_name)
		# test_name = "prefix_statistic"; test_prefix_statistic(); print_test_passed(test_name)
		test_name = "suffix_statistic"; test_suffix_statistic(); print_test_passed(test_name)
		print("Well done!")
	except AssertionError as error:
		print("Test "+test_name+' '+'\033[101m'+"ERROR"+'\033[0m')
		print(error)
		print()