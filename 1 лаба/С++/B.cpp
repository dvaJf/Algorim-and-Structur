#include <iostream>
#include <vector>
using namespace std;

vector<int> InsertionSort(vector<int> a) {
    for (int i = 1; i < (int)a.size(); i++) {
        int key = a[i];
        int j = i;
        while (j >= 1 && a[j - 1] > key) {
            a[j] = a[j - 1];
            j--;
        }
        a[j] = key;
    }
    return a;
}

int main() {
    vector<int> a;
    int x;
    while (cin >> x) a.push_back(x);

    a = InsertionSort(a);

    for (int i = 0; i < (int)a.size(); i++)
        cout << a[i] << (i + 1 < (int)a.size() ? " " : "\n");

    return 0;
}

