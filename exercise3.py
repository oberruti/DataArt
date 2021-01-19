# Task: Groups 2
# We have a set of products available. Each product receives a score from 0 to 100.
# We want to group up our products by the score. The logic is: all the products in the same group should have a score within 10 points or eachother.
# If item fits into multiple groups, it should appear in multiple groups.
#
# Example input:
#	[("Apple", 29), ("Banana", 34), ("Orange", 38), ("Pineapple", 45)]
# Example output:
#	[["Apple", "Banana", "Orange"], ["Orange", "Pineapple"]]
#
# Example input:
#	[("Apple", 12), ("Banana", 20), ("Lemon", 21), ("Pineapple", 28)]
# Example output:
#	[["Apple", "Banana", "Lemon"], ["Banana", "Lemon", "Pineapple"]]

def takeSecondValue(e):
    return e[1]

def Groups(products):
    products.sort(key=takeSecondValue)
    finalList = []
    for i in products:
        partialList = []

        for product in products:
            score = product[1]
            initialValue = i[1]
            finalValue = initialValue + 10

            if score >= initialValue and score < finalValue:
                name = product[0]
                partialList.append(name)

        if len(partialList) is not 0:
            finalList.append(partialList)

    return finalList