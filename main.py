from kivy.app import App from kivy.uix.screenmanager import ScreenManager, Screen from kivy.uix.boxlayout import BoxLayout from kivy.uix.button import Button from kivy.uix.label import Label from kivy.uix.textinput import TextInput from kivy.uix.image import Image from kivy.animation import Animation from kivy.clock import Clock from kivy.core.window import Window import json import os

Устанавливаем черно-зеленую цветовую схему

Window.clearcolor = (0, 0, 0, 1)

Файл для сохранения данных

DATA_FILE = "gem_data.json"

Загрузка данных из файла

if os.path.exists(DATA_FILE): with open(DATA_FILE, "r") as file: user_data = json.load(file) else: user_data = {}

def save_data(): with open(DATA_FILE, "w") as file: json.dump(user_data, file)

class LoadingScreen(Screen): def init(self, **kwargs): super().init(**kwargs) layout = BoxLayout(orientation='vertical', padding=50, spacing=20) label = Label(text="Кликай\nи зарабатывай\nГемыГемы", font_size='30sp', color=(0, 1, 0, 1)) layout.add_widget(label) self.add_widget(layout) Clock.schedule_once(self.switch_to_main, 3)

def switch_to_main(self, dt):
    self.manager.current = "main"

class MainScreen(Screen): def init(self, **kwargs): super().init(**kwargs) self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

self.gem_label = Label(text='Ваши гемы: 0', font_size='30sp', color=(0, 1, 0, 1))
    self.layout.add_widget(self.gem_label)
    
    self.gem_button = Button(text='Фармить', size_hint=(1, 0.3), background_color=(0, 1, 0, 1), color=(0, 0, 0, 1))
    self.gem_button.bind(on_press=self.add_gem)
    self.layout.add_widget(self.gem_button)
    
    self.withdraw_button = Button(text='Вывести гемы', size_hint=(0.7, 0.2), pos_hint={'center_x': 0.5}, background_color=(0, 0.7, 0, 1), color=(0, 0, 0, 1))
    self.withdraw_button.bind(on_press=self.go_to_withdraw)
    self.layout.add_widget(self.withdraw_button)
    
    self.help_button = Button(text='Помощь', size_hint=(1, 0.15), background_color=(0, 0.5, 0, 1), color=(1, 1, 1, 1))
    self.help_button.bind(on_press=self.go_to_help)
    self.layout.add_widget(self.help_button)
    
    self.add_widget(self.layout)

def add_gem(self, instance):
    user_data['player'] = user_data.get('player', 0) + 1
    save_data()
    self.gem_label.text = f"Ваши гемы: {user_data['player']}"

def go_to_withdraw(self, instance):
    self.manager.current = "withdraw"

def go_to_help(self, instance):
    self.manager.current = "help"

class WithdrawScreen(Screen): def init(self, **kwargs): super().init(**kwargs) layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

self.input_id = TextInput(hint_text='Введите ваш Supercell ID', multiline=False, size_hint=(1, 0.2), background_color=(0, 0.5, 0, 1), foreground_color=(1, 1, 1, 1))
    layout.add_widget(self.input_id)
    
    self.withdraw_button = Button(text='Вывести', size_hint=(1, 0.2), background_color=(0, 1, 0, 1), color=(0, 0, 0, 1))
    layout.add_widget(self.withdraw_button)
    
    self.back_button = Button(text='Назад', size_hint=(1, 0.2), background_color=(0, 0.5, 0, 1), color=(1, 1, 1, 1))
    self.back_button.bind(on_press=self.go_back)
    layout.add_widget(self.back_button)
    
    self.add_widget(layout)

def go_back(self, instance):
    self.manager.current = "main"

class HelpScreen(Screen): def init(self, **kwargs): super().init(**kwargs) layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

label = Label(text='Для вывода гемов вы должны написать свой Supercell ID, что под ником в Brawl Stars', font_size='20sp', color=(0, 1, 0, 1))
    layout.add_widget(label)
    
    self.back_button = Button(text='Назад', size_hint=(1, 0.2), background_color=(0, 0.5, 0, 1), color=(1, 1, 1, 1))
    self.back_button.bind(on_press=self.go_back)
    layout.add_widget(self.back_button)
    
    self.add_widget(layout)

def go_back(self, instance):
    self.manager.current = "main"

class GemClickerApp(App): def build(self): sm = ScreenManager() sm.add_widget(LoadingScreen(name="loading")) sm.add_widget(MainScreen(name="main")) sm.add_widget(WithdrawScreen(name="withdraw")) sm.add_widget(HelpScreen(name="help")) return sm

if name == "main": GemClickerApp().run()

