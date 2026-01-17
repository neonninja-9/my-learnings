#include <iostream>
using namespace std;
int linearSearch(int arr[], int size, int target)
{
    for (int i = 0; i <= size - 1; i++)
    {
        if (arr[i] == target)
        {
            return i;
        }
    }
    return -1;
}
int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = sizeof(arr) / sizeof(arr[0]);
    cout << linearSearch(arr, size, 9) << endl;

    return 0;
}