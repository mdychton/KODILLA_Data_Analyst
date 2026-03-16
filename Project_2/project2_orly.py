


exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = [name for name, points in exam_points.items() if points <= 45]
top_students = [name for name, points in exam_points.items() if points >= 91]
best_student = max(exam_points.items(), key=lambda x: x[1])

print(failed_students)
print(top_students)
print(best_student)
