"""
Certainly! Let's add more details to the project:

**Project: Exam Performance Comparison**

**Objective:**
Compare the exam performance of two groups of students and visualize the distributions to analyze the differences.

**Details:**

1. **Generate Data:**
   - Create two sets of exam scores for Group A and Group B.
   - Group A: Mean = 75, Standard Deviation = 10, Number of Students = 150
   - Group B: Mean = 80, Standard Deviation = 8, Number of Students = 150

2. **Calculate Statistics:**
   - Compute the mean and standard deviation for each group.

3. **Visualize Distributions:**
   - Create histograms with kernel density estimates for both groups on the same plot.
   - Use different colors or patterns to distinguish between the two groups.

4. **Analyze Differences:**
   - Annotate the plot with mean and standard deviation values for each group.
   - Compare the shapes of the distributions and observe any differences.

5. **Explore Percentiles:**
   - Identify and compare specific percentiles (e.g., 25th, 50th, and 75th percentiles) for both groups.

6. **Draw Conclusions:**
   - Based on the visualizations and statistics, draw conclusions about the relative performance of the two groups.

Feel free to adjust the parameters (mean, std, and number of students) based on your preferences or requirements. This detailed information will guide you in generating and analyzing the datasets for each group.
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mean_group_A = 75
std_group_A = 10
num_students_A = 150
GrpA_Score = np.random.normal(loc = mean_group_A, scale = std_group_A, size = num_students_A)

sns.histplot(GrpA_Score, kde = True, fill = False, color = "blue")

mean_group_B = 80
std_group_B = 8
num_students_B = 150
GrpB_Score = np.random.normal(loc = mean_group_B, scale = std_group_B, size = num_students_B)

sns.histplot(GrpB_Score, kde = True, fill = False, color = "orange")

mean_score_A = np.mean(GrpA_Score)
std_score_A = np.std(GrpA_Score)

plt.axvline(x=mean_score_A, linestyle = "--", color = "blue", label = (f"MEAN_A: {mean_score_A:.2f}"))
plt.axvline(x=mean_score_A + std_score_A, linestyle = "--", color = "blue", label = (f"STD_A: {std_score_A:.2f}"))

mean_score_B = np.mean(GrpB_Score)
std_score_B = np.std(GrpB_Score)

plt.axvline(x=mean_score_B, linestyle = "--", color = "orange", label = (f"MEAN_B: {mean_score_B:.2f}"))
plt.axvline(x=std_score_B + mean_score_B, linestyle = "--", color = "orange", label = (f"STD_B: {std_score_B:.2f}"))

percentiles = [25, 50, 75]
for p in percentiles:
    percentile_A = np.percentile(GrpA_Score, p)
    percentile_B = np.percentile(GrpB_Score, p)
    plt.axvline(x=percentile_A, linestyle = "--", color = "blue", alpha = 0.5)
    plt.axvline(x=percentile_B, linestyle = "--", color = "orange", alpha = 0.5)
    plt.text(percentile_A,0, f'{p}%', rotation = 90, va="top", ha = 'right', color = "blue", alpha = 0.7)
    plt.text(percentile_B,0, f'{p}%', rotation = 90, va = "top", ha ="right", color = "orange", alpha  = 0.7)

plt.xlabel("Exam Scores")
plt.ylabel("Frequency")
plt.title("Exam Performence Comparaison")
plt.legend()
plt.show() 