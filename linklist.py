my_list = [0]

n = int(input('Até que numero será a contagem?'))
i = 0
for i in range(n):
    if i < n and i % 2 == 1:
        i += 1
        my_list.append(i)
        print(f'{my_list}')
