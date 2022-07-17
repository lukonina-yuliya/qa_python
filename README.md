# qa_python
Приложение BooksCollector позволяет установить рейтинг книг и добавить их в избранное.

**Приложение покрыто следующими unit-тестами:** 
### test_add_new_book_add_two_books
- Тестируется метод `add_two_books` (добавление новых книг)
- Позитивная проверка: добавление двух книг. 
 
### test_add_new_book_again_not_added
- Тестируется метод `add_two_books` (добавление новых книг)
- Негативная проверка: добавление книги, которая уже находится в словаре.

### test_set_book_rating_with_raiting_3_positive    
- Тестируется метод `set_book_rating` (установка рейтинга)
- Позитивная проверка: добавление корректного рейтинга к книге, находящейся в словаре.

### test_set_book_rating_with_raiting_11_raiting_still_1
- Тестируется метод `set_book_rating` (установка рейтинга)
- Негативная проверка: добавление некорректного рейтинга (11) к книге, находящейся в словаре.

### test_set_book_rating_with_raiting_zero_raiting_still_1
- Тестируется метод `set_book_rating` (установка рейтинга)
- Негативная проверка: добавление некорректного рейтинга (0) к книге, находящейся в словаре.

### test_set_book_rating_without_books_not_rating
- Тестируется метод `set_book_rating` (установка рейтинга)
- Негативная проверка: установка рейтинга книге, не добавленной в словарь

### test_get_book_rating_shows_book_rating
- Тестируется метод `get_book_rating` (вывод рейтинга книги по ее имени)
- Позитивная проверка: вывод рейтинга книги, находящейся в словаре, по ее наименованию

### test_get_books_with_specific_rating_with_specified_rating_shows_list
- Тестируется метод `get_books_with_specific_rating` (вывод списка книга с указанным  рейтингом)
- Позитивная проверка: вывод списка книг по указанному рейтингу. 

### test_get_books_rating_with_three_books_shows_list
- Тестируется метод `get_books_rating` (вывод текущего словаря books_rating)
- Позитивная проверка: вывод текущего словаря books_rating при наличии добавленных в него книг.

### test_add_book_in_favorites_one_book_positive_add
- Тестируется метод `add_book_in_favorites` (добавление книги в избранное)
- Позитивная проверка: добавление книги, находящейся в словаре, в избранное.

### test_add_book_in_favorites_again_not_added
- Тестируется метод `add_book_in_favorites` (добавление книги в избранное)
- Негативная проверка: повторное добавление книги, уже находящейся в словаре, в избранное.

### test_add_book_in_favorites_without_books_list_not_added
- Тестируется метод `add_book_in_favorites` (добавление книги в избранное)
- Негативная проверка: добавление в избранное книги, не находящейся в словаре.

### test_delete_book_from_favorites_deleted
- Тестируется метод `delete_book_from_favorites` (удаление книги из избранного)
- Позитивная проверка: удаление книги, находящейся в избранном, из избранного.

### test_get_list_of_favorites_books_with_two_books_shows_list
- Тестируется метод `get_list_of_favorites_books` (получение списка избранных книг)
- Позитивная проверка: получение списка избранных книг при наличии книг в избранном. 