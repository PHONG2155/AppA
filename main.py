from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window

# Kích thước giả lập màn hình điện thoại khi chạy trên PC
Window.size = (400, 800)

# "CSDL" người dùng trong RAM (tạm thời)
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
        # dọn message cũ để form sạch
        self.message_label.text = ""
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
            self._set_msg("Điền đầy đủ thông tin.", error=True)
            return

        if "@" not in email:
            self._set_msg("Email không hợp lệ.", error=True)
            return

        if pw1 != pw2:
            self._set_msg("Mật khẩu không khớp.", error=True)
            return

        if len(pw1) < 4:
            self._set_msg("Mật khẩu tối thiểu 4 ký tự.", error=True)
            return

        if email in USERS:
            self._set_msg("Email đã tồn tại.", error=True)
            return

        # lưu user
        USERS[email] = {
            "name": name,
            "password": pw1
        }

        # lấy screen login để prefill email và báo thành công
        sm = self.manager
        login_screen = sm.get_screen("login")
        login_screen.email_input.text = email
        login_screen.message_label.text = "Tạo tài khoản thành công. Đăng nhập nhé."
        login_screen.message_label.color = (0.5, 1, 0.5, 1)

        # clear form đăng ký cho sạch
        self.name_input.text = ""
        self.email_input.text = ""
        self.pw_input.text = ""
        self.pw2_input.text = ""
        self._set_msg("")

        # chuyển về màn hình login
        sm.current = "login"

    def _set_msg(self, text, error=False):
        self.message_label.text = text
        if error:
            self.message_label.color = (1, 0.4, 0.4, 1)
        else:
            self.message_label.color = (0.5, 1, 0.5, 1)

    def goto_login(self):
        # user bấm link quay lại đăng nhập
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
        # load layout Kivy
        Builder.load_file("ui.kv")

        # tạo screen manager và add các màn
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(HomeScreen(name="home"))
        return sm


if __name__ == "__main__":
    LoginApp().run()
