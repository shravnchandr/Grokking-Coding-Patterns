from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_card = list()

        for oper in operations:
            
            if oper == 'C':
                score_card.pop()
            elif oper =='D':
                score_card.append(score_card[-1] *2)
            elif oper == '+':
                score_card.append(score_card[-1] + score_card[-2])
            else:
                score_card.append(int(oper))

        return sum(score_card)
    