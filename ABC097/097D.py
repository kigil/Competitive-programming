# http://www.geocities.jp/m_hiroi/light/pyalgo61.html
 
class UnionFind3:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]
 
    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]
 
    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False
 
 
N, M = [int(i) for i in input().split()]
p = [int(i) - 1 for i in input().split()]
 
uf = UnionFind3(N + 1)
for i in range(M):
    x, y = [int(i)-1 for i in input().split()]
    uf.union(x, y)
 
count = 0
for i in range(N):
    if p[i] != i:
        if uf.find(p[i]) == uf.find(i):
            count += 1
            # pi = p[i]
            # ppi = p[pi]
            # p[i], p[pi] = ppi, pi
    else:
        count += 1
print(count)