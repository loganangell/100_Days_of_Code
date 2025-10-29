/*
1. Return the company name with job category postings as:
    a. Data Analyst
    b. Data Scientist
    c. Business Analyst
    d. Data Engineer
2. Also return the minimum, maximum, and average salary for each company job posting
3. Return the Top 10 companies with the highest average salary
*/

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