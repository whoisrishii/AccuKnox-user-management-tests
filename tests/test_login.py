from pages.login_page import LoginPage

def test_login_valid(page):
    """Verify login works correctly with valid credentials"""
    login = LoginPage(page)
    login.goto()
    login.login("Admin", "admin123")
    assert "dashboard" in page.url or "Dashboard" in page.content()
