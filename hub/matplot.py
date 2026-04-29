import matplotlib.pyplot as plt
import numpy as np
plt.subplot(1, 2, 1)
history_array = np.loadtxt("history.csv", delimiter = ",", dtype = str)
history_array = history_array.reshape((-1,6))
winners_array = history_array[:,2]
winners_uniq, winners_counts = np.unique(winners_array, return_counts = True)
indices = winners_counts.argsort()[::-1][:5]
top_names = winners_uniq[indices]
top_counts = winners_counts[indices]
plt.bar(top_names, top_counts, width = 0.5)
plt.title("Top winners")
plt.xlabel("Username")
plt.ylabel("Number of wins")

plt.subplot(1, 2, 2)
games_array = history_array[:,5]
games_name, games_count = np.unique(games_array, return_counts = True)
games_name_list = list(games_name)
plt.pie(games_count, labels = games_name_list)
plt.title("Most played games")

plt.tight_layout()
plt.show()