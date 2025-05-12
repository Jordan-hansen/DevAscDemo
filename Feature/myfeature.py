def greet_user(name):
    """
    Function to greet the user with their name.
    :param name: str - The name of the user
    :return: str - Greeting message
    """
    return f"Hello, {name}! Welcome to the DevAscDemo feature."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
    print("Welcome to DevAscDemo")