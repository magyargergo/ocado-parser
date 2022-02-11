# ocado-parser

[![Lint](https://github.com/magyargergo/ocado-parser/actions/workflows/black.yml/badge.svg)](https://github.com/magyargergo/ocado-parser/actions/workflows/black.yml) [![codecov](https://codecov.io/gh/magyargergo/ocado-parser/branch/main/graph/badge.svg?token=XV1VCFJBFB)](https://codecov.io/gh/magyargergo/ocado-parser) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Generate [OpenDocument](https://www.libreoffice.org/discover/what-is-opendocument/) Spreadsheet (ods) from [Ocado](https://www.ocado.com/) receipts


## Install

```
$ git clone https://github.com/magyargergo/ocado-parser.git
$ pip install -r requirements.txt
```

## Running

Add 1 or more receipts to the folder `/static/pdf` then execute

```
$ python -m app.main
```

Your ODS files will be in `/static/output`

## Future plans

* Support parsing of substitutions
* Implement api for uploading pdf
* AWS integration
* dockerization
* Implement Sainsbury's pdf parser

## Contributors 

* [Oliver Sayers](https://github.com/SavageCore)