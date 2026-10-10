from modules.github_init import github_init

def current_user_info():
    try:
        g = github_init()

        current_user = g.get_user()

        return current_user
    
    except Exception as e:
        print(f"Encountered some issue while finding info! Error : {e}")