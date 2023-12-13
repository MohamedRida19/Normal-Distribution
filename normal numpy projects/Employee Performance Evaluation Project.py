import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

average_employee_performance = 60
std_employee_performance = 15
num_of_employees = 1500

employee_performence_score = np.random.normal(loc = average_employee_performance, scale = std_employee_performance, size = num_of_employees)

mean_score = np.mean(employee_performence_score)
std_score = np.std(employee_performence_score)
#part to understand *****************************
plt.axvline(x= mean_score, linestyle = "--",color = "red", label = f"The Mean: {mean_score: .2f}")
plt.axvline(x = std_score + mean_score, color = "orange", linestyle = "--", label = f"STD: {std_score: .2f}")


threshold = 82
above_threshold = np.sum(employee_performence_score > threshold)
pourcentage_above_threshold = (threshold / num_of_employees) * 100
#important to understand this part and learn it ****************
plt.axvline(x = threshold, color = "green", linestyle = "--", label = f"Threshold: {pourcentage_above_threshold: .2f}%")
plt.annotate(f'threshold',xy= (threshold, 0), textcoords="offset pixels", xytext=(0, 10), ha = "center", color = "green")
  
sns.histplot(employee_performence_score, bins = 100, kde = 1, fill=0)
plt.xlabel("Employees Scores")
plt.ylabel("Frequency")
plt.title("Employee Performance Evaluation")
plt.legend()
plt.show()
