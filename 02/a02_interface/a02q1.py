def is_leap_year(n):
  #YOUR CODE GOES HERE
  if n%400: return True
  if n%4==0 and n% 100!=0: return True
  return False

year=2014
print(is_leap_year(year))