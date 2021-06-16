# with open('input.txt', 'r', encoding='utf-8') as f:
#     n = int(f.readline())
#     for i in range(n):
#         el = f.readline().split()
#         with open('output.txt', 'a', encoding='utf-8') as outf:
#             outf.write(str(f'{sum(list(map(int, el)))}\n'))
#

with open('input.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for _ in range(n):
        span_list = []
        el = f.readline().replace('\n', '').strip()
        span = f.readline().replace('\n', '').strip()
        for i in range(len(el)):
            if el[i] == span[0] and len(el) - i >= len(span):
                flag = True
                for j in range(len(span)):
                    if el[i + j] != span[j]:
                        flag = False
                if flag:
                    span_list.append(str(i + 1))
        print(span_list)
        with open('output.txt', 'a', encoding='utf-8') as outf:
            outf.write(str(f'{" ".join(span_list)}\n'))
