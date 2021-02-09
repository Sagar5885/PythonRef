From - Complete-Python-Bootcamp/APIAutomation - run bellow commands to run all test cases from TestCases folder:
pytest -v TestCases
pytest TestCases
pytest test_end_to_end.py -s

Make sure you title your test files and test methods starts with 'test_'.

Run with allure:
pytest --alluredir=report_allure/ TestCases
allure serve TestCases/report_allure/ - to see report on localhost