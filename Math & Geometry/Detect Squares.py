from collections import defaultdict
import math
from typing import List


class DetectSquares:

    def __init__(self):
        self.points_store = list()

    def add(self, in_point: List[int]) -> None:
        self.points_store.append(tuple(in_point))

    def get_line_angle(self, point_a: List[int], point_b: List[int]):
        """
        Calculates the angle a line formed by two points makes with the x-axis,
        mapped to the positive quadrant (0 to 90 degrees).

        Args:
            point_a: coordinates of the first point.
            point_b: coordinates of the second point.

        Returns:
            The angle in degrees, ranging from 0 to 90.
        """

        x_a, y_a = point_a
        x_b, y_b = point_b

        delta_x = x_b - x_a
        delta_y = y_b - y_a

        # Handle the case where the points are identical (a point, not a line)
        if delta_x == 0 and delta_y == 0:
            return 0 # Or raise an error, depending on desired behavior for a zero-length line

        angle_radians = math.atan2(delta_y, delta_x)
        angle_degrees = math.degrees(angle_radians)

        # Normalize the angle to be between 0 and 360 degrees first
        if angle_degrees < 0:
            angle_degrees += 360

        # Now, map to the 0-90 range
        if 0 <= angle_degrees <= 90:
            return angle_degrees
        elif 90 < angle_degrees <= 180:
            return 180 - angle_degrees
        elif 180 < angle_degrees <= 270:
            return angle_degrees - 180
        else: # 270 < angle_degrees < 360
            return 360 - angle_degrees

    def count(self, in_point: List[int]) -> int:
        valid_points = defaultdict(list)

        for point in self.points_store:
            valid_diagonal = abs(in_point[0] - point[0]) == abs(in_point[1] - point[1]) != 0
            angle_45 = self.get_line_angle(point, in_point) == 45

            if angle_45 and valid_diagonal:
                valid_points[abs(in_point[0] - point[0])].append(point)

        for point_a in self.points_store:
            for point_b in self.points_store:

                if point_a != point_b:
                    


