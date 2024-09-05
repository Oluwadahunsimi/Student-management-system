from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
import subprocess

# Dictionary of user credentials
users = {
    "Joseph": "1234",
    "oluwapemi": "12345",
    "Glory": "123",
    "Ife": "12345"
}

class LoginScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Background Image
        self.background_image = Image(source='login_.png', allow_stretch=True, keep_ratio=False, size_hint=(0.4, 0.8), pos_hint={'x': 0.05, 'y': 0.1})
        self.add_widget(self.background_image)

        # Frame for login elements
        self.login_frame = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.4, 0.6), pos_hint={'center_x': 0.7, 'center_y': 0.5})
        self.add_widget(self.login_frame)

        # Heading
        self.heading = Label(text="Sign In", font_size=23, color="#57a1f8", bold=True, size_hint=(1, 0.2))
        self.login_frame.add_widget(self.heading)

        # Username Input
        self.user = TextInput(hint_text="Username", size_hint=(1, 0.2), multiline=False)
        self.user.bind(focus=self.on_focus)
        self.login_frame.add_widget(self.user)

        # Password Input
        self.code = TextInput(hint_text="Password", size_hint=(1, 0.2), multiline=False, password=True)
        self.code.bind(focus=self.on_focus)
        self.login_frame.add_widget(self.code)

        # Show Password Checkbox
        self.show_password_checkbox = CheckBox(size_hint=(0.1, 0.1))
        self.show_password_checkbox.bind(active=self.toggle_password_visibility)
        self.login_frame.add_widget(BoxLayout(size_hint=(1, 0.1)))
        self.login_frame.add_widget(self.show_password_checkbox)
        self.login_frame.add_widget(Label(text="Show Password", size_hint=(1, 0.1), pos_hint={'x': 0.8}))

        # Sign In Button
        self.signin_button = Button(text="Sign In", size_hint=(1, 0.2), background_color=[0.34, 0.63, 0.97, 1])
        self.signin_button.bind(on_release=self.signin)
        self.login_frame.add_widget(self.signin_button)

        # Info Label
        self.info_label = Label(text="Contact other admins for more information.", size_hint=(1, 0.2))
        self.login_frame.add_widget(self.info_label)

    def on_focus(self, instance, value):
        if value:
            instance.hint_text = ''
        elif not instance.text:
            if instance == self.user:
                instance.hint_text = 'Username'
            elif instance == self.code:
                instance.hint_text = 'Password'

    def toggle_password_visibility(self, checkbox, value):
        if value:
            self.code.password = False
        else:
            self.code.password = True

    def signin(self, instance):
        entered_username = self.user.text
        entered_password = self.code.text

        if entered_username in users and users[entered_username] == entered_password:
            content = Label(text='Login Successful!')
            popup = Popup(title='Success', content=content, size_hint=(None, None), size=(400, 400))
            popup.open()
            App.get_running_app().stop()  # Close the login window
            subprocess.run(["python", "project1.py"])
        else:
            content = Label(text='Invalid username or password')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 400))
            popup.open()

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
