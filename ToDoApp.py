import random as rdm
import math

def generateQuestion():
        difficulty = rdm.randint(1,3)
        opp = set()
        for i in range(difficulty):
            opp.add(rdm.randint(1,5))
        values = []
        for i in range(0,difficulty+1):
            values.append(rdm.randint(-10,10))
            # Use the below to make it calc required in some cases
            # values.append(rdm.randint(-10 ** (difficulty-1),10 ** (difficulty-1)))
        qa = dict()
        question = str(values[0])
        it = 1
        ans = values[0]
        oChar = (' + ',' - ',' * ',' / ','^')
        for o in opp:
            if o == 5: values[it] = values[it] % 10
            question = question + oChar[o-1] + str(values[it])
            if it < len(values) - 1:
                question = f'({question})'
            if type(ans) == int: ans = calculate(ans,values[it],o)
            it += 1
        qa['q'] = question
        qa['a'] = round(ans,2) if type(ans) != str else ans
        qa['mc'] = [round(ans,2) if type(ans) != str else ans]
        if type(ans) != str:
            for i in range(3):
                x = 0
                y = 0
                try:                
                    y = math.fabs(ans)
                    x = rdm.random() * rdm.choice([-1,1])
                    x *= (10 ** (math.log10(y)))# // 1))
                    if type(ans) == int: x //= 1
                except ValueError:
                    if len(values) >= 1:
                        x = values.pop(rdm.randint(0,len(values)-1))
                    else:
                        x = rdm.randint(-10,10)
                        # Use the below to make it calculator required in some cases
                        # x = rdm.randint(-10 ** (difficulty-1),10 ** (difficulty-1))
                qa['mc'].append(round(x,2))
        else:
            qa['mc'].extend([0,'infinity', 'negative infinity'])
        rdm.shuffle(qa['mc'])
        return qa

def calculate(a,b,opperator):
    assert opperator >= 1 and opperator <= 5, "Out of Opperator Boundery"
    if opperator == 1: return a + b
    if opperator == 2: return a - b
    if opperator == 3: return a * b
    if opperator == 4 :
        if b == 0:
            return "Undefined"
        return a / b
    if opperator == 5: return a ** b

if __name__ == '__main__':
    assert calculate(1,2,1) == 3, "Failed to addition"
    assert calculate(1,2,2) == -1, "Failed to subtract"
    assert calculate(1,2,3) == 2, "Failed to multiply"
    assert calculate(1,2,4) == 0.5, "Failed to divide"
    assert calculate(2,2,5) == 4, "Failed to exponent"
    try:
        while True:
            qDict = generateQuestion()
            answer = qDict['a']
            question = qDict['q']
            options = qDict['mc']
            print(f'What is {question}?')
            optChar = 65
            for opt in options:
                print(f'{chr(optChar)}. {opt:.2f}')
                optChar += 1
            userInput = input()
            print('Correct') if options[ord(userInput) - 65] == answer else print(f'Incorrect. {answer} is correct')
    except (KeyboardInterrupt, EOFError):
        print('Closing Program')
