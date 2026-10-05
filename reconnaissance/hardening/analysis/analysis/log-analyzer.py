from collections import Counter
import csv

protocols = Counter()
sources = Counter()
destinations = Counter()

with open("ssh_packets.csv") as f:
    for row in csv.DictReader(f):
        protocols[row["Protocol"]] += 1
        sources[row["Source"]] += 1
        destinations[row["Destination"]] += 1

print("Protocols:", protocols)
print("Sources:", sources)
print("Destinations:", destinations)
