a="59758034323742284979562302567188059299994912382665665642838883745982029056376663436508823581366924333715600017551568562558429576180672045533950505975691099771937719816036746551442321193912312169741318691856211013074397344457854784758130321667776862471401531789634126843370279186945621597012426944937230330233464053506510141241904155782847336539673866875764558260690223994721394144728780319578298145328345914839568238002359693873874318334948461885586664697152894541318898569630928429305464745641599948619110150923544454316910363268172732923554361048379061622935009089396894630658539536284162963303290768551107950942989042863293547237058600513191659935"
#test="12345678"
test="03036732577212944063491565474664"
#a=test
numbers=[int(x)for x in a]*10_000
messageIndex = int(a[:7])
numbers=numbers[messageIndex:]
iterations=100
for iteration in range(iterations):
    print(iteration)
    newNumbers=[]
    rowTotal=sum(numbers)
    for row in range(len(numbers)):
        if row!=0:
            rowTotal -= numbers[row-1]
        newNumbers.append(int(str(rowTotal)[-1]))
    numbers = newNumbers
print("".join([str(x) for x in numbers])[:8])
