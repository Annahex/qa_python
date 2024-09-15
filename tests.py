from main import BooksCollector
import pytest

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
        # assert len(collector.get_books_rating()) == 2 ошибка тут была
        assert len(collector.get_books_genre().keys()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name', ['', 'Тестовое имя книги длиной больше 41 символ'])
    def test_add_new_book_book_does_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre().keys()) == 0

    def test_set_book_genre_name_and_genre_exists_genre_set(self):
        collector = BooksCollector()
        name = 'Название книги'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_wrong_genre_genre_does_not_set(self):
        collector = BooksCollector()
        name = 'Название книги'
        genre = 'Не существующий жанр'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert len(collector.get_book_genre(name)) == 0

    def test_set_book_genre_wrong_name_genre_does_not_set(self):
        collector = BooksCollector()
        name = 'Название книги'
        wrong_name = 'Неверное название книги'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(wrong_name, genre)
        assert collector.get_book_genre(wrong_name) is None

    def test_get_book_genre_name_is_exists_returns_genre(self):
        collector = BooksCollector()
        name = 'Название книги'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_name_is_not_exists_return_none(self):
        collector = BooksCollector()
        name = 'Название книги'
        wrong_name = 'Неверное название книги'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(wrong_name, genre)
        assert collector.get_book_genre(wrong_name) is None

    def test_get_books_with_specific_genre_genre_is_exist_result_is_not_empty(self):
        collector = BooksCollector()
        name_1 = 'Название книги 1'
        name_2 = 'Название книги 2'
        genre = 'Фантастика'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, genre)
        collector.set_book_genre(name_2, genre)
        assert len(collector.get_books_with_specific_genre(genre)) == 2

    def test_get_books_with_specific_genre_genre_is_not_exist_result_is_empty(self):
        collector = BooksCollector()
        name_1 = 'Название книги 1'
        name_2 = 'Название книги 2'
        genre = 'Фантастика'
        wrong_genre = 'Фантастика 2'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, genre)
        collector.set_book_genre(name_2, genre)
        assert len(collector.get_books_with_specific_genre(wrong_genre)) == 0

    def test_get_books_genre_list_is_not_empty(self):
        collector = BooksCollector()
        name_1 = 'Название книги 1'
        name_2 = 'Название книги 2'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        assert len(collector.get_books_genre().keys()) == 2

    def test_get_books_for_children_input_all_genres_return_list_len_2(self):
        collector = BooksCollector()
        for i, g in enumerate(collector.genre):
            book_name = f"Имя книги {i}"
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, g)
        assert len(collector.get_books_for_children()) == 3

    def test_add_book_in_favorites_book_is_exists_favorites_len_1(self):
        collector = BooksCollector()
        name = 'Название книги'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_is_not_exists_favorites_len_0(self):
        collector = BooksCollector()
        name_1 = 'Название книги 1'
        name_2 = 'Название книги 2'
        collector.add_new_book(name_1)
        collector.add_book_in_favorites(name_2)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_is_exists_favorites_len_0(self):
        collector = BooksCollector()
        name = 'Название книги'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_is_not_exists_favorites_len_1(self):
        collector = BooksCollector()
        name_1 = 'Название книги 1'
        name_2 = 'Название книги 2'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.add_book_in_favorites(name_1)
        collector.delete_book_from_favorites(name_2)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_book_added_to_favorite_len_1(self):
        collector = BooksCollector()
        name = 'Название книги'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_book_not_added_to_favorite_len_0(self):
        collector = BooksCollector()
        name = 'Название книги'
        collector.add_new_book(name)
        assert len(collector.get_list_of_favorites_books()) == 0