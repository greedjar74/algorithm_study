# 백준 12849번

d = int(input())

ways = [0] * 8
ways[0] = 1

# ways[0] = ways[1] + ways[2]
# ways[1] = ways[0] + ways[2] + ways[3]
# ways[2] = ways[0] + ways[1] + ways[3] + ways[4]
# ways[3] = ways[1] + ways[2] + ways[4] + ways[5]
# ways[4] = ways[2] + ways[3] + ways[5] + ways[6]
# ways[5] = ways[3] + ways[4] + ways[7]
# ways[6] = ways[4] + ways[7]
# ways[7] = ways[5] + ways[6]

def nxt(ways):
    tmp = [0] * 8

    tmp[0] = ways[1] + ways[2]
    tmp[1] = ways[0] + ways[2] + ways[3]
    tmp[2] = ways[0] + ways[1] + ways[3] + ways[4]
    tmp[3] = ways[1] + ways[2] + ways[4] + ways[5]
    tmp[4] = ways[2] + ways[3] + ways[5] + ways[6]
    tmp[5] = ways[3] + ways[4] + ways[7]
    tmp[6] = ways[4] + ways[7]
    tmp[7] = ways[5] + ways[6]

    for i in range(8):
        tmp[i] %= 1000000007

    return tmp

for i in range(d):
    ways = nxt(ways)

print(ways[0])