import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

average_exam_scores = 75
std_exam_scores = 10
num_of_students = 100

exam_scores = np.random.normal(loc = average_exam_scores, scale =std_exam_scores, size = num_of_students)

mean_scores = np.mean(exam_scores)
std_scores = np.std(exam_scores)

print(f"Mean exam score: {mean_scores : .2f}")
print(f"Standard Deviation exam score: {mean_scores : .2f}")

threshold = 90
above_threshold = np.sum(exam_scores > threshold)
pourcentage_above_threshold = (above_threshold/num_of_students) * 100
print(f"The pourcentage about {threshold}: {pourcentage_above_threshold: .2f}%")

sns.histplot(exam_scores, bins = 20, kde = 1, fill=0)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Scores Simulation")
plt.show()