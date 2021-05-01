def secondLowestNumber(elements, lowestElemtnt):
    """Get Second Lowest Number form any List()"""
    secondLowest = None
    for element in elements:
        if(element > lowestElemtnt):
            if(secondLowest is None):
                secondLowest = element
            elif(secondLowest > element):
                secondLowest = element
    return secondLowest


N = int(input())

# Check Number of Students
if (N < 2 or N > 5):
    exit()

# variable: names to store Name
names = list()
# variable: scores to store Name
scores = list()

# get Names ans Scores of Students
for _ in range(N):
    name = input()
    score = float(input())

    names.append(name)
    scores.append(score)

# Gets the Lowest score of  Students
lowestScore = min(scores)

# get the second lowest grade
sln = secondLowestNumber(scores, lowestScore)

newNamesList = list()
for ind in range(N):
    if (scores[ind] == sln):
        newNamesList.append(names[ind])

for name in sorted(newNamesList):
    print(name)
