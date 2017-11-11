def enter_data():
    global hungry_fish, other_fishes, aquarium #make the variables global to be used in each of the methods
    hungry_fish, fishes = map(str,raw_input().split('#')) #split inputs between hungry fish and other fishes
    other_fishes = map(int,fishes.split(',')) #initialize the list of other fishes
    hungry_fish = int(hungry_fish) #initialize hungry fish
    aquarium = map(int,fishes.split(',')) #setup the aquarium with all the fishes
    aquarium.append(hungry_fish) #add the hungry fish to the aquarium

def eat():
    global hungry_fish, other_fishes, aquarium
    aquarium = [] #each time setup a new aquarium and let the hungry fish eat
    fish = hungry_fish-1 #hungry fish will eat the biggest fish it can eat which is 1 less than itself, this is to minimize the moves.
    while (fish != 0): #until there are no more fishes left that can be eaten continue.
        if(fish in other_fishes): #if the above mentioned fish is available in tank, eat it.
            aquarium=[] #empty the aquarium each time as the hungry fish is growing in size.
            hungry_fish+= fish #hungry fish's size increases
            aquarium.append(hungry_fish) #put this fish into aquarium
            del other_fishes[other_fishes.index(fish)] #remove the eaten fish from the list of other fishes
            fish = hungry_fish #increase the size of the next fish that can be eaten by the hungry fish
        fish-=1 #hungry fish cannot eat another fish of same size at itself, hence reduce size, and keep on reducing it if it is not found in the other fish list.
    for remaining in other_fishes: #now add all the remaining fishes in the aquarium
        aquarium.append(remaining)
    if hungry_fish not in aquarium: #if there was no fish availableto be eaten by hungry fish then append it again
        aquarium.append(hungry_fish)


def display_aquarium():
    global hungry_fish, other_fishes, aquarium
    print(aquarium)

def remove(iteration):
    global moves, other_fishes, aquarium
    if('stage'+str(iteration) in moves): #check if we are re-visiting some stage, it would be usually after adding a new fish
        moves['stage'+str(iteration)]+= len(aquarium)-1 #number of moves required to remove the fishes is added
    else: #if we are visiting this stage first time then simply initialize
        moves['stage'+str(iteration)] = len(aquarium)-1

def add(iteration):
    global moves, other_fishes, hungry_fish
    other_fishes.append(hungry_fish-1)
    if(iteration>2): #whenever iteration goes above 2nd stage, there becomes a need to add the steps performed in the previous stage as there were fishes added & removed before also.
        moves['stage'+str(iteration)] = 1+moves['stage'+str(iteration-1)]
    else: #for any stage between 1 & 2 we can directly add.
        moves['stage'+str(iteration)] = 1


#START OF PROGRAM
enter_data() #call the function to enter and initialize the fish tank
moves={} #dictionary to store the total moves being taken with each iteration

iteration=1 #initialize first iteration
while (len(aquarium)!=1): #iterate until there is only one fish left in the tank
    eat() #in each iteration first let the hungry fish all the smaller fishes
    remove(iteration) #after there is no more fishes left to eat, calculate the moves required if we have to remove all the remaining fishes
    iteration+=1 #increase iteration as now all we can do is add one more fish and repeat the above steps.
    add(iteration) #after we have calculated moves required to remove all fishes on by one, we add a fish and again calculate the moves required.

min_moves=1000000 # highest number of fishe allowed in tank
for key,value in moves.items():
    if value<min_moves: #calculate least number of moves required
        min_moves = value
print("minimum number of moves required : %d"%min_moves)
