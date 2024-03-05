#include <iostream>

using namespace std;

class Solution {
public:
    int charToInt(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000; 
            default: throw invalid_argument("Invalid Roman numeral: ");
        }
    }

    int romanToInt(string s) {
        int total = 0;
        int slen = s.size();
        int i = 0;
        while (i < slen-1) {
            int curInt = charToInt(s[i]);
            int nextInt = charToInt(s[i+1]);
            if(curInt >= nextInt) {
                total += curInt;
            }
            else {
                total -= curInt;
            }
            i++;
        }
        total += charToInt(s[slen-1]);
        return total;
    }

};