#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
template <typename T = int>
class Heap
{
    vector<T> heap;

public:
    void heapifyDown(int node)
    {
        int left = 2 * node + 1;
        int right = 2 * node + 2;
        int smallest = node;

        if (left < heap.size() && heap[left] < heap[smallest])
        {
            smallest = left;
        }
        if (right < heap.size() && heap[right] < heap[smallest])
        {
            smallest = right;
        }

        if (smallest != node)
        {
            swap(heap[node], heap[smallest]);
            heapifyDown(smallest);
        }
    }

    void heapifyUp(int node)
    {
        if (node == 0)
            return;
        int parent = (node - 1) / 2;
        if (heap[node] < heap[parent])
        {
            swap(heap[node], heap[parent]);
            heapifyUp(parent);
        }
    }
    void push(T val)
    {
        heap.push_back(val);
        heapifyUp(heap.size() - 1);
    }
    void pop()
    {
        if (empty())
            return;
        swap(heap[0], heap[heap.size() - 1]);
        heap.pop_back();
        if (!empty())
            heapifyDown(0);
    }
    T top()
    {
        if (empty())
            throw runtime_error("Heap is empty");
        return heap[0];
    }
    bool empty()
    {
        return (heap.size() == 0);
    }
};
template <class T>
class priorityqueue
{

public:
    Heap<int> h;

    void push(int val)
    {
        h.push(val);
    }
    void pop()
    {
        h.pop();
    }
    int top()
    {
        return h.top();
    }
    bool empty()
    {
        return h.empty();
    }
};
int main()
{

    return 0;
}