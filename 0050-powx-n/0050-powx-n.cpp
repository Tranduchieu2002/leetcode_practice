class Solution {
public:
    double myPow(double x, int n) {
        // if(x == (double)1) return 1.00;
        double ans = 1;
        if(n < 0) {
            n = abs(n);
            x = 1 / x;
        }
        while(n > 0) {
            if(n % 2 == 0) {
                x = x * x;
                n = n / 2;
            } else {
                ans *= x;   
                n--;
            }
        }
        cout << ans << endl;
        return  ans;
    }
};