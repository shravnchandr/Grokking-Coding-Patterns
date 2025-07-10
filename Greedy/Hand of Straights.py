from collections import Counter
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand_list: List[int], group_size: int) -> bool:
        if len(hand_list) % group_size != 0:
            return False
        
        card_count = [(card,count) for card,count in Counter(hand_list).items()]
        heapq.heapify(card_count)

        while card_count:
            current_hand, balance_cards = list(), list()

            for _ in range(group_size):
                if not card_count:
                    return False

                card,count = heapq.heappop(card_count)

                if current_hand and card != current_hand[-1] +1:
                    return False
                
                current_hand.append(card)

                if count > 1:
                    balance_cards.append((card, count -1))

            for cards in balance_cards:
                heapq.heappush(card_count, cards)

        return True

    def isNStraightHand(self, hand_list: List[int], group_size: int) -> bool:
        if len(hand_list) % group_size != 0:
            return False
        
        card_count = [(card,count) for card,count in Counter(hand_list).items()]
        heapq.heapify(card_count)

        while card_count:
            balance_cards = list()
            first_card, first_count = heapq.heappop(card_count)

            for index in range(1, group_size):
                if not card_count:
                    return False

                card,count = heapq.heappop(card_count)

                if first_card + index != card or first_count > count:
                    return False

                if count - first_count > 0:
                    balance_cards.append((card, count - first_count))

            for cards in balance_cards:
                heapq.heappush(card_count, cards)

        return True
    
    def isNStraightHand(self, hand_list: List[int], group_size: int) -> bool:
        if len(hand_list) % group_size != 0:
            return False
        
        cards_count = Counter(hand_list)
        unique_cards = sorted(list(cards_count.keys()))

        for card in unique_cards:
            if cards_count[card] > 0:

                required_cards = cards_count[card]
                for index in range(1, group_size):
                    new_card = card + index
                    
                    if cards_count[new_card] < required_cards:
                        return False
                
                    cards_count[new_card] = cards_count[new_card] - required_cards

        return True