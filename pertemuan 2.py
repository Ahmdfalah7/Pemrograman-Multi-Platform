#sum of natural numbers
def while_loop_example():
    sum1 = 0
    count = 1
    while (count < 10):
        sum1 = sum1 + count
        count = count + 1
        print (count)# should be 10
        print (sum1)# should be 45
while_loop_example()