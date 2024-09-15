# Реализованные тесты

### test_add_new_book_add_two_books

Тест из примера, ничего не меняла

### test_add_new_book_book_does_not_added

Негативный тест добавления книг. Используется параметризация. 

### test_set_book_genre_name_and_genre_exists_genre_set

Позитивный тест на установку жанра для книги

### test_set_book_genre_wrong_genre_genre_does_not_set

Негативный тест на установку жанра для книги (несуществующий жанр)

### test_set_book_genre_wrong_name_genre_does_not_set

Негативный тест на установку жанра для книги (несуществующая книга)

### test_get_book_genre_name_is_exists_returns_genre

Позитивный тест на получение жанра книги

### test_get_book_genre_name_is_not_exists_return_none

Негативный тест на получение жанра книги (книги не существует)

### test_get_books_with_specific_genre_genre_is_exist_result_is_not_empty

Позитивный тест на получение списка книг по их жанру

### test_get_books_with_specific_genre_genre_is_not_exist_result_is_empty

Негативный тест на получение списка книг по их жанру (жанр не существует)

### test_get_books_genre_list_is_not_empty

Позитивный тест на получение списка книг

### test_get_books_for_children_input_all_genres_return_list_len_2

Позитивный тест на получение списка книг для детей 

### test_add_book_in_favorites_book_is_exists_favorites_len_1

Позитивный тест на добавление книги в избранное

### test_add_book_in_favorites_book_is_not_exists_favorites_len_0

Негативный тест на добавление книги в избранное (книги не существует)

### test_delete_book_from_favorites_book_is_exists_favorites_len_0

Позитивный тест на удаление книги из избранного

### test_delete_book_from_favorites_book_is_not_exists_favorites_len_1

Негативный тест на удаление книги из избранного (такой книги в избранном нет)

### test_get_list_of_favorites_books_book_added_to_favorite_len_1

Позитивный тест на получение списка избранного (если в нем что-то есть)

### test_get_list_of_favorites_books_book_not_added_to_favorite_len_0

Позитивный тест на получение списка избранного (если в него ничего не добавлялось)