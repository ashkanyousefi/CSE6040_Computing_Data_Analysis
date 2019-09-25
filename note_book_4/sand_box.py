def eval_strint(s, base=2):
    assert type(s) is str
    assert 2 <= base <= 36
    
    L=len(s)
    calculated_value=0
    for i in range(L):
        print(i)
        check1=s[-1-i]
        calculated_value+=int(s[-1-i])*(base**i)
        print(calculated_value)
    
eval_strint('123',10)

