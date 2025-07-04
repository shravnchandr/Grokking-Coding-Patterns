from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        course_mapping = defaultdict(list)
        for course, pre_course in prerequisites:
            course_mapping[course].append(pre_course)

        UNCHECKED, CHECKING, CHECKED = 0, 1, 2
        course_state = [UNCHECKED] * num_courses

        def helperFunction(course_index: int) -> bool:
            if course_state[course_index] == CHECKED:
                return True
            
            if course_state[course_index] == CHECKING:
                return False
            
            course_state[course_index] = CHECKING

            for pre_course in course_mapping[course_index]:
                if not helperFunction(pre_course):
                    return False
                
            course_state[course_index] = CHECKED

            return True
        
        for course_index in range(num_courses):
            if not helperFunction(course_index):
                return False
            
        return True
            