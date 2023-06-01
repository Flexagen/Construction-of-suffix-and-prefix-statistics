import statistiCuM

class Suffix_Stat():
    def __init__(self, text, k):
        """Инициализация. Поиск всех суффиксов по полученному текстому"""
        self.stat = statistiCuM.statistic_counter()
        words = text.split(' ')
        print(words)
        for cur in range(len(words)-k):
            suffix = ""
            suffix += words[cur+k]
            print(suffix)
            self.stat.add(suffix)




if __name__ == "__main__":
	print("Нас Reboot, а мы крепчаем ʕ ᵔᴥᵔ ʔ")