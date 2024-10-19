class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            max_stone = stones[-1]
            max_stone2 = stones[-2]
            stones.pop()
            stones.pop()
            new_stone = abs(max_stone2-max_stone)
            stones.append(new_stone)
        return stones[0]
        
    
        
            
                