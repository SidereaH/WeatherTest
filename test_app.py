import pytest
import allure
from app import get_json

@pytest.mark.asyncio
@allure.feature("JSON response")
@allure.story("Weather API")
@allure.title("Test get_json with weather API")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("json", "api", "weather")
@allure.description("This test checks that the get_json function returns a correct response from weather API.")
async def test_get_json_weather(event_loop):
    url = "https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=d1de271e5d73e0f7346c43f4ade03143"
    expected = {
                 "coord" : {"lon" : 37.6156, "lat":55.7522},
                 "weather":[{"id": 800, "main" : "Clear", "description" : "clear sky", "icon" : "01d"}],
                 "base" : "stations",
                 "main" : {
                    "temp" : 284.15,
                    "feels_like": 282.79,
                    "temp_min" : 284.15,
                    "temp_max" : 284.15,
                    "pressure" : 1024,
                    "humidity" : 67,

                 },
                 "visibility" : 10000,
                 "wind" : {"speed" :3, "deg": 150},
                 "clouds" : {"all" : 0},
                 "dt" : 1633002236,
                 "sys": {
                    "type" : 2,
                    "id" : 2011538,
                    "country" : "RU",
                    "sunrise" : 1632988421,
                    "sunset" : 1633030985,
                 },
                 "timezone" : 10800,
                 "id" : 524901,
                 "name" : "Moscow",
                 "cod" : 200,
    }
    result = await get_json(url)
    assert result is not None
    assert result == expected
