eren = {
    "name": "Eren",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}

mikasa = {
    "name": "Mikasa",
    "homework": [100, 92, 98, 100],
    "quizzes": [82, 83, 91],
    "tests": [89, 97]
}

armin = {
    "name": "Armin",
    "homework": [0, 87, 75, 22],
    "quizzes": [0, 75, 78],
    "tests": [100, 100]
}

students = [eren, mikasa, armin]

for i in students:
    print("\nStudent Information: ")
    for key in i:
        print("{}: {}".format(key, i[key]))

def average(numbers):
    total = sum(numbers)
    total = float(total)/len(numbers)
    return total
    

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework*.10 + quizzes*.30 + tests*.60

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for i in students:
        results.append(get_average(i))
    return average(results)


print(get_class_average((students)))
print(get_letter_grade(get_class_average(students)))