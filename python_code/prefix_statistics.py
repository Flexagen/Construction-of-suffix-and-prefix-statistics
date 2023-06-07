import string
import StatistiCuM

from typing import List
from accessify import private

class PrefixStat:
    def __init__(self, text, k) -> None:
        """Инициализация. Поиск всех префиксов по полученному текстому"""
        self.stat = []
        self.text = []
        self.add(text, k)

    def add(self, text, k) -> None:
        """Добавление текста для анализа статистики префиксов"""
        assert(type(text) == str and type(k) == int)
        self.stat.append(StatistiCuM.statistic_counter())
        self.text.append(list(filter(lambda word: word != '', text.translate(str.maketrans('', '', string.punctuation)) \
                                .replace('\t', '') \
                                .replace('\n', '') \
                                .split(' '))))
        index = len(self.stat)-1
        for cur in range(len(self.text[index]) - k + 1):
            prefix = ""
            for word_id in range(k):
                prefix += self.text[index][word_id + cur] + ' '
            prefix = prefix[:len(prefix)-1]
            self.stat[index].add(prefix.lower())

    def most_common_in_text(self, index, n) -> List[List]:
        """Cамые часто встречающиеся префиксы в данном текстов"""
        if type(index) != int or type(n) != int or n < 1 or index < 0 or index > len(self.stat)-1:
            return [[]]
        return self.most_common_in_statistic(self.stat[index], n)

    def most_common_in_word(self, index, prefix, n, with_number=False) -> List[List]:
        """Самые часто встречаемые суффиксы после заданного префикса"""
        if type(prefix) != str or type(index) != int or type(n) != int or n < 1 or index < 0 or index > len(self.stat)-1:
            return [[]]
        s = prefix.split(' ')
        suffux = StatistiCuM.statistic_counter()
        for cur in range(len(self.text[index]) - len(s) + 1):
            current_prefix = ""
            for word_id in range(len(s)):
                current_prefix += self.text[index][word_id + cur] + ' '
            current_prefix = current_prefix[:len(current_prefix) - 1]
            if current_prefix == prefix:
                suffux.add(self.text[index][word_id + cur + 1])
        return self.most_common_in_statistic(suffux, n, with_number=with_number)

    @private
    def most_common_in_statistic(self, stat, n, with_number=False) -> List[List]:
        """Создание списка из n по частоте элементов в структуре stat"""
        stat.set_pointer(0)
        arr = [[]]
        count = 0
        last_n = current_n = None
        s = stat.get_next()
        while s != ' ':
            if s == '':
                break
            data = s.split(' ')
            prefix = ' '.join(data[:-1])
            last_n = current_n
            current_n = data[len(data) - 1]
            if current_n != last_n and last_n is not None:
                arr.append([])
                count += 1
            if count == n:
                break
            arr[count].append(prefix+ ' ' + current_n if with_number else prefix)
            s = stat.get_next()
        stat.set_pointer(0)
        return list(filter(lambda x: x != [], arr))

    def mean_frequency_of_occurrence(self, prefix) -> float:
        """Средняя частота встречаемости заданного префикса в текстах"""
        if type(prefix) != str:
            return 0.0
        arr = []
        for text in self.stat:
            arr.append(text.get_by_pref(prefix))
        return sum(arr)/len(arr)

    def max_frequency_of_prefix_occurrence(self, prefix) -> int:
        """Максимальная частота употребления заданного префикса в текстах"""
        if type(prefix) != str:
            return 0
        max = 0
        for text in self.stat:
            if text.get_by_pref(prefix) > max:
                max = text.get_by_pref(prefix)
        return max


if __name__ == "__main__":
    print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")