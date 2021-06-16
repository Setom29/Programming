import requests


def ex264():
    matrix = []
    new_matrix = []
    srt_max_ind = 0
    col_max_ind = 0
    while True:
        try:
            temp = list(map(int, (input().split(' '))))
            matrix.append(temp)
            srt_max_ind = len(matrix[0]) - 1
            col_max_ind = len(matrix) - 1
        except:
            break
    for item in matrix:
        print(*item)
    srt_max_ind = len(matrix) - 1
    col_max_ind = len(matrix[0]) - 1
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            a, b = i - 1, i + 1
            c, d = j - 1, j + 1
            if i == 0:
                a = srt_max_ind
            if i == srt_max_ind:
                b = 0
            if j == 0:
                c = col_max_ind
            if j == col_max_ind:
                d = 0
            temp.append(matrix[a][j] + matrix[b][j] + matrix[i][c] + matrix[i][d])
        new_matrix.append(temp)
    for item in new_matrix:
        print(*item)


def ex265(n=5):
    n = int(input())
    matrix = [[0 for i in range(n)] for j in range(n)]
    k, start_pos = 1, 0
    N = n - 1  # для конечных границ
    while N >= 0:
        for i in range(start_pos, N + 1):
            matrix[start_pos][i] = k
            k += 1
        for i in range(start_pos + 1, N + 1):
            matrix[i][N] = k
            k += 1
        for i in range(N - 1, start_pos - 1, -1):
            matrix[N][i] = k
            k += 1
        for i in range(N - 1, start_pos, -1):
            matrix[i][start_pos] = k
            k += 1
        start_pos += 1
        N -= 1

    for item in matrix:
        print(*item)


def ex342():
    word_dict = {}
    max_num = 0
    top_word = ''
    with open('file.txt', 'r') as f:
        while True:
            # читаем одну строку
            word_list = f.readline().split()
            if not word_list:
                break
            for item in word_list:
                item = item.lower()
                if item in word_dict.keys():
                    word_dict[item] += 1
                else:
                    word_dict[item] = 1

    for key, value in word_dict.items():
        if value > max_num:
            max_num = value
            top_word = key
        elif value == max_num:
            if key > top_word:
                max_num = value
                top_word = key
    print(f'{top_word} {max_num}')


def ex375():
    class_dict = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-', 10: '-', 11: '-'}
    with open('file.txt', 'r') as f:
        number_of_puples = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while True:
            height_list = f.readline().split('\t')
            if height_list == ['']:
                break
            height_list[2] = height_list[2].replace('\n', '')
            height_list[0], height_list[2] = int(height_list[0]), float(height_list[2])
            number_of_puples[height_list[0] - 1] += 1
            if class_dict[height_list[0]] == '-':
                class_dict[height_list[0]] = float(height_list[2])
            else:
                class_dict[height_list[0]] = float(height_list[2]) + float(class_dict[height_list[0]])
    with open('file1.txt', 'w') as f:
        for key, value in class_dict.items():
            if value == '-':
                f.write(f'{key} {value}\n')
            else:
                f.write(f'{key} {value / number_of_puples[key - 1]}\n')


def ex343():
    with open('file.txt', 'r', encoding="utf-8") as f:
        av_marks = [0, 0, 0]
        n = 0
        while True:
            temp = f.readline().split(';')
            if temp == ['']:
                break
            temp[3] = temp[3].replace('\n', '')
            for i in range(3):
                temp[i + 1] = float(temp[i + 1])
                av_marks[i] += temp[i + 1]
            with open('file1.txt', 'a') as wf:
                wf.write(f'{(temp[1] + temp[2] + temp[3]) / 3}\n')
            n += 1
        with open('file1.txt', 'a') as wf:
            wf.write(f'{av_marks[0] / n} {av_marks[1] / n} {av_marks[2] / n}')


def ex361():
    url = 'https://stepic.org/media/attachments/course67/3.6.2/088.txt'
    r = requests.get(url)
    a = r.text.splitlines()
    print(len(a))


def ex361():
    url0 = 'https://stepic.org/media/attachments/course67/3.6.3/'
    url1 = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
    r = requests.get(url1)
    print(r.text)
    n = 0
    while r.text != 'We':
        r = requests.get(url0 + r.text)
        print(f'{n}]{r.text}')
        n += 1


ex361()
