#PROBLEM 4
#NATALEE DESOTELL
#HPM 573 HOMEWORK 1

#PART 1
yours = ["Yale", "MIT", "Berkeley"]
mine = ["UW Madison", "UT Austin", "Madison College"]

ours1 = mine + yours
ours2 = []
ours2.append(mine)
ours2.append(yours)

print(ours1)
print(ours2)

#ours1 and ours2 differ how? 

#PART 2
yours = ["Yale", "MIT", "MSOE"]
mine = ["UW Madison", "UT Austin", "Madison College"]

#second element is the third in the list
print(ours1)
print(ours2)

#why does changing yours change ours2 but not ours1?