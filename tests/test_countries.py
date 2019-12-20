import json
import os
import pytest

from python_countries import CountriesApi, CountryResponse


global_client = CountriesApi()


def _resolve_relative_import(test_file):
    in_file = os.path.join(os.path.dirname(__file__), test_file)
    with open(in_file) as f:
        raw_json = f.read()
        return json.loads(raw_json)


def test_countries_client():
    test_client = global_client
    assert isinstance(test_client, CountriesApi)


def test_countries_country_name():
    result = global_client.country_name(name="colombia")

    assert isinstance(result, list)
    assert result[0] == _resolve_relative_import("testData/colombia-response.json")


def test_countries_country_name_raises():
    with pytest.raises(ValueError):
        global_client.country_name(name=None)


def test_countries_full_name():
    result = global_client.full_name(name="colombia")

    assert isinstance(result, list)
    assert result[0] == _resolve_relative_import("testData/colombia-response.json")


def test_countries_full_name_raises():
    with pytest.raises(ValueError):
        global_client.full_name(name=None)


def test_countries_iso_code():
    result = global_client.iso_code(code="pr")

    assert isinstance(result, dict)
    assert result == _resolve_relative_import("testData/puerto-rico-response.json")


@pytest.mark.parametrize(
    "code, exception", [(None, ValueError), ("a", Exception), ("abcd", Exception)]
)
def test_countries_iso_code_raises(code, exception):
    with pytest.raises(exception):
        global_client.iso_code(code=code)


def test_countries_currency():
    result = global_client.currency(currency="cop")

    assert isinstance(result, list)
    assert result[0] == _resolve_relative_import("testData/colombia-response.json")


def test_countries_currency_raises():
    with pytest.raises(ValueError):
        global_client.currency(currency=None)


def test_countries_language():
    result = global_client.language(language="es")

    assert isinstance(result, list)
    assert result[0] == _resolve_relative_import("testData/argentina-response.json")


def test_countries_language_raises():
    with pytest.raises(ValueError):
        global_client.language(language=None)


def test_capital_city():
    result = global_client.capital_city(city="Buenos Aires")

    assert isinstance(result, list)
    assert result[0] == _resolve_relative_import("testData/argentina-response.json")


def test_capital_city_raises():
    with pytest.raises(ValueError):
        global_client.capital_city(city=None)


def test_calling_codes():
    result = global_client.calling_code(calling_code=1264)

    assert isinstance(result, list)
    assert result[0] == _resolve_relative_import("testData/anguilla-response.json")


def test_calling_codes_raises():
    with pytest.raises(ValueError):
        global_client.calling_code(calling_code=None)


def test_region():
    result = global_client.region(region="americas")

    assert isinstance(result, list)
    assert result[0] == _resolve_relative_import("testData/anguilla-response.json")


def test_region_raises():
    with pytest.raises(ValueError):
        global_client.region(region=None)


def test_country_response_access():
    test_response = _resolve_relative_import("testData/anguilla-response.json")

    access_object = CountryResponse(test_response)

    assert access_object.name == "Anguilla"
    assert access_object.top_level_domain == [".ai"]
    assert access_object.alpha_two_code == "AI"
    assert access_object.alpha_three_code == "AIA"
    assert access_object.calling_codes == ["1264"]
    assert access_object.capital == "The Valley"
    assert access_object.alternate_spellings == ["AI"]
    assert access_object.region == "Americas"
    assert access_object.subregion == "Caribbean"
    assert isinstance(access_object.population, int)
    assert access_object.lat_long == [18.25, -63.16666666]
    assert access_object.demonym == "Anguillian"
    assert access_object.area == 91
    assert access_object.gini is None
    assert access_object.timezones == ["UTC-04:00"]
    assert access_object.borders == []
    assert access_object.native_name == "Anguilla"
    assert access_object.numeric_code == "660"
    assert isinstance(access_object.currencies, list)
    assert isinstance(access_object.languages, list)
    assert isinstance(access_object.translations, dict)
    assert access_object.flag == "https://restcountries.eu/data/aia.svg"
    assert access_object.regional_blocs == []
    assert access_object.cioc is ""


@pytest.mark.parametrize(
    "status, exception",
    [(500, Exception), (401, Exception), (404, Exception), (418, Exception)],
)
def test_request_status_raises(status, exception):
    with pytest.raises(exception):
        global_client._check_http_status(status)
