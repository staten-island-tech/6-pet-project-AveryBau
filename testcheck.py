def tree(number, height):
    tall = 1
    short = 1
    sstreak = 0
    tstreak = 0
    for i in range(len(height)-1):
        if height[i + 1] > height[i]:
            tall += 1
            short = 1
        if tstreak < tall:
            tstreak = tall
        if height[i + 1] < height[i]:
            short += 1
            tall = 1
        if sstreak < short:
            sstreak = short
    print(tstreak)
    print(sstreak)
tree(4, [1, 3, 4, 2])
tree(10, [2, 1, 4, 6, 8, 2, 9, 5, 2, 3])
tree(5, [1, 2, 3, 4, 5, 3])