import StatistiCuM
import string


class SuffixStat:
    def __init__(self, text, k):
        """Инициализация. Поиск всех суффиксов по полученному текстому"""
        self.stat = StatistiCuM.statistic_counter()
        words = text.translate(str.maketrans('', '', string.punctuation)).replace("\t","").replace("\n","").split(' ')
        # print(words)
        for cur in range(len(words)-k):
            suffix = ""
            suffix += words[cur+k]
            # print(suffix)
            self.stat.add(suffix)
        
    
    def most_common_in_text_suffux(self, n):
        """Cамые часто встречающиеся суффиксы в данном тексте"""

        """Cамые часто встречающиеся суффиксы в данном текстов"""
        array = []
        arr = [[]]
        if (n < 1):
            return array
        s = self.stat.get_next()
        prev = -1
        i = -1
        while s != "":
            if int(s.split(' ')[-1]) != prev:
                arr.append([])
                i += 1
            arr[i].append(s.split(' ')[:-1])

        return(arr)

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
