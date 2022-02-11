# ocado-parser

[![Lint](https://github.com/SavageCore/ocado-parser/actions/workflows/black.yml/badge.svg)](https://github.com/SavageCore/ocado-parser/actions/workflows/black.yml) [![codecov](https://codecov.io/gh/SavageCore/ocado-parser/branch/main/graph/badge.svg?token=2WZIJ3LGYH)](https://codecov.io/gh/SavageCore/ocado-parser) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Generate [OpenDocument](https://www.libreoffice.org/discover/what-is-opendocument/) Spreadsheet (ods) from [Ocado](https://www.ocado.com/) receipts


## Install

```
$ git clone https://github.com/SavageCore/ocado-parser.git
$ pip install -r requirements.txt
```

## Running

Add 1 or more receipts to the folder `/static/pdf` then execute

```
$ python -m app.main
```

Your ODS files will be in `/static/output`

## Why?

Primarily because organising the weekly shop bill with housemates is a faff!

However, I created this fork of [magyargergo/ocado-parser](https://github.com/magyargergo/ocado-parser) to do the following:

* Remove quantity from spreadsheet
* Switch from XLSX to [OpenDocument](https://www.libreoffice.org/discover/what-is-opendocument/) Spreadsheet (ods)
* Support parsing multiple receipts in one run
* Learn some more Python (primarily unit testing)
