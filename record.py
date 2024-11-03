from phone import Phone
from name import Name
from birthday import Birthday
from datetime import datetime, timedelta

class Record:
    """Клас, який представляє запис контакту з ім'ям, списком телефонів та днем народження."""

    def __init__(self, name: str):
        """Ініціалізує Record з ім'ям, списком телефонів і необов'язковим днем народження."""
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def __str__(self):
        """Повертає строкове представлення Record."""
        phones = '; '.join(p.value for p in self.phones)
        birthday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "Not set"
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}"


    def add_phone(self, number: str):
        """Додає номер телефону до контакту."""
        self.phones.append(Phone(number))


    def remove_phone(self, number: str):
        """Видаляє номер телефону з контакту."""
        self.phones = [phone for phone in self.phones if phone.value != number]


    def edit_phone(self, old_number: str, new_number: str):
        found = False

        for i, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[i] = Phone(new_number)
                found = True
                break
        if not found:
            raise KeyError(
                "The specified number does not exist or the contact has no phone numbers."
            )


    def find_phone(self, number: str):
        """Шукає номер телефону в контакті."""
        for phone in self.phones:
            if phone.value == number:
                return phone


    def add_birthday(self, birthday):
        """Додає день народження до контакту."""
        self.birthday = Birthday(birthday)


    def days_to_birthday(self):
        """Повертає кількість днів до наступного дня народження або None, якщо день народження не задано."""
        if not self.birthday:
            return None
        today = datetime.today()
        next_birthday = self.birthday.value.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days
