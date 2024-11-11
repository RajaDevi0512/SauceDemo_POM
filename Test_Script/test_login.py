from PageObject.Login import Saucedemo_login

def test_start():
    assert Saucedemo_login().start() == True
    print("SUCCESS: Automation started!!")

def test_login():
    assert Saucedemo_login().saucedemo_login() == True
    print("SUCCESS: Logged In")

def test_shutdown():
    assert Saucedemo_login().shutdown() == True
    print('SUCCESS: Automation completed!!')