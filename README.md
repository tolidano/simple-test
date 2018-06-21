Steps to install and run tests:

1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`
4. `nosetests test.py --with-timer  --with-xunit`

This will run the tests and put the results in nosetests.xml

Note that for some reason one of our test cases is a bit flaky

