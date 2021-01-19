# Task: Groups
# We have a set of students available. Each student receives a score from 0 to 100.
# We want to group up our student by the score. The logic is: all the students in the same group should have a score within 10 points or eachother.
# If item fits into multiple groups, it should appear only in the first one.
#
# Example input:
#	[("John", 29), ("Alice", 34), ("Mary", 38), ("Harry", 45)]
# Example output:
#	[["John", "Alice", "Mary"], ["Harry"]]
#
# Example input:
#	[("John", 1), ("Alice", 34), ("Harry", 15)]
# Example output:
#	[["John"], ["Alice"], ["Harry"]]

def takeSecondValue(e):
    return e[1]

def Groups(students):
    students.sort(key=takeSecondValue)
    initialValue = students[0][1]
    finalList = []
    for i in range(initialValue, 100, 10):
        partialList = []
        for student in students:
            score = student[1]
            if score >= i and score < i+10:
                name = student[0]
                partialList.append(name)
        if len(partialList) is not 0:
            finalList.append(partialList)
    return finalList

