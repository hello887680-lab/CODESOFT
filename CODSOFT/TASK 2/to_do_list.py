import os 
import json
file = os.path.join(os.path.dirname(__file__),'tasks.json')
def save_tasks(tasks):
    with open(file,'w') as f:
        json.dump(tasks,f)
def load_tasks():
    if os.path.exists('tasks.json'):
        with open(file) as f:
            t=json.load(f)
            return t 
    else:
        return []
def add_task(tasks):
    d=input("Enter the task:")
    di={'task':d,"completed":False}
    tasks.append(di)
    print('TASK ADDED SUCCESSFULLY!')
    save_tasks(tasks)
def view_tasks(tasks):
    for i in tasks:
        if i['completed']==True:
            status = '[COMPLETED]'
        else:
            status ='[PENDING]'
        print(i['task'],status)

def complete_task(tasks):
      task_to_complete= int(input('Enter the index number of the task you want to mark as complete : '))
      index=task_to_complete-1
      if 0<=index< len(tasks):
        if tasks[index]['completed']==False:
            tasks[index]['completed']=True
            print('TASK COMPLETED!')
        else:
            print('The task is already completed.')    
        save_tasks(tasks)    
      else:
          print('INVALID INDEX NUMBER TYPED!')   

def delete_task(tasks):
    view_tasks(tasks)
    task_to_delete=int(input("Enter the index number you want to delete : "))
    index=task_to_delete-1
    tasks.pop(index)
    print('TASK DELETED SUCCESSFULLY')
    save_tasks(tasks)

def main():
    tasks=load_tasks()
    while True:
        print("-----------TO DO LIST-------------")
        print(' 1.ADD TASK \n 2.VIEW TASKS \n 3.MARK A TASK COMPLETED \n 4.DELETE A TASK \n 5.EXIT')
        try: 
            choice=int(input("Enter your choice : "))
            if choice==1:
                add_task(tasks)
            elif choice==2:
                view_tasks(tasks)
            elif choice==3:
                complete_task(tasks)
            elif choice==4:
                delete_task(tasks)
            elif choice ==5:
                break
            else:
                print('INVALID INPUT! ENTER 1,2,3,4,5.')
        except ValueError:
            print('PLEASE ENTER 1,2,3,4,5 ONLY.')
  
if __name__=='__main__':
    main()

