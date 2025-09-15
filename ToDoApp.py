
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
