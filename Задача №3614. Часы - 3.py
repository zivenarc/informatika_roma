a = float(input())

H = int(a // 30)
M = int((a % 30) * 30 // 12 )

am = (H + M/60) / 12 * 360
asec = a - am

S = int( round( asec * 3600 / 30, 0))

print(H, M, S)