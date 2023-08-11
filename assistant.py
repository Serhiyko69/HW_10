from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone

    def __str__(self):
        phones_str = ", ".join(map(str, self.phones))
        return f"Name: {self.name}, Phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search_records(self, **criteria):
        results = []
        for record in self.data.values():
            match = True
            for field, value in criteria.items():
                if field == "phone":
                    if not any(str(phone) == value for phone in record.phones):
                        match = False
                        break
                elif field == "name":
                    if str(record.name) != value:
                        match = False
                        break
            if match:
                results.append(record)
        return results

