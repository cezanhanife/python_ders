# This function subtracts two numbers
def ekle(x, y):
   return x + y
# This function subtracts two numbers
def cikar(x, y):
   return x - y

# This function multiplies two numbers
def carp(x, y):
   return x * y

# This function divides two numbers
def bol(x, y):
   return x / y

print("İşlemi Seç.")
print("1.Ekle")
print("2.Çıkar")
print("3.Çarp")
print("4.Böl")

# Take input from the user
choice = input("Seçiminizi Giriniz (1/2/3/4):")

num1 = int(input("İlk Sayı : "))
num2 = int(input("İkinci Sayı : "))

if choice == '1':
   print(num1,"+",num2,"=", ekle(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", cikar(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", carp(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", bol(num1,num2))
else:
   print("Geçersiz Değer")
