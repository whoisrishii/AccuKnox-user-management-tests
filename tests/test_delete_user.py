from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_delete_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.goto()
    login.login("Admin", "admin123")

    admin.go_to_admin_module()
    admin.search_user("auto_user_")  # Replace with actual username added
    admin.delete_user()
