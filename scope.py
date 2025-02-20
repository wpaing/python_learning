# Global Variables
name = "John"
def sayhello():
    global name; #overriding the global variable
    name = "Alex"
    print(f'Hello {name}')
sayhello()
print(f'Hello {name}')