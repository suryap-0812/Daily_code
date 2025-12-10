class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)

        # Check unlocking feasibility
        root = complexity[0]
        for i in range(1, n):
            if complexity[i] <= root:
                return 0  # cannot unlock this computer

        # Compute (n-1)!
        fact = 1
        for k in range(1, n):
            fact = (fact * k) % MOD

        return fact
