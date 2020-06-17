# Aplikacja Ankiety
Aplikacja Ankiety służy do przeprowadzania anonomowych ankiet z zachowaniem możliwości sprawdzenia przez ankietowanego
czy jego odpowiedź w niezmienionej formie znajduje sie w bazie danych. Aplikacja posiada również funkcjonalność, pozwalającą
na sprawdzenie, czy dana osoba udzieliła już odpowiedzi na pytanie.

# Cechy programu
* zachowanie anonimowości głosujących
* możliwość zweryfikowania własnej odpowiedzi
* możliwośc sprawdzenia, czy dana osoba udzieliła już odpowiedzi

# Instalacja
Aplikacja działa na serwerze Django. Instrukcje, dotyczące instalacji Django
można znaleźć na stronie: https://docs.djangoproject.com/en/3.0/intro/

# Dokumantacja
Dokumentacja znajduje się w folderze 

*****
**Kod strony**
*****

Folder templates
########

*adminpanel.html* :
szablon strony z formularzem do weryfikowania udzielenia przez użytkownika odpowiedzi

*detail.html* :
szablon strony, wyświetlajacej pytanie

*index.html* :
szablon strony głównej

*results.html* :
szablon strony, na którą użytkownik jest przenoszony po udzieleniu odpowiedzi na pytanie

*useranswers.html* :
szablon strony, weryfikującej niezmienność rekordu w bazie

*whetheranswered.html* :
szablone strony, weryfikującej udzielenie przez użytkownika odpowiedzi


admin.py
########

Dodaje interfejs admina Django. Więcej informacji na stronie: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

*class QuestionAdmin(admin.ModelAdmin)* : klasa, służąca do dodawania nowych pytań

models.py
########

Plik, zawierający modele.

*class Question(models.Model)* :
model pytania

*class Choice(models.Model)* :
model odpowiedzi

*class Vote(models.Model), class Vote(models.Model)* :
modele, przechowujące udzielone odpowiedzi

*class User(models.Model), class User2(models.Model)* :
modele, przechowujące informacje o użytkownikach, którzy udzielili odpowiedzi na pytanie

urls.py
########
Definiuje ścieżki dla poszczególnych widoków.

views.py
########

*def useranswers(request)* :
służy do sprawdzenia, czy głos użytkownika w niezmianionej formie znajduje się w bazie

- id - wpisany przez użytkownika hash, który otrzymał po udzieleniu odpowiedzi

- hash - generuje hash z kolejnych rekordów w tabeli; następnie hash jest porównywany z tym, podanym przez użytkownika

*def whetheranswered(request)* :
służy do sprawdzania, czy dany użytkownik udzielił odpowiedzi na pytanie

- id2 - nazwa użytkownika

- qid - numer pytania

*def detail(request, question_id)* :
funkcja, wyświetlająca pytanie

*def vote(request, question_id)* :
służy do zapisywania głosu w bazie

- id_hash - hash, identyfikujący oddany przez użytkownika głos. Hash tworzony jest na podstawie id pytania, id odpowiedzi, tekstu odpowiedzi i czasu oddania głosu.

- rand = random.randint(0, 1) : losuje, do której tabeli zapisany zostanie głos


*****
**Pliki źródłowe**
*****

- Source Code: https://github.com/katarzyna864/ankieta
