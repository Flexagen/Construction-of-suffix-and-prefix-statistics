import StatistiCuM

class Suffix_Stat():
    def __init__(self, text, k):
        """Инициализация. Поиск всех суффиксов по полученному текстому"""
        self.stat = StatistiCuM.statistic_counter()
        words = text.split(' ')
        print(words)
        for cur in range(len(words)-k):
            suffix = ""
            suffix += words[cur+k]
            print(suffix)
            self.stat.add(suffix)



    def most_common_in_text(self, n):
        """Cамые часто встречающиеся префиксы в данном текстов"""
        # a = [1,2,3,4]
        # создать список топ три. n - длина списка
        # return(a)
        None

    def most_common_in_word(self):
        """Самые часто встречаемые префиксы после заданного слова"""
        # потом
        None

    def mean_frequency_of_occurrence(self, prefix):
        """Средняя частота встречаемости заданного суффикса в текстах"""
        # потом
        None

    def average_length(self):
        """Cредняя длина префиксов в данном тексте"""
        # число
        None

if __name__ == "__main__":
	print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")