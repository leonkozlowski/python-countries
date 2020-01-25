# -*- coding: utf-8 -*-

import enum
import logging
import re
import requests

from requests import Response

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

__author__ = "Leon Kozlowski"

__version__ = "1.0.0"
__maintainer__ = "Leon Kozlowski"
__email__ = "leonkozlowski@gmail.com"
__status__ = "Development"


class CountriesApi(object):
    """
    Python bindings (API Wrapper)
    Get information about countries via a RESTful API


    Usage:
        API Key: None

        >>> client = CountriesApi()

        >>> client.full_name(name='Colombia')

    Returns:
        {
            "name": "Colombia",
            "topLevelDomain": [".co"],
            "alpha2Code": "CO",
            "alpha3Code": "COL",
            "callingCodes": ["57"],
            "capital": "Bogotá",
            "altSpellings": ["CO", ... , "República de Colombia"],
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
    """

    def __init__(self):
        self.base_url = "https://restcountries.eu/rest/v2/"

    @staticmethod
    def _check_http_status(response_object: Response) -> None:
        """
        Check Request Status and raise exception where applicable
        Args
            status: (int) - HTTP request status code

        Returns:
            None: (NoneType) - raise exception on failure
        """
        status_code = response_object.status_code
        message = response_object.text

        if response_object.status_code != 200:
            raise CountriesApiError(message)
        else:
            logger.debug(f"Request Successful: {status_code}")

    def country_name(self, name: str) -> dict:
        """
        Request "name" endpoint
        Search by country name. It can be the native name or partial name

            (i.e) - "https://restcountries.eu/rest/v2/name/france"

        Args:
            name: (str) - name of country

        Returns:
            resp: (dict) - json response object
        """
        if not name:
            raise ValueError("Please enter a valid country name")

        stripped_name = re.sub(r"\s+", "?", name, flags=re.UNICODE)
        url = f"{self.base_url}name/{stripped_name.lower()}"
        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp

    def full_name(self, name: str) -> dict:
        """
        Request "name" endpoint
        Search by country full name

            (i.e)
                "https://restcountries.eu/rest/v2/name/france?fullText=true"

        Args:
            name: (str) - name of country

        Returns:
            resp: (dict) - json response object
        """
        if not name:
            raise ValueError("Please enter a valid country name")

        stripped_name = re.sub(r"\s+", "?", name, flags=re.UNICODE)
        url = f"{self.base_url}name/{stripped_name.lower()}"

        params = {"fullText": True}

        resp_obj = requests.get(url=url, params=params)
        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp

    def iso_code(self, code: str) -> dict:
        """
        Request "code" endpoint
        Search by ISO 3166-1 2-letter or 3-letter country code

            (i.e) - "https://restcountries.eu/rest/v2/alpha/fra"

        Args:
            code: (str) - ISO 3166-1 (2 or 3 letter code)

        Returns:
            resp: (dict) - json response object
        """
        if not code:
            raise ValueError("Please enter a valid iso_code")

        url = f"{self.base_url}alpha/{code.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp

    def currency(self, currency: str) -> list:
        """
        Request "currency" endpoint
        Search by ISO 4217 currency code

            (i.e) - "https://restcountries.eu/rest/v2/currency/usd"

        Args:
            currency: (str) - ISO 4217 currency code

        Returns:
            resp: (dict) - json response object
        """
        if not currency:
            raise ValueError("Please enter a valid currency")

        url = f"{self.base_url}currency/{currency.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp

    def language(self, language: str):
        """
        Request language endpoint
        Search by ISO 639-1 language code

            (i.e) - "https://restcountries.eu/rest/v2/lang/es"

        Args:
            language: (str) - ISO 639-1 language code

        Returns:
            resp: (dict) - json response object
        """
        if not language:
            raise ValueError("Please enter a valid language")

        url = f"{self.base_url}lang/{language.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp

    def capital_city(self, city: str) -> dict:
        """
        Request capital city endpoint
        Search by capital city

            (i.e) - "https://restcountries.eu/rest/v2/capital/tallinn"

        Args:
            city: (str) - capital city

        Returns:
            resp: (dict) - json response object
        """
        if not city:
            raise ValueError("Please enter a valid capital city")

        stripped_city = re.sub(r"\s+", "?", city, flags=re.UNICODE)
        url = f"{self.base_url}capital/{stripped_city.lower()}"

        resp_obj = requests.get(url=url)

        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp

    def calling_code(self, calling_code: int) -> dict:
        """
        Request capital city endpoint
        Search by calling code

            (i.e) - "https://restcountries.eu/rest/v2/callingcode/372"

        Args:
            calling_code: (str) - calling code
            (ref: https://countrycode.org/)

        Returns:
            resp: (dict) - json response object
        """
        if not calling_code:
            raise ValueError("Please enter a valid calling code")

        url = f"{self.base_url}callingcode/{str(calling_code)}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp

    def region(self, region: str) -> dict:
        """
        Request region endpoint
        Search by region

            (i.e) - "https://restcountries.eu/rest/v2/region/americas"

        Args:
            region: (str) - region
            [Africa, Americas, Asia, Europe, Oceania]

        Returns:
            resp: (dict) - json response object
        """

        class ExtendedEnum(enum.Enum):
            @classmethod
            def list(cls):
                return list(map(lambda c: c.value, cls))

        class Region(ExtendedEnum):
            AFRICA = "africa"
            AMERICAS = "americas"
            ASIA = "asia"
            EUROPE = "europe"
            OCEANIA = "oceania"

        if region not in Region._value2member_map_:
            raise ValueError(f"Valid regions are: {Region.list()}")

        url = f"{self.base_url}region/{region.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj)

        resp = resp_obj.json()

        return resp


class CountriesApiError(Exception):
    """Common base class for all non-exit exceptions."""
    pass


class CountryResponse(dict):
    def __init__(self, data: dict):
        """
        Country REST API Response Object Access
        Args:
            data: (dict) response json object
        """

        super(CountryResponse, self).__init__(data)

    @property
    def name(self) -> str:
        return self.get("name", None) if self else None

    @property
    def top_level_domain(self) -> list:
        return self.get("topLevelDomain", None) if self else None

    @property
    def alpha_two_code(self) -> str:
        return self.get("alpha2Code", None) if self else None

    @property
    def alpha_three_code(self) -> str:
        return self.get("alpha3Code", None) if self else None

    @property
    def calling_codes(self) -> list:
        return self.get("callingCodes", None) if self else None

    @property
    def capital(self) -> str:
        return self.get("capital", None) if self else None

    @property
    def alternate_spellings(self) -> list:
        return self.get("altSpellings", None) if self else None

    @property
    def region(self) -> str:
        return self.get("region") if self else None

    @property
    def subregion(self) -> str:
        return self.get("subregion") if self else None

    @property
    def population(self) -> int:
        return self.get("population") if self else None

    @property
    def lat_long(self) -> list:
        return self.get("latlng") if self else None

    @property
    def demonym(self) -> str:
        return self.get("demonym") if self else None

    @property
    def area(self) -> float:
        return self.get("area") if self else None

    @property
    def gini(self) -> float:
        return self.get("gini") if self else None

    @property
    def timezones(self) -> list:
        return self.get("timezones") if self else None

    @property
    def borders(self) -> list:
        return self.get("borders") if self else None

    @property
    def native_name(self) -> str:
        return self.get("nativeName") if self else None

    @property
    def numeric_code(self) -> str:
        return self.get("numericCode") if self else None

    @property
    def currencies(self) -> list:
        return self.get("currencies") if self else None

    @property
    def languages(self) -> list:
        return self.get("languages") if self else None

    @property
    def translations(self) -> dict:
        return self.get("translations") if self else None

    @property
    def flag(self) -> str:
        return self.get("flag") if self else None

    @property
    def regional_blocs(self) -> list:
        return self.get("regionalBlocs") if self else None

    @property
    def cioc(self) -> str:
        return self.get("cioc") if self else None
