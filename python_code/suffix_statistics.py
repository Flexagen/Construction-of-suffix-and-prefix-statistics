import StatistiCuM
import string

class Suffix_Stat():
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
        
    

    def most_common_in_text(self, n):

        print(123)

        """Cамые часто встречающиеся суффиксы в данном текстов"""
        array = [[]]
        count = -1
        s = self.stat.get_next()
        while(s != ''):
            if (n == 0):
                break
            if(len(array) > 1 and array[len(array)-2][1] == array[len(array)-1][1]):
                n += 1    
            else:
                array.append([])
                count += 1
            array[count] = s.split(" ")
            s = self.stat.get_next()
            n -= 1
        return(array)

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