class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if(str2.size() > str1.size()) swap(str1, str2);
        int n = str1.size(),m = str2.size();
        
        int minSize = min(n, m);
        
        string lS = "";
        while(minSize > 0) {
            
            if(n % minSize == 0 && m % minSize == 0) {
                cout << minSize << endl;
                string temp = str1.substr(0, minSize);
                
                int n1 = n / minSize, n2 = m / minSize;
                
                string s1 = "", s2 = "";
                for(int i = 0; i < n1; ++i) {
                    s1 += temp;
                }
                for(int i = 0; i < n2; ++i) {
                    s2 += temp;
                }
                
                if(s1 == str1 and s2 == str2) return temp;
            }
            
            minSize--;
        }
        return "";
    }
};