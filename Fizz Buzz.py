class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        lst = []
        for index in range(1,n+1):
            if index % 3 == 0 and index % 5 == 0:
                lst.append("FizzBuzz")
            elif index % 3 == 0:
                lst.append("Fizz")
            elif index % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(index))
        return lst
                
        