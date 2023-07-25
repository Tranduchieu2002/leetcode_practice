/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findLeftSide(int left, int right, int target ,  MountainArray &arr) {
        
        while(left <= right) {
            int mid = (right - left ) / 2 + left;
            
            if(arr.get(mid) == target) return mid;
            
            if(arr.get(mid) < target) {
                left = mid + 1;
            } else {
                right =  mid - 1;
            }
        }
        return -1;
    }
    int findRightSide(int left, int right, int target ,  MountainArray &arr) {
        
        while(left <= right) {
            int mid = (right - left ) / 2 + left;

            if(arr.get(mid) == target) return mid;
            
            if(arr.get(mid) > target) {
                left = mid + 1;
            } else {
                right =  mid - 1;
            }
        }
        return -1;
    }
    int findInMountainArray(int target, MountainArray &arr) {
        
        int  n = arr.length();
                
        int left = 0;
        int right = n - 1;
        
        while(left < right) {
            int mid = (right - left ) / 2 + left;
            if(arr.get(mid) > arr.get(mid + 1)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        // cout << "Left : " << left << endl;
        int ansLeftSide = findLeftSide(0, left, target, arr);
        int ansRightSide = findRightSide(left + 1, n - 1, target, arr);
        // cout << ansLeftSide << "   " << ansRightSide << '\n';
        return ansLeftSide != -1 ? ansLeftSide : ansRightSide;
        
    }
};