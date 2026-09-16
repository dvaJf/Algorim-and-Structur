#include <iostream>
#include <vector>
#include <string>
using namespace std;

int BubbleSort(vector<int>& b) {
    int c = 0;
    for (int i = 0; i < (int)b.size(); i++) {
        for (int j = 0; j < (int)b.size() - 1 - i; j++) {
            if (b[j] > b[j + 1]) {
                int temp = b[j];
                b[j] = b[j + 1];
                b[j + 1] = temp;
                c++;
            }
        }
    }
    return c;
}

int main() {
    string a;
    getline(cin, a);

    vector<int> b;
    int x;
    while (cin >> x) b.push_back(x);

    int result = BubbleSort(b);
    cout << result << endl;

    return 0;
}

