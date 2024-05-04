students = [
    {"name": "Hermione", "house": "Gryffindor", "patronous": "Otter"},
    {"name": "Harry" , "house": "Gryffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronous": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]
print("name |", "house |", "patronous |", sep="\t  ")
for i in range(len(students)):
    print(students[i]['name'], students[i]['house'], students[i]['patronous'], sep=" -> ")