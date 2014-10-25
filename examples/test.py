import csv

credentials_file = 'throwaway.csv'
print "doing stuff"
with open("throwaway.csv") as f:
    row = csv.reader(f)
print row


