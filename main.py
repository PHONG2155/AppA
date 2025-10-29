from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window

# KÍCH THƯỚC TEST TRÊN PC
Window.size = (400, 800)

# giả bộ database trong RAM
USERS = {}

class LoginScreen(Screen):
    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    message_label = ObjectProperty(None)

    def do_login(self):
        email = self.email_input.text.strip().lower()
        pw = self.password_input.text.strip()

        if email == "" or pw == "":
            self.message_label.text = "Vui lòng nhập đầy đủ."
            self.message_label.color = (1, 0.4, 0.4, 1)
            return

        if email in USERS and USERS[email]["password"] == pw:
            # login ok
            app = App.get_running_app()
            app.current_user = USERS[email]["name"]
            self.message_label.text = ""
            self.manager.current = "home"
        else:
            self.message_label.text = "Email hoặc mật khẩu sai."
            self.message_label.color = (1, 0.4, 0.4, 1)

    def goto_register(self):
        self.manager.current = "register"


class RegisterScreen(Screen):
    name_input = ObjectProperty(None)
    email_input = ObjectProperty(None)
    pw_input = ObjectProperty(None)
    pw2_input = ObjectProperty(None)
    message_label = ObjectProperty(None)

    def do_register(self):
        name = self.name_input.text.strip()
        email = self.email_input.text.strip().lower()
        pw1 = self.pw_input.text.strip()
        pw2 = self.pw2_input.text.strip()

        # validate
        if not name or not email or not pw1 or not pw2:
            self.message_label.text = "Điền đầy đủ thông tin."
            self.message_label.color = (1, 0.4, 0.4, 1)
            return

        if "@" not in email:
            self.message_label.text = "Email không hợp lệ."
            self.message_label.color = (1, 0.4, 0.4, 1)
            return

        if pw1 != pw2:
            self.message_label.text = "Mật khẩu không khớp."
            self.message_label.color = (1, 0.4, 0.4, 1)
            return

        if len(pw1) < 4:
            self.message_label.text = "Mật khẩu tối thiểu 4 ký tự."
            self.message_label.color = (1, 0.4, 0.4, 1)
            return

        # check tồn tại
        if email in USERS:
            self.message_label.text = "Email đã tồn tại."
            self.message_label.color = (1, 0.4, 0.4, 1)
            return

        # lưu "db"
        USERS[email] = {
            "name": name,
            "password": pw1
        }

        self.message_label.text = "Tạo tài khoản thành công! Đăng nhập nhé."
        self.message_label.color = (0.5, 1, 0.5, 1)

    def goto_login(self):
        self.manager.current = "login"


class HomeScreen(Screen):
    welcome_text = StringProperty("")

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        username = getattr(app, "current_user", "bạn")
        self.welcome_text = f"Chào {username} 👋"


class LoginApp(App):
    current_user = StringProperty("")

    def build(self):
        Builder.load_file("ui.kv")
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    LoginApp().run()
