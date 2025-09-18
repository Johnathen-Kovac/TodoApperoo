<<<<<<< HEAD
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
=======

'''
Tasks Required
 - CRUD for Tasks
 - Tasks should contain a name, completion status, notes

 - Later on should be able to do the following:
    - File control
    - Create Lists
    - Create Sub Lists
    - Create Sub Tasks
    - Allow for Completion Dates / Times for both Lists, Sub Lists and Sub Tasks
    - Can utilise Redis / DB / Redis functionality.
'''

def createTask(idx: str):
    task = {
        idx: {
            'name': None,
            'complete': False,
            'notes': None,
            'dueDate': None,
            'active': True
        }
    }
    print("Please Enter the name of the task: ")
    task[idx]['name'] = input()

    print("Please Enter the Date Due: YYYY-MM-DD i.e; 2025-09-01")
    task[idx]['dueDate'] = input()
    
    print("Are the notes you want to enter for this task? (y|n)")
    response = input()
    if response == 'y':
        print("Please enter the notes for the Task: ")
        task[idx]['notes'] = input()
    return task

def updateTask(task: dict, name=None,complete=None,
               notes=None,dueDate=None):
    if name != None: task['name'] = name 
    if complete != None: task['complete'] = complete
    if notes != None: task['notes'] = notes
    if dueDate != None: task['dueDate'] = dueDate

    return task

def deleteTask(task: dict):
    task['active'] = False;
    return task

def printTaskList(taskList: dict):
    for i in taskList['activeList']:
        print(f'{i}: {taskList["tasks"][i]}')
        #print(taskList["tasks"][i])

if __name__ == "__main__":
    taskList = {
            'tasks': dict(),
            'activeList': set(),
            'inactiveList': set()
            }
    taskIndex = 0
    try:
	    while True:
	        if len(taskList) == 0: print('You currently have no Tasks.')
	        print('What would you like to do:')
	        print('1. Create a Task')
	        if len(taskList['activeList']) > 0: print('2. Update a Task') 
	        if len(taskList['activeList']) > 0: print('3. Delete a Task')
	        if len(taskList['activeList']) > 0: print('4. See Active Tasks')
	        response = input()
	        if int(response) == 1:
	            taskList['activeList'].add(str(taskIndex))
	            taskList['tasks'].update(createTask(str(taskIndex)))
	            taskIndex += 1
	
	        if int(response) == 2:
	            printTaskList(taskList)
	            print('which task would you like to update: ')
	            taskId = input()
	            updatedName = None
	            updatedNotes = None
	            updatedDueDate = None
	            updatedCompletion = None
	
	            print('Would you like to update the task name? (y|n)')
	            res = input()
	            if res == 'y':
	                print('Enter new name below')
	                updatedName = input()
	            print('Would you like to update the task Notes (y|n)')
	            res = input()
	            if res == 'y':
	                print('Enter new notes below')
	                updatedNotes = input()
	            print('Would you like to update the task Due Date (y|n)')
	            res = input()
	            if res == 'y':
	                print('Enter new Due Date below i.e., 2025-09-09')
	                updatedDueDate = input()
	            print('Is the Task Complete? (y|n))')
	            res = input()
	            updatedCompletion = res == 'y'
	
	            taskList['tasks'][taskId] = updateTask(taskList['tasks'][taskId], 
	                                                   name=updatedName,
	                                                   notes=updatedNotes,
	                                                   dueDate=updatedDueDate,
	                                                   complete=updatedCompletion)
	
	        if int(response) == 3:
	            print('which task would you like to delete: ')
	            taskId = input()
	            taskList['tasks'][taskId] = deleteTask(taskList['tasks'][taskId])
	            taskList['activeList'].remove(taskId)
	            taskList['inactiveList'].add(taskId)
	
	        if int(response) == 4:
	            print('Current Tasks: ')
	            printTaskList(taskList)
    except KeyboardInterrupt:
        print('Closing Application')
    except:
        print('Error occurred during process')
>>>>>>> temp
