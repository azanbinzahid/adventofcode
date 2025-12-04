with open('in.txt', 'r') as f:
    ans = 0
    for line in f.readlines():
        bank = (list(line.strip()))
        a = max(bank[:-1])
        b = max(bank[bank.index(a)+1:])

        ans += int(a + b) 
        # print(a, b, ans)

    print(ans)

