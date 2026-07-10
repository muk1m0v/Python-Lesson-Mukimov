library = []  # список кортежей с книгами
next_id = 1

while True:
    print("\n=== БИБЛИОТЕКА ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу")
    print("4. Выдать книгу")
    print("5. Вернуть книгу")
    print("6. Удалить книгу")
    print("7. Сохранить в файл")
    print("8. Загрузить из файла")
    print("0. Выход")
    choice = input("Выберите действие: ")

    match choice:
        case "1":
            title = input("Название: ")
            author = input("Автор: ")
            year = int(input("Год издания: "))
            genre = input("Жанр: ")
            copies = int(input("Количество экземпляров: "))
            # id, title, author, year, genre, total, available
            library.append((next_id, title, author, year, genre, copies, copies))
            print(f"Книга добавлена с ID {next_id}")
            next_id += 1

        case "2":
            if not library:
                print("Библиотека пуста.")
            else:
                sort_choice = input("Сортировать по (1 - названию, 2 - году): ")
                if sort_choice == "1":
                    sorted_lib = sorted(library, key=lambda x: x[1].lower())
                elif sort_choice == "2":
                    sorted_lib = sorted(library, key=lambda x: x[3])
                else:
                    sorted_lib = library

                for book in sorted_lib:
                    print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, "
                            f"Год: {book[3]}, Жанр: {book[4]}, "
                            f"Всего: {book[5]}, Доступно: {book[6]}")

        case "3":
            query = input("Введите название или автора: ").lower()
            found = False
            for book in library:
                if query in book[1].lower() or query in book[2].lower():
                    print(f"ID {book[0]}: {book[1]} - {book[2]} ({book[3]})")
                    found = True
            if not found:
                print("Ничего не найдено.")

        case "4":
            book_id = int(input("Введите ID книги для выдачи: "))
            for i, book in enumerate(library):
                if book[0] == book_id:
                    if book[6] > 0:
                        # Уменьшаем доступное количество: создаём новый кортеж
                        new_book = (book[0], book[1], book[2], book[3], book[4], book[5], book[6] - 1)
                        library[i] = new_book
                        print("Книга выдана.")
                    else:
                        print("Все экземпляры заняты.")
                    break
            else:
                print("Книга с таким ID не найдена.")

        case "5":
            book_id = int(input("Введите ID книги для возврата: "))
            for i, book in enumerate(library):
                if book[0] == book_id:
                    if book[6] < book[5]:
                        new_book = (book[0], book[1], book[2], book[3], book[4], book[5], book[6] + 1)
                        library[i] = new_book
                        print("Книга возвращена.")
                    else:
                        print("Все экземпляры уже в библиотеке.")
                    break
            else:
                print("Книга с таким ID не найдена.")

        case "6":
            book_id = int(input("Введите ID книги для удаления: "))
            for i, book in enumerate(library):
                if book[0] == book_id:
                    del library[i]
                    print("Книга удалена.")
                    break
            else:
                print("Не найдена.")

        case "7":
            with open("library.txt", "w", encoding="utf-8") as f:
                for book in library:
                    f.write("|".join(map(str, book)) + "\n")
            print("Сохранено.")

        case "8":
            try:
                with open("library.txt", "r", encoding="utf-8") as f:
                    library.clear()
                    for line in f:
                        parts = line.strip().split("|")
                        if len(parts) == 7:
                            book = (int(parts[0]), parts[1], parts[2], int(parts[3]),
                                    parts[4], int(parts[5]), int(parts[6]))
                            library.append(book)
                    if library:
                        next_id = max(book[0] for book in library) + 1
                print("Загружено.")
            except FileNotFoundError:
                print("Файл не найден.")

        case "0":
            print("Выход...")
            break

        case _:
            print("Неверный выбор. Попробуйте снова.")