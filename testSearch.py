import unittest
import pandas as pd
from search import search_jobs, search_courses

jobs_df = pd.DataFrame({
    'Job Title': ['Software Engineer', 'Data Scientist'],
    'Location': ['New York', 'San Francisco']
})

courses_df = pd.DataFrame({
    'Course Name': ['Intro to Python', 'Advanced Java'],
    'Language': ['Python', 'Java']
})

# Test cases
class TestSearch(unittest.TestCase):
    def test_search_jobs(self):
        location = "new"
        result = jobs_df[jobs_df['Location'].str.contains(location, case=False)]
        self.assertTrue(result.equals(search_jobs(location)))

    def test_search_courses(self):
        language = "java"
        result = courses_df[courses_df['Language'].str.contains(language, case=False)]
        self.assertTrue(result.equals(search_courses(language)))

if __name__ == "__main__":
    unittest.main()


# # test3
# location = "paris"
# expected_jobs = jobs_df[jobs_df['Location'].str.contains(location, case=False)]
# assert search_jobs(location).equals(expected_jobs), "Test Case 3 Failed (jobs)"

# language = "C++"
# expected_courses = courses_df[courses_df['Language'].str.contains(language, case=False)]
# assert search_courses(language).equals(expected_courses), "Test Case 3 Failed (courses)"

# print("Test Case 3 Passed: Functions handle no-match cases correctly.")
