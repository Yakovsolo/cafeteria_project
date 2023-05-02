from dataclasses import dataclass
import datetime
import json


@dataclass
class TableReservation:
    current_time = datetime.datetime.now()
    name: str
    surname: str
    number_of_guests: str

    with open("tables.json", "r") as file:
        data_base_of_tables = json.load(file)

    @classmethod
    def define_table_type(cls, number_of_guests: int) -> str:
        if number_of_guests == 1:
            return "Single table"
        if number_of_guests == 2:
            return "Double table"
        if number_of_guests >= 3:
            return "Family table"

    def check_reservation(self) -> bool:
        table_type = TableReservation.define_table_type(self.number_of_guests)
        list_of_table = list(self.data_base_of_tables[table_type].keys())

        for table_number in list_of_table:
            if (
                self.data_base_of_tables[table_type][table_number]["Name"]
                == self.name + " " + self.surname
            ):
                print(f"You already have reservation. Your table is: {table_number}")
                return True
        print("I'm sorry, but there is no reservation for your name")
        return False

    def print_info_of_reservation(self) -> None:
        for table_type, table_reservation in self.data_base_of_tables.items():
            print("\nTable type", table_type)
            for key in table_reservation:
                print(f"{key} : {table_reservation[key]}")

    def get_reservation(self):
        table_type = TableReservation.define_table_type(self.number_of_guests)
        list_of_table = list(self.data_base_of_tables[table_type].keys())
        time = datetime.datetime.now().strftime("%Y %B %d at %H:%M")

        for table_number in list_of_table:
            if (
                self.data_base_of_tables[table_type][table_number]["Status"]
                == "availible"
            ):
                self.data_base_of_tables[table_type][table_number] = {
                    "Status": "reserved",
                    "Name": self.name + " " + self.surname,
                    "Time": time,
                }
                print(
                    f"We have reserved a table under your name. {table_type} №{table_number} has been reserved for {name} {surname} on {time}"
                )
                with open("tables.json", "w") as file:
                    json.dump(self.data_base_of_tables, file, indent=2)
                return True
        print(f"I'm sorry, but there are no empty {table_type}s")


if __name__ == "__main__":
    name = input("Please enter your name: \n").capitalize()
    surname = input("Please enter your surname: \n").capitalize()
    print(f"\nDear {name} {surname}, we are pleased to welcome you to our cafeteria\n")

    number_of_guests = int(input("Please enter the number of guests: \n"))

    person = TableReservation(
        name=name,
        surname=surname,
        number_of_guests=number_of_guests,
    )
    guest = person.check_reservation()
    if guest == False:
        person.get_reservation()

    person.print_info_of_reservation()
