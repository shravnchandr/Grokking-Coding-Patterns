from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.all_mapping = defaultdict(dict)
        self.key_time_mapping = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.all_mapping[key][timestamp] = value
        self.key_time_mapping[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        time_list = self.key_time_mapping[key]
        if not time_list:
            return ""

        left_index, right_index = 0, len(time_list) -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_time = time_list[middle_index]

            if middle_time < timestamp:
                left_index = middle_index +1
            elif middle_time > timestamp:
                right_index = middle_index -1
            else:
                return self.all_mapping[key][middle_time]

        key_time = time_list[left_index -1]
        return self.all_mapping[key][key_time] if key_time < timestamp else ""
