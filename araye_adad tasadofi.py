import random 
n= int (input("enter number:"))
list=[]




for i in range(n):
    
    x= random.randint(1,100)
      
    if x  not in list:
     list.append (x)
   
      
print(list)
      
       