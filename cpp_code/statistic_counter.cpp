#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<pybind11/pybind11.h>
#include<pybind11/stl.h>
#include<pybind11/numpy.h>

namespace py = pybind11;

//Ето вам не надо
class node{
public:
    node* prev;
    node* next[37];
    int count;
    int pos;
    std::string part;
    node(){
        count = 0;
        pos = 0;
        prev = nullptr;
        for (int i = 0; i < 37; i++)
            next[i] = nullptr;
    }
};


class index_error: public std::exception{
public:
    index_error(const std::string& message): message{message}{}
    const char* what() const noexcept override{
        return message.c_str();
    }
private:
    std::string message;
};


// Вам надо ето
class statistic_counter{
private:
    node** statistic = new node*[200000000];
    node* root;
    std::pair<int, int>* count = new std::pair<int, int>[20000000];
    int size;
    int pointer;
    node* split(node* cur, int& p){
        std::string prev_part(cur->part.begin(), cur->part.begin() + p);
        std::string new_part(cur->part.begin() + p, cur->part.end());
        int k = new_part[0] - 'a';
        if (new_part[0] == ' ')
            k = 26;
        if (new_part[0] >= '0' && new_part[0] <= '9')
            k = new_part[0] - '0' + 27;
        node* new_node = new node();
        new_node->prev = cur->prev;
        new_node->part = prev_part;
        new_node->next[k] = cur;
        k = prev_part[0] - 'a';
        if (prev_part[0] == ' ')
            k = 26;
        if (new_part[0] >= '0' && new_part[0] <= '9')
            k = new_part[0] - '0' + 27;
        cur->prev->next[k] = new_node;
        cur->prev = new_node;
        cur->part = new_part;
        return new_node;
    }

    void update_statistic(node* cur){
        if (cur->count != 1){
            if (count[cur->count - 1].second != count[cur->count - 1].first){
                int prev_pos = statistic[count[cur->count - 1].first]->pos;
                statistic[count[cur->count - 1].first]->pos = cur->pos;
                std::swap(statistic[count[cur->count - 1].first], statistic[cur->pos]);
                cur->pos = prev_pos;
            }
        }
        else{
            cur->pos = size;
            statistic[size] = cur;
            size ++;
        }
        count[cur->count - 1].first++;
        count[cur->count].second++;
    }

    node* create_node(std::string part){
        node* new_node = new node();
        new_node->part = part;
        new_node->count++;
        count[new_node->count].second ++;
        new_node->pos = size;
        statistic[size] = new_node;
        size ++;
        return new_node;
    }
    
public:
    statistic_counter(){
        root = new node();
        for (int i = 0; i < 100000; i++)
            count[i] = {0, 0};
        size = 0;
        pointer = 0;
    }

// Добавление преффикса/суффикса 
    void add(std::string pref){
        node* cur = root;
        int len = pref.length();
        for (int i = 0; i < len; i++){
            int j = pref[i] - 'a';
            if (pref[i] == ' ')
                j = 26;
            if (pref[i] >= '0' && pref[i] <= '9')
                j = pref[i] - '0' + 27;
            if (cur->next[j] == nullptr){
                std::string cur_part(pref.begin() + i, pref.end());
                cur->next[j] = create_node(cur_part);
                i = len - 1;
                cur->next[j]->prev = cur;
                cur = cur->next[j];
            }
            else{
                cur = cur->next[j];
                std::string cur_part(pref.begin() + i, pref.end());
                int p = 0;
                for (p = 0; p < cur->part.length() && p < cur_part.length() && cur->part[p] == cur_part[p]; p++);
                if (p < cur->part.length()){
                    cur = split(cur, p);
                    if (i + p < len) {
                        int k = pref[i + p] - 'a';
                        if (pref[i + p] == ' ')
                            k = 26;
                        if (pref[i] >= '0' && pref[i] <= '9')
                            k = pref[i] - '0' + 27;;
                        cur->next[k] = new node();
                        node* new_node = cur;
                        cur = cur->next[k];
                        cur->prev = new_node;
                        std::string s(cur_part.begin() + p, cur_part.end());
                        cur->part = s;
                    }
                    i = len - 1;
                }
                else
                    i += p - 1;
                if (i >= len - 1){
                    cur->count++;
                    update_statistic(cur);
                }
            }
        }
    }

// Получение числа префиксов/суффикса pref
    int get_by_pref(std::string pref){
        node* cur = root;
        int len = pref.length();
        bool fl = true;
        for (int i = 0; i < len; i++){
            int j = pref[i] - 'a';
            if (pref[i] == ' ')
                j = 26;
            if (pref[i] >= '0' && pref[i] <= '9')
                j = pref[i] - '0' + 27;
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
    std::string get_by_number(int k){
        k --;
        node* cur = statistic[k];
        if (k >= size)
            throw index_error("!Exeption: There is no k-th element!");
        std::string result = "";
        while(cur->prev != nullptr){
            result = cur->part + result; 
            cur = cur->prev;
        }
        return result;
    }

// Получение следующего по встречаемости преффикса/суффикса я хз как нормально сделать поэтому колличество тупо через пробел верну
// Можно while get_next(): использовать чтобы все слова получить.
    std::string get_next(){
        if (pointer >= size){
            set_pointer(0);
            return "";
        }
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

// Изменение текущего по встречаемости преффикса/суффикса возвращает текущий номер преффикса/суффикса
    int set_pointer(int new_value){
        int old_pointer = pointer;
        pointer = new_value;
        return old_pointer;
    }

    int get_size(){
        return size;
    }

    ~statistic_counter(){
        for (int i = 0; i < size; i++)
            delete statistic[i];
        delete [] statistic;
        delete [] count;
    }
};

// int main()
// {
//     statistic_counter s;
//     s.add("the is the link to019");
//     s.add("is the Link to");
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
//     while(p != ""){
//         std::cout << p << "\n";
//         p = s.get_next();
//     }
//     std::cout << s.get_by_number(4) << "\n";
// }

PYBIND11_MODULE(StatistiCuM, module_handle) {
    py::class_<statistic_counter>(module_handle, "statistic_counter")
        .def(py::init<>())
        .def("add", &statistic_counter::add)
        .def("get_by_pref", &statistic_counter::get_by_pref)
        .def("get_by_number", &statistic_counter::get_by_number)
        .def("get_next", &statistic_counter::get_next)
        .def("set_pointer", &statistic_counter::set_pointer)
        .def("get_size", &statistic_counter::get_size);
}