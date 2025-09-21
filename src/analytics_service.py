from typing import Dict, Any


def analyze_weather(raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transform and analyze raw weather API payload.
    Returns a dict with computed fields:
      - temperature_c, feels_like_c, humidity, summary, alerts (list)
    """
    alerts = []
    main = raw.get('main', {})
    weather_list = raw.get('weather', [])
    wind = raw.get('wind', {})
    sys = raw.get('sys', {})

    temp = main.get('temp')
    feels = main.get('feels_like')
    humidity = main.get('humidity')

    # Compose summary
    if weather_list:
        description = weather_list[0].get('description', '')
        summary = f"{description.capitalize()} with wind {wind.get('speed', '?')} m/s"
    else:
        summary = "No summary"

    # Simple alert rules
    if temp is not None and temp >= 35:
        alerts.append({'type': 'heat', 'message': f'High temperature {temp}°C'})
    if temp is not None and temp <= -10:
        alerts.append({'type': 'cold', 'message': f'Extreme cold {temp}°C'})
    if humidity is not None and humidity >= 90:
        alerts.append({'type': 'humidity', 'message': f'High humidity {humidity}%'})
    for w in weather_list:
        id_code = w.get('id', 0)
        # OpenWeatherMap condition codes: heavy rain/drizzle/snow are in certain ranges
        if 200 <= id_code < 600 and 'rain' in w.get('description', '').lower():
            alerts.append({'type': 'precipitation', 'message': 'Rain expected'})

    return {
        'temperature': temp,
        'feels_like_t': feels,
        'humidity': humidity,
        'summary': summary,
        'alerts': alerts
    }
