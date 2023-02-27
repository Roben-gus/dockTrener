import calendar

print('Добро пожаловать в календарь\n')

year = int(input ('Введите год'))
month = int(input('Месяц'))
print(calendar.month(year, month))

print('Всего хорошего')