class Person:
    def __init__(self, name, age, pol, eyeclr):
        #Создание атрибутов
        self.name = name
        self.age = age
        self.pol = pol
        self.eyeclr = eyeclr
    def __str__(self):
        return f"1.{self.name} 2.{self.age} 3.{self.pol}. 4.{self.eyeclr}"

person = Person('Джон', 20, 'Мужчина', 'Карий')#Создания экземпляра

while True:
    print(person)
    print('Не хотите изменить данные о человеке')
    print('y = да, n = нет')
    yn = input()
    if yn == 'y':
        #Установка значения атрибутов
        print('Какой атрибут вы хотите изменить 1-4')
        a = int(input())
        if a == 1:
            nm = input('Введите имя: ')
            person.name = nm
        if a == 2:
            ag = input('Введите возраст: ')
            person.age = ag
        if a == 3:
            print('m = Мужчина, w = Женщина')
            pl = input()
            if pl == 'm':
                person.pol = 'Мужчина'
            if pl == 'w':
                person.pol = 'Женщина'
        if a == 4:
            clr = input('Введите цвет глаз: ')
            person.eyeclr = clr
    elif yn == 'n':
        pass