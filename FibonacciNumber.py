#fibonacci number less than 100 - 0,1,1,2,3,5,8,13,21,34,55,89
x=0
y=1
print(x) 
print(y)
result=0

while result <= 100:
  result=x+y
  x=y
  y=result
  if result < 100:
    print(result) 



