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
            show_id = int(input("Enter show id to book tickets: "))
            match = False
            for hall in Star_Cinema.hall_list:
                if show_id in hall.seats:
                    match = True
                    break
            if not match:
                print(f"\tShow id '{show_id}' does not exist")
                option_1 = input("Enter correct show id or check by going to 'View All Show Today'.Continue or back?(C/B): ")
                if option_1 == 'C' or option_1 == 'c':
                    continue
                if option_1 == 'B' or option_1 == 'b':
                    return
            book_seat = []
            row = int(input("Enter the row number: "))
            col = int(input("Enter the column number: "))
            book_seat.append((row, col))
            for hall in Star_Cinema.hall_list:
                if hall.seats.get(show_id):
                    for (row, col) in book_seat:
                        if row < 0 or row >= hall.row or col < 0 or col >= hall.col:
                            print(f"\tSeat at row {row}, column {col} does not exist.")
                            option_1 = input("Enter correct show id or check by going to 'View All Show Today'.Continue or back?(C/B): ")
                            if option_1 == 'C' or option_1 == 'c':
                                continue
                            if option_1 == 'B' or option_1 == 'b':
                                return
                        elif hall.seats[show_id][row][col] == 1:
                            print(f"\tThe seat at row {row}, column {col} is already booked.")
                            option_1 = input("Choose an available seat or check by going to 'View Available Seats'.Continue or back?(C/B): ")
                            if option_1 == 'C' or option_1 == 'c':
                                continue
                            if option_1 == 'B' or option_1 == 'b':
                                return
                        else:
                            hall.seats[show_id][row][col] = 1
                            print(f"\tSeat at position ({row}, {col}) successfully booked")
                            option_2 = input("Do you want to buy more tickets? (Y/N): ")
                            if option_2 == 'Y' or option_2 == 'y':
                                continue
                            if option_2 == 'N' or option_2 == 'n':
                                return
    
    @staticmethod
    def view_available_seats():
        show_id = int(input("Enter the show id to view available seat: "))
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
    
    choice = int(input("Enter Option: "))

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