
#Ro'yxatni to'ldirish

friends = []

n = int(input("Nechta tanishingizni kiritasiz  "))

for x in range(0,n):
    name = input(f"{x+1}-Ismni kiriting ")
    friends.append(name)
    
print(friends)