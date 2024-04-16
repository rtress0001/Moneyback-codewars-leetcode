class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for ele in moves:
            if ele == "U":
                pos[1] += 1
            elif ele == "D":
                pos[1] -= 1
            elif ele == "R":
                pos[0] += 1
            elif ele == "L":
                pos[0] -= 1
        if pos[0] == 0 and pos[1] == 0:
            return True
        else:
            return False
                