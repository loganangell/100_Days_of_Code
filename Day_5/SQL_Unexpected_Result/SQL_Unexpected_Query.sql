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