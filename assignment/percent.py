marks = list(map(int, input("Enter subject marks: ").split()))

total = sum(marks)
percentage = total / len(marks)

print("Total Marks =", total)
print("Percentage =", percentage)