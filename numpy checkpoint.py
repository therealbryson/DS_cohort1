import numpy as np

# Create the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calculate mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_dev_grade = np.std(grades)

# Find maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# Sort grades in ascending order
sorted_grades = np.sort(grades)

# Find index of the highest grade
max_grade_index = np.argmax(grades)

# Count number of grades above 90
num_above_90 = np.sum(grades > 90)

# Calculate percentage of grades above 90
percent_above_90 = np.mean(grades > 90) * 100

# Calculate percentage of grades below 75
percent_below_75 = np.mean(grades < 75) * 100

# Extract grades above 90 into a new array
high_performers = grades[grades > 90]

# Create array of passing grades (above 75)
passing_grades = grades[grades > 75]

# Print results
print("Grades Array:", grades)
print("Mean Grade:", mean_grade)
print("Median Grade:", median_grade)
print("Standard Deviation of Grades:", std_dev_grade)
print("Maximum Grade:", max_grade)
print("Minimum Grade:", min_grade)
print("Sorted Grades:", sorted_grades)
print("Index of Maximum Grade:", max_grade_index)
print("Number of Grades Above 90:", num_above_90)
print("Percentage of Grades Above 90:", percent_above_90)
print("Percentage of Grades Below 75:", percent_below_75)
print("High Performers:", high_performers)
print("Passing Grades:", passing_grades)
