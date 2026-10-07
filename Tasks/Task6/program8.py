# create list of numbers extract the number between 15 and 40 incliding limits
data = [12,5,18,25,30,42,50]

extract = list(filter(lambda num: (num>15 and num<40),data))
print(extract)
