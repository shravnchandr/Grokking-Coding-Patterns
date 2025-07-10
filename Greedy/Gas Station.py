from typing import List


class Solution:
    def canCompleteCircuit(self, gas_list: List[int], cost_list: List[int]) -> int:
        if sum(gas_list) < sum(cost_list):
            return -1
        
        gas_balance, return_index = 0, 0

        for index, (gas,cost) in enumerate(zip(gas_list, cost_list)):
            current_balance = gas - cost
            gas_balance = gas_balance + current_balance

            if gas_balance < 0:
                gas_balance, return_index = 0, index +1

        return return_index
    