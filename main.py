from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from network import NetworkManager

class MainDashboard(BoxLayout):
    def _init_(self, **kwargs):
        super(MainDashboard, self)._init_(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # Title / Status
        self.title_label = Label(text="[b]Advanced Control Panel[/b]", markup=True, font_size=24)
        self.status_label = Label(text="Status: Initializing...", font_size=18)
        
        self.add_widget(self.title_label)
        self.add_widget(self.status_label)

        # Action Buttons for Dashboard
        self.connect_btn = Button(text="Check Connection", size_hint=(1, 0.2))
        self.connect_btn.bind(on_press=self.update_status)
        self.add_widget(self.connect_btn)

        # Initialize Network Manager (Multiple network support)
        self.net_manager = NetworkManager(targets=["10.226.24.104", "127.0.0.1"], port=12345)
        self.net_manager.connect()

        # Schedule status updater loop
        Clock.schedule_interval(self.check_net_status, 2)

    def update_status(self, instance):
        if self.net_manager.is_connected:
            self.status_label.text = f"Status: Connected to {self.net_manager.active_host}"
        else:
            self.status_label.text = "Status: Connecting..."

    def check_net_status(self, dt):
        if self.net_manager.is_connected:
            self.status_label.text = f"Status: Online ({self.net_manager.active_host})"
        else:
            self.status_label.text = "Status: Disconnected / Reconnecting..."

class CyberApp(App):
    def build(self):
        return MainDashboard()

if __name__ == _mai_":
    CyberApp().run()
