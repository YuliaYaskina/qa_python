# qa_python
1. test_add_new_book_incorrect_name_length: проверяет, что если название книги больше 41 символа, книга не добавится в список books_genre
2. test_set_book_genre_valid_name_and_genre: проверяет присваивание книге из списка books_genre жанра
3. test_get_book_genre_no_such_book: проверяет отсутствие жанра у книги, которой нет в списке books_genre
4. test_get_books_with_specific_genre_genre_exists: проверяет, что функция по жанру возвращает название книги
5. test_get_books_genre_one_book_with_genre: проверяет, что функция возвращает словарь с названиями и жанрами книг
6. test_get_books_for_children_book_in_age_rating: проверяет, что функция не возвращает книги запрещенных для детей жанров
7. test_add_book_in_favorites_already_in_favorites: проверяет, что функция дважды не добавляет одну и ту же книгу в список favorities
8. test_add_book_in_favorites_book_not_in_book_genre_list: проверяет, что нельзя добавить книгу с писок favorities, если ее нет в списке books_genre
9. test_delete_book_from_favorites_delete_one_book: проверка удаления одно из книг из списка favorities
10. test_get_list_of_favorites_books_no_books: проверка получения пустого списка favorities
