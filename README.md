# Exploring-US-Bikeshare-Data


## Project Details

*  Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles for short trips, typically 30 minutes or less. Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

*  In this project, I will perform an exploratory analysis on data provided by [Motivate](https://www.motivateco.com/), a bike-share system provider for many major cities in the United States. You will compare the system usage between three large cities: New York City, Chicago, and Washington, DC. You will also see if there are any differences within each system for those users that are registered, regular users and those users that are short-term, casual users.



## The Datasets

*   In this project, we will focus on the record of individual trips taken in 2016 
    from our selected cities: **(New York City, Chicago, and Washington)**. Each of these cities has a page where we can freely download the trip data :

 1.   [New York City Data](https://ride.citibikenyc.com/system-data)

 2.    [Chicago](https://ride.divvybikes.com/system-data) 

 3.    [Washington](https://ride.capitalbikeshare.com/system-data) 


*   If you visit these pages, you will notice that each city has a different way of delivering its data. Chicago updates with new data twice a year, Washington DC is quarterly, and New York City is monthly.


*   Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

  Start Time (e.g., 2017-01-01 00:07:57)

  End Time (e.g., 2017-01-01 00:20:53)

  Trip Duration (in seconds - e.g., 776)

  Start Station (e.g., Broadway & Barry Ave)

  End Station (e.g., Sedgwick St & North Ave)

  User Type (Subscriber or Customer)

  **The Chicago and New York City files also have the following two columns:**
  
   **Gender**
 
   **Birth Year** 


*    **Note:** The original files are much larger and messier . These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns 
   ,You can contact me to get them,the cleaned 3 data sets that I worked on for this project
 


## Statistics Computed

1.    Popular times of travel (i.e., occurs most often in the start time)

 *   most common month

 *   most common day of week

 *   most common hour of day

2. Popular stations and trip

 *   most common start station

 *   most common end station

 *   most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

 *   total travel time

 *   average travel time

4. User info

 *   counts of each user type

 *   counts of each gender (only available for NYC and Chicago)

 *   earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Packages
 
python 3.8.10  
numpy	1.21.4	/
pandas	1.3.4	  
pip	21.1.2	   
python-dateutil	2.8.2  
pytz	2021.3  
setuptools	57.0.0  	/
six	1.16.0 / 	
wheel	0.36.2  /




## resources :

wikihow.com

wikipedia.org

python.org/doc/

python.org/dev/peps/pep-0008/#tabs-or-spaces

pandas.pydata.org/pandas-docs/stable/reference/index.html

w3schools.com/python/python_reference.asp

nfpdiscussions.udacity.com

Data Analysis  Nanodegree Program - Udactiy.
