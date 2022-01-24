import sys


def equal_numbers(file):
    list_numbers = []
    with open(file, 'r', encoding='utf-8') as work_file:
        for number in work_file.readlines():
            list_numbers.append(int(number))
    list_numbers.sort()
    mid = len(list_numbers) // 2
    medium = 0
    for i in list_numbers:
        medium += abs(i - list_numbers[mid])
    print(f"{medium}\n")


if __name__ == "__main__":
    equal_numbers(sys.argv[1])
