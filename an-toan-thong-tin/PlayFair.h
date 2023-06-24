//
// Created by michael on 23/06/2023.
//

#ifndef ALGO_PLAYFAIR_H
#define ALGO_PLAYFAIR_H
#include <bits/stdc++.h>
using namespace std;
class PlayFair {
    char grid[5][5] =
            {
            {'M', 'I', 'N', 'H', 'A'},
            {'B', 'C', 'D', 'E', 'F'},
            {'G', 'K', 'L', 'O', 'P'},
            {'Q', 'R', 'S', 'T', 'U'},
            {'V', 'W', 'X', 'Y', 'Z'}
            };
    string input = "thuong mai dien tu";
    string keyword = "minh";
    vector<pair<char, char>> mp;
public:
    string removeSpaces(std::string str) {
        str.erase(remove(str.begin(), str.end(), ' '), str.end());
        return str;
    }
    pair<int, int> findElementIndex(char grid[][5], int rows, int cols, char s1, char s2) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == s1 && grid[i][j+1] == s2) {
                    return make_pair(i, j);
                }
            }
        }

        return make_pair(-1, -1); // Return (-1, -1) if the element is not found
    }

    void encode() {
        keyword = removeSpaces(keyword);
        if(input.length() % 2 == 1) input.push_back('x');
        int n = input.length();
        for(int i = 0; i < n; i+=2) {
            mp.push_back(make_pair(input[i], input[i+1]));
        }
        string ans;

        for(auto val : mp) {
            char s1 = toupper(val.first);
            char s2 = toupper(val.second);
            pair<int, int> is1;
            pair<int, int> is2;

            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (grid[i][j] == s1) {
                        is1 = make_pair(i, j);
                    }
                    if(grid[i][j] == s2) {
                        is2 = make_pair(i, j);
                    }
                }
            }
            // TH1 cùng hàng lấy chữ bên phải

            if(is1.first == is2.first) {
                string temp;
                if(is1.second == 5 - 1) {
                    ans.push_back(grid[is1.first][0]);
                }
                if(is2.second == 5 -1) {
                    ans.push_back(grid[is1.first][0]);
                }
                if(is1.second < 5 - 1 && is2.second < 5 - 1) {
                    ans.push_back(grid[is1.first][is1.second + 1]);
                    ans.push_back(grid[is2.first][is2.second + 1]);
                }
            }
            // TH2 cùng cột lấy cột dưới
            else if(is1.second == is2.second) {
                if(is1.first == 5 - 1) {
                    ans.push_back(grid[0][is1.second]);
                }
                if(is2.first == 5 -1) {
                    ans.push_back(grid[0][is2.second]);
                }
                if(is1.first < 5 - 1 && is2.first < 5 - 1) {
                    ans.push_back(grid[is1.first + 1][is1.second]);
                    ans.push_back(grid[is2.first + 1][is2.second]);
                }
            } else {
                ans.push_back(grid[is1.first][is2.second]);
                ans.push_back(grid[is2.first][is1.second]);
            }


        }
        cout << ans;
    }
};


#endif //ALGO_PLAYFAIR_H
