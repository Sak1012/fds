import matplotlib.pyplot as plt

# Math and Science scores
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
math_scores = [88, 76, 95, 67, 89, 82]
science_scores = [92, 80, 85, 70, 90, 75]

# Create scatter plot
plt.scatter(math_scores, science_scores)

# Annotate points
for i, student in enumerate(students):
    plt.text(math_scores[i], science_scores[i], student)

plt.title('Math vs Science Scores')
plt.xlabel('Math Scores')
plt.ylabel('Science Scores')
plt.show()
