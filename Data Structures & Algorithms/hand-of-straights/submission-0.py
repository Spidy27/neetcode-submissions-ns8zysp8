class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        res = []
        hand.sort()
        i = 0
        while len(res) != groupSize:
            if hand[i] not in res:
                res.append(hand[i])
                del hand[i]
            i += 1

        for i in range(1, len(res)):
            if res[i] - res[i-1] != 1:
                return False

        for i in range(1, len(hand)):
            if hand[i] - hand[i-1] != 1:
                return False

        return True 
            