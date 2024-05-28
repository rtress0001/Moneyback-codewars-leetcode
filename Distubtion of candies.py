class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        lst_of_candies = [0]*num_people
        count = 1
        while candies>0:
            for index in range(num_people):
                if candies >= count:
                    lst_of_candies[index]+=count
                    candies-=count
                else:
                    lst_of_candies[index] += candies
                    candies = 0
                count+=1
        return lst_of_candies
                    
        