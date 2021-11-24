num= int(input("enter the number:"))
if num%3==0:
    print ("odd weird")
if num%2==0 and 2<num<5:
    print ("even weird")
if num%2==0 and 6>num>2:
    print("weird")
if num%2==0 and num>20:
    print ("even not weird")        
else:
    print("not")
