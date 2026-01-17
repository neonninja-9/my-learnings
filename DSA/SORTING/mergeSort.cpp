#include <iostream>
#include <vector>

using namespace std;

void mergeArray(vector<int>& arr, int st, int mid, int end) {
    vector<int> ans;
    int i = st;        
    int j = mid + 1;

    while(i <= mid && j <= end) {
        if(arr[i] < arr[j]) {
            ans.push_back(arr[i++]);
        } else {
            ans.push_back(arr[j++]);
        }
    }

    
    while(i <= mid) {
        ans.push_back(arr[i++]); 
    }
    while(j <= end) {
        ans.push_back(arr[j++]);
    }

    // Copying back to the original array
    for(int k = 0; k < ans.size(); k++) {
        arr[st + k] = ans[k];
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        mergeArray(arr, left, mid, right);
    }
}

int main() {
    vector<int> arr = {1, 3, 4, 5, 7, 4, 3, 7, 9};
    mergeSort(arr, 0, arr.size() - 1);
    
    for (int i : arr)
        cout << i << " ";
    cout << endl;
    
    return 0;
}
