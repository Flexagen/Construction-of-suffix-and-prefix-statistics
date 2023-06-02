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

	n = p.get_size()
	for i in range(1, n+1):
		if p.get_by_number(i) == p.get_next():
			raise AssertionError("Тест поиск префикса/суффикса по номеру")

	if p.get_by_number(1) != 'The is ':
		raise AssertionError("Тест проверки в структуре слова с маленьких букв")

def test_prefix_statistic():
	p = PrefixStat(text, n_prefix)

	# Тест самых часто встречающихся префиксов в данном тексте
	if p.most_common_in_text(-10 ** 20) != []:
		raise AssertionError("Тест самых часто встречающихся префиксов в данном тексте 1")
	if p.most_common_in_text(-10) != []:
		raise AssertionError("Тест самых часто встречающихся префиксов в данном тексте 2")
	if p.most_common_in_text(0) != []:
		raise AssertionError("Тест самых часто встречающихся префиксов в данном тексте 3")
	if n_prefix == 2 and p.most_common_in_text(1) != [['if an', 'an advert', 'be interested', 'the same', 'same technique']]:
		raise AssertionError("Тест самых часто встречающихся префиксов в данном тексте 4")
	if n_prefix == 2 and p.most_common_in_text(10) != [['if an', 'an advert', 'be interested', 'the same', 'same technique'],
									 ['so that', 'that they', 'they can', 'can teach', 'teach them',
									  'them to', 'to respond', 'respond to', 'to their', 'their advertising',
									  'advertising they', 'they want', 'want us', 'us to', 'to be', 'how people',
									  'interested to', 'to try', 'try something', 'something and', 'and then',
									  'then to', 'to do', 'do it', 'it again', 'again these', 'these are',
									  'are the', 'the elements', 'elements of', 'of to', 'to learning',
									  'learning interest', 'interest experience', 'experience and', 'and repetition',
									  'repetition if', 'advertisers study', 'study how', 'advert can',
									  'can achieve', 'achieve this', 'this it', 'it is', 'is successful',
									  'successful if', 'advert works', 'works well', 'well the', 'people learn',
									  'learn so', 'technique can', 'can be', 'be used', 'used to', 'to advertise',
									  'advertise different', 'different things', 'things so', 'so for', 'for example',
									  'example in', 'in winter', 'winter if', 'if the', 'the weather', 'weather is',
									  'is cold', 'cold and', 'and you', 'you see', 'see a', 'a family',
									  'family having', 'having a', 'a warming', 'warming cup', 'cup of',
									  'of tea', 'tea and', 'and feeling', 'feeling cosy', 'cosy you', 'you may',
									  'may be', 'interested and', 'and note', 'note the', 'the name', 'name of',
									  'of the', 'the tea', 'tea here', 'here the', 'technique is', 'is being',
									  'being used', 'used as', 'as with', 'with the', 'the cool', 'cool refreshing',
									  'refreshing drink']]:
		raise AssertionError("Тест самых часто встречающихся префиксов в данном тексте 5")
	if p.most_common_in_text_suffux(10 ** 20) != [['if an', 'an advert', 'be interested', 'the same', 'same technique'],
									 ['so that', 'that they', 'they can', 'can teach', 'teach them',
									  'them to', 'to respond', 'respond to', 'to their', 'their advertising',
									  'advertising they', 'they want', 'want us', 'us to', 'to be', 'how people',
									  'interested to', 'to try', 'try something', 'something and', 'and then',
									  'then to', 'to do', 'do it', 'it again', 'again these', 'these are',
									  'are the', 'the elements', 'elements of', 'of to', 'to learning',
									  'learning interest', 'interest experience', 'experience and', 'and repetition'
										 , 'repetition if', 'advertisers study', 'study how', 'advert can',
									  'can achieve', 'achieve this', 'this it', 'it is', 'is successful',
									  'successful if', 'advert works', 'works well', 'well the', 'people learn',
									  'learn so', 'technique can', 'can be', 'be used', 'used to', 'to advertise',
									  'advertise different', 'different things', 'things so', 'so for', 'for example',
									  'example in', 'in winter', 'winter if', 'if the', 'the weather', 'weather is',
									  'is cold', 'cold and', 'and you', 'you see', 'see a', 'a family',
									  'family having', 'having a', 'a warming', 'warming cup', 'cup of',
									  'of tea', 'tea and', 'and feeling', 'feeling cosy', 'cosy you', 'you may',
									  'may be', 'interested and', 'and note', 'note the', 'the name', 'name of',
									  'of the', 'the tea', 'tea here', 'here the', 'technique is', 'is being',
									  'being used', 'used as', 'as with', 'with the', 'the cool', 'cool refreshing',
									  'refreshing drink']]:
		raise AssertionError("Тест самых часто встречающихся префиксов в данном тексте 6")


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
	# if p.most_common_in_text_suffux(1) != [['to', 'the']]:
	# 	raise AssertionError("Тест самых часто встречающихся суффиксов в данном тексте 4")
	if p.most_common_in_text_suffux(3) != [['to', 'the'], ['and'], ['if', 'can', 'be', 'of', 'is']]:
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