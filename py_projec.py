import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).Using a while loop with exception handling  for invalid inputs
    while True:
        try:
            city=str(raw_input("Enter a city , select from: chicago, new york city, washington: ")).lower()
            break
        except ValueError:
            print("that is not a valid input")
        except KeyboardInterrupt:
            print("No input taken")
            break

    #get user input for month (all, january, february, ... , june)
    month=str(raw_input("choose which month to enter (january, february, ... , june) or choose all :" )).lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=str(raw_input("choose which day of week to enter (monday, tuesday, ... sunday) or choose all: ")).lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    popular_month=df['month'].mode()[0]
    print("the most common start hour: ",popular_month)

    # display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print("the most common start hour: ",popular_day)

    #display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print("the most common start hour: ",popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_Start_station= df['Start Station'].mode()[0]
    print("most commonly used start station: ",common_Start_station)

    # display most commonly used end station
    common_End_station= df['End Station'].mode()[0]
    print("most commonly used end station: ",common_End_station)


    # display most frequent combination of start station and end station trip
    Start_End_station= df['Start Station'] + df['End Station']
    common_Start_End_station= Start_End_station.mode()[0]
    print("most commonly used start and end station: ",common_Start_End_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("The total travel time",total_travel_time)

    # display mean travel time
    Average_travel_time=df['Trip Duration'].mean()
    print("The average travel time",Average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types =df['User Type'].value_counts()
    print("counts of user types: ",user_types)
    # TO DO: Display counts of gender
    print("values of gender",df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    earliest_BD = min(df['Birth Year'])
    print("Earliest birth date is: ",earliest_BD)
    recent_BD = min(df['Birth Year'])
    print("Most recent birth date is: ",earliest_BD)
    common_BD = df['Birth Year'].mode()
    print("common birth date is: ",common_BD)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_input_display=input('\nWould you like to display raw input? Enter yes or no.\n')
        if raw_input_display.lower() == 'yes':
                print("first five rows of raw data:",df.head())
        else:
                 break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
