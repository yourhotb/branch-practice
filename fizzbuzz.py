for j in range(1, 15+1):
    if j % 15 ==0 or 5 j % 5 ==0:
        print('fizz' * (j % 3 == 0) + 'buzz' * (j % 5 == 0))
    else:
        print(j)
