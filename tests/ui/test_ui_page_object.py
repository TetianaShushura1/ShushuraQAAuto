from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    # create page object
    sign_in_page = SignInPage()

    # open page http://github.com/login
    sign_in_page.go_to()
    
    # try to enter to Gitub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # check that page name is one as expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # close browser
    sign_in_page.close()