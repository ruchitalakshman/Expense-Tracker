class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.date} | {self.category} | {self.description} | {self.amount}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
        for expense in self.expenses:
            print(expense)

    def total_expenses(self):
        total = sum(float(expense.amount) for expense in self.expenses)
        print(f"Total Expenses: {total}")

    def view_by_category(self, category):
        filtered_expenses = [exp for exp in self.expenses if exp.category == category]
        if not filtered_expenses:
            print(f"No expenses found for category: {category}")
        for expense in filtered_expenses:
            print(expense)

    def load_expenses(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    date, category, description, amount = line.strip().split(',')
                    expense = Expense(date, category, description, amount)
                    self.add_expense(expense)
        except FileNotFoundError:
            print("Expense file not found, starting with an empty list.")

    def save_expenses(self, file_name):
        with open(file_name, 'w') as file:
            for expense in self.expenses:
                file.write(f"{expense.date},{expense.category},{expense.description},{expense.amount}\n")

def menu():
    tracker = ExpenseTracker()
    tracker.load_expenses('expenses.txt')

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Total Expenses")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Transport, etc.): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            expense = Expense(date, category, description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully.")

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            category = input("Enter category to filter: ")
            tracker.view_by_category(category)

        elif choice == '4':
            tracker.total_expenses()

        elif choice == '5':
            tracker.save_expenses('expenses.txt')
            print("Expenses saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu function to start the program
if __name__ == '__main__':
    menu()
