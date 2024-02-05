'''This program allows a user to build a holiday package, including a choice
of flight destinations, hotels, and cars to hire. The cost for each element
is displayed if the user chooses to include it, and a final total is also
shown at the end.'''

# This function finds the flight price for a user-chosen destination.
def plane_cost(city):
    flight_price = 0
    for item in dest_choices:
        if item[0] == city:
            flight_price = int(item[1])
    return flight_price

# This function calculates the total car hire cost.
def car_rental(days, rate):
    total = days * rate
    return total

# This function calculates total hotel cost.
def hotel_cost(days, rate):
    total = days * rate
    return total

# This function calculates and shows user overall holiday cost.
def holiday_cost(hotel, flight, car):
    total = hotel + flight + car
    print(f'''
HOLIDAY FINAL SUMMARY:
Your hotel cost is £{hotel}.
Your car hire cost is £{car}.
Your flight cost is £{flight}.

Total : £{total}.
''')
    return total

# This dictionary contains departure airports and destination prices.
flight_prices = {
"London Heathrow" : {"Athens" : 170, "Miami" : 649, "New York" : 750,
                        "Paris" : 209},
"Manchester" : {"Barcelona" : 257, "Los Angeles" : 850, 
                "Rio de Janeiro" : 950, "Warsaw" : 195},
"Birmingham" : {"Amsterdam" : 165, "Dublin" : 95, "Munich" : 346,
                "Vancouver" : 786},
"Edinburgh" : {"Bruges" : 168, "Marseille" : 289, "Naples" : 401, 
                "Seville" : 394},
"Bristol" : {"Berlin" : 175, "Rome" : 379, "San Francisco" : 699, 
                "Vienna" : 345}
}

# User begins here.
print('''
Welcome to City Trip Planner!
\nHere we can build your perfect getaway with hotel, flights and car hire,
all bundled into one package price.
\nTo begin, we will need some basic details about your trip.''')

# Valid user inputs are collected for length of stay, hotel requirement,
# and car hire requirement.
while True:
    num_nights = input("\nHow many nights would you like to stay? Enter here : ")
    try:
        num_nights = int(num_nights)
        if num_nights == 0:
            print("Please select a value greater than zero.")
            continue
        break
    except ValueError:
        print("Please enter whole numbers only.")
        continue

while True:
    hotel_choice = input("\nDo you need a hotel booking? Y/N : ").strip().capitalize()
    if hotel_choice == "Y":
        break
    elif hotel_choice == "N":
        break
    else:
        print("Please type Y or N to continue with your booking.")
        continue

while True:
    car_choice = input("\nDo you need to hire a car? Y/N : ").strip().capitalize()
    if car_choice == "Y":
        break
    elif car_choice == "N":
        break
    else:
        print("Please type Y or N to continue with your booking.")
        continue
print("Great! Now please select your departure airport from the list below : ")

# Creates a list of departure options for the user.
depart_choices = "\n".join(flight_prices)

# Gets a valid departure choice from user,
# and creates related list of possible destinations.
while True:
    user_depart = input(f'''
{depart_choices}
\nType selection here : ''').strip().capitalize()
    try:
        dest_choices = flight_prices[user_depart].items()
        print("\nDeparture airport selected!")
        break
    except KeyError:
        print("\nError - enter the city name as it appears in the list.")
        continue

# Displays destination choices for user.
print(f'''
From {user_depart} we have some great destinations!
See the list below for cities and return flight price/pp : 
''')
for item in dest_choices:
    print(f"{item[0]}: £{item[1]}\n")

# Gets destination from user and if valid, stores flight cost.
flight_price = 0
city_flight = None
while flight_price == 0:
    city_flight = input("Please type a destination name to proceed : ").strip().capitalize()
    flight_price = plane_cost(city_flight)
    if flight_price == 0:
        print("\nError - type the destination as it appears in the list.")
print(f"\nFlight selected!\nYour flight price to {city_flight} is £{flight_price}.")

# Allows user choice of hotel and calculates cost.
if hotel_choice == "Y":
    print(f'''
\nNow for your hotel!
We have partnered with hotels in all our destination cities to offer you
excellent choices, at the same rate regardless of destination!
\nSimply choose your desired level of comfort from the list:
\n1 - Standard (£50/night) - A comfortable space with basic amenities.
\n2 - Upgrade (£75/night) - A stylish choice for those who want a little luxury.
\n3 - Premium (£150/night) - Our most exclusive rooms for an extra-special stay.
''')
    while True:
        user_hotel = input("Please choose a hotel level for your trip : ").strip()
        hotel_rate = 0
        try:
            user_hotel = int(user_hotel)
            if user_hotel == 1:
                hotel_rate = 50
                break
            elif user_hotel == 2:
                hotel_rate = 75
                break
            elif user_hotel == 3:
                hotel_rate = 150
                break
            else:
                print("Please only type 1, 2, or 3.")
                continue
        except ValueError:
            print("Please only type 1, 2 or 3.")
            continue
    hotel_final = hotel_cost(num_nights, hotel_rate)
    print(f'''
Excellent choice!
Your hotel cost for a {num_nights}-night stay will be £{hotel_final}.
''')
else:
    hotel_final = 0

# Allows user choice of rental length and car, and calculates cost.
if car_choice == "Y":
    print("\nNow for your car!\n")
    while True:
        rental_days = input("How many days would you like to hire a car for? : ")
        try:
            rental_days = int(rental_days)
            if rental_days > num_nights:
                print("Your hire days are longer than your trip, please re-enter.")
                continue
            elif rental_days == 0:
                print("Please enter a number greater than zero.")
                continue
            break
        except:
            print("Car hire is only available for full days.")
            continue
    print(f'''
We have several styles of vehicle to suit your needs!
Please choose from the list below:
1 - Compact (e.g. Honda Jazz) £12/day
2 - Large/Family (e.g. Kia Sorento) £25/day
3 - Prestige (e.g. Maserati) £150/day
''')
    while True:
        user_car = input("Please choose a car type : ").strip()
        try:
            user_car = int(user_car)
            if user_car == 1:
                car_rate = 12
                break
            elif user_car == 2:
                car_rate = 25
                break
            elif user_car == 3:
                car_rate = 150
                break
            else:
                print("Please only type 1, 2, or 3.")
                continue
        except ValueError:
            print("Please type 1, 2, or 3.")
            continue
    car_final = car_rental(rental_days, car_rate)
    print(f"Your vehicle hire for {rental_days} days will cost £{car_final}.")
else:
    car_final = 0

# Final display of package breakdown and costs.
print(f'''
Your holiday package is now complete!
Your cost breakdown for a {num_nights}-day trip to {city_flight} is below:
''')
holiday_cost(hotel_final, flight_price, car_final)