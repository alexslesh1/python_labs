def format_record(rec: tuple[str, str, float]):
    
    if not isinstance(rec, tuple):
        raise TypeError(f"Ожидается tuple, получен {type(rec).__name__}")
    
    if len(rec) != 3:
        raise ValueError(f"Ожидается кортеж из 3 элементов, получено {len(rec)}")
        
    fio, group, gpa = rec
    
    if not isinstance(fio, str):
        raise TypeError(f"ФИО должен быть строкой, получен {type(fio).__name__}")
    
    if not isinstance(group, str):
        raise TypeError(f"Группа должна быть строкой, получен {type(group).__name__}")
    
    if not isinstance(gpa, (int, float)):
        raise TypeError(f"GPA должен быть числом, получен {type(gpa).__name__}")
    
    if gpa < 0 or gpa > 5:
        raise ValueError(f"GPA должен быть в диапазоне от 0 до 5, получено {gpa}")
    
    
    parts = fio.strip().split()
    family = parts[0]
    initials = ""
    for part in parts[1:]:
        initials += part[0].upper() + "."
    if not initials:
        initials = ""
    
    form_gpa = f"{gpa:.2f}"
    return f"{family} {initials}, гр. {group}, GPA {form_gpa}"



print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

#12323