#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    long long w, h, n;
    if (!(cin >> w >> h >> n))
        return 0;

    long long l = 1;
    long long r = n * max(w, h);
    long long res = r;

    while (l <= r)
    {
        long long mid = l + (r - l) / 2;
        if ((mid / w) * (mid / h) >= n)
        {
            res = mid;
            r = mid - 1;
        }
        else
        {
            l = mid + 1;
        }
    }

    cout << res << "\n";

    return 0;
}
