## TIP Open WiFi Test Automation

### Overview

This repository contains the test automation framework and scripts for TIP Open WiFi.
Test Framework is implemented in pytest

![Automation Overview](.img/automation_overview.png)

The vision is to create an open test framework to ensure production grade Open Wifi Solution.

This test automation tied into our overall tooling at TIP as shown below:

![Tools and Test Automation](.img/Tools_and_Testing.png)

### General guidelines

This testing code adheres to generic [pep8](https://www.python.org/dev/peps/pep-0008/#introduction) style guidelines, most notably:

1. [Documentation strings](https://www.python.org/dev/peps/pep-0008/#documentation-strings)
2. [Naming conventions](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions)
3. [Sphynx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

Using [pytest](https://docs.pytest.org/en/6.2.x/) as the test execution framework.

Using [pylint](http://pylint.pycqa.org) for code quality monitoring.

We are using the `pylint` package to do the linting. Documentation for it can be found [here](http://pylint.pycqa.org/en/latest/).
In general, the customizations are possible via the `.pylintrc` file:

1. Line length below 120 characters is fine (search for max-line-length)
2. No new line at the end of file is fine (search for missing-final-newline)
3. Multiple new lines at the end of file are fine (search for trailing-newlines)
4. Indent using 4 spaces (search for indent-string)

In future we should enforce a policy, where we cannot merge a code where the pylint scoe goes below 7:

```shell
pylint --fail-under=7 *py
```

the command above would produce a non-zero exit code if the score drops below 7.

### TIP Controller Integration

Using Swagger Autogenerated CloudSDK Library pypi package (implemented with [swagger codegen](https://github.com/swagger-api/swagger-codegen)).

### Reporting

Currently the plan is to use pytest integrated with [allure](https://docs.qameta.io/allure/#_pytest) to create visual reports for the test outcomes

### Miscellaneous

1. Do not use old style string formatting: `"Hello %s" % var`; use `f"Hello {var}` instead
2. use `"""` in Docstrings

### Useful links

https://docs.pytest.org/en/latest/example/markers.html  
https://docs.pytest.org/en/latest/usage.html  
http://pythontesting.net/framework/pytest/pytest-introduction/

### Test status

![total test count](https://raw.githubusercontent.com/Telecominfraproject/wlan-testing/badges/total-count.svg)

[![R2.x sanity testing](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/uc_sanity.yml/badge.svg)](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/uc_sanity.yml)

[![R1.x sanity testing](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/sanity.yml/badge.svg)](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/sanity.yml)
![sanity test count](https://raw.githubusercontent.com/Telecominfraproject/wlan-testing/badges/sanity-count.svg)

[![interop testing](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/interop.yml/badge.svg)](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/interop.yml)
![interop test count](https://raw.githubusercontent.com/Telecominfraproject/wlan-testing/badges/interop-count.svg)

[![performance testing](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/performance.yml/badge.svg)](https://github.com/Telecominfraproject/wlan-testing/actions/workflows/performance.yml)
![performance test count](https://raw.githubusercontent.com/Telecominfraproject/wlan-testing/badges/performance-count.svg)

### Best Practice

1. Ensure to have a python version > 3
2. We strongly recommend to use virtualenv to ensure that your dev environment sandbox is created.

### Code style

All code must be written in python 3 and conform to PEP 8 style guide. The test framework is built using pytest.  

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)  

### Directory Structure

```bash
├── lanforge              - /* to be migrated */
├── libs
│   ├── controller_tests  -/* Library Support for controller_tests part  */
    ├── apnos             -/* Library Support for Access Points (uses AP SSH)  */
│   ├── lanforge          -/* Library Support for LanForge Traffic Generator */
│   ├── perfecto          -/* Library Support for Perfecto Systems */
│   ├── testrails         -/* Result Visualization (will be depreciated ) */
├── tests                 -/* Pytest cases Directory */
│   ├── _basic_test_setup
│   ├── access_point_tests
│   ├── controller_tests
│   ├── e2e
      ├── advanced
      ├── basic
      ├── interOp
      ├── mdu
      |── mesh
      |── scale
```

### Setup Instructions

#### Step 1

Set up the repository in your base directory of choice. Currently, it is 
important to clone the wlan-lanforge-scripts repository and link to wlan-testing  
directory (The sync_repos.bash provides that linkage).

```shell
git clone https://github.com/Telecominfraproject/wlan-testing
git clone https://github.com/Telecominfraproject/wlan-lanforge-scripts

Make sure this directory structure exists
├── wlan-lanforge-scripts
├── wlan-testing

cd wlan-testing

./sync_repos.bash
```

#### Step 2

Please ensure you follow the steps outlined in [here](./libs/controller/README.md)

```shell
Lets add the TIP pypi repository by following the below steps:

mkdir ~/.pip
echo "[global]" > ~/.pip/pip.conf
echo "index-url = https://pypi.org/simple" >> ~/.pip/pip.conf
echo "extra-index-url = https://tip-read:tip-read@tip.jfrog.io/artifactory/api/pypi/tip-wlan-python-pypi-local/simple" >> ~/.pip/pip.conf
```

#### Step 3

Please ensure you have python version >= 3 is required. Double check this by running "python --version" command.

```shell
User this to check "python --version"

Lets Install the Python Packages needed

pip3 install -r requirements.txt
```

#### Step 4

Setup configuration.py file
This file is autogenerated by Quali-Lab-Orchestration
You can custom create the configuration file, by following the sample configuration data structure (tests/configuration.py)

#### Step 5

You are all set,

To verify that everything is working,

cd wlan-testing/tests
pytest -m test_connection -s -vvv

### Executing and Contributing new test cases

Follow instructions provided [here](./tests/README.md)  to understand the Testing Framework, and How to run and 
write new tests

### Issue Reporting
Please submit issues using our JIRA project [here](https://telecominfraproject.atlassian.net/browse/WIFI)

Use the Test Automation [backlog](https://telecominfraproject.atlassian.net/secure/RapidBoard.jspa?projectKey=WIFI&rapidView=48&view=planning.nodetail)
