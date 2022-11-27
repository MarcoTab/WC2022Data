import matplotlib.pyplot as plt
import numpy as np
from math import log
import pandas as pd

dataframe = pd.read_csv("wc2022matchdata.csv", header=0)

# This command gets all the values currently available :)
existing = dataframe[dataframe.home_possession.notna()]

# Game number
game_nbr = list(existing.game)

# possession
home_poss = list(round(existing.home_possession * 100))
away_poss = [100 - x for x in home_poss]

# Goal differential
goal_difference = list(existing.home_goals - existing.away_goals)

home_poss_neg = []
away_poss_neg = []
goal_difference_neg = []
games_neg = []

home_poss_neut = []
away_poss_neut = []
goal_difference_neut = []
games_neut = []

home_poss_pos = []
away_poss_pos = []
goal_difference_pos = []
games_pos = []

for (x, y, z, label) in zip(away_poss, home_poss, goal_difference, game_nbr):
    if z == 0:
        away_poss_neut.append(x)
        home_poss_neut.append(y)
        goal_difference_neut.append(z)
        games_neut.append(label)
    elif z < 0:
        away_poss_neg.append(x)
        home_poss_neg.append(y)
        goal_difference_neg.append(z)
        games_neg.append(label)
    else:
        away_poss_pos.append(x)
        home_poss_pos.append(y)
        goal_difference_pos.append(z)
        games_pos.append(label)


s = 1.25
plt.scatter(away_poss_pos, home_poss_pos, c="green", s=np.array([log(x+1, s)*250 for x in goal_difference_pos]), alpha=0.5)
plt.scatter(away_poss_neut, home_poss_neut, c="grey", s=np.array([250 for _ in goal_difference_neut]), alpha=0.5)
plt.scatter(away_poss_neg, home_poss_neg, c="red", s=np.array([log(abs(x)+1, s)*250 for x in goal_difference_neg]), alpha=0.5)

for i, part in enumerate(games_pos):
    plt.annotate(part, (away_poss_pos[i], home_poss_pos[i]), ha="center", va="center", weight="bold")

for i, part in enumerate(games_neut):
    plt.annotate(part, (away_poss_neut[i], home_poss_neut[i]), ha="center", va="center", weight="bold")

for i, part in enumerate(games_neg):
    plt.annotate(part, (away_poss_neg[i], home_poss_neg[i]), ha="center", va="center", weight="bold")

plt.xlabel("Possession of \"Away\" team", weight="bold")
plt.ylabel("Possession of \"Home\" team", weight="bold")

plt.suptitle("Possession vs Goal difference in Qatar 2022 World Cup matches.", size="xx-large", weight="bold")

xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()

plt.text(xmax-11.5, ymax-4.5, "Circle size indicates goal difference.\nGreen circles indicate positive goal difference for home team.\nRed circles indicate negative goal difference for home team.\nLabel is game #.", backgroundcolor="#FFCBA4")

fig = plt.gcf()
fig.set_size_inches((1920/96, 1080/96), forward=False)
fig.savefig("results/poss_v_gd.png", dpi=96)

plt.show()
