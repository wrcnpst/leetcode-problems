#include<iostream>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return "";
        }

        string first = strs[0];
        string common = "";

        for (int i = 0; i < first.length(); ++i) {
            int commonCount = 0;
            for(const string &str : strs) {
                if (first[i] == str[i]) {
                    commonCount++;
                }
                else {
                    return common;
                }
                if (commonCount == strs.size()) {
                    common += first[i];
                }
            }
        }
        return common;
    }
};