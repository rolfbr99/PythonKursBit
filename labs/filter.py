lst=list(range(1,21))

print(lst)

even=lambda num:True if num % 2 == 0 else False
odd=lambda num:True if num % 2 == 1 else False
even_numbers=list(filter(even,lst))
odd_numbers=list(filter(odd,lst))
print(even_numbers)
print(odd_numbers)