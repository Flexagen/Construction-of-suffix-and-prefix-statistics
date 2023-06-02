import StatistiCuM
import string


class PrefixStat:
    def __init__(self, text, k):
        """Инициализация. Поиск всех префиксов по полученному текстому"""
        self.stat = StatistiCuM.statistic_counter()
        words = list(filter(lambda word: word != '', text.translate(str.maketrans('', '', string.punctuation))  \
                            .replace('\t', '') \
                            .replace('\n', '') \
                            .split(' ')))
        # print(words)
        for cur in range(len(words) - k + 1):
            prefix = ""
            for word_id in range(k):
                prefix += words[word_id + cur] + ' '
            # print(prefix)
            self.stat.add(prefix)

    def most_common_in_text(self, n):
        """Cамые часто встречающиеся префиксы в данном текстов"""
        assert (n > 0)
        arr = [[]]
        count = 0
        current_n = None
        last_n = None
        s = self.stat.get_next()

        while s != ' ':
            if s == '':
                break
            data = s.split(' ')
            # print(s)
            last_n = current_n
            current_n = s[len(s) - 1]
            prefix = ""

            for word in data:
                if word == '':
                    break
                prefix += word + ' '

            if current_n != last_n and last_n is not None:
                arr.append([])
                count += 1

            if count == n:
                break

            arr[count].append(prefix[:len(prefix) - 1])
            s = self.stat.get_next()
        return list(filter(lambda x: x != [], arr))

    def most_common_in_word(self):
        """Самые часто встречаемые префиксы после заданного слова"""
        None

    def mean_frequency_of_occurrence(self, prefix):
        """Средняя частота встречаемости заданного префикса в текстах"""
        None

    def max_frequency_of_prefix_occurrence(self, prefix):
        """Масимальная частота употребления заданного префикса в тексте"""
        None


if __name__ == "__main__":
    print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")