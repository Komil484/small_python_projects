# Input
alpha = input("Input alphabet: ")

while True:
    try:
        size = int(input("Input combination length: "))
        if size > len(alpha):
            print("Must not be more than the length of the alphabet")
            raise ValueError
        break
    except ValueError:
        print("Must be a number")

indexes = [i for i in range(size)]


# Main function (recursive)
def check_and_inc(index):
    if index < 0:
        return None

    if indexes[index] < len(alpha) - size + index:
        indexes[index] += 1
        return indexes[index]

    prev_index = check_and_inc(index - 1)
    if prev_index is None:
        return None

    indexes[index] = prev_index + 1
    return indexes[index]


# Output
for index in indexes:
    print(alpha[index], end="")
print()

while not check_and_inc(size - 1) is None:
    for index in indexes:
        print(alpha[index], end="")
    print()
