#PROBLEM 4
#NATALEE DESOTELL
#HPM 573 HOMEWORK 1

# 1. Describe how ours1 and ours2 differ from each other.

#"Append" adds an object to the list, but "+" combines two lists
# and sets a new list = to a variable (ours1). Ours2 will continue
#to reference the old lists, while ours1 is an entirely new list.

# 2. Explain why changing yours would changes ours2 but not ours1.

#Using "+" created a new list that doesn't continue to reference the
#old lists. However, .append continues to reference the original lists,
#meaning it will be changed when the original lists are changed. Hence, the
#change in ours2 while ours1 stayed the same.

#PART 1
yours = ["Yale", "MIT", "Berkeley"]
mine = ["UW Madison", "UT Austin", "Madison College"]
ours1 = mine + yours
ours2 = []
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)

yours[2] = "MSOE"

print("After changing 'yours':", ours1)
print("After changing 'yours':", ours2)
