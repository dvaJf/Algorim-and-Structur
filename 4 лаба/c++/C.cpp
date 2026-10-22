#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class MinHeap {
private:
    vector<long long> heap;

    void sift_up(int idx) {
        while (idx > 0) {
            int parent = (idx - 1) / 2;
            if (heap[idx] < heap[parent]) {
                swap(heap[idx], heap[parent]);
                idx = parent;
            } else {
                break;
            }
        }
    }

    void sift_down(int idx) {
        int n = heap.size();
        while (2 * idx + 1 < n) {
            int left = 2 * idx + 1;
            int right = 2 * idx + 2;
            int smallest = idx;
            if (heap[left] < heap[smallest]) {
                smallest = left;
            }
            if (right < n && heap[right] < heap[smallest]) {
                smallest = right;
            }
            if (smallest != idx) {
                swap(heap[idx], heap[smallest]);
                idx = smallest;
            } else {
                break;
            }
        }
    }

public:
    void clear() {
        heap.clear();
    }

    void add(long long val) {
        heap.push_back(val);
        sift_up(heap.size() - 1);
    }

    bool extract(long long &result) {
        if (heap.empty()) {
            return false;
        }
        result = heap[0];
        long long last = heap.back();
        heap.pop_back();
        if (!heap.empty()) {
            heap[0] = last;
            sift_down(0);
        }
        return true;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    MinHeap heap;
    string cmd;

    while (cin >> cmd) {
        if (cmd == "ADD") {
            long long n;
            cin >> n;
            heap.add(n);
        } else if (cmd == "CLEAR") {
            heap.clear();
        } else if (cmd == "EXTRACT") {
            long long res;
            if (heap.extract(res)) {
                cout << res << "\n";
            } else {
                cout << "CANNOT\n";
            }
        }
    }

    return 0;
}
