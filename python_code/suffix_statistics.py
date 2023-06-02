import StatistiCuM
import string

from typing import List


class SuffixStat:
    def __init__(self, text, k) -> None:
        """Инициализация. Поиск всех суффиксов по полученному текстому"""
        self.stat = []
        self.text = []
        self.add(text, k)

    def add(self, text, k) -> None:
        self.stat.append(StatistiCuM.statistic_counter())
        self.text.append(list(filter(lambda word: word != '', text.translate(str.maketrans('', '', string.punctuation)) \
                                .replace('\t', '') \
                                .replace('\n', '') \
                                .split(' '))))
        # print(words)
        index = len(self.stat)-1
        for cur in range(len(self.text[index]) - k):
            suffix = self.text[index][cur+k]
            # print (list(suffix))
            self.stat[index].add(suffix.lower())
        
    
    def most_common_in_text_suffux(self, index, n) -> List:
        """Cамые часто встречающиеся суффиксы в данном тексте"""
        if n < 1 or index < 0 or index > len(self.stat) - 1:
            return []
        self.stat[index].set_pointer(0)
        arr = [[]]
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
        self.stat[index].set_pointer(0)
        return list(filter(lambda x: x != [], arr))

    def max_frequency_of_suffix_occurrence(self, suffix):
        """Максимальная частота употребления заданного суффикса в текстах"""
        max = 0
        for text in self.stat:
            if max < text.get_by_pref(suffix):
                max = text.get_by_pref(suffix)
        return (max)
        

    def mean_frequency_of_suffix_occurrence(self, suffix):
        """Средняя частота встречаемости заданного суффикса в текстах"""
        arr = []
        for text in self.stat:
            arr.append(text.get_by_pref(suffix))
        return sum(arr) / len(arr)

if __name__ == "__main__":
	print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")
