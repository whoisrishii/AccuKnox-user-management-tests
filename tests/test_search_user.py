from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_search_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.goto()
    login.login("Admin", "admin123")
    admin.go_to_admin_module()
    admin.search_user("Admin")

    assert "Admin" in page.content()
