import os


# Функция для вывода записей постранично
def display_entries(entries, page_size=10):
    total_entries = len(entries)
    total_pages = (total_entries + page_size - 1) // page_size

    page = 1
    while True:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        print("Справочник:")
        print("--------------------")
        for entry in entries[start_index:end_index]:
            print(f"ФИО: {entry['last_name']}, "
                  f"{entry['first_name']}, "
                  f"{entry['patronymic']}")
            print(f"Организация: {entry['organization']}")
            print(f"Рабочий телефон: {entry['work_phone']}")
            print(f"Личный телефон: {entry['personal_phone']}")
            print("--------------------")

        print(f"Страница {page}/{total_pages}")

        if total_pages == 1:
            break

        user_input = input("Введите 'n' для следующей страницы,"
                           "'p' для предыдущей страницы или 'q' для выхода: ")
        if user_input == 'n':
            page = min(page + 1, total_pages)
        elif user_input == 'p':
            page = max(page - 1, 1)
        elif user_input == 'q':
            break


# Функция для добавления новой записи в справочник
def add_entry(entries):
    entry = {}
    entry['last_name'] = input("Введите фамилию: ")
    entry['first_name'] = input("Введите имя: ")
    entry['patronymic'] = input("Введите отчество: ")
    entry['organization'] = input("Введите название организации: ")
    entry['work_phone'] = input("Введите рабочий телефон: ")
    entry['personal_phone'] = input("Введите личный телефон: ")
    entries.append(entry)
    print("Запись успешно добавлена!")


# Функция для редактирования записей в справочнике
def edit_entry(entries):
    display_entries(entries)
    entry_index = int(input("Введите номер записи,"
                            " которую хотите отредактировать: ")) - 1

    if 0 <= entry_index < len(entries):
        entry = entries[entry_index]
        print(f"Редактирование записи {entry_index + 1}:")
        print("--------------------")
        print(f"1. Фамилия: {entry['last_name']}")
        print(f"2. Имя: {entry['first_name']}")
        print(f"3. Отчество: {entry['patronymic']}")
        print(f"4. Название организации: {entry['organization']}")
        print(f"5. Рабочий телефон: {entry['work_phone']}")
        print(f"6. Личный телефон: {entry['personal_phone']}")
        print("--------------------")

        field_index = int(input("Введите номер поля, "
                                "которое хотите отредактировать: ")) - 1
        field_name = ['last_name', 'first_name', 'patronymic',
                      'organization', 'work_phone',
                      'personal_phone'][field_index]
        new_value = input("Введите новое значение: ")
        entry[field_name] = new_value
        print("Запись успешно отредактирована!")
    else:
        print("Неверный номер записи!")


# Функция для поиска записей по характеристикам
def search_entries(entries):
    search_term = input("Введите фамилию, имя, "
                        "отчество или организацию для поиска: ")
    search_results = []
    for entry in entries:
        if search_term.lower() in entry['last_name'].lower() or \
                search_term.lower() in entry['first_name'].lower() or \
                search_term.lower() in entry['patronymic'].lower() or \
                search_term.lower() in entry['organization'].lower():
            search_results.append(entry)

    if search_results:
        display_entries(search_results)
    else:
        print("Ничего не найдено.")


# Функция для сохранения записей в текстовый файл
def save_entries(entries, filename):
    with open(filename, 'w') as file:
        for entry in entries:
            file.write(f"{entry['last_name']}, "
                       f"{entry['first_name']}, "
                       f"{entry['patronymic']}, "
                       f"{entry['organization']}, "
                       f"{entry['work_phone']}, "
                       f"{entry['personal_phone']}\n")


# Функция для загрузки записей из текстового файла
def load_entries(filename):
    entries = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                values = line.strip().split(',')
                entry = {
                    'last_name': values[0],
                    'first_name': values[1],
                    'patronymic': values[2],
                    'organization': values[3],
                    'work_phone': values[4],
                    'personal_phone': values[5]
                }
                entries.append(entry)
    return entries


# Основная функция программы
def main():
    filename = "справочник.txt"

    # Загрузка записей из файла
    entries = load_entries(filename)

    while True:
        print("Меню:")
        print("1. Вывод записей на экран")
        print("2. Добавление новой записи")
        print("3. Редактирование записей")
        print("4. Поиск записей")
        print("5. Выход")

        choice = input("Введите номер операции: ")
        if choice == '1':
            display_entries(entries)
        elif choice == '2':
            add_entry(entries)
        elif choice == '3':
            edit_entry(entries)
        elif choice == '4':
            search_entries(entries)
        elif choice == '5':
            save_entries(entries, filename)
            print("Справочник сохранен. До свидания!")
            break
        else:
            print("Неверный номер операции. Попробуйте снова.")


if __name__ == '__main__':
    main()
