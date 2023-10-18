n=(input("saisire votre chaine:"))
s=""
for i in reversed(n):
    s+=i
if s==n:
    print(n,"est palindrom")
else:
    print(n,"n'est pas palindrom")