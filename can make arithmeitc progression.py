   def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        difference = arr[1] - arr[0]
        for index in range(1,len(arr)):
            if arr[index] - arr[index-1] != difference:
                return False
        return True
            
            