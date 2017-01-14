class Student(Person):
    def __init__(Person, firstName, lastName, idNumber, scores):
        Person.firstName = firstName
        Person.lastName = lastName
        Person.idNumber = idNumber
        Person.scores = scores
        
    def calculate(Person):
        avg = sum(Person.scores)/len(scores)
        if 90 <= avg and avg <= 100:
            return 'O'
        elif 80 <= avg and avg < 90:
            return 'E'
        elif 70 <= avg and avg < 80:
            return 'A'
        elif 55 <= avg and avg < 70:
            return 'P'
        elif 40 <= avg and avg < 55:
            return 'D'
        elif 40 > avg:
            return 'T'
