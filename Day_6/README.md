# 100 Day Coding Challenge - Day 5: Ranking SQL Query Executions

## Introduction

Data professionals are in high demand, according to the [Bureau of Labor Statistics](https://www.bls.gov/ooh/fastest-growing.htm). Organizations require data professionals to inform data-driven decisions, enhance operations, and maintain competitiveness. Industries that are typically competitive (technology, finance, hospitality, etc.) require strong, analytical minds to efficiently request data for powerful insights. When there is high demand, there are lucrative compensation packages.

## Background

This project will take a dataset provided from [Luke Barousse's 'SQL For Data Analytics' course](https://www.lukebarousse.com/), which provides the top ten paying companies based on average salary, as well as provides the minimum and maximum salaries for the specific company.

## Tools I Used

* <b> SQL </b> - the foundation of my project, allowing me to query the database for critical insights using subqueries and ranking window functions.
* <b> VSCode </b> - the code editor for developing and managing the project environment.
* <b> PostgreSQL </b> - The database management system that was chosen for this project to handle the dataset.
* <b> Git and Github </b> - essential for version control, project tracking, and collaboration.

## The Analysis

The following SQL code was queried and executed to rank the top 25 paying data jobs in 2025:

```SQL
WITH postings_2025 AS (
    SELECT
        j.company_id,
        c.name AS company_name,
        j.job_title_short,
        j.job_title,
        j.salary_year_avg,
        j.job_id
    FROM
        job_postings_fact AS j
    JOIN
        company_dim AS c ON j.company_id = c.company_id
    WHERE
        j.salary_year_avg IS NOT NULL AND
        j.job_title_short IN ('Data Analyst', 'Data Scientist', 'Business Analyst', 'Data Engineer') AND
        j.job_posted_date >= DATE '2025-01-01'
),
company_info AS (
    SELECT
        company_id,
        company_name,
        AVG(salary_year_avg) AS avg_salary,
        COUNT(DISTINCT job_id) AS posting_count,
        COUNT(DISTINCT job_title) AS job_title,
        MIN(salary_year_avg) AS min_salary,
        MAX(salary_year_avg) AS max_salary
    FROM
        postings_2025
    GROUP BY
        company_id, company_name
),
ranked AS (
    SELECT *,
    DENSE_RANK() OVER (ORDER BY avg_salary DESC) AS avg_salary_rank
    FROM company_info
)

SELECT
    avg_salary_rank,
    company_name,
    ROUND(avg_salary, 2) AS avg_salary,
    min_salary,
    max_salary
FROM
    ranked
WHERE
    avg_salary_rank <= 10
ORDER BY avg_salary_rank, company_name;
```
### Top 10 companies based on pay

Refer to the [executed output](https://github.com/loganangell/100_Days_of_Code/blob/main/Day_6/company_salaries.csv) for the top 10 paying companies in 2025. 

For the project, the following information was noted:
* The top 10 salaries derived from various well-known companies, such as:
    * Netflix
    * Dow Jones
    * OpenAI
    * ByteDance
    * and more
* Netflix, as of their 2025 job postings, reported the highest average salary postings for all their job postings at $428,375
    * Also, they appear to have the longest range of salaries, from $106,000 to $680,000
* Dow Jones appears to have the next highest average salary at $377,500
* Other companies in the top 10 have average salaries above $267,500

## Conclusion

This project reinforced key SQL concepts, including developing subqueries for easier data manipulation and retrieval, ranking records based on a specific criterion, and manipulating values such as rounding and extracting.
