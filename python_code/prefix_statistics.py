import statistics

class Prefix_Stat():
	def __init__(self, text, k):
		"""Инициализация. Поиск всех префиксов по полученному текстому"""
		self.stat = statistics.statistic_counter()
		words = text.split(' ')
		print(words)
		for cur in range(len(words)-k+1):
			prefix = ""
			for word_id in range(k):
				prefix += words[word_id+cur]+' '
			print(prefix)
			self.stat.add(prefix)

	def most_common_in_text(self):
		"""Cамые часто встречающиеся префиксы в данном текстов"""
		None

	def most_common_in_word(self):
		"""Самые часто встречаемые префиксы после заданного слова"""
		None

	def mean_frequency_of_occurrence(self, prefix):
		"""Средняя частота встречаемости заданного префикса в тексте"""
		None

	def average_length(self):
		"""Cредняя длина префиксов в данном тексте"""
		None

	def max_length(self):
		"""Максимальная длина найденных префиксов"""
		None

	def max_frequency_of_prefix_occurrence(self, prefix):
		"""Масимальная частота употребления заданного префикса в тексте"""
		None

if __name__ == "__main__":
	print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")