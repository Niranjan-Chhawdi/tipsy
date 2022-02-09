#If entered no. lies between 10to30 then print :
# 1) If n is divible by 3 print "Sacred"
# 2) If n is divible by 7 print "Heart"
# 3) If n is divible by 3 and 7 both  print "Sacred Heart"
n = int(input("Enter the number : "))

for i in range(20,101):
    if n%3==0 and n%7==0:
        print("tipsytopsy")
    elif n%3==0:
        print("tipsy")
    
    elif n%7==0 :
        print("Topsy")
        
    
    break    
    
  