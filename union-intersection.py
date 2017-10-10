#This does NOT maintain order of values in sets
print('WARNING: USE COMA (,) SEPERATED LISTS ONLY')
firstInput = input('Enter set A: ')
setA = firstInput.split(',')

secondInput = input('Enter set B: ')
setB = secondInput.split(',')

neuteredSetA = set(setA)
neuteredSetB = set(setB)
noDupsA = list(neuteredSetA)
noDupsB = list(neuteredSetB)

if len(noDupsA) > len(noDupsB):
	largerArray = noDupsA
	smallerArray = noDupsB
else:
	largerArray = noDupsB
	smallerArray = noDupsA
	
union = smallerArray[:]
intersect = []
differenceA = []
differenceB = []

#union
for i in largerArray:
	if i not in smallerArray:
		union.append(i)
print("union: ", union)

#intersect
for i in largerArray:
	if i in smallerArray:
		intersect.append(i)
print("intersect: ",intersect)

#A-B
for i in noDupsA:
	if i not in noDupsB:
		differenceA.append(i)
print("A - B: ",differenceA)

#B-A
for i in noDupsB:
	if i not in noDupsA:
		differenceB.append(i)
print("B - A: ",differenceB)