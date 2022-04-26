def make_division_by(n):
   return lambda x: x/n

division_by_3 = make_division_by(3)
print(division_by_3(18))