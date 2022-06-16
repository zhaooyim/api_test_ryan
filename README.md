# api_test_yimian
This is a test project that accomendates an API test and the supporting utilities, for URL `https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false` against following criteria,
```
* Name = "Carbon credits"
* CanRelist = true
* The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
```

## Requirements:
Python 3 ([How to install Python 3](https://realpython.com/installing-python/))

Note: For macOS - the recent versions come with a pre-installed Python3 which is sufficient for this project. If it is not the case by any chance or you prefer to use a third party Python for any reason, it is recommended to install Python from HomeBrew. See the How-To linked above and go to section How to Install From Homebrew.

## Platform
The program has been tested on the following platforms:
* macOS 12.4
* Windows 10

## How To Use
It may take a few minutes to launch at the first time due to the installation of dependencies.

### via Command Line (Recommended)
Navigate to <b><i>the top level directory</i></b> of the project in the console and execute,

#### macOS Terminal
```bash
# At /example/path/api_test_yimian
$ sh ./run_tests.sh
```

#### Windows Command Prompt
```
C:\example\path\api_test_yimian> run_tests.bat
```

### via IDE
* Alternatively, feel free to load the project in an IDE of choice, such as PyCharm, Visual Studio Code, and follow the guides to set up the Python interpreter properly.
* Open IDE's terminal, and execute ```pytest``` at the top level folder of the project.
* Or, create a pytest confirugation in IDE, and run the test from the configuration.

## Check Test Results

### PASS example
```
============================================================ test session starts =============================================================
platform darwin -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/mymac/Workspace/assurity_test
collected 1 item

test_category_rules.py .                                                                                                               [100%]

============================================================= 1 passed in 1.11s ==============================================================
```

### FAIL example
```
============================================================ test session starts =============================================================
platform darwin -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/mymac/Workspace/assurity_test
collected 1 item

test_category_rules.py F                                                                                                               [100%]

================================================================== FAILURES ==================================================================
_ test_promotion_gallery_has_good_position_in_category[https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false-6317-Carbon credits-True] _

url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false', category_id = 6317, category_name = 'Carbon credits'
can_relist = True

    @pytest.mark.parametrize("url, category_id, category_name, can_relist", testdata)
    def test_promotion_gallery_has_good_position_in_category(url, category_id, category_name, can_relist):
        actual_response_json = helpers_http.send_request_get(url)

>       assert(category_id == actual_response_json['CategoryId'])
E       assert 6317 == 6327

test_category_rules.py:20: AssertionError
========================================================== short test summary info ===========================================================
FAILED test_category_rules.py::test_promotion_gallery_has_good_position_in_category[https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false-6317-Carbon credits-True]
============================================================= 1 failed in 0.47s ==============================================================
```
