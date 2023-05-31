#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

// Ето вам не надо
class node{
public:
    node* prev;
    node* next[27];
    int count;
    int pos;
    char c;
    node(){
        count = 0;
        pos = 0;
        prev = nullptr;
        for (int i = 0; i < 27; i++)
            next[i] = nullptr;
    }
};

// Вам надо ето
class statistic_counter{
private:
    node** statistic = new node*[200000000];
    node* root;
    std::pair<int, int>* count = new std::pair<int, int>[1000000];
    int size;
    int pointer;
public:
    statistic_counter() {
        root = new node();
        for (int i = 0; i < 100000; i++)
            count[i] = {0, 0};
        size = 0;
        pointer = 0;
    }
// Добавление для префикса - просто слово передать, для суффикса - чуть посложнее ;)
    void add(std::string pref)
    {
        node* cur = root;
        int len = pref.length();
        for (int i = 0; i < len; i++){
            if (pref[i] >= 'A' && pref[i] <= 'Z')
                pref[i] = pref[i] - 'A' + 'a';
            int j = pref[i] - 'a';
            if (pref[i] == ' ') {
                j = 26;
            }
            if (cur->next[j] == nullptr){
                cur->next[j] = new node();
                cur->next[j]->prev = cur;
                cur = cur->next[j];
                cur->c = pref[i];
                if (i == len - 1)
                {
                    cur->count++;
                    count[cur->count].second ++;
                    cur->pos = size;
                    statistic[size] = cur;
                    size ++;
                }
            }
            else{
                cur = cur->next[j];
                if (i == len - 1){
                    cur->count++;
                    if (cur->count != 1){
                        if (count[cur->count - 1].second != count[cur->count - 1].first) {
                            int prev_pos = statistic[count[cur->count - 1].first]->pos;
                            statistic[count[cur->count - 1].first]->pos = cur->pos;
                            std::swap(statistic[count[cur->count - 1].first], statistic[cur->pos]);
                            cur->pos = prev_pos;
                        }
                    }
                    else {
                        cur->pos = size;
                        statistic[size] = cur;
                        size ++;
                    }
                    count[cur->count - 1].first++;
                    count[cur->count].second++;
                }
            }
        }
    }

// Получение числа префиксов/суффикса pref
    int get_by_pref(std::string pref)
    {
        node* cur = root;
        int len = pref.length();
        bool fl = true;
        for (int i = 0; i < len; i++){
            int j = pref[i] - 'a';
            if (pref[i] == ' ')
                j = 26;
            if (cur->next[j] != nullptr)
                cur = cur->next[j];
            else{
                fl = false;
                break;
            }
        }
        return (fl ? cur->count : 0);
    }

// Получение k-го по встречаемости преффикса/суффикса
    std::string get_by_number(int k)
    {
        k --;
        node* cur = statistic[k];
        std::string result = "";
        while(cur->prev != nullptr) {
            result = cur->c + result; 
            cur = cur->prev;
        }
        return result;
    }

// Получение следующего по встречаемости преффикса/суффикса я хз как нормально сделать поэтому колличество тупо через пробел верну
// Можно while get_next(): использовать чтобы все слова получить.
    std::string get_next()
    {
        if (pointer >= size)
            return "";
        node* cur = statistic[pointer];
        std::string result = "";
        int count = cur->count;
        while(count > 0){
            result = result + (char)((count % 10) + '0');
            count /= 10;
        }
        result = get_by_number(pointer + 1) + " " + result;
        pointer++;
        return result;
    }

// Изменение текущего по встречаемости преффикса/суффикса возвращает текущий номер слова
    int set_pointer(int new_value){
        int old_pointer = pointer;
        pointer = new_value;
        return old_pointer;
    }

    ~statistic_counter() {
        delete [] statistic;
        delete [] count;
    }
};

// int main()
// {
//     statistic_counter s;
//     s.add("The is the link to");
//     s.add("is the link to");
//     s.add("is the link to");
//     s.add("is the link to");
//     s.add("the link to");
//     s.add("the");
//     s.add("the link to");
//     s.add("the");
//     s.add("the");
//     s.add("the");
//     s.add("the");
//     s.add("the");
//     std::string p = s.get_next();
//     while(p != "")
//     {
//         std::cout << p << "\n";
//         p = s.get_next();
//     }
//     std::cout << s.get_by_number(2) << "\n";
// }

PYBIND11_MODULE(statistics, module_handle) {
    py::class_<statistic_counter>(module_handle, "statistic_counter")
        .def(py::init<>())
        .def("add", &statistic_counter::add)
        .def("get_by_pref", &statistic_counter::get_by_pref)
        .def("get_by_number", &statistic_counter::get_by_number)
        .def("get_next", &statistic_counter::get_next)
        .def("set_pointer", &statistic_counter::set_pointer);
}