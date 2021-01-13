candiNames = []
voterNames = []

#you'd want to validate here the stuff initially in the task like students between 28-35 and all that jazz but i cba
tutGroup = input("Enter your tutor group: ")
tutSize = int(input("How many students are there in the class? "))
candiNum = int(input("How many candidates are there? "))

form = [tutGroup, tutSize, candiNum]

#create list of candidates
for i in range(candiNum):
    name = input("Enter the name of candidate {}: ".format(i+1))
    name = [name, 0]
    candiNames.append(name)  
form.append(candiNames)

#don't let people vote if they already have
while True:
    abstain = 0
    for i in range(tutSize):
        voter = False
        while voter == False:
            votID = input("Enter your unique voter number: ")
            if votID not in voterNames:
                voterNames.append(votID)
                voter = True
            else:
                print("You've already voted.")
        
        #voting
        print("Student {}: The candidates to vote for are:".format(i+1))
        for c in range(len(candiNames)):
            print("{}: {}".format(c+1,candiNames[c][0]))
        intent = int(input("Do you want to 1: Vote or 2: Abstain. Enter the number: "))
        if intent == 1:
            vote = int(input("Enter the number next to the candidate you want to vote for: "))
            currentVote = form[3][vote-1][1]
            currentVote += 1
            form[3][vote-1][1] = currentVote
        else:
            abstain += 1
    form.append(abstain)

    #display votes and work out winner
    print("Group {}:".format(form[0]))
    highVotes = 0
    winner = []
    print("There were {} votes and {} abstentions".format(tutSize-abstain, abstain))
    for i in range(len(candiNames)):
        print("Candidate {}: {}: {} votes, {:.1f}%".format(i+1, form[3][i][0], form[3][i][1], 100*(form[3][i][1]/(tutSize-abstain))))
        if form[3][i][1] > highVotes:
            highVotes = form[3][i][1]
            winner = [[form[3][i][0], form[3][i][1]]]
        elif form[3][i][1] == highVotes:
            alsoWin = [form[3][i][0], form[3][i][1]]
            winner.append(alsoWin)

    #display winner and re-run election if tie
    if len(winner) == 1:
        print("The winner of the election was {} with {} votes, getting a {:.1f}% share of the votes.".format(winner[0][0], winner[0][1], 100*(winner[0][1]/(tutSize-abstain))))
        break
    else:
        newNames = []
        print("The election is tied between {} candidates.".format(len(winner)))
        for i in range(len(winner)):
            print("Candidate {} with {} votes".format(winner[i][0], winner[i][1]))
            nameNew = [winner[i][0], 0]
            newNames.append(nameNew)
        print("The election will be run again with only the tied candidates.")
        print(form[3])
        form[3] = newNames
        candiNames = newNames
        voterNames = []