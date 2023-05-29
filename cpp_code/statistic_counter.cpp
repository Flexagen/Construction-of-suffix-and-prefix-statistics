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
        for (int i = 0; i < 27; i++)
            next[i] = nullptr;
    }
};

class statistic_counter{
private:
    node* statistic[10000000];
public:

};

int main()
{

}