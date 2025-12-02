student_count=0
adult_count=0
senior_count=0
ticket_no=0
total_sales=0.0
while True:
        while True:
                try:
                    print("\n1. Log In")
                    print("2. Exit")
                    choice=input("\nEnter your choice (1/2): ")

                    users={
                        "ticketer1": "12345",
                        "ticketer2": "12345"
                    }

                    if choice=="1":
                        username=input("\nEnter username (ticketer1/ticketer2): ")
                        password=input("Enter password (12345): ")
                        if username in users and users[username] == password:
                            print("\n Login successful!")
                            print("WELCOME TICKETER!!\n")
                            break
                        else:
                            print("\nInvalid username or password. Please try again.")
                    elif choice=="2":
                        print("\n------- TOTAL TICKET SOLD -------")
                        print(f"Total Student Passengers : {student_count}")
                        print(f"Total Adult Passengers   : {adult_count}")
                        print(f"Total Senior Passengers  : {senior_count}")
                        print("---------------------------")
                        print(f"Total Tickets Sold       : {student_count + adult_count + senior_count}")
                        print(f"Total Sales              : Php{total_sales:.2f}")
                        print("---------------------------------")
                        print("\nGood Bye!! :>")
                        exit()

                except ValueError:
                    print("Invalid Input! Please Try Again!")
        while True:        
                print("\nCostumer Passenger type!!")
                print("\n1. Student (20% Discount)")
                print("2. Adult (Regular Price)")
                print("3. Senior (30% Discount)")
                passenger_type=str(input("\nEnter your passenger type (1/2/3): ")).lower()
                if passenger_type=="1":
                    print("\nYour Passenger Type is Student(20% Discount). Please proceed.")
                    student_count+=1
                elif passenger_type=="2":
                    print("\nYour Passenger Type is Adult(Regular Price). Please proceed.")
                    adult_count+=1
                elif passenger_type=="3":
                    print("\nYour Passenger Type is Senior(30% Discount). Please proceed.")
                    senior_count+=1
                else:
                    print("\nInvalid Passenger Type. Fare will be charged as a regular price.")
                    adult_count+=1

                print("\nBUS DESTINATIONS!!")
                print("\n1. Cagayan De Oro (240 Php)")
                print("2. Iligan (250 Php)")
                print("3. Butuan (300 Php)")
                print("4. Malaybalay (450 Php)")
                print("5. Valencia (500 Php)")
                while True:
                    try:
                        destination=str(input("\nEnter bus destination (1/2/3/4/5): "))
                        if destination=="1":
                            print("\nSelected Destination is Cagayan De Oro.")
                        elif destination=="2":
                            print("\nSelected Destination is Iligan.")
                        elif destination=="3":
                            print("\nSelected Destination is Butuan.")
                        elif destination=="4":
                            print("\nSelected Destination is Malaybalay.")
                        elif destination=="5":
                            print("\nSelected Destination is Valencia.")
                        else:
                            print("\nInvalid Input! Please Enter a number between 1-5.")
                            continue
                        break
                    except ValueError:
                        print("\nInvalid Input! Please Enter a number between 1-5.")

                if destination=="1":
                    fare=240
                    if passenger_type=="1":
                        fare*=0.80
                    if passenger_type=="2":
                        fare*=1.00
                    elif passenger_type=="3":
                        fare*=0.70
                    else:
                        fare*1.00
                elif destination=="2":
                    fare=250
                    if passenger_type=="1":
                        fare*=0.80
                    elif passenger_type=="2":
                        fare*=1.00
                    elif passenger_type=="3":
                        fare*=0.70
                    else:
                        fare*=1.00
                elif destination=="3":
                    fare=300
                    if passenger_type=="1":
                        fare*=0.80
                    elif passenger_type=="2":
                        fare*=1.00
                    elif passenger_type=="3":
                        fare*=0.70
                    else:
                        fare*=1.00
                elif destination=="4":
                    fare=450
                    if passenger_type=="1":
                        fare*=0.80
                    elif passenger_type=="2":
                        fare*=1.00
                    elif passenger_type=="3":
                        fare*=0.70
                    else:
                        fare*=1.00
                elif destination=="5":
                    fare=500
                    if passenger_type=="1":
                        fare*=0.80
                    elif passenger_type=="2":
                        fare*=1.00
                    elif passenger_type=="3":
                        fare*=0.70
                    else:
                        fare*=1.00
                print(f"\nTotal price: Php{fare}")

                while True:
                    try:
                        payment_amount=int(input("\nEnter Payment amount: "))
                        if payment_amount<fare:
                            print("\nNot enough efficiency!. Please enter again.")
                            continue
                        break
                    except ValueError:
                            print("\nInvalid Input! Please enter a number!.")
                print(f"Your change is: {payment_amount-fare}")

                print("\nRECEIPT")
                print("______________________________")
                ticket_no+=1
                print(f"Ticket No: {ticket_no}")
                if passenger_type == "1":
                    print("Passenger Type: Student (20% Discount)")
                elif passenger_type == "2":
                    print("Passenger Type: Adult (Regular Price)")
                elif passenger_type == "3":
                    print("Passenger Type: Senior (30% Discount)")
                else:
                    print("Passenger type: Regular (Regular Price)")
                if destination=="1":
                    print("Destination: Cagayan De Oro")
                elif destination=="2":
                    print("Destination: Iligan")
                elif destination=="3":
                    print("Destination: Butuan")
                elif destination=="4":
                    print("Destination: Malaybalay")
                elif destination=="5":
                    print("Destination: Valencia")
                print(f"Total fare: Php{fare}")
                print(f"Total Change: Php{payment_amount-fare}")
                total_sales+=fare
                print("______________________________")
                    
                print("\nThank you for purchasing our ticket, Enjoy your ride!! :>")
                again=(input("\nWould you like to add another ticket? (Yes/No): ")).lower()
                if again !="yes":
                    break
