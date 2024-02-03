import pytest 

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'
    

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'
    

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']
  
   
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('tetiana_repo_non_exist')
    assert r['total_count'] == 0
    

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('a')
    assert r['total_count'] != 0

@pytest.mark.api
def test_search_emojis_existence(github_api):
    r = github_api.search_emojis('')
    assert len(r) > 0

@pytest.mark.api
def test_search_emojis_with_name(github_api):
    emoji_name = '100'
    r = github_api.search_emojis(emoji_name)
    assert emoji_name in r
    assert r[emoji_name] is not None

@pytest.mark.api
def test_commits_existence(github_api, owner, repo):
    r = github_api.commits(owner, repo)
    assert len(r) > 0

@pytest.mark.api
def test_commits_author(github_api, owner, repo):
    r = github_api.commits(owner, repo)
    if len(r) > 0:
        first_commit_author = r[0]['commit']['author']['name']
        assert first_commit_author is not None

@pytest.mark.api
def test_commits_invalid_repo(github_api, owner, invalid_repo):
    r = github_api.commits(owner, invalid_repo)
    assert r['message'] == 'Not Found'


