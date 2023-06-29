//
// Created by michael on 29/06/2023.
//

#ifndef ALGO_UTILS_H
#define ALGO_UTILS_H
#include <vector>
using  namespace std;
class Utils {
public:
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

    vector<vector<int>> scalarMultiplication( const std::vector<std::vector<int>>& matrix, int scalar, int mod) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        // Create a new matrix to store the result
        vector<vector<int>> result(rows, vector<int>(cols));

        // Perform scalar multiplication on each element of the matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = (scalar * matrix[i][j]) % mod;
            }
        }

        return result;
    }

};


#endif //ALGO_UTILS_H
