class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 锁定k值 
        kk = k
        # 全字符直接list(),有空格用split()
        s = list(s)
        l = len(s)
        # print(l)
        rem = l % (2*kk)
        # print(rem)
        for idx, x in enumerate(s):
            # 针对余项：相对坐标，积累坐标
            rel_idx = (idx) % (2*kk)
            acc_idx = idx - rel_idx
            if l - rem <= idx:
                if rem <= k:
                    k = rem
            # 反转
            if rel_idx <= k // 2 - 1:
                # print(acc_idx, rel_idx, k, acc_idx + k - rel_idx - 1)
                s[idx], s[acc_idx + k - rel_idx - 1] = s[acc_idx + k - 1 - rel_idx], s[idx]
                # print(rel_idx, acc_idx)
        return ''.join(s)
        
            
                
