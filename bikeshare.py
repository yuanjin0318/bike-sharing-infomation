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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("***********************************************************************")
        city = input("\nPlease enter the name of the city to analyze, thanks very much!\n").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("\nThe entered name of the city is wrong. \n")
            continue
        else: 
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        print("***********************************************************************")
        month = input ("\nPlease enter name of the month to filter by, or \'all\' to apply no month filter, thanks very much!\n").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
             print("\nThe entered month to filter is wrong. \n")
             continue
        else: 
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print("***********************************************************************")
        day = input ("\nPlease enter name of the day of week to filter by, or \'all\' to apply no day filter, thanks very much!\n").lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']:
             print("\nThe entered day of week to filter is wrong. \n")
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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("The most common month is: ", months[popular_month-1].title())

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]                  
    print("The most common day is: ", popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]                  
    print("The most common hour is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #print(df)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].value_counts().idxmax()                  
    print("The most common start station is: ", popular_station)


    # TO DO: display most commonly used end station
    popular_station_end = df['End Station'].value_counts().idxmax()                   
    print("The most common end station is: ", popular_station_end)


    # TO DO: display most frequent combination of start station and end station trip
    df['combine'] =  df['Start Station'] + ' to ' + df['End Station']
    popular_combine = df['combine'].mode()[0]
    print("The most combination is from ", popular_combine)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #noprint(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total trip duration time is: %.2f min"%(total_time/60))


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is: %.2f min"%(mean_time/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types is:\n',df['User Type'].value_counts())


    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """Displays the data."""
    print( "****************************************************************")
    show_or_not = input("\nDo you want to see raw data? Please type \'yes\' or \'no\' \n").lower()
    
    i = 0
    while show_or_not != 'no':
        if show_or_not not in ['no', 'yes']:
            show_or_not = input("\nPlease enter \'yes\' or \'no\'\n").lower()
            continue
        elif show_or_not == 'yes':
            print(df.iloc[i:i+5])
            show_or_not = input("\nDo you want to see more 5 lines of raw data?\n").lower()
            i += 5
               
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nHello, would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
