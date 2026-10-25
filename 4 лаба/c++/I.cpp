#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 1e9;

int main() {
    int n, k, p;
    if (!(cin >> n >> k >> p)) 
        return 0;

    vector<int> z(p);
    for (int i = 0; i < p; ++i) {
        cin >> z[i];
    }

    vector<int> pos(p, INF);
    vector<int> last(n + 1, -1);

    for (int i = p - 1; i >= 0; --i) {
        int car = z[i];
        if (last[car] != -1) {
            pos[i] = last[car];
        }
        last[car] = i;
    }

    vector<bool> pol(n + 1, false);
    int pol_size = 0;
    vector<int> nx(n + 1, 0);
    priority_queue<pair<int, int>> h;
    int res = 0;

    for (int i = 0; i < p; ++i) {
        int car = z[i];

        if (pol[car]) {
            nx[car] = pos[i];
            h.push({pos[i], car});
            continue;
        }

        if (pol_size == k) {
            while (!h.empty()) {
                auto top_element = h.top();
                int next_pos_in_heap = top_element.first;
                int car_in_heap = top_element.second;
                h.pop();

                if (pol[car_in_heap]) {
                    if (nx[car_in_heap] == next_pos_in_heap) {
                        pol[car_in_heap] = false;
                        pol_size--;
                        break;
                    }
                }
            }
        }

        pol[car] = true;
        pol_size++;
        res++;
        nx[car] = pos[i];
        h.push({pos[i], car});
    }

    cout << res << endl;

    return 0;
}
