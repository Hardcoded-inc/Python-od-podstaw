# Operatory logiczne

username = None  # Przypisanie pustej wartości
password = None

while not username:
    username = input("Wprowadź nazwę użytkownika: ")
password = input("Wprowadź swoje hasło: ")
if username == "admin" and password == "admin":  # Oba warunki muszą być spełnione
    print("Przyznano uprawnienia administratora")
elif username == "admin" or password == "admin":  # Conajmniej jeden warunek musi być spełniony
    print("Przyznano prawie uprawnienia administratora")
else:
    print("Witaj gościu!")
