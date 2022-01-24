import math
import sys


def circular_array(file_circular, file_point):
    with open(file_circular, 'r', encoding='utf-8') as f_circular:
        for i_line in f_circular.readlines():
            if len(i_line) > 1:
                i_line = i_line.split(' ')
                centre_circular = (float(i_line[0]), float(i_line[1]))
            else:
                radius = float(i_line)

    with open(file_point, 'r', encoding='utf-8') as f_point:
        all_points = []
        for i_line in f_point.readlines():
            i_line = i_line.split(' ')
            point = (float(i_line[0]), float(i_line[1]))
            all_points.append(point)

    for i_point in range(len(all_points)):
        distance_to_point = math.sqrt(
            math.pow((all_points[i_point][0] - centre_circular[0]), 2)
            + math.pow((all_points[i_point][1] - centre_circular[1]), 2)
        )
        if round(distance_to_point, 10) == round(radius, 10):
            print(f"{i_point} - точка лежит на окружности\n")
        elif distance_to_point < radius:
            print(f"{i_point} - точка внутри\n")
        else:
            print(f"{i_point} - точка снаружи\n")


if __name__ == "__main__":
    circular_array(sys.argv[1], sys.argv[2])
