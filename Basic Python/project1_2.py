kata = ["apel", "jeruk", "anggur", "nanas", "pisang"]
print(kata)
n = len(kata)
for i in range(n):
    for j in range(0, n-i-1):
        if kata[j] > kata[j+1]:
            kata[j], kata[j+1] = kata[j+1], kata[j]
print(kata)
