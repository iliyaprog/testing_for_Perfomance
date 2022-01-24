import sys


def circular_array(num_array, length_interval):
    massive = [n for n in range(1, num_array + 1)]
    answer = ''
    last_array = []
    if num_array >= length_interval:
        last_array = massive[:length_interval]
    else:
        len_interval = length_interval
        while True:
            if num_array <= len_interval:
                arg = num_array
            else:
                arg = len_interval
            last_array += massive[:arg]
            len_interval -= arg
            if len_interval == 0:
                break
    while True:
        answer += str(last_array[0])
        if last_array[-1] != 1:
            i = last_array[-1]
            last_array = []
            for n in range(i, i + length_interval):
                if n <= num_array:
                    last_array.append(n)
                else:
                    last_array.append(n - num_array)
        else:
            break

    return answer


if __name__ == "__main__":
    if int(sys.argv[1]) <= 0 and int(sys.argv[2]) <= 0:
        print('Входные данные не верны\n')
    else:
        try:
            print(f"{circular_array(int(sys.argv[1]), int(sys.argv[2]))}\n")
        except:
            print('Входные данные не верны\n')

