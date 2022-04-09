for t in range(int(input())):
    string = list(input())
    i = 0
    count = 1
    while i < len(string)-1:
        if string[i] == string[i+1]:
            count += 1
        elif string[i] < string[i+1]:
            string.insert(i+1, string[i]*count)
            i += 1
            count = 1
        else:
            count = 1
        i += 1
    print(f'Case #{t+1}: {"".join(string)}')
