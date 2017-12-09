n = input("How many instructions are there?   ")
print("Copy-paste the instructions")
a = range(0, n)
for i in range(0, n):
    a[i] = input()
pointer = 0
steps = 0
while (pointer < len(a)):
    temp = a[pointer]
    a[pointer] += 1
    pointer += temp
    steps += 1

print steps

