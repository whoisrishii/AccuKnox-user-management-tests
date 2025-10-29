class AddUserPage:
    def __init__(self, page):
        self.page = page
        self.role_dropdown = "div.oxd-select-text:below(label:has-text('User Role'))"
        self.status_dropdown = "div.oxd-select-text:below(label:has-text('Status'))"
        self.employee_name = "input[placeholder='Type for hints...']"
        self.username_input = "input.oxd-input:below(label:has-text('Username'))"
        self.password_input = "input[type='password']:below(label:has-text('Password'))"
        self.confirm_password_input = "input[type='password']:below(label:has-text('Confirm Password'))"
        self.save_button = "button:has-text('Save')"
        self.success_popup = "div.oxd-toast--success"

    def add_user(self, emp_name, username, password):
        self.page.click(self.role_dropdown)
        self.page.get_by_text("Admin", exact=True).click()
        self.page.click(self.status_dropdown)
        self.page.get_by_text("Enabled", exact=True).click()
        self.page.fill(self.employee_name, emp_name)
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.fill(self.confirm_password_input, password)
        self.page.click(self.save_button)
        self.page.wait_for_selector(self.success_popup)
