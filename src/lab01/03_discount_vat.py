price = int(input("Цена: "))
dis = int(input("Скидка: "))
vat = int(input("Налог: "))

base = price * (1 - dis / 100)
vat_am = base * (vat / 100)
total = base + vat_am

print(f"База после скидки: {total:.2f}")
print(f"НДС: {vat_am:.2f}")
print(f"Итого к оплате: {total:.2f}")
