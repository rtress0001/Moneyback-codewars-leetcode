class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        #initize a sum of apples and count
        sum_apples = sum(apple)
        count = 0
        capacity.sort(reverse=True)
        
        #loop though boxes
        for box in capacity:
            #incrementing a signfigiying the use of boxes
            count += 1
            #reduce the sum by box size if less than sum
            sum_apples -= box
            #end the loop if box is greater than sum
            if sum_apples <=0:
                break
            
        
        #return the count of boxes used.
        return count        