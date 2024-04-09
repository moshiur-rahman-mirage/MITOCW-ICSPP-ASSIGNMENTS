def intToStr(i):
    digits="0123456789"
    if i ==0:
        return '0'
    result=''
    while i>0:
        result = digits[i%10]+result
        i=i//10
    return result

print(intToStr(5))



def genSubsets(L):
    if len(L)==0:
        return [[]]
    smaller=genSubsets(L[:-1])
    extra=L[-1:]
    new=[]
    for small in smaller:
        new.append(small+extra)
    return smaller+new

print(genSubsets([1,2,3,4]))