import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 200, 180, 250]

students = [1, 2, 3, 4, 5]
marks = [60, 75, 80, 70, 90]

subjects = ['Math', 'Science', 'English']
marks_sub = [85, 90, 75]

# 1. Line Graph
plt.plot(months, sales)
plt.title("Line Graph - Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 2. Bar Graph
plt.bar(months, sales)
plt.title("Bar Graph - Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 3. Pie Chart
plt.pie(sales, labels=months, autopct='%1.1f%%')
plt.title("Pie Chart - Sales Distribution")
plt.show()

# 4. Scatter Plot
plt.scatter(students, marks)
plt.title("Scatter Plot - Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 5. Histogram
plt.hist(marks)
plt.title("Histogram - Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 6. Horizontal Bar Graph
plt.barh(subjects, marks_sub)
plt.title("Horizontal Bar - Subject Marks")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.show()