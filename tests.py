from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_again_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.add_new_book('Сияние')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_with_raiting_3_positive(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_rating('Сияние', 3)

        assert collector.get_book_rating('Сияние') == 3

    def test_set_book_rating_with_raiting_11_raiting_still_1(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_rating('1984', 11)

        assert collector.get_book_rating('1984') == 1

    def test_set_book_rating_with_raiting_zero_raiting_still_1(self):
        collector = BooksCollector()

        collector.add_new_book('Carry')
        collector.set_book_rating('Carry', 0)

        assert collector.get_book_rating('Carry') == 1

    def test_set_book_rating_without_books_not_rating(self):
        collector = BooksCollector()

        collector.set_book_rating('Мизери', 3)

        assert collector.get_book_rating('Мизери') is None

    def test_get_book_rating_shows_book_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Harry Potter')
        collector.set_book_rating('Harry Potter', 10)

        assert collector.get_book_rating('Harry Potter') == 10

    def test_get_books_with_specific_rating_with_specified_rating_shows_list(self):
        collector = BooksCollector()

        collector.add_new_book('Anna')
        collector.set_book_rating('Anna', 3)

        collector.add_new_book('Maria')
        collector.set_book_rating('Maria', 5)

        collector.add_new_book('Vera')
        collector.set_book_rating('Vera', 5)

        assert collector.get_books_with_specific_rating(5) == ['Maria', 'Vera']

    def test_get_books_rating_with_three_books_shows_list(self):
        collector = BooksCollector()

        collector.add_new_book('Anna')
        collector.set_book_rating('Anna', 9)

        collector.add_new_book('Maria')
        collector.set_book_rating('Maria', 8)

        collector.add_new_book('Vera')
        collector.set_book_rating('Vera', 7)

        assert collector.get_books_rating() == {'Anna': 9, 'Maria': 8, 'Vera': 7}

    def test_add_book_in_favorites_one_book_positive_add(self):
        collector = BooksCollector()

        collector.add_new_book('Скотный двор')
        collector.add_book_in_favorites('Скотный двор')

        assert collector.get_list_of_favorites_books() == ['Скотный двор']

    def test_add_book_in_favorites_again_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Скотный двор')
        collector.add_book_in_favorites('Скотный двор')
        collector.add_book_in_favorites('Скотный двор')

        assert collector.get_list_of_favorites_books() == ['Скотный двор']

    def test_add_book_in_favorites_without_books_list_not_added(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('В дороге')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_deleted(self):
        collector = BooksCollector()

        collector.add_new_book('Дневник памяти')
        collector.add_book_in_favorites('Дневник памяти')
        collector.delete_book_from_favorites('Дневник памяти')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_two_books_shows_list(self):
        collector = BooksCollector()

        collector.add_new_book('Дневник памяти')
        collector.add_new_book('Сияние')
        collector.add_new_book('Узорный покров')
        collector.add_new_book('Властелин колец')

        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Узорный покров')

        assert collector.get_list_of_favorites_books() == ['Сияние', 'Узорный покров']
