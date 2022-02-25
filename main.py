import random

#add an introduction!

#generate the initial random option
def generate_random_option(list):
    option_index = random.randint(0, len(list) - 1) 
    option = list[option_index]
    return option

#get approval/final option from user
#BUG: need to fix issue where random generator can give user the option they just declined 
#BUG: need to fix issue where if user inputs text other than Y/N, the application stops - need to handle for exception
def user_confirm_option(current_option, list, list_type):
    option = current_option
    option_index = ''
    user_approval = ''
    approval = False
    while approval == False:
        option_index = random.randint(0, len(list) - 1) 
        option = list[option_index]
        print(f'The {list_type} we have picked for you is {option}')
        user_approval = input("Do you approve? Y/N")
        if user_approval == 'Y':
            approval = True
        else: 
            print('Please enter Y or N')
            user_approval = input("Do you approve? Y/N")
    return option

#confirm trip. if use confirms, print the final itinerary, if they do not confirm, prompt them to start over)
#BUG: need to fix issue where if user inputs text other than Y/N, the application stops - need to handle for exception
def confirm_trip(final_trip):
    user_confirmation = input(f'Please confirm your trip. Y to confirm, N to decline. Destination: {final_trip[0]}, Transportation: {final_trip[1]}, Entertainment: {final_trip[2]}, Restaurant: {final_trip[3]}')
    if user_confirmation == 'Y':
        print('Thank you for confirming.')
        print(f'Your destination is {final_trip[0]} where you will arrive by {final_trip[1]}. While in {final_trip[0]}, you will enjoy your day by {final_trip[2]} and finish the day with a meal at {final_trip[3]}.')
    elif user_confirmation == 'N':
        print('Boo - please start over.')
    else: 
        print('Please enter Y or N')
        user_confirmation = input(f'Please confirm your trip. Y to confirm, N to decline. Destination: {final_trip[0]}, Transportation: {final_trip[1]}, Entertainment: {final_trip[2]}, Restaurant: {final_trip[3]}')

#define lists/data for each input
destinations = ['Chicago', 'Wisconsin Dells', 'Devil\'s Lake', 'Johnson Creek', 'Door County']
transportations = ['Car', 'Bike', 'Bus', 'Train']
entertainments = ['Hiking', 'Shopping', 'Swimming', 'Touring Winieries']
restaurants = ['Joe\'s Pizza', 'Joe\'s Chinese', 'Joe\'s Burgers', 'Joe\'s Greek', 'Joe\'s Tacos', 'Joe\'s Pasta']

#define a list to hold the final trip option values
daytrip_items = []

#generate initial recommendations for user
initial_destination = generate_random_option(destinations)
initial_transportation = generate_random_option(transportations)
initial_entertainment = generate_random_option(entertainments)
initial_restaurant = generate_random_option(restaurants)

#confirm destination (if declined, regeneration a random option)
final_destination = user_confirm_option(initial_destination, destinations, 'destination')
daytrip_items.append(final_destination)

#confirm transportation (if declined, regeneration a random option)
final_transportation = user_confirm_option(initial_transportation, transportations, 'transportation')
daytrip_items.append(final_transportation)

#confirm entertainment (if declined, regeneration a random option)
final_entertainment = user_confirm_option(initial_entertainment, entertainments, 'entertainment')
daytrip_items.append(final_entertainment)

#confirm restaurant (if declined, regeneration a random option)
final_restaurant = user_confirm_option(initial_restaurant, restaurants, 'restaurant')
daytrip_items.append(final_restaurant)

#confirm the whole trip with the user - if they approve, print the trip description, if they decline, tell them to start over
confirm_trip(daytrip_items)
