from typing import List
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
        
    
    def most_common_in_text_suffux(self, n) -> List:
        """Cамые часто встречающиеся суффиксы в данном тексте"""
        self.stat.set_pointer(0)
        arr = [[]]
        if n < 1:
            return []
        s = self.stat.get_next()
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
            s = self.stat.get_next()
        self.stat.set_pointer(0)
        return list(filter(lambda x: x != [], arr))

    def most_common_in_word(self, suffix, n_text, text):
        """Самые часто встречаемые суффиксы после заданного слова"""
        arr = []
        words = text.translate(str.maketrans('', '', string.punctuation)).replace("\t","").replace("\n","").split(' ')
        
        print(words)
        return words
        

    def mean_frequency_of_occurrence(self, suffix, n_text):
        """Средняя частота встречаемости заданного суффикса в текстах"""
        # потом
        None

if __name__ == "__main__":
	print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")
