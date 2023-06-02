import StatistiCuM
import string

from typing import List


class PrefixStat:
    def __init__(self, text, k) -> None:
        """Инициализация. Поиск всех префиксов по полученному текстому"""
        self.stat = []
        self.text = []
        self.add(text, k)

    def add(self, text, k) -> None:
        self.stat.append(StatistiCuM.statistic_counter())
        self.text.append(list(filter(lambda word: word != '', text.translate(str.maketrans('', '', string.punctuation)) \
                                .replace('\t', '') \
                                .replace('\n', '') \
                                .split(' '))))
        index = len(self.stat)-1
        # print(self.text[index])
        for cur in range(len(self.text[index]) - k + 1):
            prefix = ""
            for word_id in range(k):
                prefix += self.text[index][word_id + cur] + ' '
            prefix = prefix[:len(prefix)-1]
            # print(prefix)
            self.stat[index].add(prefix.lower())

    def most_common_in_text(self, index, n) -> List[List]:
        """Cамые часто встречающиеся префиксы в данном текстов"""
        if n < 1 or index < 0 or index > len(self.stat)-1:
            return [[]]
        self.stat[index].set_pointer(0)
        arr = [[]]
        count = 0
        current_n = None
        last_n = None
        s = self.stat[index].get_next()
        # print(s)
        while s != ' ':
            if s == '':
                break
            data = s.split(' ')
            prefix = ' '.join(data[:-1])
            last_n = current_n
            current_n = data[len(data)-1]

            if current_n != last_n and last_n is not None:
                arr.append([])
                count += 1

            if count == n:
                break

            arr[count].append(prefix)
            s = self.stat[index].get_next()
        self.stat[index].set_pointer(0)
        return list(filter(lambda x: x != [], arr))

    def most_common_in_word(self) -> None:
        """Самые часто встречаемые префиксы после заданного слова"""
        None

    def mean_frequency_of_occurrence(self, prefix) -> None:
        """Средняя частота встречаемости заданного префикса в текстах"""
        arr = []
        for text in self.stat:
            arr.append(text.get_by_pref(prefix))
        return sum(arr)/len(arr)

    def max_frequency_of_prefix_occurrence(self, prefix) -> None:
        """Масимальная частота употребления заданного префикса в текстах"""
        max = 0
        for text in self.stat:
            if text.get_by_pref(prefix) > max:
                max = text.get_by_pref(prefix)
        return max


if __name__ == "__main__":
    print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")