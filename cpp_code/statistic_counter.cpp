#include<vector>
#include<iostream>

using namespace std;

class node{
public:
    node* prev;
    node* next[27];
    int count;
    node() {
        count = 0;
        prev = nullptr;
    }
};

class statistic_counter{

};

int main()
{

}