first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

third_strings = [first_strings.extend(second_strings)]                   # 1й вариант объединения списков
third_result = {x: len(x) for x in first_strings if len(x) % 2 == 0}

# third_strings_1 = first_strings + second_strings                        # 2й вариант объединения списков
# third_result_1 = {x: len(x) for x in third_strings_1 if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
# print(third_result_1)
