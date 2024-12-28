import unittest
import pandas as pd
from search import search_jobs, search_courses

class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       
        cls.jobs_df = pd.read_excel("jobs.xlsx")
        cls.courses_df = pd.read_excel("courses.xlsx")

    def test_search_jobs(self):
        location = "Cairo"  
        expected_result = self.jobs_df[self.jobs_df['Location'].str.contains(location, case=False)]
        actual_result = search_jobs(location)
        self.assertTrue(expected_result.equals(actual_result))

    def test_search_courses(self):
        language = "JavaScript"  
        expected_result = self.courses_df[self.courses_df['Language'].str.contains(language, case=False)]
        actual_result = search_courses(language)
        self.assertTrue(expected_result.equals(actual_result))

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
