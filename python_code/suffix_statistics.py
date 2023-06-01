import StatistiCuM
import string


class Suffix_Stat:
    def __init__(self, text, k):
        """Инициализация. Поиск всех суффиксов по полученному текстому"""
        self.stat = StatistiCuM.statistic_counter()
        words = text.translate(str.maketrans('', '', string.punctuation)).replace("\t", "").replace("\n", "").split(' ')
        # print(words)
        for cur in range(len(words) - k):
            suffix = ""
            suffix += words[cur + k]
            # print(suffix)
            self.stat.add(suffix)

    def most_common_in_text_suffux(self, n):
        """Cамые часто встречающиеся суффиксы в данном тексте"""
        array = []
        s = self.stat.get_next()
        n = n + 1
        k = 0
        while s != '':
            if n > 0:
                n -= 1
                array.append(s.split(' '))
                if len(array) > 1 and array[len(array) - 2][1] == array[len(array) - 1][1]:
                    n += 1
            if k == 1:
                array = array[:-1]
                break
            if n == 0:
                k = 1
            s = self.stat.get_next()
        return array

    def most_common_in_word(self):
        """Самые часто встречаемые суффиксы после заданного слова"""
        # потом
        None

    def mean_frequency_of_occurrence(self, prefix):
        """Средняя частота встречаемости заданного суффикса в текстах"""
        # потом
        None

    def average_length(self, text):
        """Cредняя длина суффиксов в данном тексте"""
        count = 0
        avle = 0
        arr = text.translate(str.maketrans('', '', string.punctuation)).replace("\t", "").replace("\n", "").split(' ')
        words = [x for x in arr if x != '']
        # print(words)
        for i in range(len(words)):
            count += 1
            avle += len(words[i])
        print("Общая длина всех символов:", avle, "\nВсего слов:", count)
        avle /= count
        return "Средняя длина суффикса =>", avle


if __name__ == "__main__":
    print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")
