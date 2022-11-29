import kivy
from kivy.uix.togglebutton import ToggleButton
from kivy import Config
from kivy.uix.image import Image
from kivy.uix.popup import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import warnings
import string
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import StringProperty, Clock
from kivy.core.window import Window
from body import *

Window.clearcolor = (1, 1, 1, 1)

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '700')
Config.write()
read()
check_items()

Builder.load_string('''
<ScrolllabelLabel>:
    Label:
        text: root.text
        font_size: 20
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
        color: [1,1,1,1]
''')


class ScrolllabelLabel(ScrollView):
    text = StringProperty('')

class SayHello(App):
    k = []

    def ok(self):
        box_ok = BoxLayout(orientation="vertical")

        self.popup_ok = Popup(title='Zapisano z sukcesem !', auto_dismiss=True,
                                       content=box_ok,
                                       size_hint=(None, None),
                                       size=(350, 350),
                                       pos_hint={"center_x": 0.5, "center_y": 0.5},
                                       )

        box_ok.add_widget(Image(source='ok.jpg'))
        self.popup_ok.open()
        Clock.schedule_once(self.popup_ok.dismiss, 2)

    def not_ok(self):
        box_ok = BoxLayout(orientation="vertical")

        self.popup_ok = Popup(title='Błędnie wprowadzone dane !', auto_dismiss=True,
                              content=box_ok,
                              size_hint=(None, None),
                              size=(350, 350),
                              pos_hint={"center_x": 0.5, "center_y": 0.5},
                              )

        box_ok.add_widget(Image(source='zakaz.jpeg'))
        self.popup_ok.open()
        Clock.schedule_once(self.popup_ok.dismiss, 3)

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.9, 1.0)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.add_widget(Image(source='logo.png'))

        self.grid = GridLayout(cols=2, size_hint_x=None, width="800dp")
        self.grid.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.grid.size_hint = (1.2, 1.2)
        self.window.add_widget(self.grid)

        btn1 = Button(text='Zastawianie przedmiotu')  # create a button instance
        btn1.bind(on_press=self.dodaj_osobe)  # binding the button with the function below
        self.grid.add_widget(btn1)
        btn2 = Button(text='Zakup przedmiotu')  # create a button instance
        btn2.bind(on_press=self.buy_item)  # binding the button with the function below
        self.grid.add_widget(btn2)
        btn3 = Button(text='Lista klientów')  # create a button instance
        btn3.bind(on_press=self.lista_klientow)  # binding the button with the function below
        self.grid.add_widget(btn3)
        btn4 = Button(text='Lista przedmiotów')  # create a button instance
        btn4.bind(on_press=self.lombard_items)  # binding the button with the function below
        self.grid.add_widget(btn4)
        btn5 = Button(text='Wyszukaj / Wpłata')  # create a button instance
        btn5.bind(on_press=self.payment)  # binding the button with the function below
        self.grid.add_widget(btn5)
        btn6 = Button(text='Pomoc/Kontakt')  # create a button instance
        btn6.bind(on_press=self.contact_help)  # binding the button with the function below
        self.grid.add_widget(btn6)

        return self.window

    def dodaj_osobe(self, instance):
        self.dni = 0
        box_dodaj_osobe = BoxLayout(orientation="vertical")

        self.popup_dodaj_osobe = Popup(title='Dodawanie osoby :', auto_dismiss=True,
                                       content=box_dodaj_osobe,
                                       size_hint=(None, None),
                                       size=(750, 500),
                                       pos_hint={"center_x": 0.5, "center_y": 0.32},
                                       )

        grid_osoba = GridLayout(cols=2, size_hint_y=.3)
        self.imie = TextInput(text='', hint_text='Podaj imię', multiline=False, size_hint_x=.2, font_size=20,
                              size_hint_y=None, height=40)
        grid_osoba.add_widget(self.imie)
        self.nazwisko = TextInput(text='', hint_text='Podaj nazwisko', multiline=False, size_hint_x=.2, font_size=20,
                                  size_hint_y=None, height=40)
        grid_osoba.add_widget(self.nazwisko)
        box_dodaj_osobe.add_widget(grid_osoba)
        self.adres = TextInput(text='', hint_text='Podaj adres', multiline=True, size_hint_x=1.0, font_size=20,
                               size_hint_y=None, height=40)
        box_dodaj_osobe.add_widget(self.adres)

        grid_pes_tel = GridLayout(cols=2, size_hint_y=.3)
        self.pesel = TextInput(text='', hint_text='Podaj pesel', multiline=False, font_size=20, size_hint_y=None,
                               height=40)
        grid_pes_tel.add_widget(self.pesel)
        self.tel = TextInput(text='', hint_text='Podaj nr telefonu', multiline=False, font_size=20, size_hint_y=None,
                             height=40)
        grid_pes_tel.add_widget(self.tel)
        box_dodaj_osobe.add_widget(grid_pes_tel)
        pop_label = Label(text='Wprowadź przedmiot i wybierz długość pożyczki:', size_hint_y=0.4)
        box_dodaj_osobe.add_widget(pop_label)

        grid_rzecz = GridLayout(cols=2, size_hint_y=.3)
        self.nazwa_rzeczy = TextInput(text='', hint_text='Nazwa przedmiotu', multiline=False, font_size=20,
                                      size_hint_y=None, height=40)
        grid_rzecz.add_widget(self.nazwa_rzeczy)
        self.wartosc = TextInput(text='', hint_text='Wartość PLN', multiline=False, font_size=20, size_hint_y=None,
                                 height=40)
        grid_rzecz.add_widget(self.wartosc)
        box_dodaj_osobe.add_widget(grid_rzecz)

        grid_buttons = GridLayout(cols=3, row_force_default=True, row_default_height=40, size_hint_y=.3)
        btn_choose7 = ToggleButton(text='7 dni', group='Dni', )
        btn_choose7.bind(on_release=self.set_togle_buttton7)
        grid_buttons.add_widget(btn_choose7)
        btn_choose14 = ToggleButton(text='14 dni', group='Dni', )
        btn_choose14.bind(on_release=self.set_togle_buttton14)
        grid_buttons.add_widget(btn_choose14)
        btn_choose31 = ToggleButton(text='31 dni', group='Dni', )
        btn_choose31.bind(on_release=self.set_togle_buttton31)
        grid_buttons.add_widget(btn_choose31)

        grid_buttons_save = GridLayout(cols=1, row_force_default=True, row_default_height=40, size_hint_y=.3)
        btn1 = Button(text='Zapisz', size_hint_x=0.2, width=80)  # create a button instance
        btn1.bind(on_press=self.dodaj_osobe_f)  # binding the button with the function below
        grid_buttons_save.add_widget(btn1)

        box_dodaj_osobe.add_widget(grid_buttons)
        box_dodaj_osobe.add_widget(grid_buttons_save)
        box_dodaj_osobe.add_widget(Image(source='dolar.jpeg'))

        self.popup_dodaj_osobe.open()

    def set_togle_buttton7(self, instance):
        self.dni = 7

    def set_togle_buttton14(self, instance):
        self.dni = 14

    def set_togle_buttton31(self, instance):
        self.dni = 31


    def dodaj_osobe_f(self, instance):
        try:
            n = self.imie.text
            s = self.nazwisko.text
            a = self.adres.text
            i = self.pesel.text
            t = self.tel.text
            item_nam = self.nazwa_rzeczy.text
            val_i = self.wartosc.text
            val_i = int(val_i)
            dni = self.dni
            ad_person(n, s, a, i, t, item_nam, val_i, dni)
            write_json()
            self.ok()
            Clock.schedule_once(self.popup_dodaj_osobe.dismiss, 1)
        except:
            self.not_ok()

    def lombard_items(self,instance):
        box = BoxLayout(orientation="vertical")

        self.popup_items = Popup(title='Lista przedmiotów :', auto_dismiss=True,
                                     content=box,
                                     size_hint=(None, None),
                                     size=(500, 650),
                                     )
        t = print_lombard_items()
        self.pop_display_lomb_item = ScrolllabelLabel(text=f'{t}')
        box.add_widget(self.pop_display_lomb_item)
        self.pop_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False, size_hint=(.8, .1), pos_hint={'top': .40}, )

        box.add_widget(self.pop_scroll)

        self.grid_one_item = GridLayout(cols=2, size_hint_y=.1)
        self.item_id_in = TextInput(text='', hint_text='ID przedmiotu', multiline=False, size_hint_x=0.1, font_size=20,
                                         size_hint_y=None, height=40, width=40)
        self.grid_one_item.add_widget(self.item_id_in)

        self.btn_search_item = Button(text='Szukaj', size_hint_x=0.2, width=60, size_hint_y=None,
                              height=40)  # create a button instance
        self.btn_search_item.bind(on_press=self.one_item_search)  # binding the button with the function below
        self.grid_one_item.add_widget(self.btn_search_item)
        box.add_widget(self.grid_one_item)

        self.popup_items.open()

    def one_item_search(self, instance):
        try:
            a = self.item_id_in.text
            a = int(a)
            b = search_one_item(a)
            t = f"\n ID: {b[0]['item_id']}\nNazwa: {b[0]['item']}\nKwota pozyskania: {b[0]['item_price']} PLN\n" \
                f"Własnościa lomabrdu od: {b[0]['take_date']}\n\n" \
                f"Pozyskano od:\n\n{b[0]['name']} {b[0]['surname']}\n" \
                f"adres: {b[0]['adress']}\n" \
                f"tel: {b[0]['tel']}, pesel: {b[0]['id']}"
            self.one_item_id = b[0]['item_id']
            self.btn_sold = Button(text='Sprzedaj', size_hint_x=0.2, width=60, size_hint_y=None,
                                          height=40)  # create a button instance
            self.btn_sold.bind(on_press=self.item_sold)

            self.pop_display_lomb_item.text = t
            self.item_id_in.text =""
            self.item_id_in.hint_text = "Kwota"
            self.grid_one_item.remove_widget(self.btn_search_item)
            self.grid_one_item.add_widget(self.btn_sold)
        except:
            self.not_ok()

    def item_sold(self, instance):
        try:
            b = self.one_item_id
            val = self.item_id_in.text
            val = int(val)
            sold_item(b, val)
            self.ok()
        except:
            self.not_ok()

    def lista_klientow(self, instance):
        box = BoxLayout(orientation="vertical")

        self.popup_searching = Popup(title='Lista klientów :', auto_dismiss=True,
                                     content=box,
                                     size_hint=(None, None),
                                     size=(500, 650),
                                     )
        ik = people_counter()
        kz = people_cash_counter()
        t = print_people()
        self.pop_display = ScrolllabelLabel(
            text=f'Ilość klientów: {ik} \nŁączna kwota zadłużenia: {kz} PLN\n {t}')  # create a label instance
        box.add_widget(self.pop_display)
        self.pop_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False, size_hint=(.8, .1), pos_hint={'top': .40}, )

        box.add_widget(self.pop_scroll)

        self.popup_searching.open()

    def buy_item(self, instance):
        box_dodaj_osobe = BoxLayout(orientation="vertical")

        self.popup_buy_item = Popup(title='Dodawanie osoby :', auto_dismiss=True,
                                       content=box_dodaj_osobe,
                                       size_hint=(None, None),
                                       size=(750, 500),
                                       pos_hint={"center_x": 0.5, "center_y": 0.32},
                                       )

        grid_osoba_item = GridLayout(cols=2, size_hint_y=.3)
        self.imie_item = TextInput(text='', hint_text='Podaj imię', multiline=False, size_hint_x=.2, font_size=20,
                              size_hint_y=None, height=40)
        grid_osoba_item.add_widget(self.imie_item)
        self.nazwisko_item = TextInput(text='', hint_text='Podaj nazwisko', multiline=False, size_hint_x=.2, font_size=20,
                                  size_hint_y=None, height=40)
        grid_osoba_item.add_widget(self.nazwisko_item)
        box_dodaj_osobe.add_widget(grid_osoba_item)
        self.adres_item = TextInput(text='', hint_text='Podaj adres', multiline=True, size_hint_x=1.0, font_size=20,
                               size_hint_y=None, height=40)
        box_dodaj_osobe.add_widget(self.adres_item)

        grid_pes_tel = GridLayout(cols=2, size_hint_y=.3)
        self.pesel_item = TextInput(text='', hint_text='Podaj pesel', multiline=False, font_size=20, size_hint_y=None,
                               height=40)
        grid_pes_tel.add_widget(self.pesel_item)
        self.tel_item = TextInput(text='', hint_text='Podaj nr telefonu', multiline=False, font_size=20, size_hint_y=None,
                             height=40)
        grid_pes_tel.add_widget(self.tel_item)
        box_dodaj_osobe.add_widget(grid_pes_tel)
        pop_label = Label(text='Wprowadź przedmiot i wybierz długość pożyczki:', size_hint_y=0.4)
        box_dodaj_osobe.add_widget(pop_label)

        grid_rzecz = GridLayout(cols=2, size_hint_y=.3)
        self.nazwa_rzeczy_item = TextInput(text='', hint_text='Nazwa przedmiotu', multiline=False, font_size=20,
                                      size_hint_y=None, height=40)
        grid_rzecz.add_widget(self.nazwa_rzeczy_item)
        self.wartosc_item = TextInput(text='', hint_text='Wartość PLN', multiline=False, font_size=20, size_hint_y=None,
                                 height=40)
        grid_rzecz.add_widget(self.wartosc_item)
        box_dodaj_osobe.add_widget(grid_rzecz)

        grid_buttons_save = GridLayout(cols=1, row_force_default=True, row_default_height=40, size_hint_y=.3)
        btn1 = Button(text='Kup przedmiot', size_hint_x=0.2, width=80)  # create a button instance
        btn1.bind(on_press=self.buy_item_btn)  # binding the button with the function below
        grid_buttons_save.add_widget(btn1)

        box_dodaj_osobe.add_widget(grid_buttons_save)
        box_dodaj_osobe.add_widget(Image(source='dolar.jpeg'))

        self.popup_buy_item.open()

    def buy_item_btn(self, instance):
        n = self.imie_item.text
        s = self.nazwisko_item.text
        a = self.adres_item.text
        i = self.pesel_item.text
        t = self.tel_item.text
        item_nam = self.nazwa_rzeczy_item.text
        val_i = self.wartosc_item.text
        val_i = int(val_i)
        create_item_buy(n, s, a, i, t, item_nam, val_i)
        write_json()
        self.ok()
        Clock.schedule_once(self.popup_buy_item.dismiss, 1)



    def payment(self, instance):
        box = BoxLayout(orientation="vertical")

        self.popup_pay_searching = Popup(title='Spłata zadłużenia :', auto_dismiss=True,
                                         content=box,
                                         size_hint=(None, None),
                                         size=(500, 550),
                                         )

        grid_pay_search = GridLayout(cols=2, size_hint_y=.1)
        self.osoba_pay = TextInput(text='', hint_text='Wprowadź Pesel', multiline=False, font_size=20,
                                   size_hint_y=None, height=40)
        grid_pay_search.add_widget(self.osoba_pay)
        btn_search = Button(text='Wyszukaj', size_hint_x=0.2, width=10, size_hint_y=None,
                            height=40)  # create a button instance
        btn_search.bind(on_press=self.searching_pay_btn)  # binding the button with the function below
        grid_pay_search.add_widget(btn_search)
        box.add_widget(grid_pay_search)

        self.pop_pay_display_searching = ScrolllabelLabel(text='')  # create a label instance
        box.add_widget(self.pop_pay_display_searching)
        self.pop_pay_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False, size_hint=(.8, .1),
                                         pos_hint={'top': .40}, )
        box.add_widget(self.pop_pay_scroll)

        grid_payment = GridLayout(cols=3, size_hint_y=.1)
        self.osoba_paymentID = TextInput(text='', hint_text='ID', multiline=False, size_hint_x=0.1, font_size=20,
                                         size_hint_y=None, height=40, width=40)
        grid_payment.add_widget(self.osoba_paymentID)
        self.osoba_payment_kwota = TextInput(text='', hint_text='Kwota', multiline=False, size_hint_x=0.3, font_size=20,
                                             size_hint_y=None, height=40)
        grid_payment.add_widget(self.osoba_payment_kwota)
        btn_search_p = Button(text='Wpłata', size_hint_x=0.2, width=60, size_hint_y=None,
                              height=40)  # create a button instance
        btn_search_p.bind(on_press=self.cash_pay)  # binding the button with the function below
        grid_payment.add_widget(btn_search_p)
        box.add_widget(grid_payment)

        self.popup_pay_searching.open()

    def searching_pay_btn(self, instance):
        try:
            p = int(self.osoba_pay.text)
            self.t_pay = search(p)
            if self.t_pay == 0:
                self.pop_pay_display_searching.text = "Brak osoby w bazie danych lub \n źle wprowadzony pesel"
            else:
                l = ""
                for i in self.t_pay[0]['items']:
                    l += f'\nID: {i["item_id"]} {i["item_name"]}\nKwota: {i["val"]} PLN \nData wygaśnięcia: {i["data"]} \n'

                self.pop_pay_display_searching.text = f'{self.t_pay[0]["name"]} {self.t_pay[0]["surname"]} \n' \
                                                      f'\nPrzedmioty:\n{l} \nŁączna kwota: {self.t_pay[0]["sum"]} PLN'
        except:
            self.pop_pay_display_searching.text = f'Wprowadź prawidłowe dane\n'

    def cash_pay(self, instance):
        try:
            t = self.t_pay
            id_p = self.osoba_paymentID.text
            kwota = self.osoba_payment_kwota.text

            c = payment(t, id_p, kwota)
            self.pop_pay_display_searching.text = f'{c}'
            write_json()
        except:
            self.pop_pay_display_searching.text = f'Wprowadź prawidłowe dane\n'


    def contact_help(self,instance):
        box = BoxLayout(orientation="vertical")

        self.popup_contact = Popup(title='Kontakt / Pomoc :', auto_dismiss=True,
                                     content=box,
                                     size_hint=(None, None),
                                     size=(500, 650),
                                     )

        self.pop_display_contact = ScrolllabelLabel(
            text=f'Pytania, sugestie, problemy prosimy zgłaszać e-mailowo lub telefonicznie:'
                 f'\ntel: 884 811 288\ne-mail: e055@wp.pl'
                 f'\n\nZapraszamy !!!')
        box.add_widget(self.pop_display_contact)
        self.pop_scroll_contact = ScrollView(do_scroll_y=True, do_scroll_x=False, size_hint=(.8, .1), pos_hint={'top': .40}, )

        box.add_widget(self.pop_scroll_contact)

        self.popup_contact.open()


if __name__ == "__main__":
    SayHello().run()
