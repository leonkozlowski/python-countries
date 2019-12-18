"""python-countries"""

import enum
import logging
import re
import requests

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

__author__ = "Leon Kozlowski"

__version__ = "0.0.1"
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
        [{
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
        }]
    """

    def __init__(self):
        self.base_url = "https://restcountries.eu/rest/v2/"
        self.params = dict()

    @staticmethod
    def _check_http_status(status: int) -> None:
        """
        Check Request Status and raise exception where applicable
        Args
            status: (int) - HTTP request status code

        Returns:
            None: (NoneType) - raise exception on failure
        """
        if 500 <= status <= 503:
            logger.error(f"Exception: {status}")
            raise Exception(status)

        elif status == 401:
            logger.error(f"Exception: {status} - Access Denied")
            raise Exception(status)

        elif status == 404:
            logger.error(f"Exception: {status} - Invalid Request")
            raise Exception(status)

        elif status != 200:
            logger.error(f"Exception: {status} - Error")

        else:
            logger.info(f"Status: {status}")

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
            raise ValueError("Please enter a name for python-countries request")

        stripped_name = re.sub(r"\s+", "", name, flags=re.UNICODE)
        resp_obj = requests.get(url=f"{self.base_url}name/{stripped_name.lower()}")
        self._check_http_status(resp_obj.status_code)

        resp = resp_obj.json()

        return resp

    def full_name(self, name: str) -> dict:
        """
        Request "name" endpoint
        Search by country full name

            (i.e) - "https://restcountries.eu/rest/v2/name/france?fullText=true"

        Args:
            name: (str) - name of country

        Returns:
            resp: (dict) - json response object
        """
        if not name:
            raise ValueError("Please enter a name for python-countries request")

        stripped_name = re.sub(r"\s+", "", name, flags=re.UNICODE)
        url = f"{self.base_url}name/{stripped_name.lower()}"

        params = {"fullText": True}

        resp_obj = requests.get(url=url, params=params)
        self._check_http_status(resp_obj.status_code)

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
            raise ValueError("Please enter a iso_code for python-countries request")

        elif 2 < len(code) < 3:
            raise ValueError("ISO 3166-1 code must be 2 or 3 characters")

        url = f"{self.base_url}alpha/{code.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj.status_code)

        resp = resp_obj.json()

        return resp

    def currency(self, currency: str) -> dict:
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
            raise ValueError("Please enter a currency for python-countries request")

        url = f"{self.base_url}currency/{currency.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj.status_code)

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
            raise ValueError("Please enter a language for python-countries request")

        url = f"{self.base_url}lang/{language.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj.status_code)

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
            raise ValueError("Please enter a capital city for python-countries request")

        stripped_city = re.sub(r"\s+", "", city, flags=re.UNICODE)
        url = f"{self.base_url}capital/{stripped_city.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj.status_code)

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
            raise ValueError("Please enter a calling code for python-countries request")

        url = f"{self.base_url}callingcode/{str(calling_code)}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj.status_code)

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

        if not region in Region._value2member_map_:
            raise ValueError(f"Valid regions are: {Region.list()}")

        url = f"{self.base_url}region/{region.lower()}"

        resp_obj = requests.get(url=url)
        self._check_http_status(resp_obj.status_code)

        resp = resp_obj.json()

        return resp
