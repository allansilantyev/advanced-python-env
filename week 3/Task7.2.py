n = int(input("Enter a non-negative integer: "))

# преобразуем в восьмеричное
octal = format(n, 'o')  # 'o' — восьмеричный формат
# добавляем ведущие нули, чтобы длина была 10
octal_10 = octal.zfill(10)

print(f"10-digit octal code: {octal_10}")
