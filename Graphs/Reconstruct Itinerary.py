from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets_list: List[List[str]]) -> List[str]:
        travel_map = defaultdict(list)
        for src,dst in tickets_list:
            travel_map[src].append(dst)

        for src in travel_map.keys():
            travel_map[src] = sorted(travel_map[src], reverse=True)

        itinerary = list()
        city_name = 'JFK'

        while city_name:
            itinerary.append(city_name)

            if travel_map[city_name]:
                city_name = travel_map[city_name].pop()
            else:
                break

        return itinerary

        
        