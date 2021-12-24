import statistics
import sys


def equal_numbers(file):
    list_numbers = []
    with open(file, 'r', encoding='utf-8') as work_file:
        for number in work_file.readlines():
            list_numbers.append(int(number))
    medium = int(statistics.mean(list_numbers))
    count = 0
    for num in list_numbers:
        if num < medium:
            while num != medium:
                num += 1
                count += 1
        else:
            while num != medium:
                num -= 1
                count += 1
    print(f"{count}\n")


if __name__ == "__main__":
    equal_numbers(sys.argv[1])
