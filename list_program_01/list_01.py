L = ['[11,10,5]','[1,2,3]','[200,50]']

x = []
for i in L:
    a = []
    b = ''
    for j in i:
      if j.isdigit():
          b+=j
      else:
          if len(b)>0:
              a.append(int(b))
              b=''
    x.append(a)
print(x)
    
