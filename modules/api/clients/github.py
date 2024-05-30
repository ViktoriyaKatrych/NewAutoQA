import requests

class GitHub:
    
    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()
        return body
    
    def get_non_exists_user(self):
        r = requests.get('https://api.github.com/users/butenkosergiii')
        body = r.json()
        return body
    
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()
        return body   
    
    def search_repo(self, namerepo):
        r = requests.get("https://api.github.com/search/repositories",
                         params={"q": namerepo})
        body = r.json()
        return body 
    
   # def get_emo(self, nameemo):
       #emo= requests.get("https://api.github.com/emojis",
       #                   params ={"q": nameemo})
     #  r = requests.get(f'https://api.github.com/emojis/{nameemo}')
      # body = r.json()
       #return body
       
    def get_emo(self, nameicon):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()
        return body
    
    def get_commit(self, owner, repo, ref):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/{ref}')
        body = r.json()
        return body