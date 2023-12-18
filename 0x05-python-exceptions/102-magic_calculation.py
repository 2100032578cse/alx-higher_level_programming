#!/usr/bin/python3
def magic_calculation(a, b):
    ans = 0
    for i in range(1, 3):
        try:
            if (a < i):
                raise Exception('Too far')
            else:
                ans = ans + a ** b / i
        except Exception:
            ans = a + b
            break
    return ans
