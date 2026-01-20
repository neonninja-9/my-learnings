#include <iostream>
#include <vector>
using namespace std;
int fibDP(int n, vector<int> &f)
{
    if (n == 0 || n == 1)
        return n;
    if (f[n] != -1)
        return f[n];
    f[n] = fibDP(n - 1, f) + fibDP(n - 2, f);
    return f[n];
}
int fibTab(int n)
{
    vector<int> f(n+1 , 0);
    f[1]=1;
    for(int i = 2 ; i<=n;i++){
        f[i] = f[i-1]+f[i-2];
    }
    return f[n];
}
int main()
{
    vector<int> f(7, -1);
    cout << fibDP(6, f) << endl;
    cout << fibTab(6) << endl;

    return 0;
}