import testModule

print(testModule.pi)


def argument_test(a, b, c):
    print(f"a {a}")
    print(f"b {b}")
    print(f"c {c}")


argument_test(a="a", c="b", b="c")


def greet_with(name, location):
    print("")


greet_with(location="long beech", name="adam")

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    desc = ""
    student_score = student_scores[student]
    if student_score > 80:
        desc = "Great!"
    elif student_score <= 80 and student_score > 60:
        desc = "Do better!"
    else:
        desc = "You're horrible"
    student_grades[student] = desc
print(student_grades)


