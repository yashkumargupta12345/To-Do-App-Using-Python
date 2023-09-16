from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

user_prompt = 'Type add, show or exit: '
while True:
    user_action = input(user_prompt).strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Command invalid! ")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number-1
            todos = get_todos()
            todos.pop(number)

            write_todos(todos)
        except IndexError:
            print("There is no item with that number")

    elif 'exit' in user_action:
        break

    else :
        print("Hey! you entered an invalid command")

print("Bye!")

