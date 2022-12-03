import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataframe = pd.read_csv("data/wc2022matchdata.csv", header=0)

# This command gets all the values currently available :)
existing = dataframe[dataframe.home_fouls.notna()]

# Matplotlib doesn't support emojis :(
team_to_flag = {
    "argentina": "🇦🇷",
    "australia": "🇦🇺",
    "belgium": "🇧🇪",
    "brazil": "🇧🇷",
    "cameroon": "🇨🇲",
    "canada": "🇨🇦",
    "costa rica": "🇨🇷",
    "croatia": "🇭🇷",
    "denmark": "🇩🇰",
    "ecuador": "🇪🇨",
    "england": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "france": "🇫🇷",
    "germany": "🇩🇪",
    "ghana": "🇬🇭",
    "iran": "🇮🇷",
    "japan": "🇯🇵",
    "mexico": "🇲🇽",
    "morocco": "🇲🇦",
    "netherlands": "🇳🇱",
    "poland": "🇵🇱",
    "portugal": "🇵🇹",
    "qatar": "🇶🇦",
    "saudi arabia": "🇸🇦",
    "senegal": "🇸🇳",
    "serbia": "🇷🇸",
    "south korea": "🇰🇷",
    "spain": "🇪🇸",
    "switzerland": "🇨🇭",
    "tunisia": "🇹🇳",
    "united states": "🇺🇸",
    "uruguay": "🇺🇾",
    "wales": "🏴󠁧󠁢󠁷󠁬󠁳󠁿"
}

team_to_denom = {
    "argentina": "ARG",
    "australia": "AUS",
    "belgium": "BEL",
    "brazil": "BRA",
    "cameroon": "CMR",
    "canada": "CAN",
    "costa rica": "CRC",
    "croatia": "CRO",
    "denmark": "DEN",
    "ecuador": "ECU",
    "england": "ENG",
    "france": "FRA",
    "germany": "GER",
    "ghana": "GHA",
    "iran": "IRN",
    "japan": "JPN",
    "mexico": "MEX",
    "morocco": "MAR",
    "netherlands": "NED",
    "poland": "POL",
    "portugal": "POR",
    "qatar": "QAT",
    "saudi arabia": "KSA",
    "senegal": "SEN",
    "serbia": "SRB",
    "south korea": "KOR",
    "spain": "ESP",
    "switzerland": "SUI",
    "tunisia": "TUN",
    "united states": "USA",
    "uruguay": "URU",
    "wales": "WAL"
}

foul_data = dict()

for x,y,stop in zip(existing.home_fouls, existing.home, existing.game_type):
    if stop != "group":
        break
    try:
        foul_data[team_to_denom[y]] += int(x)
    except KeyError:
        foul_data[team_to_denom[y]] = int(x)


for x,y,stop in zip(existing.away_fouls, existing.away, existing.game_type):
    if stop != "group":
        break
    try:
        foul_data[team_to_denom[y]] += int(x)
    except KeyError:
        foul_data[team_to_denom[y]] = int(x)

        
foul_data = list(foul_data.items())
foul_data.sort(key=lambda x: x[1])


histogram_ready = [([foul_data[0][0]], foul_data[0][1])]

for item in foul_data[1:]:
    if item[1] == histogram_ready[-1][1]:
        histogram_ready[-1][0].append(item[0])
    else:
        histogram_ready.append(([item[0]], item[1]))

    
for tup in histogram_ready:
    i = 0.05
    for country in tup[0]:
        plt.scatter(tup[1], i, c="grey", s=750, alpha=0.5)
        plt.annotate(country, (tup[1], i), ha="center", va="center", weight="bold")
        i += 0.05

plt.ylim(ymax=1, ymin=0)

plt.yticks([])
# plt.xlim(xmin=)
plt.xticks(np.arange(round(plt.xlim()[0])-1, plt.xlim()[1]+1, 1))
plt.suptitle("Histogram showing the number of fouls commited by each team at the group stage", size="xx-large", weight="bold" )
plt.xlabel("Number of fouls across all group stage matches")


fig = plt.gcf()
fig.set_size_inches((1920/96, 1080/96), forward=False)
fig.savefig("results/fouls_groupstage.png", dpi=96)


plt.show()