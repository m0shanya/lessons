def three_args(*spis):
    j = 1
    for i in spis:
        if i == None:
            j += 1
        if i != None:
            print(f"elements passed:\nvar{j} = {i}")
            j += 1
    return


k = int(input("Test(1) or input from keyboard(2)?"))
if k == 2:
    a = int(input("Input any number:\n"))
    b = int(input("Input any number:\n"))
    c = int(input("Input any number:\n"))
    spis = []
    spis.append(a)
    spis.append(b)
    spis.append(c)
    three_args(*spis)
else:
    three_args(None, 1, 2)
