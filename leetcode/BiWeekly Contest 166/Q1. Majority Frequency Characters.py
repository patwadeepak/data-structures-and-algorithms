from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter = Counter(s)

        d = defaultdict(list)
        for k, v in counter.items():
            d[v].append(k)

        mx = float('-inf')
        mk = float('-inf')
        for k, g in d.items():
            if mx < len(g):
                mx = len(g)
                mk = k
            elif mx == len(g):
                if mk < k:
                    mk = k

        return ''.join(d[mk])
