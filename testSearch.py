import unittest

from search import search

jobs_df = pd.read_excel("jobs.xlsx")
courses_df = pd.read_excel("courses.xlsx")
# test case 1
language = "JavaScript"
expected_courses = courses_df[courses_df['Language'].str.contains(language, case=False)]
assert search_courses(language).equals(expected_courses), "Test Case 2 Failed"

print("Test Case 2 Passed: search_courses function works correctly for language search.")

# test case 2
location = "Cairo"
expected_jobs = jobs_df[jobs_df['Location'].str.contains(location, case=False)]
assert search_jobs(location).equals(expected_jobs), "Test Case 1 Failed"

print("Test Case 1 Passed: search_jobs function works correctly for location search.")

# test3
location = "paris"
expected_jobs = jobs_df[jobs_df['Location'].str.contains(location, case=False)]
assert search_jobs(location).equals(expected_jobs), "Test Case 3 Failed (jobs)"

language = "C++"
expected_courses = courses_df[courses_df['Language'].str.contains(language, case=False)]
assert search_courses(language).equals(expected_courses), "Test Case 3 Failed (courses)"

print("Test Case 3 Passed: Functions handle no-match cases correctly.")
