import csv
from collections import Counter

with open("favoritos.csv",mode='r') as file:
    reader = csv.DictReader(file)
    counts = Counter()

    for row in reader:
        favorite = row["cores"]
        counts[favorite] += 1


for favorite, count in counts.most_common(): 
    print(f"-----»»»»»»    {favorite} :   {counts[favorite]}  ««««««-----\n")