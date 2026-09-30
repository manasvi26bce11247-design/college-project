# Watch My Movie

## Movie Recommendation System

**Name:** Manasvi Jain  
**Reg No.:** 26BCE11247  
**Branch:** B.Tech Computer Science  
**College:** VIT Bhopal University  

## About the Project

Watch My Movie is a simple Python-based movie recommendation system. It helps users find movies from a movie dataset based on their interests.

The project provides three main options. Users can get movie recommendations based on genres, search for information about a particular movie, and find movies according to a selected rating.

## Features

- Recommend movies based on one, two, or three genres.
- Search for a particular movie.
- Display the genre and rating of a movie.
- Recommend movies based on a given rating.
- Store search and recommendation records in CSV files.
- Handle incorrect inputs and movies that are not found.

## How It Works

The project uses a movie dataset stored in a CSV file. Pandas is used to read the dataset and filter the required movies.

When the program starts, the user is shown a menu. The user can select the required option and enter the necessary information.

For genre recommendations, the program checks the selected genres and displays matching movies.

For movie searches, the program looks for the entered movie name and shows its available information.

For rating-based recommendations, the program checks the rating entered by the user and displays movies having the matching rating.

## Technologies Used

- Python
- Pandas
- CSV files
- Command Line Interface

## Project Structure

The project mainly contains the Python program, the movie dataset, and CSV files used for storing records.

The system is divided into different functions so that each part of the program can handle a specific task.

## Dataset Used
https://www.kaggle.com/datasets/chaitanyahivlekar/large-movie-dataset

## Testing

The program was tested using different inputs and situations.

The menu options were tested to make sure each option works correctly. Different genres were entered to check movie recommendations. Movie names were searched to check whether their information was displayed properly. Ratings were also entered to check rating-based recommendations.

Invalid inputs were tested to make sure the program does not stop unexpectedly.

## Challenges

Some of the main challenges during the project were handling multiple genre selections, searching movie names without depending on exact capitalization, managing CSV files, and handling invalid user input.

Keeping the different operations separated into simple functions also helped make the program easier to understand.

## Learning Outcomes

This project helped in understanding Python functions, loops, conditions, user input, and exception handling.

It also provided practical experience with Pandas, CSV files, filtering datasets, and creating a simple command-line application.

## Future Improvements

In the future, the project can be improved by adding a graphical or web interface. A better movie search system can also be added.

The recommendation system could use more factors such as genre and rating together. More detailed movie information, user profiles, and personalised recommendation history could also be included.

## Conclusion

Watch My Movie is a simple movie recommendation system that demonstrates the use of Python and Pandas to solve a practical problem. It provides an easy way for users to search for movies and get recommendations based on genres and ratings.
