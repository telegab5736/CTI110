#tracker for bugs collected in a 5 day span
#6JULY2020
#CTI-110 P4T2- Bug Collector
#Brian Telega

#Accumulator
total = 0

#Number of bugs collect for 5 days
for day in range(1,6):
    print('Enter bugs collected ',day)
    bugs = int(input())
    total = total + bugs

#Dispay total bugs
print('You collected a total of', total, 'bugs.')
