import random

#introduction - welcomes users and explains the application
def introduction():
    print('Welcome to the Wisconsin Day Trip Generator! I will generate a destination, mode of transportation, activity, and restaurant.') 
    print('Don\'t like an option? No problem! You can swap it out for another.')
    print('Let\'s get started!')

#generate the initial random options
def generate_random_option(list):
    option_index = random.randint(0, len(list) - 1) 
    option = list[option_index]
    return option

#get final option & approval from user - including regeneration of options if they do not approve
def user_confirm_option(initial_option, list, list_type):
    option = initial_option
    option_index = list.index(option)
    user_approval = ''
    approval = False
    print(f'The {list_type} we have picked for you is {option}')
    user_approval = input("Do you approve? Y/N ").upper() 
    if user_approval != 'N' and user_approval != 'Y': 
            print('Please enter Y or N. Regenerating option...')
    elif user_approval == 'Y':
        approval = True
    while approval == False:
        popped_value = list.pop(option_index)
        option_index = random.randint(0, len(list) - 1)
        option = list[option_index]
        list.append(popped_value)
        print(f'The {list_type} we have picked for you is {option}')
        user_approval = input("Do you approve? Y/N ").upper()
        if user_approval == 'Y':
            approval = True
    return option

#confirm trip. if user confirms, print the final itinerary, if they do not confirm, prompt them to start over
def confirm_trip(final_trip):
    confirmed_status = False
    while confirmed_status == False:
        user_confirmation = input(f'Please confirm your trip details. Destination: {final_trip[0]}, Transportation: {final_trip[1]}, Entertainment: {final_trip[2]}, Restaurant: {final_trip[3]}. Y to confirm, N to decline. ').upper()
        if user_confirmation != 'N' and user_confirmation != 'Y': 
            print('Please enter Y or N')
        elif user_confirmation == 'Y':
            print('Thank you for confirming.')
            print(f'Your destination is {final_trip[0]} where you will arrive by {final_trip[1]}. While in {final_trip[0]}, you will enjoy your day by {final_trip[2]} and finish the day with a meal at {final_trip[3]}.')
            confirmed_status = True
        elif user_confirmation == 'N':
            print('Sorry to hear you didn\'t confirm, please start over to generate a new trip.')
            confirmed_status = True

def run_daytrip_generator():
    introduction()
    #generate initial recommendations for user
    initial_destination = generate_random_option(destinations)
    initial_transportation = generate_random_option(transportations)
    initial_entertainment = generate_random_option(entertainments)
    initial_restaurant = generate_random_option(restaurants)
    #confirm destination (if declined, regenerate a new random option)
    final_destination = user_confirm_option(initial_destination, destinations, 'destination')
    daytrip_items.append(final_destination)
    #confirm transportation (if declined, regenerate a new random option)
    final_transportation = user_confirm_option(initial_transportation, transportations, 'transportation')
    daytrip_items.append(final_transportation)
    #confirm entertainment (if declined, regenerate a new random option)
    final_entertainment = user_confirm_option(initial_entertainment, entertainments, 'entertainment')
    daytrip_items.append(final_entertainment)
    #confirm restaurant (if declined, regenerate a new random option)
    final_restaurant = user_confirm_option(initial_restaurant, restaurants, 'restaurant')
    daytrip_items.append(final_restaurant)
    #confirm the whole trip with the user - if they approve, print the trip description, if they decline, tell them to start over
    confirm_trip(daytrip_items)


#define lists/data for each input
destinations = ['Chicago', 'Wisconsin Dells', 'Devil\'s Lake', 'Johnson Creek', 'Door County']
transportations = ['Car', 'Bike', 'Bus', 'Train', 'Foot', 'Horse', 'Dogsled']
entertainments = ['Hiking', 'Shopping', 'Swimming', 'Touring Winieries']
restaurants = ['Joe\'s Pizza', 'Joe\'s Chinese', 'Joe\'s Burgers', 'Joe\'s Greek', 'Joe\'s Tacos', 'Joe\'s Pasta', 'Joe\'s Steaks', 'Joe\'s Seafood']

#define a list to hold the final trip option values
daytrip_items = []

#run application
run_daytrip_generator()
