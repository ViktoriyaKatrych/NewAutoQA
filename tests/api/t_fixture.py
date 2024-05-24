class User:
    def __init__(self)->None:
        self.name = 'Sergiy'
        self.second_namclasse ='Butenko'
user=User()

def test_remove_name():
    user.name=''
    assert user.name==''

def test_name():
    assert user.name=='Sergiy'

def test_second_name():
    assert user.second_name=='Butenko'    