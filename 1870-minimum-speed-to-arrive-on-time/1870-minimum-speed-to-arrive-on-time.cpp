class Solution {
public:
    double calcTimeBySpeed(vector<int>& dist, int speed) {
        int n = dist.size();
        double sum = 0;
        for(int i = 0; i < n - 1; ++i) {
            sum += ceil((double)dist[i] / (double)speed);
        }
        
        sum += (double)dist[n - 1] / speed;
        return sum;
    }
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int n = dist.size();
        int left = 1, right = 1e7, speed;
        
        if(hour <= n - 1) return -1;
        
        cout << calcTimeBySpeed(dist, 2) << endl;
        
        while (left <= right) {
            int mid  =  (right - left) / 2 + left;
            
            if(calcTimeBySpeed(dist, mid) <=  hour) {
                speed = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
        }
        return speed;
    }
};