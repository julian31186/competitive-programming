'''
Returns the Z prefix array

When we need to search for a pattern, use the following input
z_string(pattern + $ + string)

'''

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
