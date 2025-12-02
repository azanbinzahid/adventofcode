with open('sample.txt', 'r') as f:
    pos = 50
    ans = 0
    for line in f.readlines():
        curr = pos
        # get dir and val from line which is L10 or R10
        direction = line[0]
        value = int(line[1:].strip())

        # position is between 0 and 99 and is circular
        # Count how many times the dial points at 0 during this rotation.
        # ========================================================================
        # Uses Copilot Chat to help implement this "multiple" logic.
        # ========================================================================
        # This handles moves that may pass 0 multiple times (value >= 100).
        crosses = 0
        if direction == 'L':
            new_pos = (pos - value) % 100
            # For a left move, we hit 0 when we've moved k steps where k == pos (mod 100).
            # The first such k is `pos` (unless pos == 0, then it's 100), and subsequent
            # hits occur every 100 steps.
            first_needed = pos if pos != 0 else 100
            if value >= first_needed:
                crosses = 1 + (value - first_needed) // 100
            pos = new_pos
        elif direction == 'R':
            new_pos = (pos + value) % 100
            # For a right move, we hit 0 when we've moved k steps where k == 100 - pos (mod 100).
            # The first such k is `100 - pos` (or 100 when pos == 0).
            first_needed = (100 - pos) if pos != 0 else 100
            if value >= first_needed:
                crosses = 1 + (value - first_needed) // 100
            pos = new_pos

        ans += crosses
        
print(ans)