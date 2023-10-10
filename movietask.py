movieNames = ['sherlock holmes','avengers','titanic','La La Land','WaLL-e']
data = {
            'person1':[4,5,3,4,2],
            'person2':[3,4,3,2,4],
            'person3':[2,3,4,5,3],
            'person4':[3,4,4,5,2],
            'person5':[4,'?',3,'?',4],
        }

targetPerson = 'person5'
simarityScore = {}
differenceScore = {}
for user in data:
    if(user != targetPerson):         
        numberOfMovies = len(movieNames)
        simarityScore[user] = 0;
        differenceScore[user] = 0;
        # let's find the similarities and differences between the users
        for x in range(0,numberOfMovies):
            if(data[targetPerson][x] != '?'):
                if(data[targetPerson][x] == data[user][x]):
                        simarityScore[user] += 1
                else:
                        bothData = [data[targetPerson][x],data[user][x]]
                        differenceScore[user] += differenceScore[user] + (max(bothData) - min(bothData))


#lets now compare the simarity score to find who matches the most
matchedUser = []
maxScore = -1
for user in simarityScore:
    if(simarityScore[user] > maxScore):
        matchedUser = []
        matchedUser.append(user)
        maxScore = simarityScore[user]
    elif(maxScore == simarityScore[user]):
        matchedUser.append(user)

# if more than 1 user, we will have to check the differnces
if(len(matchedUser) > 1):
    finalUser = ''
    minScore = 99999999;

    for user in differenceScore:
        if(differenceScore[user] < minScore):
            finalUser = user
            minScore = differenceScore[user]

#lets replace the results and print in
for index,value in enumerate(data[targetPerson]):
    if(value == '?'):
        data[targetPerson][index] = data[finalUser][index]


print(f'predicted rating of {targetPerson} for the movies are as follows')
print(data[targetPerson])