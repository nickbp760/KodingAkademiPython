# Define the 2x2 matrix
a: list[list[int]] = [
    [1, 2],
    [3, 4]]

# Calculate the determinant
determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]

# Calculate the inverse
inverse: list[list[float]] = [
    [a[1][1] / determinant, -a[0][1] / determinant],
    [-a[1][0] / determinant, a[0][0] / determinant]]

print(f"Determinant: {determinant}")
print("Inverse:")
for row in inverse:
    print(row)
print("-----------------------------------------------------------")
# Define the 2x2 matrix
b: list[list[int]] = [
    [4, 5],
    [2, 6]]

# Calculate the determinant
determinant = b[0][0] * b[1][1] - b[0][1] * b[1][0]

# Calculate the inverse
inverse: list[list[float]] = [
    [b[1][1] / determinant, -b[0][1] / determinant],
    [-b[1][0] / determinant, b[0][0] / determinant]]

print(f"Determinant: {determinant}")
print("Inverse:")
for row in inverse:
    print(row)
