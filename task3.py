def check(formula):
    if formula and formula[0].isdigit():
        for i in range(len(formula)):
            # if first element of string is digit
            # delete it until get to other symbol or until string is empty
            if formula[0] in '0123456789':
                formula = formula[1:]
            else:
                break
        if not formula:
            return True
        # if we get to + or -, use recursion to check formula from next index
        if formula[0] in '+-':
            return check(formula[1:])
    return False


if name == 'main':
    formulaInput = input('Input: ')
    if check(formulaInput):
        print('true, ', eval(formulaInput))
    else:
        print('false, none')