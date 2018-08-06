import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = str(input('Data from which of the following cities would you like to analyze? Chicago, New York City, or Washington?\n')).lower()
        if city not in CITY_DATA.keys():
            print('Sorry, you have input an invalid city, please try again.\n')
            continue
        else: 
            break
    
    # get user input for month (all, january, february, ... , june)
    
    while True:
        month = str(input('Data from what month would you like to analyze? January, February, March, April, May, June or All?\n')).lower()
        if month not in months:
            print('Sorry, you have input an invalid month, please try again.\n')
            continue
        else: 
            break     
           
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = str(input('Data from what day of the week would you like to analyze? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All.\n')).lower()
        if day not in days:
            print('Sorry, you have input an invalid day, please try again.\n')
            continue
        else: 
            break      


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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df =  pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, hour, day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nThe most frequent month of travel is: {}'.format(months[df['month'].mode()[0]]))   

    # display the most common day of week
    print('\nThe most frequent day of the week travelled is: {}'.format(df['day_of_week'].mode()[0]))
    
    # display the most common start hour
    print('\nThe most frequent start hour is: {}'.format(df['hour'].mode()[0])) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nThe most frequent start station is: {}'.format(df['Start Station'].mode()[0])) 
    
    # display most commonly used end station
    print('\nThe most frequent end station is: {}'.format(df['End Station'].mode()[0])) 

    # display most frequent combination of start station and end station trip
    df['start_end_combo'] = df['Start Station'] + ' to ' + df['End Station']
    print('\nThe most frequent combination of start station and end station trip is: {}'.format(df['start_end_combo'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = ((df['Trip Duration'].sum()/60)/60)
    print('\nTotal travel time for this time period is: {}'.format(round(total_travel,2)))

    # display mean travel time
    mean_travel = ((df['Trip Duration'].mean()/60)/60)
    print('\nThe mean travel time is: {} hours'.format(round(mean_travel,2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print (pd.value_counts(df['User Type'].values))
    
    print ('\n')    

    # Display counts of gender
    if 'Gender' in df.columns:
        print (pd.value_counts(df['Gender'].values))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe eldest person to use the bikeshare was born in: {}'.format(int(df['Birth Year'].min()))) 
        print('\nThe youngest person to use the bikeshare was born in: {}'.format(int(df['Birth Year'].max()))) 
        print('\nThe most common year of birth amongst bikesharers was: {}'.format(int(df['Birth Year'].mode()[0]))) 


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
