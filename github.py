import os
import requests
import json


class GitHub():
    def __init__(self):
        self.username = None
        self.token = None
        
        creds = self.check_creds()
        if not creds:
            self.auth()
        
        self.username = creds.get("username")
        self.token = creds.get("token")            
        self.headers = {
            "Accept":"application/vnd.github+json",
            "Authorization": f"token {self.token}",
            "X-GitHub-Api-Version": "2022-11-28" 
        }

    def create_repo(self):
        
        URL =   'https://api.github.com/user/repos'
        name_repo = input("Введите название репозитория на английском: ")
        description = input("Введите описание репозитория: ")
        is_privat = None
      
        while is_privat not in ['y', 'n']:
            is_privat = input("Сделать репозиторий приватным? (y/n):  ")
            
        if is_privat == 'y':
            is_privat = True
            
        elif is_privat == 'n':
            is_privat = False

        data = {
            'name': name_repo,
            'description': description,
            'private': is_privat  # Set to True for a private repository
        }

        try:
            response = requests.post(URL, headers=self.headers, data = json.dumps(data))
            
            if response.status_code in [200, 201]:
                print("repo ", f"https://github.com/{self.username}/{name_repo}.git")
            else:
                print()
                print(response.json()['message'])
        except Exception as e:
            print(e)
    
    def delete_repo(self):
        name_repo = input("Введите название репозитория: ")
        realy_delete = input("Подтвердить удаление?(y/n): ")
        while realy_delete not in ['y', 'n']:
            realy_delete = input("Подтвердить удаление?(y/n): ")
        if realy_delete == 'n':
            return 
        
        
        URL =   f'https://api.github.com/repos/{self.username}/{name_repo}'
        print(URL)
        try:
            response = requests.delete(URL, headers=self.headers,)
            # print(response.content)
            if response.status_code in [204]:
                print("repo ", f"https://github.com/{self.username}/{name_repo}", ' was deleted!')
            else:
                print()
                print(response.json()['message'])
        except Exception as e:
            print(e)
    
    
    def check_creds(self):
        if not os.path.exists("cred.json"):
            return False
        
        with open("cred.json", 'rb') as file:
            cred = json.load(file)
            return cred
           
    
    def auth(self):
        username = input('Введите username от github: ')
        token = input("Введите токен от github аккаунта: ")


        save = input("Сохранить данные для входа? (y/n): ")
        while save not in ['y', 'n']:
            save = input("ERROR: Сохранить данные для входа? (y/n)")

        if save == 'y':
            self.saving_creds(username, token)
        else:
            self.username = username
            self.token = token

    def saving_creds(self, username, token):
        auth = {
            "username":username, 
            "token": token
        }
    
        with open("cred.json", 'w') as file:
            json.dump(auth, file)
