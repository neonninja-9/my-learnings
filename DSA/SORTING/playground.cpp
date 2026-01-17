#include <iostream>
#include <vector>
using namespace std;
int partition(vector<int> &arr, int st, int end);
void quicksort(vector<int> &arr, int st, int end)
{
    if (st >= end)
    {
        return;
    }
    int pivot = partition(arr, st, end);
    quicksort(arr, st, pivot - 1);
    quicksort(arr, pivot + 1, end);
}
int partition(vector<int> &arr, int st, int end)
{
    int pivot = arr[end];
    int i = st - 1;
    for (int j = st; j < end; j++)
    {
        if (arr[j] <= pivot)
        {
            swap(arr[++i], arr[j]);
        }
    }
    swap(arr[++i], arr[end]);
    return i;
}
int main()
{
    vector<int> arr = {1, 3, 4, 5, 7, 4, 3, 7, 9};
    quicksort(arr, 0, arr.size() - 1);
    for (int i : arr)
    {
        cout << i << " ";
    }
    cout << endl;
    return 0;

    return 0;
}