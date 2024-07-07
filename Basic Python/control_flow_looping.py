score = 1
end_score = 10
while True:
    print(score)
    if score == end_score:
        break
    score += 1

n = int(input("masukan jumlah "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

for i in range(1, n + 1):
    print('*' * i)
