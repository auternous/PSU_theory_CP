#8 L(G)={(ac)n | n>0, a∈{b, d}, c∈{+, -}}
#Лавов, Логвин 21вп1


str = "-bb+d-d-d+b-b+d-"
flag = True
n = 0
i = 0
print("----------------")
while (i < len(str)):
  p = ""

  while len(p) < 2 and n < len(str):
    p += str[n]
    n += 1
  i = n
  print(p)
  if ((p!="b-") and (p!="b+") and (p!="d-") and (p!="d+")):
    flag = False
    break

if(len(str) == 0):
  flag = False

print(flag)