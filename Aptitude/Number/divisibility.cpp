/*
Problem: A code to check the divisibility of number by 2,3,4,5,6,8,9,10,11.
code: divisibility.cpp
Name: Himanshu Shekhar (Pal)
*/

#include<iostream>
#include<cmath>

using namespace std;

int main()
{
    int number;

    cout << "\n Please enter an integer:";
    cin >> number;

    if (number % 2 == 0)
        cout << number << " is divisible by 2." << endl;
    else if (number % 3 == 0)
        cout << number << " is divisible by 3." << endl;
    else if (number % 4 == 0)
        cout << number << " is divisible by 4." << endl;
    else if (number % 5 == 0)
        cout << number << " is divisible by 5." << endl;
    else if (number % 6 == 0)
        cout << number << " is divisible by 6." << endl;
    else if (number % 8 == 0)
        cout << number << " is divisible by 8." << endl;
    else if (number % 9 == 0)
        cout << number << " is divisible by 9." << endl;
    else if (number % 10 )
        cout << number << " is divisible by 10." << endl;
    else if (number % 11)
        cout << number << " is divisible by 11." << endl;
    
return 0;
}
