from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, cities_count: int, flights_cost: List[List[int]], src_city: int, dst_city: int, stops_count: int) -> int:
        city_travel_graph = defaultdict(list)        
        for src,dst,cost in flights_cost:
            city_travel_graph[src].append((dst,cost))

        travel_cost = dict()

        def depth_first_search(city, stop):
            if city == dst_city:
                return 0
            if stop < 0:
                return float('inf')

            if (city,stop) in travel_cost:
                return travel_cost[(city,stop)]
        
            min_cost = float('inf')
            for next_city,new_price in city_travel_graph[city]:
                curr_cost = new_price + depth_first_search(next_city, stop -1)
                min_cost = min(min_cost, curr_cost)

            travel_cost[(city,stop)] = min_cost
            return min_cost
        
        min_cost = depth_first_search(src_city, stops_count)
        return min_cost if min_cost != float('inf') else -1
    
