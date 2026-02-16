def two_sums(numbers, target):
    fp = 0
    sp = len(numbers)-1
    while fp<sp:
        if numbers[fp]+numbers[sp]== target:
            return [fp+1,sp+1]
        elif numbers[fp]+numbers[sp]>target:
            sp-=1
        else:
            fp+=1  
    return list

print(two_sums([2,7,11,15],9))
print(two_sums([2,3,4],6))
print(two_sums([-1,0],-1))