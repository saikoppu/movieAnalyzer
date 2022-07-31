import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
f = open("imdb.csv", encoding = "utf-8")
reader = csv.DictReader(f)
movielikes = []
budgets = []
for row in reader:
  if int(row["movie_facebook_likes"]) != 0 and int(row["movie_facebook_likes"]) < 200000 and row["budget"] != "" and int(row["budget"]) < 0.4: 
    movielikes.append(int(row["movie_facebook_likes"]))
    budgets.append(int(row["budget"]))
f.close()
sns.distplot(movielikes, kde = False)
plt.savefig("histogram.png")
plt.clf()
sns.scatterplot(movielikes, budgets)
plt.savefig("scatter.png")
plt.clf()
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
categories = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]
frequency = [10, 8, 7, 3]
graph = sns.barplot(categories, frequency,  palette = "Reds_d")
graph.set(title = "Ice Cream Popularity", xlabel = "Flavors", ylabel = "Number of People")
plt.savefig("bar.png")
plt.clf()
"""
