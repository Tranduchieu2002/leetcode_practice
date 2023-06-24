//
// Created by michael on 23/06/2023.
//
#include <bits/stdc++.h>
using namespace std;
#ifndef ALGO_SHIFT_CIPHER_H
#define ALGO_SHIFT_CIPHER_H


class shift_cipher {
    string s = "attack";
    unordered_map<char, int> mp;
    int k = 17; // 0 <= k <= 25
public:
    shift_cipher() {
        init_map();
    }
    void init_map() {
        for (char c = 'A'; c <= 'Z'; c++) {
            int value = c - 'A';  // Gán giá trị từ 1 đến 26
            mp[c] = value;  // Thêm cặp key-value vào unordered_map
        }
    }
    string removeSpaces(std::string str) {
        str.erase(remove(str.begin(), str.end(), ' '), str.end());
        return str;
    }
    char findKeyByValue(const unordered_map<char, int>& mp, int value) {
        for (const auto& pair : mp) {
            if (pair.second == value) {
                return pair.first;
            }
        }
        return ' '; // Return an empty string if the value is not found
    }
    string encode() {
        s = removeSpaces(s);
        int len = s.length();
        string ans;
        for(int i = 0; i < len; i++) {
            char val = toupper(s[i]);
            int key = (mp[val] + k) % 26;
            char foundByKey = findKeyByValue(mp,key);
            ans.push_back(foundByKey);
        }
        return ans;
    }
    string decode(string code) {
        int len = code.length();
        string ans;
        for(int i = 0; i < len; i++) {
            char val = toupper(code[i]);
            int key = (mp[val] - k + 26) % 26;
            char foundByKey = findKeyByValue(mp,key);
            ans.push_back(foundByKey);
        }
        return ans;
    }
};


#endif //ALGO_SHIFT_CIPHER_H
