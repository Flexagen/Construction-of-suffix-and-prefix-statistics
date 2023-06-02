from typing import List
import StatistiCuM
import string


class SuffixStat:
    def __init__(self, text, k) -> None:
        """Инициализация. Поиск всех суффиксов по полученному текстому"""
        self.stat = []
        self.text = []
        self.add(text, k)

    def add(self, text, k) -> None:
        self.stat = StatistiCuM.statistic_counter()
        words = text.translate(str.maketrans('', '', string.punctuation)).replace("\t","").replace("\n","").split(' ')
        # print(words)
        for cur in range(len(words)-k):
            suffix = ""
            suffix += words[cur+k]
            # print(suffix)
            self.stat.add(suffix.lower())
        
    
    def most_common_in_text_suffux(self, index, n) -> List:
        """Cамые часто встречающиеся суффиксы в данном тексте"""
        self.stat[index].set_pointer(0)
        arr = [[]]
        if n < 1:
            return []
        s = self.stat[index].get_next()
        prev = -1
        count = -1

        while s != "":
            if int(s.split(' ')[-1]) != prev:
                arr.append([])
                prev = int(s.split(' ')[-1])
                count += 1
            if count == n:
                break
            arr[count].append(s.split(' ')[:-1][0])
            s = self.stat[index].get_next()
        self.stat.set_pointer(0)
        return list(filter(lambda x: x != [], arr))

    def max_frequency_of_suffix_occurrence(self, suffix, n_text, text):
        """Максимальная частота употребления заданного суффикса в текстах"""
        arr = []
        for text in self.stat:
            arr = text.translate(str.maketrans('', '', string.punctuation)).replace("\t","").replace("\n","").split(' ')
            arr = list(filter(lambda x: x != '', arr))
            while arr != '':
                n = 1
            # print(arr)
            return 
        

    def mean_frequency_of_suffix_occurrence(self, suffix, n_text):
        """Средняя частота встречаемости заданного суффикса в текстах"""
        # потом
        None

if __name__ == "__main__":
	print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")
