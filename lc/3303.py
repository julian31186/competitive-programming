class Solution:
    def minStartingIndex(self, s: str, p: str) -> int:
        
        def z_string(s):
            mn = len(s)
            _z = [0]*mn
            x, y = 0, 0
            for i in range(1, mn):
                _z[i] = max(0, min(_z[i-x], y-i+1))
                while i+_z[i] < mn and s[_z[i]] == s[i+_z[i]]:
                    x, y = i, i+_z[i]
                    _z[i] += 1
            _z[0] = mn
            return _z

        pre,suf = z_string(p + "$" + s)[len(p) + 1:],z_string(p[::-1] + "$" + s[::-1])[len(p) + 1:][::-1]
        for i in range(len(s) - len(p) + 1):
            if pre[i] == len(p): return i
            required_suffix = len(p) - pre[i] - 1
            if suf[i + pre[i] + required_suffix] == required_suffix: return i
        return -1