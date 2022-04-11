import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
menu = [('yes'), ('no')]
citys = [('chicago'), ('new york city'), ('washington')]
months = [('january'), ('february'), ('march'), ('april'), ('may'),
          ('june'), ('all')]
days = [('saturday'), ('sunday'), ('monday'), ('tuesday'), ('wednesday'),
        ('thursday'), ('friday'), ('all')]


def welcome_msg():
    """
    Gets the client name

    faction will loop if client input a number
    Returns:
        The the name from user input
    """
    print("Hello , Welcome to US biker-share program please enter your name ")
    while True:
        temp = input().casefold().title()
        if not temp.isnumeric():
            print(f"Hello {temp} ,I hope you have a lovely day .")
            print()
            break
        else:
            print("sorry i didn't get that please enter a valid name  ")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city_choice - name of the city to analyze
        (str) month_choice - name of the month to filter by, or"all" to apply no month filter
        (str) day_choice- name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Wooo hooo Let\'s explore some US bike-share data!')
    print()
    # ask the user for the city he would like to show it's data.
    while True:
        print("Please enter a number for the city you would like from the list below:")
        for index, city in enumerate(citys):
            print(f"{index + 1}: {city}")
        try:
            choice_1 = int(input())
            if 1 <= choice_1 <= len(citys):
                city_choice = citys[choice_1 - 1]
                break
            else:
                print("Sorry invalid choose ,please try again ")
        except:
            print("Please enter a number between 1 and 3 ")
    # ask user if he would like to filter by month .
    while True:
        print(' Would you like to filter the data by month ?: ')
        for index, value in enumerate(menu):
            print(f"{index + 1}: {value}")
        try:
            answer_1 = int(input())
            if 1 <= answer_1 <= len(menu):
                answer_choice = menu[answer_1 - 1]
                month_choice = 'all'
                break
            else:
                print("Sorry invalid choose ,please try again ")
        except:
            print("Please enter a number between 1 and 2. ")
    # ask the user of which month he want to filter .
    while answer_choice != 'no':
        print("Please choose the month you would like from the list below :")
        for index, month in enumerate(months):
            print(f"{index + 1}: {month}")
        try:
            choice_m = int(input())
            if 1 <= choice_m <= len(months):
                month_choice = months[choice_m - 1]
                break
            else:
                print("Sorry invalid choose ,please try again ")
        except:
            print("Please enter a number between 1 and 7. ")

    # ask user if he would like to filter by day .
    while True:
        print(' Would you like to filter the data by day ? ')
        for index, value in enumerate(menu):
            print(f"{index + 1}: {value}")
        try:
            answer_2 = int(input())
            if 1 <= answer_2 <= len(menu):
                answer_2choice = menu[answer_2 - 1]
                day_choice = 'all'
                break
            else:
                print("Sorry invalid choose ,please try again ")
        except:
            print("Please enter a number between 1 and 2. ")
    # ask the user of which day he want to filter .
    while answer_2choice != 'no':

        print("Please choose the month you would like from the list below :")
        for index, day in enumerate(days):
            print(f"{index + 1}: {day}")
        try :
            choice_day = int(input())
            if 1 <= choice_day <= len(days):
                day_choice = days[choice_day - 1]
                break
            else:
                print("Sorry invalid choose ,please try again ")
        except:
            print("Please enter a number between 1 and 8.")

    print('-' * 40)
    return city_choice, month_choice, day_choice


def load_data(city_choice, month_choice, day_choice):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city_choice - name of the city to analyze
        (str) month_choice - name of the month to filter by, or "all" to apply no month filter
        (str) day_choice - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city_choice])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month_choice != 'all':
        # use the index of the months list to get the corresponding int
        months_1 = ['january', 'february', 'march', 'april', 'may', 'june']
        month_choice = months_1.index(month_choice) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_choice]

    # filter by day of week if applicable
    if day_choice != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_choice.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()[0]
    print('The most Popular month is :', popular_month)

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('the Most Popular day of week is :', popular_day_of_week)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Popular Start Hour is :', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The Most Popular start station is :', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The Most Popular end station is :', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' -to- ' + df['End Station']
    trip = df['Trip'].mode()[0]
    print(f"The most popular trip is:{trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in int (hours, minutes) and flot(seconds)
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_hours = int(total_travel_time // 3600)
    total_travel_time_mins = int((total_travel_time % 3600) // 60)
    total_travel_time_sec = round((total_travel_time % 60), 5)
    print(f"The total travel time is {total_travel_time_hours} hours,"
          f" {total_travel_time_mins} minutes "
          f"and {total_travel_time_sec} seconds ")

    # display mean travel in int(hours, minutes) and flot(seconds)
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_hours = int(mean_travel_time // 3600)
    mean_travel_time_mins = int((mean_travel_time % 3600) // 60)
    mean_travel_time_sec = round((mean_travel_time % 60), 5)
    print(f"The average travel time is {mean_travel_time_hours} hours,"
          f" {mean_travel_time_mins} minutes "
          f"and {mean_travel_time_sec} seconds ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    


def user_stats(df):
    """Displays statistics on bike-share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print()

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
        print()
    else:
        print()
    
    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print('The earliest year of birth  :', earliest_year_of_birth)
        mostrecent_year_of_birth = int(df['Birth Year'].max())
        print('The most recent year of birth  :', mostrecent_year_of_birth)
        mostcommon_year_of_birth = int(df['Birth Year'].mode()[0])
        print('The most common year of birth  :', mostcommon_year_of_birth)
    else:
        print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw(df):
    """ Displays 5 rows from the data according to user input ."""

    # ask user if he want to show more raw data
    while True:
        print(' \nWould you like to display more raw data ?:\n ')
        for index, value in enumerate(menu):
            print(f"{index + 1}: {value}")
        try:
            answer_3 = int(input())
            if 1 <= answer_3 <= len(menu):
                answer_choice3 = menu[answer_3 - 1]
                if answer_choice3 != 'no':
                    pd.set_option('display.max_columns', 200)
                    print(df.sample(5))
                else:
                    break
            else:
                print("Sorry invalid choose ,please try again ")
        except:
            print("Please enter a number between 1 and 2 ")


def one_more_time():
    """
    Asking the user if he would like to restart the program again for more information and some fun
    or he had enough for today
    """

    # ask user if he want restart the program or not.
    print(' Would you like to restart the program ?: ')
    for index, value in enumerate(menu):
        print(f"{index + 1}: {value}")
    try:
        answer_4 = int(input())
        if 1 <= answer_4 <= len(menu):
            answer_choice4 = menu[answer_4 - 1]
            if answer_choice4 != 'yes':
                ending_msg("=")
                ending_msg("Made by:Ahmed Soliman.")
                ending_msg("Udacity Data_analyst nanodegree.")
                ending_msg("Project 1.")
                ending_msg("US biker-share program.")
                ending_msg(f"Thanks for your time ,take care and see you soon . ")
                ending_msg("=")
            else:
                main()
        else:
            print("Sorry invalid choose ,please try again ")
    except:
        print("Please enter a number between 1 and 2 ")


def ending_msg(txt, wide=80):
    """
    Displays text in specific format
    Args:
        txt: The text to apply format on .
        wide: the screen wide that hold the text

    Returns: None

    """
    if txt == "=":
        print("=" * wide)
    else:
        txt = txt.center(wide - 6)
        formatted_txt = f"==={txt}==="
        print(formatted_txt)


def main():
    while True:
        welcome_msg()
        city_choice, month_choice, day_choice = get_filters()
        df = load_data(city_choice, month_choice, day_choice)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)
        one_more_time()
        break


if __name__ == "__main__":
    main()
