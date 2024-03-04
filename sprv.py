import csv

def read_contacts_from_csv(filename):
    contacts = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def write_contacts_to_csv(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = [surname, name, patronymic, phone_number]
    return contact

def display_contacts(contacts):
    for contact in contacts:
        print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Телефон: {contact[3]}")

def save_contacts(contacts):
    write_contacts_to_csv("contacts.csv", contacts)
    print("Контакты сохранены в файле contacts.csv")

def load_contacts():
    try:
        contacts = read_contacts_from_csv("contacts.csv")
        print("Контакты успешно загружены из файла contacts.csv")
        return contacts
    except FileNotFoundError:
        print("Файл contacts.csv не найден. Создайте новый список контактов.")
        return []

def find_contact_index(contacts, search_query):
    for i, contact in enumerate(contacts):
        if search_query in (contact[0], contact[1], contact[2]):
            return i
    return -1

def main():
    contacts = load_contacts()

    while True:
        print("Выберите действие:")
        print("1. Показать все контакты")
        print("2. Добавить новый контакт")
        print("3. Сохранить контакты")
        print("4. Выйти")

        choice = input("Ваш выбор: ")
        print()

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            contact = add_contact()
            contacts.append(contact)
            print("Контакт успешно добавлен.")
        elif choice == "3":
            save_contacts(contacts)
        elif choice == "4":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()

    