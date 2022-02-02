total=int(input('Enter no. of bananas at starting :'))
distance=int(input('Enter distance you want to cover :'))
load_capacity=int(input('Enter max load capacity of your camel :'))
lose=0
start=total
for i in range(distance):
while start>0:
start=start-load_capacity #updating the bananass on the camel after it eats a ban
ana
if start==1:
lose=lose-1 #updating the number of bananas eaten by the camel
lose=lose+2 #updating the number of bananas eaten by the camel
lose=lose-1
start=total-lose #update to know the number of bananas on the camel
if start==0:
break
print(f"Number of bananas delivered:{start}")
