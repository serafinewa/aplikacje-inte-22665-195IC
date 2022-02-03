# Aplikacje internetowe 22665 195ICA

<p><a href="#Laboratorium1">Laboratorium 1</a></p>
<p><a href="#Laboratorium2">Laboratorium 2</a></p>  
<p><a href="#Laboratorium3">Laboratorium 3</a></p>
<p><a href="#Laboratorium4">Laboratorium 4</a></p>
<p><a href="#Laboratorium5">Laboratorium 5</a></p>
<p><a href="#Laboratorium9">Laboratorium 9</a></p>
<p><a href="#Laboratorium10">Laboratorium 10</a></p>

<a id="laboratorium1"></a>
## Laboratorium 1 - Blog

Link do bloga na heroku - [BLOG](https://ewekmarchewek-blog.herokuapp.com/blog/)

#### Strona startowa

Po wejściu na stronę, można zauważyć tytuł strony oraz dodane posty. 
W lewym górnym rogu widać plus, za którego pomocą możemy dodać nowy post.

![screen_main_page](assets/main_page.png)

#### Dodawanie postu

Po wciśnieciu wcześniej wspomnianego plusa, przechodzimy do okna, w którym możemy stowrzyć nowy post.

![screen_crt_post](assets/new_post.png)

#### Detale postu

Po kliknięciu na tytuł posta, wyświetlają się jego detale. 

![post_details](assets/post_details.png)

### Panel administratora

![panel_adm](assets/admin_pane.png)

<a id="laboratorium2"></a>
## Laboratorium 2 - Blog i konta użytkowników.

#### Widok bloga przed zalogowaniem się użytkownika.
![before_login](assets/blog_beforelogin.png)

#### Widok bloga po zalogowaniu się użytkownika
![logged_user](assets/blog_loggeduser.png)

#### Formularz rejestracji
![register_form](assets/blog_registerform.png)

#### Pomyślna rejestracja użytkownika
![after_register](assets/blog_afterregister.png)

#### Formularz logowania
![login_form](assets/blog_loginform.png)

#### Niepomyślne logowanie
![failed_login](assets/blog_failedlogin.png)

#### Formularz resetowania hasła
![reset_password_form](assets/blog_resetpasswordform.png)

<a id="laboratorium3"></a>
## Laboratorium 3 - Różne sposoby uwierzytelniania.
#### Uwierzytelnianie za pomocą Google
![googleauth](assets/auth_google_working.png)
#### Uwierzytelnianie za pomocą Facebooka
![facebookauth](assets/auth_facebook_working.png)

<a id="laboratorium4"></a>
## Laboratorium 4 - REST API z DRF.
#### Books ( dodanie własnej książki )
![booksadd](assets/books_add.png)
#### Books - wyświetlanie listy książek
![books](assets/books.png)
#### API Books
![facebookauth](assets/api.png)


<a id="laboratorium5"></a>
## Laboratorium 5 - Web Scraping.
#### Podczas scrape'owania najczęściej zależy nam na wyciągnięciu informacji z kodu HTML na stronach, do tego przydadzą się biblioteka Beautifulsoup oraz pakiet Requests. 
#### Za pomocą biblioteki Requests możemy pobierać strony w Pythonie, a pakiet Beautifulsoup analizuje kod HTML i pomaga w formatowaniu i organizowaniu danych ze strony internetowej na bardziej przyjazne dla oka struktury.
#### Jeśli chcemy wyodrębnić pojedynczy tag, możemy użyć metody find (find_all), która znajdzie wszystkie wystąpienia tagu na stronie. Używając tej samej metody można zbadać konkretną klasę lub identyfikator na stronie. Żeby dowiedzieć się, jak oznaczony jest element, który chcemy znaleźć wystarczy na wybranej stronie internetowej użyć opcji Inspect (zbadaj element)
![inspect](assets/scraping_inspect.png)
#### W kodzie szukamy elementów, które nas interesują :
![inspect_elements](assets/scraping_inspect_code.png)
#### Jako pierwszy przykład scrape'ingu pobiorę ze [strony](https://coreyms.com) nagłówki postów razem z treściami i linkami do filmików na youtube. Zapiszę je w pliku scrape_one.
![scraping1](assets/scraping1_result.png)
#### Jak widać, wybrane elementy wyświetliły się w konsoli oraz zostały zapisane w pliku scrape_one - dane są od siebie oddzielone przecinkami.
![scraping1](assets/scraping1_excel.png)

#### W drugim przykładzie pobiorę ze [strony](https://pl.wikisource.org/wiki/Kategoria:Polscy_poeci) autorów wierszy i podam czas, który komputer poświęcił na pobranie informacji.
![scraping2](assets/scraping2_result.png)
#### Pobiorę 10 pierwszych autorów
![scraping2](assets/scraping_two_result2.png)
#### Dodam też foldery z autorami (niestety bez polskich znaków).
![scraping2](assets/scraping2_result2_folders.png)


<a id="laboratorium9"></a>
## Laboratorium 9 - Django + React (aplikacja CRUD)

<a id="laboratorium10"></a>
## Laboratorium 10 - Django + React (aplikacja typu ToDo)

### backend
1. TODO admin panel
![todoadmpan](assets/TODO.png)
2. TOTO - task add
![todotaskadd](assets/todotask1added.png)
3. TODO - task delete
![todotaskdel](assets/todotask1delete.png)
4. TODO - delete confirm
![tododelconf](assets/tododeletingconfirm.png)
5. TODO - deleted task
![tododeletedtask](assets/tododeletedtask.png)
6. TODO - Api todos
![todoapitodos](assets/todoapitodos.png)
7. TODO - todolist
![todolist](assets/todolist.png)
8. TODO - example task 2 address
![todolist](assets/todotask2address.png)

### frontend
 
![todofront](assets/frontendreact.png)
![](assets/frontendtodocompleted.png)
![](assets/frontendtodoedit.png)
