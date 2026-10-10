from modules.userinfo import get_user_info
from modules.current_user_info import current_user_info

def welcome():
    print("===== Github Analyzer =====\n\n")
    print("Choose one of the following options:\n")
    print("1. Find a user's Github info by username")
    print("2. Get your Github's info")
    print("3. Exit Program\n")


def main(user_input:int):
    try:

        if user_input == 1:
            username = input("Enter username to search for: ")
            data = get_user_info(username)

            print("\n===== User Profile =====\n")
            print(f"-Name: {data.name}")
            print(f"-Profile URL: {data.html_url}")
            print(f"-Avatar: {data.avatar_url}")
            print(f"-Email: {data.email}")
            print(f"-Created On: {data.created_at}")
            print(f"-Bio: {data.bio}")
            print(f"-Followers: {data.followers}")
            print(f"-Following: {data.following}")
            print(f"-Public Repos: {data.public_repos}\n")

        elif user_input == 2:
            user_info = current_user_info()
            print("\n===== Your Profile =====\n")
            print(f"-Username: {user_info.login}")
            print(f"-Name: {user_info.name}")
            print(f"-Profile URL: {user_info.html_url}")
            print(f"-Avatar: {user_info.avatar_url}")
            print(f"-Email: {user_info.email}")
            print(f"-Created On: {user_info.created_at}")
            print(f"-Bio: {user_info.bio}")
            print(f"-Followers: {user_info.followers}")
            print(f"-Following: {user_info.following}")
            print(f"-Public Repos: {user_info.public_repos}\n")

    except Exception as e:
        pass

if __name__ == "__main__":
    while True:
        welcome()
        user_input = int(input("Enter your preference number: "))
        if user_input == 3:
            print("Exiting program")
            break
        else:
            main(user_input)
        