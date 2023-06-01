# ----------PART 1----------
#1

print("Hello,world!")

#2
'''
a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))

if a > b:
    print(a-b)
elif a < b:
    print(b-a)
'''
#3
'''
for i in range(1,101):
    if i % 2 == 0:
        print(sum(i))
    else:
        pass
'''
#4
'''
ryadok = input("Введіть якесь слово:")

for i in ryadok:
    print(i)
'''
#5
'''
slovo = input("Введіть якесь слово і я перевірю чи є воно паліндромом:")

if slovo == slovo[::-1]:
    print("Слово є паліндромом")
else:
    print("Слово не є паліндромом")
'''
#6

'''
def parni(spysok):
    numbers = []
    for num in spysok:
        if num % 2 == 0:
            numbers.append(num)
    return numbers
spysok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list = parni(spysok)
print(numbers_list)
'''

#7 !!!
'''
def get_top_student(grades_spys):
    gradee = max(grades_spys.values())
    top_student = [name for name, grade in grades_spys.items() if grade == gradee]
    return top_student[0]
students = {'Vasyl': 9,'Petro': 7,'Kolya': 12}
top_student_name = get_top_student(students)
print("Студент з найвищою оцінкою:", top_student_name)
'''

#8

#поки не знаю

#9

#поки не знаю також


# ----------PART 2----------

#1
'''
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"Ім'я: {self.name} , Вік: {self.age}")
student = Student("Діма" , 16)
student.get_info()
'''
#2
'''
class BankAccount:
    def __init__(self,account_number ,balance):
        self.account_number = account_number
        self.balance = balance
        if self.balance < 0:
            print("Ото прікол,баланс може бути мінусовим ))")
    def deposit(self):
        print(self.balance + 1000)
    def withdraw(self):
        print(self.balance - 500)

babki = BankAccount(10000 , "Dima")
babki.deposit() - babki.withdraw()
'''
#3
'''
class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def get_info(self):
        print(f"Назва: {self.title} , Автор: {self.author}")
book = Book("1984" , "Джордж Орвелл")
book.get_info()
'''
#4
'''
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print("Gav")

ronnie = Animal("RONNIE" , "гав")
ronnie.make_sound()
'''










