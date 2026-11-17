""" Customer Due Management System """

customers = []

def add_customer():
    try:
        customer_name = input("Enter customer name :- ").strip()
        if not customer_name:
            print("Customer name cannot be empty.")
            return     
        due = int(input("Enter due amount :- "))
        if due <= 0:
            print("Due amount cannot be negative or zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
        
    customer = {"Name": customer_name, "Due": due}
    customers.append(customer)
    print("Customer added successfully!")

def view_customers():
    name = input("Enter your name :- ").strip().lower()

    if name == "all":
        if len(customers) == 0:
            print("No customer found.")
            
        else:
            for customer in customers:
                print(f"Name: {customer['Name']} | Due: {customer['Due']} TK")
    else:
        for customer in customers:
            if customer ["Name"].lower() == name:
                print(f"Name: {customer['Name']} | Due: {customer['Due']} TK")
                break
        else:
            print("Customer not found.")

def payment_system():
    name = input("Enter your name :- ").strip().lower()
    found = False

    for customer in customers:
        if customer["Name"].lower() == name:
            print(f"Name: {customer['Name']} | Due: {customer['Due']} TK")
            found = True
            
            ask = input("Do you want to pay right now? (yes or no) :- ").strip().lower()

            if ask == "yes":
                try:
                    payment = int(input("Enter your payment :- "))
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    return
                
                if payment <= 0:
                    print("Payment cannot be negative or zero.")
                    return
                
                elif customer['Due'] == payment:
                    customer['Due'] = customer['Due'] - payment
                    print("Payment successfully! Your Due Balance is 0")

                elif payment < customer['Due']:
                    customer['Due'] = customer['Due'] - payment
                    print(f"Payment successfully! Your Due Balance is {customer['Due']}.")
                    
                else:
                    print("Payment cannot exceed due amount.")
            else:
                print("Please pay on time.")
            break

    if not found:
        print("This name doesn't exist.")

def calculate_total_due():
    if not customers:
        print("No customer found.")
        return
    
    else:
        name = input("Enter your name :- ").strip().lower()
        if name == "nazmul":
            total_sum = 0 
            for customer in customers:
                due_amount = customer['Due']
                total_sum = total_sum + due_amount
            print(f"Total customers due {total_sum}")

        else:
            print("You are not the owner. Only the can view the total.")

menu = ["1. Add", "2. View", "3. Payment", "4. Total Due", "5. Exit"]

while True:
    print("========= Menu =========")
    for i in menu:
        print(i)

    option = None
    try:
        option = int(input("\nSelect an option :- "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if option == 1:
        add_customer()

    elif option == 2:
        view_customers()

    elif option == 3:
        payment_system()

    elif option == 4:
        calculate_total_due()

    elif option == 5:
        print("Thank you for using the Customer Due Book System!")
        break

    else:
        print("Please select an option between 1 and 3")
        print("Invalid input! Please enter a valid number.")

result = "\n".join(
    f"Name: {customer['Name']} - Due: {customer['Due']} TK"
    for customer in customers
)

with open("customers.txt", "a") as f:
    f.write(result)