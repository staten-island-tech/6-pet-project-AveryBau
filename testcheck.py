def tree(number, height):
    tall = 1
    short = 1
    sstreak = []
    tstreak = []
    for i in range(number):
        if height[i + 1] > height[i]:
            tall += 1
            tstreak.append(tall)
            tall == 1
        elif height[i + 1] < height[i]:
            short += 1
            sstreak.append(short)
            short == 1
    print(max(tstreak))
    print(max(sstreak))
tree(4, [1, 3, 4, 2])