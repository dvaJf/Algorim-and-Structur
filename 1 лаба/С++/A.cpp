#include <iostream>
#include <vector>
using namespace std;

vector<int> SelectionSort(vector<int> b) {
    for (int i = 0; i < (int)b.size(); i++) {
        int max = -1000000000;
        int maxi = i;
        for (int j = i; j < (int)b.size(); j++) {
            if (b[j] > max) {
                max = b[j];
                maxi = j;
            }
        }
        int temp = b[i];
        b[i] = max;
        b[maxi] = temp;
    }
    return b;
}

int main() {
    vector<int> b;
    int x;
    while (cin >> x) b.push_back(x);

    b = SelectionSort(b);

    for (int i = 0; i < (int)b.size(); i++)
        cout << b[i] << (i + 1 < (int)b.size() ? " " : "\n");

    return 0;
}

