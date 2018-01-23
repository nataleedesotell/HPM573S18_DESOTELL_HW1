#PROBLEM 4
#NATALEE DESOTELL
#HPM 573 HOMEWORK 1

#the end of lecture 5 is helpful for this

#PART 1
#create a list named yours and store fave schools
yours = ["Yale", "MIT", "Berkeley"]
#each of these schools is an attribute and they are changeable

#create a list named mine with my face schools
mine = ["UW Madison", "UT Austin", "Madison College"]

#use the + operator to create a new list, named ours1, to represent our fave schools
ours1 = mine + yours

#now, create another list ours2 to again represent our fave schools but use:
ours2 = []
ours2.append(mine)
#add things to the end of list
ours2.append(yours)

print(ours1)
print(ours2)


#ours1 and ours2 differ how?
print(type(ours1))
print(type(ours2))

#tuples are immutable
#lists are muutable objects

#can add elements to end of list with L.append(element)
#mutates the list

#yours[2] = "MSOE" #is this how I change element 2?
#side effect of mutating a list



#the plus operator gives a new list that's the sum of the 2 lists
#does not mutate the list
#gives a new list, doesn't change the original lists

#we have to assign the result of the addition to the new list otherwise the result is lost
#mutate a list directly: use extend

#the list that gets mutated is the one that's passed into the (argument?)




# #PART 2
# yours = ["Yale", "MIT", "MSOE"]
# mine = ["UW Madison", "UT Austin", "Madison College"]

#second element is the third in the list
# print(ours1)
# print(ours2)

#why does changing yours change ours2 but not ours1?
