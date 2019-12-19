# python-countries

<p align="center">
<a href="https://travis-ci.com/leonkozlowski/python-countries"><img alt="Build Status" src="https://travis-ci.com/leonkozlowski/python-countries.svg?branch=master"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


Wraps [REST Countries](https://restcountries.eu/#api-endpoints-calling-code)


## Installation

From Source:
```bash
$ git clone https://github.com/leonkozlowski/python-countries.git
$ cd python-countries
$ pip install -e .
```

## Usage

Create the client
```bash
>>> client = CountriesApi()
```

Request for country data by full name
```bash
>>> client.full_name('Colombia')
```

Response for `full_name` endpoint
```bash
{
    "name": "Colombia",
    "topLevelDomain": [".co"],
    "alpha2Code": "CO",
    "alpha3Code": "COL",
    "callingCodes": ["57"],
    "capital": "Bogotá",
    "altSpellings": ["CO", "Republic of Colombia", "República de Colombia"],
    "region": "Americas",
    "subregion": "South America",
    "population": 48759958,
    "latlng": [4.0, -72.0],
    "demonym": "Colombian",
    "area": 1141748.0,
    "gini": 55.9,
    "timezones": ["UTC-05:00"],
    "borders": ["BRA", "ECU", "PAN", "PER", "VEN"],
    "nativeName": "Colombia",
    "numericCode": "170",
    "currencies": [{
        "code": "COP",
        "name": "Colombian peso",
        "symbol": "$"
    }],
    "languages": [{
        "iso639_1": "es",
        "iso639_2": "spa",
        "name": "Spanish",
        "nativeName": "Español"
    }],
    "translations": {
        "de": "Kolumbien",
        "es": "Colombia",
        "fr": "Colombie",
        "ja": "コロンビア",
        "it": "Colombia",
        "br": "Colômbia",
        "pt": "Colômbia"
    },
    "flag": "https://restcountries.eu/data/col.svg",
    "regionalBlocs": [{
        "acronym": "PA",
        "name": "Pacific Alliance",
        "otherAcronyms": [],
        "otherNames": ["Alianza del Pacífico"]
    }, {
        "acronym": "USAN",
        "name": "Union of South American Nations",
        "otherAcronyms": ["UNASUR", "UNASUL", "UZAN"],
        "otherNames": ["Unión de Naciones Suramericanas"..."]
    }],
    "cioc": "COL"
}
```