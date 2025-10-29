class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_tab = "a[href='/web/index.php/admin/viewAdminModule']"
        self.add_button = "button:has-text('Add')"
        self.search_input = "input[placeholder='Type for hints...']"
        self.search_button = "button:has-text('Search')"
        self.delete_icon = "i.oxd-icon.bi-trash"
        self.confirm_delete = "button:has-text('Yes, Delete')"

    def go_to_admin_module(self):
        self.page.click(self.admin_tab)
        self.page.wait_for_url("**/admin/viewAdminModule")

    def click_add_user(self):
        self.page.click(self.add_button)

    def search_user(self, username):
        self.page.fill(self.search_input, username)
        self.page.click(self.search_button)
        self.page.wait_for_timeout(2000)

    def delete_user(self):
        self.page.click(self.delete_icon)
        self.page.click(self.confirm_delete)
