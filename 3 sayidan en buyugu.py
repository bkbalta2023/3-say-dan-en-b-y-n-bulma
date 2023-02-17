print("""
**********************************

3 Sayidan En buyugunu bulan program!!!

**********************************


""")

s1 = int(input("Sayi 1:"))
s2 = int(input("Sayi 2:"))
s3 = int(input("Sayi 3:"))

if(s1>=s2 and s1>=s3):
    print("En buyuk sayi: {}".format(s1))
if(s1==s2==s3):
    print("Sayilar birbirine esittir.")
elif(s2>=s1 and s2>=s3):
    print("En buyuk sayi: {}".format(s2))
elif(s3>=s1 and s3>=s2):
    print("En buyuk sayi: {}".format(s3))
