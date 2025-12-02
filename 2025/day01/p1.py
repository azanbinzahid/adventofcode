with open('in.txt', 'r') as f:
    pos = 50
    ans = 0
    for line in f.readlines():
        
        curr = pos
        # get dir and val from line which is L10 or R10
        direction = line[0]
        value = int(line[1:].strip())

        # position is between 0 and 99 and is circular
        if direction == 'L':
            pos = (pos - value) % 100
        elif direction == 'R':
            pos = (pos + value) % 100

        ans += 1 if pos == 0 else 0
        
print(ans)