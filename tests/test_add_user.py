from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
import random

def test_add_new_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)
    add_user = AddUserPage(page)

    login.goto()
    login.login("Admin", "admin123")

    admin.go_to_admin_module()
    admin.click_add_user()

    username = f"auto_user_{random.randint(1000,9999)}"
    add_user.add_user("Linda Anderson", username, "Test@123")

    # Verify success toast appeared
    assert page.is_visible("div.oxd-toast--success")
