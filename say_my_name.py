def say_my_name(name=None):
    if name != "":
        print(name + "??? You are right !!!")
    else:
        print("Heisenberg??? You are right !!!")


if __name__ == "__main__":
    say_my_name(input("Now.. Say My Name? "))