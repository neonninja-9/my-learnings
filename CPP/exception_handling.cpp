#include <iostream>
#include <string>
using namespace std;

int main()
{

    try
    {
        int a, b;
        cout << "Enter number 1: ";
        cin >> a;
        cout << "Enter number 2: ";
        cin >> b;
        if (b == 0)
        {
            throw string("DivideByZero");
        }
        else
        {
            cout << float(a )/ b << endl;
        }
    }
    catch (string error)
    {
        cout << error<<endl;
    }
    return 0;
}