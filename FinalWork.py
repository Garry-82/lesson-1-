grades = [[5, 4, 4, 3, 5, 5, 5], [5, 5, 5, 4, 5, 5], [3, 5, 5, 4, 5, 4, 5], [4, 4, 4, 5, 4, 5], [3, 3, 3, 2, 3, 3, 4],
          [5, 5, 5, 5, 5, 5, 5]]
students = {'Roman', "Maks", "Segr", "Andrey", "Igor", "Vadim"}
print("Условие задания. Дано:")
print("- оценки учеников: ", grades)
print("- имена учеников:  ", students)

if len(grades) == len(students):
    students = list(students)
    students.sort()
    #sorted_students=sorted(students) # - еще один метод сортировки
    print("отсортированный список учеников: ", students)
    a = 0  # - переменная, счетчик учеников
    dict_students = {}  # - переменная итогового словаря
    while a < len(students):
        average_score = sum(grades[a]) / len(grades[a])
        dict_students[students[a]] = average_score
        a = a + 1
else:
    print("количество учеников и их оценок не совпадает. БУДЬТЕ ВНИМАТЕЛЬНЕЕ!")

print("вывод словаря учеников с указанием их среднего балла: ")
print(dict_students)
