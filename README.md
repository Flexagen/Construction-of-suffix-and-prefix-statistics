# Construction-of-suffix-and-prefix-statistics
Задача №2 "Построение статистики суффиксов и префиксов"  
  
<table style="border-collapse: collapse; border: none;">
  <tr style="border: none;">
    <td style="border: none;"><b>Разработчики:</b> студенты группы 22207 ПрИн ИМИТ ПетрГУ <br>
                             <center> Афанасьев Артём <br>
                                        Павлов Максим <br>
                                        Кириллов Иван </center>
    </td>
  </tr>
</table>
  
Разработанная библиотека считает следующие статистики для суффиксов и префиксов:  
1. Cамые часто встречающиеся суффиксы/префиксы в данном тексте.  
2. Самые часто встречаемые суффиксы после заданного префикса.  
3. Средняя частота встречаемости заданного суффикса/префикса в текстах.  
4. Максимальная частота употребления заданного суффикса/префикса в текстах.  
  
## Содержание  
1. [Модуль статистики префиксов](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics#модуль-статистики-префиксов)
2. [Модуль статистики суффиксов](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics#модуль-статистики-суффиксов)
3. [Использование custom структуры для статистики суффиксов/префиксов](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics#использование-custom-структуры-для-статистики-суффиксовпрефиксов)
  
### Модуль статистики префиксов
Для подсчёта статистик и анализа префиксов в текстах был разработан python-класс PrefixStat. При инициализации достаточно указать строку с
текстом (можно и с многострочным) в первом аргументе, и кол-во слов в префиксе во втором.  
```python
from python_code.prefix_statistics import PrefixStat

# Пример использования PrefixStat. 
example = PrefixStat("Test text 1", 2)
example.add("Test text 2", 3)
print(example.most_common_in_text(0, 10))
```  
**Методы класса PrefixStat:**
1. **Добавление текста в структуру для анализа**<br>add(text, k) -> None<br>text - строка исходного текста, k - кол-во слов в префиксе 
<br><br>  
2. **Топ n по частоте префиксов в тексте index**<br>most_common_in_text(self, index, n) -> List[List]
<br><br>
3. **Самые часто встречаемые суффиксы после заданного префикса**<br>most_common_in_word(self, index, prefix, n, with_number=False) -> None
<br><br>
4. **Средняя частота встречаемости заданного префикса в текстах**<br>mean_frequency_of_occurrence(self, prefix) -> float
<br><br>
5. **Масимальная частота употребления заданного префикса в текстах**<br>max_frequency_of_prefix_occurrence(self, prefix) -> int

### Модуль статистики суффиксов
Для подсчёта статистик и анализа суффиксов в текстах был разработан python-класс SuffixStat. При инициализации достаточно указать строку с
текстом (можно и с многострочным) в первом аргументе, и кол-во слов в префиксе во втором, чтобы найти соответсвующие суффиксы после них.  
```python
from python_code.suffix_statistics import SuffixStat

# Пример использования SuffixStat. 
example = SuffixStat("Test text 1", 2)
example.add("Test text 2", 3)
print(example.most_common_in_text(0, 10))
```  
**Методы класса SuffixStat:**
1. **Добавление текста в структуру для анализа**<br>add(text, k) -> None<br>text - строка исходного текста, k - кол-во слов в префиксе 
<br><br>  
2. **Топ n по частоте суффиксов в тексте index**<br>most_common_in_text(self, index, n) -> List[List]
<br><br>
3. **Средняя частота встречаемости заданного суффикса в текстах**<br>mean_frequency_of_suffix_occurrence(self, suffix) -> float
<br><br>
4. **Масимальная частота употребления заданного суффикса в текстах**<br>max_frequency_of_suffix_occurrence(self, suffix) -> int 

### Использование custom структуры для статистики суффиксов/префиксов
Для хранения суффиксов/префиксов и их статистики была создана [собственная структура на C++](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics/blob/main/cpp_code/statistic_counter.cpp), в основе которой лежит бор укказателей, чтобы максимально оптимизировать и ускорить алгоритм Маркова.  
  
С помощью библиотки pybind11 созданная структура обёрнута в [python .so и .pyd библиотки](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics/blob/main/python_code) - "Статистикум" (StatistiCuM).
Обёртка класса была создана для двух ОС Windows и Linux (файлы .pyd и .so соответсвенно в /python_code). Для их получения достаточно установить через pip pybind11 и запустить скрипт сборки бибиотеки - /cpp_code/setup.py.  
```bash
python3 setup.py build_ext -i

# Для использования структуры необходимо только импортировать созданную обёртку
import StatistiCuM

# Которая будет перемычкой между разработанным классом
p = StatistiCuM.statistic_counter()
p.add('test')
print(p.get_next())
```  

<center><a>
    <img style="width: 350px" src="./images/main_image.jpg">
      <div style='width: 90%; text-align: center;'><b>Показательная схема внутренней работы созданных модулей</b></div>
</a></center><br>  

Для её тестирования и базового использования написаны [тесты](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics/blob/main/python_code/test.py) (функциональные, позитивные и негативные).
