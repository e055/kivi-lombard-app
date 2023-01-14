* Aplikacja Lombard 1.0 ma służyć do maksymalnie uproszczonej obsługi lombardu.
    - zapisywanie klientów i ich zastawów wraz z dodawaniem kolejnych przedmiotów
    - operowanie na czasie w oparciu o czas komputera w kwestii rozpoczęcia zastawu jak i sprzedaży
    - automatyczny system naliczania prowizji od zastawu oraz proponowanej prowizji od sprzedaży zakupionych
        przedmiotów
    - zapis i archiwizowanie użytkowników zarówno sprzedających jak i zastawiających przedmioty
    - automatyczny system przenoszenia do histori (archiwum) rzeczy i użytkowników nie aktywnych
        czyli takich którzy wykupili zastaw, bądź sprzedali go i przedmiot dalej został sprzedany
    - aktualna cena złota według NBP oraz proponowana kwota skupu 

* Wersja Pythona użyta do budowy aplikacji to 3.10, odbyły się testy na drugim urządzeniu z pythonem 3.09

* W celu zainstalowania zależności wpisz w terminalu pip install i skopiuj listę z pliku requirments

* Aplikacja stworzona przez Macieja Tutaka, e055@wp.pl, za wszelkiego rodzaju feedback pozytywny, a 
        szczególnie negatywny bardzo z góry dziękuję.

* Aby uruchomić aplikację należy otworzyć baza_init.py a następnie uruchomić aplikację z pliku app.py

---------------
* W planach wersji 1.1
    - dodanie "skarbca", pełne zarządzenie przepływem pieniędzy startując od kwoty początkowej
      automatyczne dodawanie kwoty przy sprzedazy i odejmowanie przy zakupie przedmiotów
    - generowanie dokumentów zakupu do formatu pdf
    - system powiadamiania pracownika o przepadających zastawach z nadaniem nowego numeru ID
      po przejściu przedmiotu do bazy danych przedmiotów będących własnościa lombardu