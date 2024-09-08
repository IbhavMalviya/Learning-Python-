def make_shirt(size=45, message="I love Python"):
    size=input("Enter the size of the shirt: ")
    int(size)
    message=input("Enter the message to be printed on the shirt: ")
    print(f"The size if the tshirt is {size} and the message to be printed is {message}")

make_shirt()

def make_shirt(size="large", message="I love Python"):
    print(f"The size if the tshirt is {size} and the message to be printed is {message}")
make_shirt()