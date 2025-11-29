import matplotlib.pyplot as plt


class Family:
    def __init__(self, name, members, aid_type):
        self.name = name
        self.members = members
        self.aid_type = aid_type
        self.received = False

    def __repr__(self):
        return f"<Family {self.name}, Members: {self.members}, Aid: {self.aid_type}, Received: {self.received}>"


class AidSystem:
    def __init__(self):
        self.families = {}

    def add_family(self, name, members, aid_type):
        if name in self.families:
            print("Error: Family already exists!")
            return

        self.families[name] = Family(name, members, aid_type)
        print(f"Added family: {name}")

    def search_family(self, name):
        family = self.families.get(name)
        if family:
            print(family)
        else:
            print("Family Not Found")

    def mark_received(self, name):
        family = self.families.get(name)
        if family:
            family.received = True
            print(f"{name} marked as received ✔")
        else:
            print("Family Not Found")

    def show_all(self):
        if not self.families:
            print("No families added yet.")
            return

        for f in self.families.values():
            print(f)

    def list_sorted_by_members(self):
        sorted_list = sorted(self.families.values(), key=lambda f: f.members)
        print("\nSorted By Family Size:")
        for f in sorted_list:
            print(f)

    def plot_statistics(self):
        if not self.families:
            print("No data to plot.")
            return

        names = [f.name for f in self.families.values()]
        members = [f.members for f in self.families.values()]

        plt.bar(names, members)
        plt.title("Family Size Distribution")
        plt.xlabel("Family")
        plt.ylabel("Members Count")
        plt.show()

    def debug_test(self):
        try:
            print(10 / 0)
        except ZeroDivisionError:
            print("Debugging Test: Division by zero handled successfully ✔")


def main():
    system = AidSystem()

    while True:
        print("\n--- Aid Management Menu ---")
        print("1. Add Family")
        print("2. Show All Families")
        print("3. Search Family")
        print("4. Mark as Received")
        print("5. Sort by Members")
        print("6. Plot Statistics")
        print("7. Debug Test")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            members = int(input("Members Count: "))
            aid = input("Aid Type: ")
            system.add_family(name, members, aid)

        elif choice == "2":
            system.show_all()

        elif choice == "3":
            system.search_family(input("Enter Name: "))

        elif choice == "4":
            system.mark_received(input("Enter Name: "))

        elif choice == "5":
            system.list_sorted_by_members()

        elif choice == "6":
            system.plot_statistics()

        elif choice == "7":
            system.debug_test()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
