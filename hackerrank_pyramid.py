n=10
s="".join([chr(i) for i in range(96+n,96,-1)])
st=""
if n==1:
  print(s)
else:
  for i in range(1,n+1):
    st=""
    for j in range(i):
      st+=s[j]
    print(("-".join(st)+"-"+"-".join(s[:j][::-1])).center(4*n-3,"-"))

  for i in range(n-1,0,-1):
    st=""
    for j in range(i):
      st+=s[j]
    print(("-".join(st)+"-"+"-".join(s[:j][::-1])).center(4*n-3,"-"))
  