class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        total = len(hand) // groupSize
        res = [[] for _ in range(total)]
        hand.sort()
        i = 0
        j = 0

        while hand:
            if hand[i] not in res[j]:
                res[j].append(hand[i])
                del hand[i]
            else:
                i += 1    

            if len(res[j]) == groupSize:
                j += 1
                i = 0 

        for m in range(len(res)):
            for n in range(1,len(res[0])):
                if res[m][n] - res[m][n-1] != 1:
                    return False      
        
        return True
            