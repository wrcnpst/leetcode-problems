#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        long long reversed = 0;
        long long temp = x;

        while (temp > 0) {
            int last = temp % 10;
            reversed = reversed * 10 + last;
            temp /= 10;
            cout << reversed, temp << endl;
        }

        return (reversed == x);
    }
};