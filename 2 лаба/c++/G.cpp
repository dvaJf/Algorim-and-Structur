#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, k;
    if (!(cin >> n >> k))
        return 0;

    vector<int> a(n);
    int max_val = 0;
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
        if (a[i] > max_val)
        {
            max_val = a[i];
        }
    }

    int l = 1;
    int r = max_val;
    int res = 0;

    while (l <= r)
    {
        int mid = l + (r - l) / 2;
        long long c = 0;

        for (int i = 0; i < n; ++i)
        {
            c += a[i] / mid;
        }

        if (c >= k)
        {
            res = mid;
            l = mid + 1;
        }
        else
        {
            r = mid - 1;
        }
    }

    cout << res << "\n";

    return 0;
}
