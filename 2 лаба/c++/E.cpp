#include <iostream>
#include <vector>

using namespace std;

bool cor(int mid, const vector<int>& a, int k) {
    int z = a[0];
    k = k - 1;
    for (size_t x = 1; x < a.size(); ++x) {
        if (a[x] - z >= mid) {
            k--;
            z = a[x];
        }
    }
    return k <= 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int l = 0;
    int r = a[n - 1] - a[0];
    int res = 0;

    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (cor(mid, a, k)) {
            res = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    cout << res << "\n";

    return 0;
}
