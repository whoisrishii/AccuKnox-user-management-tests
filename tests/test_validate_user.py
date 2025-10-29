from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_validate_user(page):
    login = LoginPage(page)
    login.login("Admin", "admin123")
    admin = AdminPage(page)
    admin.go_to_admin_module()
    admin.search_user("AdminUpdated")
    assert page.locator("text=AdminUpdated").is_visible()
