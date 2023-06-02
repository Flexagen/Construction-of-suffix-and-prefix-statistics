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
  
### Использование custom структуры для статистики суффиксов/префиксов
Для хранения суффиксов/префиксов и их статистики была создана [собственная структура на C++](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics/blob/main/cpp_code/statistic_counter.cpp), в основе которой лежит бор укказателей, чтобы максимально оптимизировать и ускорить алгоритм Маркова.  
  
С помощью библиотки pybind11 созданная структура обёрнута в [python .so библиотку](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics/blob/main/python_code/statistics.so).
Обёртка класса была создана для двух ОС Windows и Linux (файлы .pyd и .so соответсвенно в /python_code). Для их получения достаточно установить через pip pybind11 и запустить скрипт сборки бибиотеки - /cpp_code/setup.py.  
```bash
python3 setup.py build_ext -i
```  
Для её тестирования и базового использования написаны [мини-тесты](https://github.com/Flexagen/Construction-of-suffix-and-prefix-statistics/blob/main/python_code/test.py) (функциональные, позитивные и негативные).  
```python
# Для использования структуры необходимо только импортировать созданную обёртку
import StatistiCuM

# Которая будет перемычкой между разработанным классом
p = StatistiCuM.statistic_counter()
p.add('test')
print(p.get_next())
```  
  
<img width="90%" src="./images/main_image.jpg">