class Star_Cinema:
    hall_list = []
    
    def entry_hall(self):
        Star_Cinema.hall_list.append(self)

class Hall:
    def __init__(self, row, col, hall_no):
        self.seats = {}
        self.show_list = []
        self.row = row
        self.col = col
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self,show_id, movie_name, time):
        show_info = (movie_name,show_id,time)
        self.show_list.append(show_info)
        self.seat_matrix(show_id)
    
    def seat_matrix(self, show_id):
        seats = [[0 for _ in range(self.col)]for _ in range(self.row)]
        self.seats[show_id] = seats

    def view_show_list(self):
        for show_info in self.show_list:
            movie_name, show_id, time = show_info
            print(f"\tMovie Name: {movie_name} Show Id: {show_id} Time: {time}")

    @staticmethod
    def book_seats():
        while True:
            try:
                show_id = int(input("Enter show id to book tickets: "))
            except ValueError:
                print("\tInvalid value. Please enter integer value")
                continue
            
            match = False
            for hall in Star_Cinema.hall_list:
                if show_id in hall.seats:
                    match = True
                    break
            if not match:
                print(f"\tShow id '{show_id}' does not exist")
                while True:
                    option_1 = input("Enter correct show id or check by going to 'View All Show Today'.Continue or back?(C/B): ")
                    if option_1 == 'C' or option_1 == 'c':
                        break
                    elif option_1 == 'B' or option_1 == 'b':
                        return
                    else:
                        print(f"'{option_1}' is an invalid command!")
                continue

            book_seat = []
            try:
                row = int(input("Enter the row number: "))
            except ValueError:
                print("\tInvalid value. Please enter an integer value")
                continue
            if row < 0 or row >= hall.row:
                print(f"\tThis '{row}' does not exist.")
                continue  
            try:    
                col = int(input("Enter the column number: "))
            except ValueError:
                print("\tInvalid value. Please enter an integer value")
                continue
                
            book_seat.append((row, col))
            for hall in Star_Cinema.hall_list:
                if hall.seats.get(show_id):
                    for (row, col) in book_seat:

                        if row < 0 or row >= hall.row or col < 0 or col >= hall.col:
                            print(f"\tSeat at row {row}, column {col} does not exist.")
                            while True:
                                option_2 = input("Enter correct row and column or check by going to 'View Available Seats'.Continue or back?(C/B): ")
                                if option_2 == 'C' or option_2 == 'c':
                                    break
                                elif option_2 == 'B' or option_2 == 'b':
                                    return
                                else:
                                    print(f"\t'{option_2}' is an invalid command!")
                            continue
                        
                        elif hall.seats[show_id][row][col] == 1:
                            print(f"\tThe seat at row {row}, column {col} is already booked.")
                            while True:
                                option_3 = input("Choose an available seat or check by going to 'View Available Seats'.Continue or back?(C/B): ")
                                if option_3 == 'C' or option_3 == 'c':
                                    break
                                elif option_3 == 'B' or option_3 == 'b':
                                    return
                                else:
                                    print(f"\t'{option_3}' is an invalid command!")
                            continue
                        
                        else:
                            hall.seats[show_id][row][col] = 1
                            print(f"\tSeat at position ({row}, {col}) successfully booked")
                            while True:
                                option_4 = input("Do you want to buy more tickets? (Y/N): ")
                                if option_4 == 'Y' or option_4 == 'y':
                                    break
                                elif option_4 == 'N' or option_4 == 'n':
                                    return
                                else:
                                    print(f"\t'{option_4}' is an invalid command!")
                            continue
                                            
    @staticmethod
    def view_available_seats():
        while True:
            try:
                show_id = int(input("Enter the show id to view available seat: "))
            except ValueError:
                        print("\tInvalid value. Please enter an integer value")
                        continue
            match = False
            for hall in Star_Cinema.hall_list:
                if show_id in hall.seats:
                    match = True
                    seats = hall.seats[show_id]
                    print(f"\nAvailable seats for show {show_id}:")
                    for row in range(hall.row):
                        for col in range(hall.col):
                            print(seats[row][col], end=' ')    
                        print()
            if not match:
                print(f"\tShow id '{show_id}' does not exist")
            else:
                break

hall_one = Hall(row=5, col=10, hall_no=1)
hall_two = Hall(row=6, col=8, hall_no=2)

hall_one.entry_show(movie_name="Kung Fu Panda 1", show_id=101, time="24/05/2023 3:00 PM")
hall_two.entry_show(movie_name="Kung Fu Panda 2", show_id=102, time="24/05/2023 4:00 PM")

while True:
    print("\nOptions: ")
    print("1 : View all show today")
    print("2 : View available seats")
    print("3 : Book Ticket")
    print("4 : Exit")
    try:
        choice = int(input("Enter Option: "))
    except ValueError:
        print("\tInvalid value. Please enter an interger value")
        continue

    if choice == 1:
        print("\nCurrently running shows:")
        for hall in Star_Cinema.hall_list: 
            hall.view_show_list()
    elif choice == 2:
            Hall.view_available_seats()
    elif choice == 3:
            Hall.book_seats()
    elif choice == 4:
        print("\n\tExiting the system. Have a nice day!")
        break
    else:
        print("\n\tInvalid Option. Please try again")
