import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Valid_City = ['chicago','new york city', 'washington','all']
Valid_Month = ["january", "february", "march", "april", "may", "june", "all"]
Valid_Dayofweek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Please type the city name you want to analyze: ").lower()
        if city in Valid_City:
            break
        else:
            print("Please only choose from 'chicago','new york city', 'washington'")
    while True:
        month = input("Please type the month you want to analyze, or type 'all' if you don't need a filter: ").lower()
        if month in Valid_Month:
            break
        else:
            print("Please only choose from 'january', 'february', 'march', 'april', 'may', 'june'")
    while True:
        day = input("Please type the day of week you want to analyze, or type 'all' if you don't need a filter: ").lower()
        if day in Valid_Dayofweek:
            break
        else:
            print("Please only choose from 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday'")
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
            df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['dayofweek'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.month
    # display the most common month
    popular_month = df['month'].mode()[0]
    print("\nThe most common month is:", popular_month)
    # display the most common day of week
    popular_dayofweek = df['dayofweek'].mode()[0]
    print("\nThe most common day of week is:", popular_dayofweek)
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("\nThe most common hour is:", popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most common used start station is:", popular_start_station)
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most common used end station is:", popular_end_station)
    # display most frequent combination of start station and end station trip
    df['station_combi'] = df['Start Station']+' to '+df['End Station']
    popular_combi_station = df['station_combi'].mode()[0]
    print("\nThe most common combincation of start and end station trip is:", popular_combi_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("\nThe total travel time is:", total_travel_time)
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("\nThe mean travel time is:", mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe counts of user types is:", user_types)
    # Display counts of gender
    try:
        df['Gender'].fillna('No Data',inplace=True)
    except:
        print("\nThere's no gender data in the selected city")
    else:
        gender = df['Gender'].value_counts()
        print("\nThe counts of gender is:", gender)
#     Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min().astype(int)
        recent_year= df['Birth Year'].max().astype(int)
        common_year= df['Birth Year'].mode()[0].astype(int)
    except:
        print("\nThere's no year of birth data in the selected city")
    else:
        print("\nThe earliest year of birth is:", earliest_year,"\nThe most recent year of birth is:", recent_year,"\nThe most common year of birth is:", common_year)
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
        
        lower_bound = 0
        upper_bound = 5
        while True:
            raw_input = input('\nWould you like to see more individual data? Enter yes or no to proceed.\n')
            if raw_input == 'yes':
                print(df.iloc[lower_bound:upper_bound, 0:])
                lower_bound += 5
                upper_bound += 5
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no to proceed.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

    