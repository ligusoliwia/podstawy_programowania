class greet:
    def __init__(self, name: str, surname: str, age: int):
        self._name = name
        self._surname = surname
        self._age = age
    def __str__(self):
        return f"{self._name} {self._surname} is {self._age} years old."

def get_id(data: dict, id: int) -> greet | None:
    return data.get(id)

data = {}
id = 1

while True:
    agred = input('''hello! to add users to the database please answer my questions
         if you want to exit please type "exit": ''')
    if agred == "exit":
        print("well looks like you don't want to use my great program (mf), suit urself!")
        break

    n = input(f"please state the name of user {id}: ")
    if n == "exit":
        break
    s = input(f"please state the surname of user {id}: ")
    if s == "exit":
        break
    a = input(f"please state the age of user {id}: ")
    if a == "exit":
        break

    data[id] = greet(n, s, a) #obiekt do klasy
    #do pustego slownika dodane id=1 stworzone zgodnie z klasa greet

    print(f"new user was added! id : {id}")
    id += 1

    go_view = input('''to continue please type \"go\", 
                    to view the user database please type \"view\": ''')
    if go_view == "view":
        break
    elif go_view == "go":
        continue
    else:
        print("invalid input, please try again")
        break

if not data:
    print("no user was added, please try again.")
else:
    try:
        num = int(input("please state desired id: "))
        result = get_id(data, num)
        if result:
            print(f"for id: {num}: {result}.")
        else:
            print("the id does not exist, please try again.")
    except ValueError:
        print("the id is not correct, please try again.")

