def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list
     of to-do items """
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
        file_local.close()
        return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text
    file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
        file_local.close()


if __name__ == "__main__":
    print("Hello from functions")