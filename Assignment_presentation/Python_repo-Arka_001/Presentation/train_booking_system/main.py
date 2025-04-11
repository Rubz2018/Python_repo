# main.py

from train import Train
from railway_system import RailwaySystem

def main():
    system = RailwaySystem()

    # Adding sample trains
    train1 = Train(101, "Express A", 3)
    train2 = Train(102, "Express B", 2)

    system.add_train(train1)
    system.add_train(train2)

    while True:
        print("\n====== Railway Booking System ======")
        print("1. Show all trains")
        print("2. Book a ticket")
        print("3. Cancel a ticket")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.show_all_trains()

        elif choice == '2':
            train_no = int(input("Enter Train No: "))
            passenger_name = input("Enter Passenger Name: ")
            train = system.find_train(train_no)
            if train:
                train.book_seat(passenger_name)
            else:
                print("❌ Train not found!")

        elif choice == '3':
            train_no = int(input("Enter Train No: "))
            passenger_name = input("Enter Passenger Name: ")
            train = system.find_train(train_no)
            if train:
                train.cancel_seat(passenger_name)
            else:
                print("❌ Train not found!")

        elif choice == '4':
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
