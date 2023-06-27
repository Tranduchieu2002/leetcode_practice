//
// Created by michael on 23/06/2023.
//

#ifndef ALGO_AFFINE_H
#define ALGO_AFFINE_H
#include <bits/stdc++.h>
using namespace std;

class affine {
    int a = 17 , b = 20;
    string s = "TWENTY FIFTEEN";
public:
    affine(string s, int a, int b) {
        this->s = s;
        this->a = a;
        this->b = b;
    }
    affine() {
    }
    string encode() {
        string ans;
        for(char c : s) {
            if(c == ' ') continue;
            char encodeChar = (a * (toupper(c) - 'A') + b) % 26 + 'A';
            ans.push_back(encodeChar);
        }
        return ans;
    }
    int extendedGCD(int a, int b, int& x, int& y) {
        if (a == 0) {
            x = 0;
            y = 1;
            return b;
        }

        int x1, y1;
        int gcd = extendedGCD(b % a, a, x1, y1);

        x = y1 - (b / a) * x1;
        y = x1;

        return gcd;
    }
    int modInverse(int a, int b) {
        int x, y;
        int gcd = extendedGCD(a, b,x ,y);

        if (gcd != 1) {
            return -1;
        }

        // Đảm bảo phần tử nghịch đảo là dương và nằm trong phạm vi modulo
        int inverse = (x % b + b) % b;

        return inverse;
    }
    string decode(string code) {
        const int i = modInverse(a,26);
        if(i == -1) return "Khong co ans";
        string ans = "";
        for(auto c : code) {
            if(c == ' ') continue;
            char encodeChar = (i * (toupper(c) - 'A' - b  + 26)) % 26 + 'A';
            ans.push_back(encodeChar);
        }
        return ans;
    }
};


#endif //ALGO_AFFINE_H
