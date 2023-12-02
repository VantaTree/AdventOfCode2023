print("Day 02:")
FILE = "days/d02/main.txt"

max_balls = {"red": 12, "green": 13, "blue": 14} # part 1
ball_color = {"red": 0, "green": 1, "blue": 2}
sum_gid = 0 # part 1
power_sum = 0 # part 2

with open(FILE) as f:
    for line in f.readlines():
        line = line.rstrip()
        spp = line.split(": ")
        game_id = int(spp[0][5:])
        possible = True # part 1
        min_possible = {"red": 0, "green": 0, "blue": 0} # part 2
        for draw in spp[1].split("; "):
            them_balls = {"red": 0, "green": 0, "blue": 0} # part 2
            for ball in draw.split(", "):
                num, col = ball.split(" ")
                num = int(num)
                them_balls[col] = num
                if num > max_balls[col]: # part 1
                    possible = False
            for col, num in them_balls.items(): # part 2
                if num > min_possible[col]:
                    min_possible[col] = num
        power_sum += min_possible["red"] * min_possible["green"] * min_possible["blue"]
        if possible: # part 1
            sum_gid += game_id


print("Part 1:", sum_gid)
print("Part 2:", power_sum)
