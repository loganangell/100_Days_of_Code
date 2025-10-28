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
