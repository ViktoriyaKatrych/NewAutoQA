import pytest

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

@pytest.fixture       
def user():
    user=User()
    user.create()
    yield user
    user.remove() 