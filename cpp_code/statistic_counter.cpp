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
    node* statistic[10000000];
    node* root;
    int size;
    int pointer;
public:
    statistic_counter() {
        root = new node();
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
            if (pref[i] == ' ')
                j = 26;
            if (cur->next[j] == nullptr){
                cur->next[j] = new node();
                cur->next[j]->prev = cur;
                cur = cur->next[pref[j]];
                if (pref[i] == ' ')
                {
                    cur->count++;
                    cur->pos = size;
                    statistic[size] = cur;
                    size ++;
                }
                cur->c = pref[i];
            }
            else{
                cur->next[j];
                cur->count++;
                if (cur->pos > 0 && cur->count > statistic[cur->pos - 1]->count)
                {
                    cur->pos --;
                    statistic[cur->pos - 1]->pos ++;
                    std::swap(statistic[cur->pos - 1], statistic[cur->pos]);
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
        node* cur = statistic[pointer];
        std::string result = "";
        int count = cur->count;
        while(count > 0){
            result = result + (char)((count % 10) + '0');
            count /= 10;
        }
        result = get_by_number(pointer) + " " + result;
        pointer++;
        return result;
    }

// Изменение текущего по встречаемости преффикса/суффикса возвращает текущий номер слова
    int set_pointer(int new_value){
        int old_pointer = pointer;
        pointer = new_value;
        return old_pointer;
    }
};

// int main()
// {

// }

PYBIND11_MODULE(module_name, module_handle) {
    py::class_<statistic_counter>(module_handle, "statistic_counter")
        .def(py::init<>())
        .def("add", &statistic_counter::add)
        .def("get_by_pref", &statistic_counter::get_by_pref)
        .def("get_by_number", &statistic_counter::get_by_number)
        .def("get_next", &statistic_counter::get_next)
        .def("set_pointer", &statistic_counter::set_pointer);
}