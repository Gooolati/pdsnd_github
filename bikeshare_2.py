import time
import pandas as pd
import numpy as np
import random


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#function to obtain inputs from user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = 'something'
    
    while (city not in CITY_DATA.keys()):
        city = str(input('Would you like to see data for Chicago, New York City, or Washington?\n')).lower()

    # get user input for month (all, january, february, ... , june)
    monthArr = np.arange(-1, 7, 1)
    month = 14
    
    while (month not in monthArr):
        try:
            month = int(input('\nWhich month? Please type your response as an integer (e.g., 1 = January), to see all months, please enter 0: \n'))
        except:
            continue
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = 10
        
    while (day not in np.arange(0, 8)):
        try:
            day = int(input('\nWhich day? Please type your response as an integer (e.g., 1 = Sunday), to see all days, please enter 0: \n'))
        except:
            continue
    
    
    print('-'*40)
    return city, month, day

#applies user's filters to data
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
    
    
    #declares DF for csv that user chose
    if (city == 'chicago'):
        df = pd.read_csv(r'D:\MFE Prep\PDSND\Project2 Files\bikeshare-2\chicago.csv')
    elif (city == 'new york city'):
        df = pd.read_csv(r'D:\MFE Prep\PDSND\Project2 Files\bikeshare-2\new_york_city.csv')
    elif (city == 'washington'):
        df = pd.read_csv(r'D:\MFE Prep\PDSND\Project2 Files\bikeshare-2\washington.csv')
    
    df['Month'] = pd.to_datetime(df['Start Time']).dt.month
    df['Day'] = pd.to_datetime(df['Start Time']).dt.day
    
    #leave out month/day filter if user selected all
    if (month != 0):
        df = df[(df.Month == month)]
    if (day != 0):
        df = df[(df.Day == day)]
          

    return df


#gets time stats of filtered data
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Month'] = pd.to_datetime(df['Start Time']).dt.month
    df['Day'] = pd.to_datetime(df['Start Time']).dt.day    
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour  
    
    # display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Most Common Month: \n' + str(most_common_month))
    
    # display the most common day of week
    most_common_day = df['Day'].mode()[0]
    print('\nMost Common Day: \n' + str(most_common_day))

    # display the most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print('\nMost Common Hour: \n' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#gets station stats of filtered data
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('Most Common Start Station: ' + str(most_common_start))
    
    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('Most Common End Station: ' + str(most_common_end))

    # display most frequent combination of start station and end station trip
    df2 = df['Start Station'].map(str) + '--' + df['End Station'].map(str)
    most_common_combo = df2.mode()[0].split('--')
    print('\nMost Common Combo of Start Station and End Station: ')
    print('Start: ' + str(most_common_combo[0] + '; End: ' + str(most_common_combo[1]) + '\n'))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#gets trip stats for filtered data
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time: ' + str(total_time) + ' Days')
    
    # display mean travel time
    mean_time = round(df['Trip Duration'].mean(), 2)
    print('\nAverage Travel Time: ' + str(mean_time) + ' Days')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#gets user stats for filtered data
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of Each User Type: \n')
    print(df.groupby('User Type')['User Type'].count())

    if ('Gender' in df.keys()):
        # Display counts of gender
        print('\nCount of Each Gender: \n')
        print(df.groupby('Gender')['Gender'].count())
    else:
        print('\nGender Info Not Available')

    if ('Birth Year' in df.keys()):
        # Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        print('\nEarliest Birth Year: ' + str(earliest))
    
        recent = int(df['Birth Year'].max())
        print('Most Recent Birth Year: ' + str(recent))
        
        common = int(df['Birth Year'].mode()[0])
        print('Most Common Birth Year: ' + str(common))
    else:
        print('\nBirth Year Info Not Available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#run script with user inputs
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        view_date = input('\nWould you like to view data for 5 individual trips? Enter yes or no. \n')
        
        while (view_date.lower() != 'no'):
            random_int = random.randrange(len(df))
            print(df.iloc[random_int : random_int + 5])
            view_date = input('\nWould you like to view data for another 5 individual trips? Enter yes or no. \n')


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
 	main()
