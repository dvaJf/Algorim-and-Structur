#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    long long n, x, y;
    if (!(cin >> n >> x >> y))
        return 0;

    if (n == 1)
    {
        cout << min(x, y) << "\n";
        return 0;
    }

    long long l = 0;
    long long r = (n - 1) * min(x, y);
    long long res = r;

    while (l <= r)
    {
        long long mid = l + (r - l) / 2;
        if ((mid / x) + (mid / y) >= n - 1)
        {
            res = mid;
            r = mid - 1;
        }
        else
        {
            l = mid + 1;
        }
    }

    cout << res + min(x, y) << "\n";

    return 0;
}
