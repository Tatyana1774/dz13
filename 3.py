from student import Student

# Пример использования:
student = Student("Алексей Третьяков", "subjects.csv")
student.add_score("Русский язык", 2)
student.add_test_result("Русский язык", 15)
print(student.average_test_score("Русский язык"))
print(student.average_score())