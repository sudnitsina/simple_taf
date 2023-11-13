def test_login(ui):
    username = "tester"
    password = "password"
    ui.login_page.login(username, password)
    assert username in ui.admin_page.header.text
