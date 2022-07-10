class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=list(str(n))
        k=len(n)
        while k>3:
            n.insert(k-3,'.')
            k-=3
        n=''.join(n)
        return n