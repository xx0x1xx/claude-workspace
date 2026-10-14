"""서울 구로구 날씨·미세먼지를 가져와 weather.txt에 이어 쓰는 스크립트.

- 데이터: Open-Meteo (API 키 불필요)
- 미세먼지는 모델 추정치이며 에어코리아 공식 측정값과 다를 수 있음
- 매일 08:00 Windows 작업 스케줄러(GuroWeather)로 실행
- .env에 DISCORD_WEBHOOK_URL이 있으면 디스코드 채널에도 전송
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

# 구로구청 근처 좌표
LAT, LON = 37.4954, 126.8874
BASE_DIR = Path(__file__).resolve().parent.parent
OUT_FILE = BASE_DIR / "weather.txt"
ENV_FILE = BASE_DIR / ".env"

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
AIR_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

# WMO 날씨 코드 → 한글
WEATHER_CODES = {
    0: "맑음", 1: "대체로 맑음", 2: "구름 조금", 3: "흐림",
    45: "안개", 48: "서리 안개",
    51: "약한 이슬비", 53: "이슬비", 55: "강한 이슬비",
    56: "약한 어는 이슬비", 57: "어는 이슬비",
    61: "약한 비", 63: "비", 65: "강한 비",
    66: "약한 어는 비", 67: "어는 비",
    71: "약한 눈", 73: "눈", 75: "강한 눈", 77: "싸락눈",
    80: "약한 소나기", 81: "소나기", 82: "강한 소나기",
    85: "약한 눈보라", 86: "강한 눈보라",
    95: "뇌우", 96: "우박 동반 뇌우", 99: "강한 우박 동반 뇌우",
}


def get_json(url, params):
    full_url = url + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(full_url, timeout=30) as resp:
        return json.load(resp)


def read_env(name):
    # .env에서 값 하나 읽기 (없으면 None)
    if not ENV_FILE.exists():
        return None
    for line in ENV_FILE.read_text(encoding="utf-8-sig").splitlines():
        key, sep, value = line.partition("=")
        if sep and key.strip() == name:
            return value.strip().strip('"') or None
    return None


def send_discord(text):
    url = read_env("DISCORD_WEBHOOK_URL")
    if not url:
        return "디스코드: 주소 없음(건너뜀)"
    body = json.dumps({"content": text}).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Content-Type": "application/json",
        # 기본 Python User-Agent는 디스코드에서 차단될 수 있음
        "User-Agent": "GuroWeather/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return f"디스코드: 전송 성공({resp.status})"
    except Exception as e:
        # 에러 메시지에 주소가 섞이지 않도록 종류만 기록
        return f"디스코드: 전송 실패({type(e).__name__} {getattr(e, 'code', '')})"


def pm10_grade(v):
    # 환경부 기준 (㎍/㎥)
    if v <= 30:
        return "좋음"
    if v <= 80:
        return "보통"
    if v <= 150:
        return "나쁨"
    return "매우나쁨"


def pm25_grade(v):
    if v <= 15:
        return "좋음"
    if v <= 35:
        return "보통"
    if v <= 75:
        return "나쁨"
    return "매우나쁨"


def build_report(now):
    w = get_json(WEATHER_URL, {
        "latitude": LAT, "longitude": LON, "timezone": "Asia/Seoul", "forecast_days": 1,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
    })
    a = get_json(AIR_URL, {
        "latitude": LAT, "longitude": LON, "timezone": "Asia/Seoul",
        "current": "pm10,pm2_5",
    })

    cur, day = w["current"], w["daily"]
    sky = WEATHER_CODES.get(cur["weather_code"], f"코드 {cur['weather_code']}")
    wind_ms = cur["wind_speed_10m"] / 3.6  # km/h → m/s
    pm10, pm25 = a["current"]["pm10"], a["current"]["pm2_5"]

    return (
        f"[{now:%Y-%m-%d %H:%M}] 서울 구로구\n"
        f"- 날씨: {sky}, 현재 {cur['temperature_2m']:.1f}°C "
        f"(최고 {day['temperature_2m_max'][0]:.1f} / 최저 {day['temperature_2m_min'][0]:.1f}), "
        f"습도 {cur['relative_humidity_2m']}%, 바람 {wind_ms:.1f}m/s, "
        f"강수확률 {day['precipitation_probability_max'][0]}%\n"
        f"- 미세먼지: PM10 {pm10:.0f}㎍/㎥ ({pm10_grade(pm10)}), "
        f"초미세먼지 PM2.5 {pm25:.0f}㎍/㎥ ({pm25_grade(pm25)})\n"
    )


def main():
    now = datetime.now()
    try:
        text = build_report(now)
    except Exception as e:
        # 실패해도 기록을 남겨서 나중에 원인을 알 수 있게
        text = f"[{now:%Y-%m-%d %H:%M}] ⚠ 가져오기 실패: {e}\n"
    discord_result = send_discord(text)
    with open(OUT_FILE, "a", encoding="utf-8") as f:
        f.write(text + f"- ({discord_result})\n\n")
    if sys.stdout:  # pythonw(창 없이 실행)에서는 출력 생략
        print(text + discord_result)


if __name__ == "__main__":
    main()
