class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10**9 + 7
        indexS = []

        for i in range(len(corridor)):
            if corridor[i] == 'S':
                indexS.append(i)
        

        if len(indexS) < 2 or len(indexS) % 2 != 0:
            return 0

        
        ways = 1

        for i in range(0, len(indexS) - 2, 2):
            gap = indexS[i + 2] - indexS[i + 1] - 1
            ways = (ways * (gap + 1)) % MOD

        return ways