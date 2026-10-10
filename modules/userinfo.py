from modules.github_init import github_init

def get_user_info(username):
    try:
        g = github_init()
        user = g.get_user(username)

        return user

    except Exception as e:
        print(f"Encountered Some issue while finding user info!: {e}")

    