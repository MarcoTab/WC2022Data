import matplotlib.pyplot as plt
import numpy as np
from math import log2
import pandas as pd

dataframe = pd.read_csv("wc2022matchdata.csv", header=0)

# This command gets all the values currently available :)
existing = dataframe[dataframe.home_possession.notna()]

# Game number
game_nbr = list(existing.game)

# Possession
home_poss = list(round(existing.home_possession * 100))

# Goal differential
goal_difference = list(existing.home_goals - existing.away_goals)

home_poss_neg = []
goal_difference_neg = []
games_neg = []

home_poss_neut = []
goal_difference_neut = []
games_neut = []

home_poss_pos = []
goal_difference_pos = []
games_pos = []

for (x, y, label) in zip(home_poss, goal_difference, game_nbr):
    if y == 0:
        home_poss_neut.append(x)
        goal_difference_neut.append(y)
        games_neut.append(label)
    elif y < 0:
        home_poss_neg.append(x)
        goal_difference_neg.append(y)
        games_neg.append(label)
    else:
        home_poss_pos.append(x)
        goal_difference_pos.append(y)
        games_pos.append(label)


s = 1
plt.scatter(home_poss_pos, goal_difference_pos, c="green", s=500, alpha=0.5)
plt.scatter(home_poss_neut, goal_difference_neut, c="grey", s=500, alpha=0.5)
plt.scatter(home_poss_neg, goal_difference_neg, c="red", s=500, alpha=0.5)
plt.axhline(0, color="black")

for i, part in enumerate(games_pos):
    plt.annotate(part, (home_poss_pos[i], goal_difference_pos[i]), ha="center", va="center", weight="bold")

for i, part in enumerate(games_neut):
    plt.annotate(part, (home_poss_neut[i], goal_difference_neut[i]), ha="center", va="center", weight="bold")

for i, part in enumerate(games_neg):
    plt.annotate(part, (home_poss_neg[i], goal_difference_neg[i]), ha="center", va="center", weight="bold")

plt.xlabel("Home team possession %", weight="bold")
plt.ylabel("Goal difference for home team", weight="bold")

plt.suptitle("Possession vs Goal difference in Qatar 2022 World Cup matches.", size="xx-large", weight="bold")
plt.title("Labels refer to the game number.")

plt.xlim(0, 100)
plt.xticks(np.arange(0, 101, 10))
ymin, ymax = plt.ylim()

fig = plt.gcf()
fig.set_size_inches((1920/96, 1080/96), forward=False)
fig.savefig("results/poss_v_gd_2.png", dpi=96)

plt.show()
