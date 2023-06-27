//
// Created by michael on 23/06/2023.
//

#ifndef ALGO_SUBSTITUTION_CIPHER_H
#define ALGO_SUBSTITUTION_CIPHER_H
#include <bits/stdc++.h>

using namespace std;

class substitution_cipher {
    string s = "hanoimuathu";
    unordered_map<char, char> mp;
    int k = 17; // 0 <= k <= 25
public:
    substitution_cipher() {
        init_substitutionMap();
    }
    void init_substitutionMap() {
        mp = {
                {'a', 'X'},
                {'b', 'N'},
                {'c', 'Y'},
                {'d', 'A'},
                {'e', 'H'},
                {'f', 'P'},
                {'g', 'O'},
                {'h', 'G'},
                {'i', 'Z'},
                {'j', 'Q'},
                {'k', 'W'},
                {'l', 'B'},
                {'m', 'T'},
                {'n', 'S'},
                {'o', 'F'},
                {'p', 'L'},
                {'q', 'R'},
                {'r', 'C'},
                {'s', 'V'},
                {'t', 'M'},
                {'u', 'U'},
                {'v', 'E'},
                {'w', 'K'},
                {'x', 'J'},
                {'y', 'D'},
                {'z', 'I'},
        };
    }
    string encode() {
        string encodedMessage = "";

        for (char c : s) {
            if (mp.find(c) != mp.end()) {
                encodedMessage += mp[c];
            } else {
                encodedMessage += c;
            }
        }

        return encodedMessage;
    }
    string decode(string encodedMessage) {
        string decodedMessage = "";

        for (char c : encodedMessage) {
            bool found = false;

            for (const auto& pair : mp) {
                if (pair.second == c) {
                    decodedMessage += pair.first;
                    found = true;
                    break;
                }
            }

            if (!found) {
                decodedMessage += c;
            }
        }

        return decodedMessage;
    }

};


#endif //ALGO_SUBSTITUTION_CIPHER_H
