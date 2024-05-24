class User:
    def __init__(self) -> None:
        self.name=None
        self.second_name=None

    def create(self):
        self.name='Sergiy'
        self.second_name='Butenko' 

    def remove(self):
        self.name=''
        self.seconf_name=''

def test_change_name():
    user=User()
    user.create() 
    assert user.name=='Sergiy'
    user.remove() 

def test_change_second_name():
    user =User()
    user.create()
    assert user.second_name=='Butenko'
    user.remove()             