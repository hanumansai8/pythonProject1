import datetime
expenses=[]
def add_expense(category,amount):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({'date': date, 'amount': amount, 'category': category})


def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("Date\t\t\tAmount\tCategory")

        print("------------------------------------")
        for expense in expenses:
            print(f"{expense['date']}\t${expense['amount']}\t{expense['category']}")





def main():
    while True:
        print("\n1. Record an expense")
        print("2. Display all expenses")
        print("3. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            category=input("enter category:")
            cost=int(input("enter cost:"))
            add_expense(category,cost)
            print(f"category{category},cost{cost}")
        elif choice==2:
            display_expenses()
        elif choice==3:
            print("Exiting program...")
            break
        else:
            print(
                "Invalid Option.Please try again"
            )

if __name__ == '__main__':
    main()





