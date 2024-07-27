import random

print("Password Generator : ")
print("---------------------\n")

new_list = []
string_password = ""
length = 0

list_val = ["7","3","e","g","&",")","+","!","f","h","d","v","b","o","c","x","h","d","r","8","8","6","0","9","@","#","^","D","}","|","O","d","q","s","r","7",">","?","<",":",";","I","=","y","s","x","y","x","w","r"]

length = int(input("\nEnter the length of password : "))

for val in range(0,length):
    val = random.choice(list_val)
    new_list.append(val)

for val in new_list:
    string_password += val

if string_password=="":
    print("\nInvalid Input!")
else:
    print(f"\nNew Password : {string_password}")
    print("\nPassword Length : ",length)