# 100 Day Coding Challenge - Day 4: Data Cleaning Exercise

## Introduction

Video games have been one of my favorite hobbies since I first played Crash Bandicoot 2 on the original PlayStation when I was 4 years old. Since playing Crash Bandicoot 2, I have seen and played games that ranged from the weird camera angles Resident Evil used to the dazzling visuals like Red Dead Redemption 2. As games have evolved, so has the need to analyze sales and review trends so developers and publishers can assess performance and determine future project demands. My interest in video gaming has gone beyond playing my favorite games like Cyberpunk 2077, Grand Theft Auto, and Battlefield. It has included an interest in seeing how we can make insights out of video game sales and review data.

## Background

This project will pull a video game dataset (developed by Ghassen Khaled) with the intent of cleaning the data to make it useful for future insight and analysis.

## Tools I Used

* <b> Python </b> - the foundation of my project, used to define and execute the loan payment calculations efficiently and accurately.
* <b> VSCode </b> - the code editor for developing and managing the project environment.
* <b> Juypter Notebook </b> - an extension used quick testing and exploration.
* <b> Pandas </b> - the Python library used for reading and cleaning the dataset for analysis.
* <b> Git and Github </b> - essential for version control, project tracking, and collaboration.

## The Analysis

The following code was developed to perform the hotel KPI calculations for this project:

```Python
# import libaries
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import csv
```

```Python
# Read and display the video game dataset
df = pd.read_csv('../raw_vg_data/Video_Games.csv')
df.head()
```

```Python
# display information about the dataset and raw records
raw_df = len(df)
df.info()
print(f'\n Total Raw Records: {raw_df}')
```

```Python
# Clean the dataset

# Remove names with missing values - unable to analyze missing title names
df.dropna(subset=['Name'], inplace=True)

# Remove years and publishers with missing values - unable to analyze missing year or publisher
df.dropna(subset=['Year_of_Release', 'Publisher'], inplace=True)

# Remove ratings and developer columns - unable to analyze missing ratings and developer info
df.drop(columns=['Rating', 'Developer'], inplace=True)

# Make the year_of_release column into an integer type - years should be whole numbers
df['Year_of_Release'] = df['Year_of_Release'].astype(int)

# Remove any duplicate records - a title and its platform should be unique
df.drop_duplicates(inplace=True)

# Display cleaned dataset information
cleaned_df = len(df)
df.info()

print()
print('--- Cleaned Dataset Preview ---')
print(f'\n Total cleaned records: {cleaned_df}')
print(f'\n Total records removed: {raw_df - cleaned_df}')
print(f'\n Percentage of raw records removed: {((raw_df - cleaned_df) / raw_df) * 100:.2f}%')
```

```Python
# Display cleaned dataset information
platforms = df['Platform'].nunique()
publishers = df['Publisher'].nunique()
genres = df['Genre'].nunique()

print(f'\n --- Video Game Sample Summary ---')
print(f'\n Total platforms (consoles): {platforms}')
print(f'\n Total publishers: {publishers}')
print(f'\n Total genres: {genres}')
```

```Python
# Create CSV folder and extract datasets

# --- Descriptive Data Dataset - Remove Review Ratings---

# Drop critic and user review count and score columns
VG_descriptive = df.drop(columns=['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count'])

# Save cleaned sales dataset to CSV
VG_descriptive.to_csv('../cleaned_vg_data/VG_Descriptive_Cleaned.csv', index=False)

print('Dataset has been cleaned and extracted to cleaned_vg_data folder.')
```

```Python
# --- Review Ratings Dataset - Considers Games with Review Ratings ---

# Remove records without critic or review data
VG_reviews = df.dropna(subset=['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count'])

# Display cleaned review dataset
VG_reviews_clean = len(VG_reviews)
VG_reviews.info()

print()
print('--- Cleaned VG Review Dataset Preview ---')
print(f'\n Total cleaned review records: {VG_reviews_clean}')
print(f'\n Total records removed for VG reviews: {raw_df - VG_reviews_clean}')
print(f'\n Percentage of raw records removed: {((raw_df - VG_reviews_clean) / raw_df) * 100:.2f}%')

# Save cleaned review dataset to CSV
VG_reviews.to_csv('../cleaned_vg_data/VG_Reviews_Cleaned.csv', index=False)
print()
print('Dataset has been cleaned and extracted to cleaned_vg_data folder.')
```

### Data Cleaning and Preparation Summary

The raw dataset consisted of 16,719 entries. Through the data cleaning process, the following refinements were implemented to improve accuracy and consistency:
* Removed incomplete records without:
    * A title name
    * A release year or publisher name
* Dropped columns that had excessive null values:
    * ESRB Ratings
        * For future projects, the ESRB ratings may not provide direct analytical value
    * Developers
        * Typically, video games have a developer
        * The raw dataset contained only 10,096 non-null records
        * For the best interest of future projects, it was decided to remove the developer column 
    * Converted the release year from a ```float``` to a ```integer``` for improved data type consistency
    * Removed duplicates to eliminate redundancy

After processing, 303 records (or 1.81%) of the original dataset records were removed.

### Dataset Structuring

After further review of the dataset, significant gaps were identified with the critic/user scores and critic/user count fields. Rather than discarding these records or removing the null values, the dataset was strategically segmented into two purpose-driven datasets:
1. Descriptive Dataset
    * Focused on sales information categorized by the publisher, genre, and platform
2. Reviewed Dataset
    * Focused on sales performance relative to critic and user scores and review counts

This dual-structure design enables flexible pathways, allowing stakeholders to explore trends through a market composition perspective (descriptive) or sentiment and quality perspective (review). Notably, the review-focused dataset experienced a significant size reduction. 9,826 records were removed (or 58.77%) from the raw dataset (due to missing review data). Future projects using the review-focused dataset will make note of these limitations.

### Descriptive Dataset Key Metrics

For the descriptive dataset, the following categorical values were validated:
* Total Platforms (Consoles): 31
* Total Publishers: 579
* Total Genres: 12

These categories provide a rich foundation for future projects exploring sales performance across platforms, publishers, and genres, which may support targeted insights and business intelligence use-cases.

## Conclusion
This project reinforced key Python and data-cleaning concepts, including removing null values, dropping non-essential columns, and segmenting data into separate data frames to address distinct analytical questions. Future projects may include:
* Analyzing sales trends across platforms, genres, and publishers using the descriptive dataset
* Investigating correlations between sales and review scores to identify performance drivers
* Investigating whether critic reviews influence user sentiment and uncovering potential relationships between critic and player perspectives

