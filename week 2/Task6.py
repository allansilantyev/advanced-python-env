def all_eq(lst):
    max_len = max(len(s) for s in lst)  
    return [s + "_" * (max_len - len(s)) for s in lst]  

# Пример использования
strings = input("Введите строки через пробел: ").split()
result = all_eq(strings)
print("Результат:", result)
