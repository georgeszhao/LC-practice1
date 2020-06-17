class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        left, right = 0, len(s) - 1
        if s[left] in '+-':
            left += 1
        if left > right:
            return False
        dot, exp, sign = -1, -1, -1
        for i in range(left, right + 1):
            if s[i].isdigit():
                continue
            if s[i] == '.':
                if dot >= 0:
                    return False
                else:
                    dot = i
            elif s[i] in 'eE':
                if exp >= 0:
                    return False
                else:
                    exp = i
            elif s[i] in '+-':
                if sign >= 0:
                    return False
                else:
                    sign = i
            else:
                return False
        if exp == left or exp == right or sign == left or sign == right \
            or dot > exp != -1 or exp > sign != -1 or (exp == -1 and sign == 1):
            return False
        if dot == left:
            return dot < right and s[dot + 1].isdigit()
        if dot == right:
            return dot > left and s[dot - 1].isdigit()
        return True

def execute():
    s = "95a54e53"
    sol = Solution()
    print(sol.isNumber(s))

if __name__ == "__main__":
    execute()