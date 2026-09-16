#include <iostream>
#include <vector>
using namespace std;

void CountSort(vector<int> &a)
{
    vector<int> s(101, 0);
    for (int x : a)
        s[x]++;

    int i = 0;
    for (int j = 0; j < 101; j++)
    {
        for (int x = 0; x < s[j]; x++)
        {
            a[i] = j;
            i++;
        }
    }
}

int main()
{
    vector<int> b;
    int x;
    while (cin >> x)
        b.push_back(x);

    CountSort(b);

    for (int i = 0; i < (int)b.size(); i++)
        cout << b[i] << (i + 1 < (int)b.size() ? " " : "\n");

    return 0;
}

