big_cap = int(input())
small_cap = int(input())
goal = int(input())
def jugs(J1=0, J2=0):
while(J1 != goal):
# print(J1, J2)
J2 = J2+(small_cap-J2) # fill J2
print(J1, J2)
if(J1+J2 > big_cap):
temp = big_cap - J1
J1 += temp
J2 -= temp # transfer J2->J1
else:
J1 += J2 # transfer J1->J2
J2 = 0
print(J1, J2)
if(J1 == big_cap):
J1 = 0
J1 += J2
J2 = 0
print(J1, J2)
if __name__ == "__main__":
jugs()