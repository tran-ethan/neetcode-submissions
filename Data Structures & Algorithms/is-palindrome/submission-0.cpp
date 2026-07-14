class Solution {
public:
    bool isPalindrome(string s) {
        std::erase_if(s, [](unsigned char c) {
            return !std::isalnum(c);
        });

        std::transform(s.begin(), s.end(), s.begin(), ::tolower);

        std::cout << s << endl;

        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }
            l++;
            r--;
        }
        
        return true;
    }
};
