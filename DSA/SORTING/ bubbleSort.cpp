#include <iostream>
#include <vector>
using namespace std;
void bubbleSort(vector<int>& arr){
    int n = arr.size();
    int swapped;
    for(int i = 0 ; i <=n ;i++){
        swapped = false;
        for(int j = 0; j < n - i - 1;j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if(!swapped){
            break;
        }
    }

}
int main() {
    vector<int> arr = {1,3,4,5,7,4,3,7,9};
    bubbleSort(arr);
    for (int i : arr)
        cout << i << " ";
    cout << endl;
    return 0;
}