fio = input('ФИО: ').strip()
parts = fio.split()
initials = ''.join([part[0].upper() for part in parts])
length = len(fio)

print(f'Инициалы: {initials}.')
print(f'Длина (символов): {length}')

