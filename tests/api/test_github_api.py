#import sys
#sys.path.append("c:\\Users\\Viktoriya\\NewAutoQA\\")

import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user =api.get_user_defunkt()
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_non_user_exists():
    api = GitHub()
    nuser =api.get_non_exists_user()
    print(nuser) 
    assert nuser['message'] == 'Not Found'  

@pytest.mark.api
def test_user_exists1(github_api):
    user =github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_non_user_exists1(github_api):
    nuser =github_api.get_user('butenkosergiii')
    print(nuser) 
    assert nuser['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    #print(r)
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiybutenko_repo_non_exist')
    print(r)
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    k = r['total_count']
    print("Total Count: {}".format(k))
    assert r['total_count'] != 0

#@pytest.mark.apiemo
#def test_emo():
 #   api = GitHub()
  #  icon = api.get_emo()
   # print([icon])
    

@pytest.mark.apiemo
def test_emo_exist(github_api):
    icon = github_api.get_emo('white_circle')
      
    assert 'white_circle' in icon
    #assert icon['white_circle'] == 'white_circle'
  
    print(f'Icon "white_circle" is on {icon['white_circle']}')
  
@pytest.mark.apiemo
def test_emo_no_exist(github_api):
    icon = github_api.get_emo('white_circlehhh')
      
    assert ('white_circlehhh'not in icon) == True
        
    print('No icon "white_circlehhh"') 

@pytest.mark.apicommit
def test_commit_realdata(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych', 'NewAutoQA', 'main')
  
    d =comm['commit']['author']
    print(d)
    assert d['name'] == 'Viktoriya Katrych'
    assert d['email'] == 'vkatrych@gmail.com'

    f = comm['commit']['message']
    print(f)
    print(comm['commit']['url'])


@pytest.mark.apicommit
def test_commit_otherREPO(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych', 'WorkAutoQA', 'main')
  
    d =comm['commit']['author']
    print(d)
    assert d['name'] == 'Viktoriya Katrych'
    assert d['email'] == 'vkatrych@gmail.com'
    
    f = comm['commit']['message']
    print(f)
    print(comm['commit']['url'])


@pytest.mark.apicommit
def test_commit_noexists_owner(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych111', 'WorkAutoQA', 'main')
    print(comm)
   
    assert comm['message'] == 'Not Found'
    print('No Owner') 

@pytest.mark.apicommit
def test_commit_noexists_REPO(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych', 'wwqeWorkAutoQA', 'main')
    print(comm)

    assert comm['message'] == 'Not Found'
    print('No REPO') 
   
  
@pytest.mark.apicommit
def test_commit_noexists_REF(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych111', 'WorkAutoQA', 'wwmain')
    print(comm)

    assert comm['message'] == 'Not Found'
    print('No REF') 
   
 