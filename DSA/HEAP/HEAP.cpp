#include <vector>
#include <iostream>
using namespace std;

class HEAP
{
private:
    vector<int> heap;

public:
    HEAP(){
        cout<<"Heap Created"<<endl;
    }
    ~HEAP(){

    }
    void push(int val)
    {
        heap.push_back(val);
        int x = heap.size() - 1; // child index
        int parIdx = (x - 1) / 2;
        while (heap[x] > heap[parIdx] && parIdx >= 0)
        {
            swap(heap[x], heap[parIdx]);
            x=parIdx;
            parIdx=(x-1)/2;
        }
    }
    void heapify(int i){
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int largest = i;

        if (left < heap.size() && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < heap.size() && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != i) {
            swap(heap[i], heap[largest]);
            heapify(largest);
        }
    }
    void pop()
    {
        //step 1: swap root and last child of CBT
        swap(heap[0], heap[heap.size()-1]);
        //step 2: delete last one
        heap.pop_back();
        //step 3:fix heap
        heapify(0);
    }
    int top()
    {
        return heap[0];
    }
    bool empty()
    { return heap.size()==0;
    }
};
int main(){
    HEAP heap;
    heap.push(10);
    heap.push(20);
    heap.push(5);
    heap.push(30);
    heap.push(15);

    cout << "Top: " << heap.top() << endl; // should be 30

    heap.pop();
    cout << "After pop, Top: " << heap.top() << endl; // should be 20

    heap.pop();
    cout << "After pop, Top: " << heap.top() << endl; // should be 15

    return 0;
}
