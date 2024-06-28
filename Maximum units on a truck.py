class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        #sorted by the number of units in each box
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        
        #declare a variable to store number of units
        unit_count = 0
        
        for box_number, units in boxTypes:
            
            #take the min of truck remaining truck size and box of that type
            boxes_to_take = min(truckSize,box_number)
            
            #boxes count increase by units
            unit_count += boxes_to_take * units
            
            #Reduce Truck Size
            truckSize-=boxes_to_take
        
        #finish the code by returning total boxes 
        return unit_count
        
        