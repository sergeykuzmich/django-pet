# Django Pet Project

## Getting Started

### Prerequisites

* `python-3.11.*`
* `poetry-1.8.2`

### Setup & Startup

`make`

#### Notes

* All users (`sergey`,`bob`,`alice`,`billgates`,`johndoe`) have `!Q@W#E$R` password.
* Only `sergey` & `johndoe` have superuser role.

## Directories

```plaintext
.
├── blog # primary app
├── ├── fixtures # initial data
├── ├── ├── initial_data.json
├── ├── migrations # database migrations
├── ├── ├── ...
├── ├── templates # html templates
├── ├── ├── blog
├── ├── ├── ├── ...
├── ├── ├── ...
├── core # core django settings
├── ├── templates # html templates
├── ├── ├── registration
├── ├── ├── ├── ...
├── ├── ...
├── tests # test cases
├── ├── ...
├── utils # utility functions
├── ├── ...
```
