#include <iostream>
#include <vector>
using namespace std;

vector<int> BubbleSort(vector<int> b) {
    for (int i = 0; i < (int)b.size(); i++) {
        for (int j = 0; j < (int)b.size() - 1 - i; j++) {
            if (b[j] < b[j + 1]) {
                int temp = b[j];
                b[j] = b[j + 1];
                b[j + 1] = temp;
            }
        }
    }
    return b;
}

int main() {
    vector<int> b;
    int x;
    while (cin >> x) b.push_back(x);

    b = BubbleSort(b);

    for (int i = 0; i < (int)b.size(); i++)
        cout << b[i] << (i + 1 < (int)b.size() ? " " : "\n");

    return 0;
}
