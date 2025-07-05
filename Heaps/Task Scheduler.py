from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks_list: List[str], interval: int) -> int:
        tasks_count, cooldown_period = list(), deque()
        for task,count in Counter(tasks_list).items():
            heapq.heappush(tasks_count, (-count,task))
        
        final_count = 0
        while tasks_count or cooldown_period:

            if tasks_count:
                count,task = heapq.heappop(tasks_count)
            
                if count +1 != 0:
                    cooldown_period.append((task, count +1, final_count + interval +1))

            final_count = final_count +1

            if cooldown_period and final_count == cooldown_period[0][2]:
                task,count,_ = cooldown_period.popleft()
                heapq.heappush(tasks_count, (count,task))            

        return final_count        
                
