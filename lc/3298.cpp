class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        vector<int> w2a(26, 0);
        for (char c : word2) {
            w2a[c - 'a']++;
        }

        vector<int> c(26, 0);
        int l = 0;
        long long res = 0;

        for (int r = 0; r < word1.length(); ++r) {
            c[word1[r] - 'a']++;

            while (allCharactersInW2(c, w2a)) {
                c[word1[l] - 'a']--;
                l++;
            }

            res += l;
        }

        return res;
    }

    bool allCharactersInW2(const vector<int>& c, const vector<int>& w2a) {
        for (int i = 0; i < 26; ++i) {
            if (c[i] < w2a[i]) {
                return false;
            }
        }
    return true;
}
};