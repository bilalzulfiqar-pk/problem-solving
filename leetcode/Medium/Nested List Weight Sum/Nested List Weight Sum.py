def power_sum(array,power=1):
    #write code here
    
    sum = 0
    for e in array:
        if isinstance(e, list):
            sum += power_sum(e,power+1)
        else:
            sum += e
    
    return sum**power
            
            
#Test Cases
print(power_sum([1, 1, 1])) # 3
print(power_sum([1, [4, 1], -1])) # 25
print(power_sum([1, [2, 3], [4, 5]])) # 107
