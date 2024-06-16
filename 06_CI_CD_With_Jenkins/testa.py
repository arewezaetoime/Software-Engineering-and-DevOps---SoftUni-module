def tryLambda():
    our_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(list(filter(lambda x: x % 2 == 0, our_list)))

tryLambda()
