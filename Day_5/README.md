# 100 Day Coding Challenge - Day 5: Ranking SQL Query Executions

## Introduction

Data professionals are in high demand, according to the [Bureau of Labor Statistics](https://www.bls.gov/ooh/fastest-growing.htm). Organizations need data professionals to help make data-driven decisions, improve operations, and remain competitive. Industries that are typically competitive (technology, finance, hospitality, etc.) require strong, analytical minds to efficiently request data for powerful insights, and when there is high demand, there are lucrative compensation packages.

## Background

This project will take a dataset provided from [Luke Barousse's 'SQL For Data Analytics' course](https://www.lukebarousse.com/), which provides listings of various international data job postings from various job networking websites. For our analysis, we will focus on ranking data analysis, data scientist, data engineer, business analyst, and data engineer job categories, were posted in 2025, and rank those jobs based on average yearly salary.

## Tools I Used

* <b> SQL </b> - the foundation of my project, allowing me to query the database for critical insights using subqueries and ranking window functions.
* <b> VSCode </b> - the code editor for developing and managing the project environment.
* <b> PostgreSQL </b> - The database management system that was chosen for this project to handle the dataset.
* <b> Git and Github </b> - essential for version control, project tracking, and collaboration.

## The Analysis

The following SQL code was queried and executed to rank the top 25 paying data jobs in 2025:

```SQL
WITH unique_jobs AS (
    SELECT
        job_id,
        job_via AS job_posting_source,
        company_id,
        job_title_short AS job_category,
        job_title,
        salary_year_avg,
        job_posted_date,
        EXTRACT(YEAR FROM job_posted_date) AS year_posted,
        ROW_NUMBER() OVER (PARTITION BY job_title ORDER BY salary_year_avg DESC) as rank
    FROM
        job_postings_fact
    WHERE
        job_title_short IN ('Data Analyst', 'Data Scientist', 'Business Analyst', 'Data Engineer') AND
        salary_year_avg IS NOT NULL AND
        job_posted_date >= '2025-01-01'
)

SELECT
    RANK() OVER (ORDER BY salary_year_avg DESC) AS salary_rank,
    job_id,
    name AS company_name,
    job_posting_source,
    job_category,
    job_title,
    ROUND(salary_year_avg, 0) AS average_yearly_salary_$,
    EXTRACT(YEAR FROM job_posted_date) AS year_posted
FROM
    unique_jobs
LEFT JOIN company_dim ON unique_jobs.company_id = company_dim.company_id
WHERE
    rank = 1
ORDER BY
    salary_year_avg DESC
LIMIT 25;
```
### Top 25 Data Jobs based on Salary

Refer to the [executed output](https://github.com/loganangell/100_Days_of_Code/blob/main/Day_5/Rank_Output/top_25_paying_data_jobs.csv) for the top 25 paying data jobs in 2025. 

For the project, the following information was noted:
* The top 25 salaries derived from various well-known companies such as:
    * Netflix
    * ByteDance
    * Meta
    * Cisco
    * and more
* There appears to be a variety of job posting sources which include:
    * LinkedIn
    * Taro
    * ShowbizJobs
    * and more
* The salaries in the query ranged from $287,500 to $680,000
    * The highest paying job was a Data Scientist role with Netflix's Games Division
    * The lowest paying job in the query is for an AI & Product Director for Harnham

### Data Validation and Quality Insights

During the project, I initally used the following SQL query:

```SQL
SELECT
    RANK() OVER (ORDER BY salary_year_avg DESC) AS salary_rank,
    job_id,
    name AS company_name,
    job_title_short AS position,
    job_title AS full_job_title,
    job_location,
    ROUND(salary_year_avg, 0)  average_yearly_salary_$,
    EXTRACT(YEAR FROM job_posted_date) AS year_posted
FROM
    job_postings_fact
LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
WHERE
    job_title_short IN ('Data Analyst', 'Data Scientist', 'Business Analyst', 'Data Engineer') AND --filter if opportunities should be split up
    salary_year_avg IS NOT NULL AND
    job_posted_date >= '2025-01-01'
    -- AND job_location = 'Anywhere' -- uncomment this line for remote jobs
ORDER BY
    salary_year_avg DESC
LIMIT 25;
```
The output of the above query can be found in the [SQL_Unexpected_Result](https://github.com/loganangell/100_Days_of_Code/blob/main/Day_5/SQL_Unexpected_Result/SQL_Unexpected_Result.csv) folder. From evaluating the executed query, I noticed that Netflix's 'Privacy Engineer (L4), Data Protection' job was posted multiple times in Taro (although each instance had its own unique job ID). Out of caution and careful consideration, I have decided to develop a subquery that gives me unique job names to ensure no possible duplications are included in the results.

## Conclusion

This project reinforced key SQL concepts, including developing subqueries for easier data manipulation and retrieval, ranking records based on a specific criterion, and manipulating values such as rounding and extracting. Future projects may include:
* Ranking the average annual salaries a specific company is offering
* Finding specific job categories in a specific location (or remote)
* Comparing the highest paying job opportunities in 2024 against 2025