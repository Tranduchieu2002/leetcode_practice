//
// Created by michael on 29/06/2023.
//

#ifndef ALGO_HILL_H
#define ALGO_HILL_H
#include "../Utils.h"
#include <bits/stdc++.h>
using namespace std;
class Hill : Utils {
    int m = 2;
    int len;
    int mod = 26;
    vector<vector<int>> K = {{ 3, 3 }, { 2, 5}};
    string s;
public:
    int determinant(const vector<vector<int>>& matrix) {
        int n = matrix.size();

        // Trường hợp cơ bản: ma trận 1x1
        if (n == 1) {
            return matrix[0][0];
        }

        int det = 0.0;
        int sign = 1;

        // Khai triển theo hàng đầu tiên
        for (int j = 0; j < n; j++) {
            // Tạo ma trận con bằng cách loại bỏ hàng đầu và cột j
            vector<vector<int>> submatrix(n - 1, vector<int>(n - 1, 0));

            for (int k = 1; k < n; k++) {
                for (int l = 0, m = 0; l < n; l++) {
                    if (l != j) {
                        submatrix[k - 1][m++] = matrix[k][l];
                    }
                }
            }

            // Đệ quy tính định thức ma trận con
            double subdet = determinant(submatrix);

            // Tính định thức của ma trận A bằng cách lấy tổng các phần tử được khai triển
            det += sign * matrix[0][j] * subdet;

            // Đổi dấu để khai triển hàng tiếp theo
            sign = -sign;
        }

        return det % mod;
    }
    // Hàm tính ma trận chuyển vị
    vector<vector<int>> transposeMatrix(const vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<vector<int>> transpose(cols, vector<int>(rows, 0.0));

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transpose[j][i] = matrix[i][j];
            }
        }

        return transpose;
    }
    vector<vector<int>> cofactorMatrix(const vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<vector<int>> cofactor(rows, vector<int>(cols, 0.0));

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Tạo ma trận con bằng cách loại bỏ hàng i và cột j
                vector<vector<int>> submatrix(rows - 1, vector<int>(cols - 1, 0.0));

                int p = 0;
                int q = 0;

                for (int k = 0; k < rows; k++) {
                    for (int l = 0; l < cols; l++) {
                        if (k != i && l != j) {
                            submatrix[p][q++] = matrix[k][l];

                            if (q == cols - 1) {
                                q = 0;
                                p++;
                            }
                        }
                    }
                }

                // Tính định thức của ma trận con
                int subdet = determinant(submatrix);

                // Đổi dấu theo quy tắc (-1)^(i+j)
                int sign = ((i + j) % 2 == 0) ? 1.0 : -1.0;

                // Gán giá trị phụ đại số cho phần tử tương ứng
                cofactor[i][j] = (sign * subdet) < 0 ? (sign * subdet) + 26 : (sign * subdet) % mod;
            }
        }

        return cofactor;
    }

    // Hàm nhân hai ma trận
    vector<vector<int>> multiplyMatrix(const vector<vector<int>>& matrix1, const vector<vector<int>>& matrix2) {
        int rows1 = matrix1.size();
        int cols1 = matrix1[0].size();
        int cols2 = matrix2[0].size();

        vector<vector<int>> result(rows1, vector<int>(cols2, 0));

        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                for (int k = 0; k < cols1; k++) {
                    result[i][j] = (result[i][j] + (matrix1[i][k] * matrix2[k][j])) % mod;
                }
            }
        }

        return result;
    }
    string encode(string s) {
        string ans;
        len = s.size();
        vector<vector<char>> temp;
        vector<vector<int>> matrixEncode;
        //
        for (int i = 0; i < len; i += m) {
            vector<char> group;
            vector<int> mt;
            for (int j = i; j < i + m; j++) {
                char character = 'X';
                if (j < len) {
                    character = s[j];
                }
                int encodeChar = ((toupper(character) - 'A')) % 26;
                mt.push_back(encodeChar);
                group.push_back(character);
            }
            matrixEncode.push_back(mt);
            temp.push_back(group);
        }
        // end init
        vector<vector<int>> multipliedMatrix = multiplyMatrix(matrixEncode, K);
        for (const auto& group : multipliedMatrix) {
            for (const auto &character: group) {
                char encodeChar = (character + 'A');
                ans.push_back(encodeChar);
            }
            cout << '\n';
        }
        return ans;
    }



    string decode(string s) {
        string ans;
        int len = s.size();
        int detK = determinant(K);
        cout <<"Det(K) = " << detK << '\n';
        int kInverse = Utils().modInverse(detK, mod);
        cout <<"Det(K)^-1 = " << kInverse << '\n';
        vector<vector<int>> adjugate = this->scalarMultiplication(cofactorMatrix(transposeMatrix(K)), kInverse, mod);




        vector<vector<char>> temp;
        vector<vector<int>> matrixEncode;
        //
        for (int i = 0; i < len; i += m) {
            vector<char> group;
            vector<int> mt;
            for (int j = i; j < i + m; j++) {
                char character = 'X';
                if (j < len) {
                    character = s[j];
                }
                int encodeChar = ((toupper(character) - 'A')) % 26;
                mt.push_back(encodeChar);
                group.push_back(character);
            }
            matrixEncode.push_back(mt);
            temp.push_back(group);
        }

        vector<vector<int>> multipliedMatrix = multiplyMatrix(matrixEncode, adjugate);

        // end init
        for (const auto& group : multipliedMatrix) {
            for (const auto &character: group) {
                char encodeChar = (character + 'A');
                ans.push_back(encodeChar);
            }
            cout << '\n';
        }
        return ans;
    }

    void printMatrix(const vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
    }
};


#endif //ALGO_HILL_H
