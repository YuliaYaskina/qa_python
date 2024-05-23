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
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_incorrect_name_length(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить: Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid_name_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Детективы'

    def test_get_book_genre_no_such_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == None

    def test_get_books_with_specific_genre_genre_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        assert len(collector.get_books_with_specific_genre('Детективы')) == 1

    def test_get_books_genre_one_book_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Детективы'}

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Детективы'], ['Что делать, если ваш кот хочет вас убить', 'Ужасы']])
    def test_get_books_for_children_book_in_age_rating(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_already_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    names = ['Гордость и предубеждение', '', 'Что делать если', 'Гордость и предубеждение и зомби 2']
    @pytest.mark.parametrize('name', 'names')
    def test_add_book_in_favorites_book_not_in_book_genre_list(self, name):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_no_books(self):
        collector = BooksCollector()
        assert len(collector.get_list_of_favorites_books()) == 0

