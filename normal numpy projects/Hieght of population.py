import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

average_people_height = 170
std_people_height = 10
people_num = 1000

people_height = np.random.normal(loc = average_people_height, scale = std_people_height, size = people_num)

mean_height = np.mean(people_height)
std_height = np.std(people_height)

plt.axvline(x= mean_height, color = "red", linestyle = "--", label = f"MEAN: {mean_height: .2f}")
plt.axvline(x = std_height + mean_height, color = "orange", linestyle = "--", label= f"STD: {std_height:.2f}")

threshold = 185
above_threshold = np.sum(threshold < people_height)
pourcentage_above_threshold = (above_threshold / people_num) *100
plt.axvline(x = threshold, color = "green", linestyle = "--", label = f"THRESHOLD: {pourcentage_above_threshold: .2f}%")
plt.annotate("threshold", xy = (threshold,0), xytext=(0,10), textcoords = "offset points", ha = "center", color = "black" )

sns.histplot(people_height, bins = 100, kde = True, fill = 0, label = "PB DENSITY")
plt.xlabel("Heights")
plt.ylabel("Frequancy")
plt.title("Visualizing Peoples Heights")
plt.legend()
plt.show()