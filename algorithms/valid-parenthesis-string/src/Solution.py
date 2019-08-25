class Solution:
    def checkValidString(self, s: str) -> bool:
        parenthesis = []
        stars = []
        for i in range(len(s)):
            string = s[i]
            if string == '*':
                stars.append((string, i))
            else:
                if len(parenthesis) == 0:
                    if string == ')':
                        if len(stars) > 0:
                            stars.pop()
                        else:
                            return False
                    else:
                        parenthesis.append((string, i))
                else:
                    if string == '(':
                        parenthesis.append((string, i))
                    else:
                        parenthesis.pop()
        while parenthesis:
            if len(stars) == 0:
                return False
            p, pi = parenthesis.pop()
            s, si = stars.pop()
            if si < pi:
                return False

        return True
