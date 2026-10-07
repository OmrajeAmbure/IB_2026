# using lambda , find the number grater then 20 and divible

data = [5,12,18,21,24,30,35,42]
even_with_replace_10 = list(filter(lambda num : num>20 and num%3==0,data))
print(even_with_replace_10)
