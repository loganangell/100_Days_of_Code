## Project: Green Bay Packer Dashboard

Today, I decided to take what I have learned so far in Python and create a program that will request data from Pro Football Reference (PFP) and create a data frame of the requested data for a specific NFL team's gamelogs.

Refer to the 'Packer_Dashboard' repository for the project.

The end goal of this project is to:
1. Learn how to request data from HTML sources
2. Create a code that a user can use to request range of seasons' data for a specific NFL team
3. The code will take the data, place it in a data frame, and then converted to a saved CSV file
4. I will then create a dashboard in Power BI that will give a stakeholder information about various statistics about the requested team.
5. For this project, we will request 2015-2024 NFL team data from the Green Bay Packers and their opponents

Today, I have developed the following:
1. Created a code that requests data for a specific team from PFP (Green Bay Packers)
2. Created a config files that helps with manipulating the data to give me opponents' conferences and divisions as well as their PFP abbreviations
3. Created input variables as well as validate the requests for error handling