
#Shart operatorlaridan foydalanish

print("Bu dastur orqali siz sinfdagi o'quvchilarning reytingini bilib olishingiz mumkin ")

n = int(input("Nechta bahoni hisoblaysiz "))

s = 0

for x in range(0,n):
    
    baho = int(input(f"{x+1}-fandan olgan bahoingizni kiriting "))
    
    s = s + baho
    
print(f"O'quvchining reytingi {n}ta fandan {s/n} ")

if s/n > 4:
    print("Bu o'quvchi a'lochi")
elif s/n > 3:
    print("Bu o'quvchi yaxshi")
elif s/n > 2:
    print("Bu o'quvchi qoniqarli")
else:
    print("Bu o'quvchi qoniqarsiz")