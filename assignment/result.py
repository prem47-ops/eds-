marks = []
for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

if min(marks) >= 40:
    print("Pass")
    print("Percentage =", percentage)

    if percentage >= 75:
        print("Distinction")

    elif percentage >= 60:
        print("First Division")

    elif percentage >= 50:
        print("Second Division")

    else:
        print("Third Division")

else:
    print("Fail")