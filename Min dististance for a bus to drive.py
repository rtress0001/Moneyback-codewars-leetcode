class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        if start > destination:
            start, destination = destination, start

        
        total_dis = sum(distance)
        clock_wise = sum(distance[start:destination])
        counter_wise = total_dis - clock_wise
        return min(clock_wise,counter_wise)
        
        