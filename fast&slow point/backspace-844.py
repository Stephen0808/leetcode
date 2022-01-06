def backspaceCompare(self, s: str, t: str) -> bool:
        def backspacedependent(s):
            ls = list(s)
            fast, slow = 0, 0
            for i in ls:
                if ls[fast] != '#':
                    ls[slow] = ls[fast]
                    slow += 1
                # slow必须判断，越界则置0
                elif slow - 1 >= 0:
                    slow -= 1
                else:
                    slow = 0
                fast += 1
            if slow <= 0:
                return None
            else:
                result = "".join(ls[:slow])
                return result
        if backspacedependent(s) == backspacedependent(t):
            return True
        else:
            return False
