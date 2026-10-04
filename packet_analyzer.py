from collections import Counter
import csv

p=Counter()
s=Counter()
d=Counter()


with open("ssh_packets.csv") as f:
    for r in csv.DictReader(f):
       p[r["Protocol"]]+=1
       s[r["Source"]]+=1
       d[r["Destination"]]+=1

print("Protocols:",p)
print("Sources:",s)
print("Destinations:",d)