# 📁 claude-workspace

> 이옥슬(데이터분석가)의 Claude Code 작업 폴더입니다.
> 처음 열었다면 **이 파일 → CLAUDE.md → tasks/todo.md** 순서로 보세요.

---

## 🗂️ 폴더 구조

`📤` = GitHub에 올라가는 파일 · `🔒` = 내 PC에만 있는 파일 (`.gitignore`로 제외)

```
claude-workspace/
├── 📤 README.md                  ← 지금 보는 파일 (폴더 안내서)
├── 📤 CLAUDE.md                  ← Claude Code 행동 규칙 (자동으로 읽힘)
├── 📤 SECURITY.md                ← 🚨 키 노출 비상 매뉴얼
├── 📤 .gitignore                 ← GitHub에 올리지 않을 파일 목록
├── 🔒 .env                       ← API 키·Webhook 주소 (절대 공유 금지)
│
├── tasks/                        ← 작업 기록
│   ├── 📤 todo.md                ← 할 일 체크리스트
│   └── 📤 progress.md            ← 한 일 기록 (아래에 추가만)
│
├── scripts/                      ← 자동화 스크립트
│   └── 📤 weather.py             ← 구로구 날씨·미세먼지 → weather.txt + 디스코드
│
├── portfolio/                    ← 포트폴리오 웹페이지
│   └── 📤 index.html             ← 브라우저로 열기
│
├── docs/                         ← 자료 (전부 내 PC 전용)
│   ├── 🔒 DATA_DOWN_2608.csv     ← 다운로드 원본 데이터 (618MB) ⚠️ 개인정보
│   ├── 🔒 analysis/              ← 다운로드 데이터 집계·분석 리포트
│   ├── 🔒 resume.pdf             ← 이력서
│   └── 🔒 자기소개서_IT마케팅_초안.md
│
├── 🔒 콘텐츠다운로드_2608.html     ← 8월 다운로드 현황 페이지
└── 🔒 weather.txt                ← 날씨 기록 (매일 08:00 자동 추가)
```

**폴더 밖에 있는 것**

```
~/.ssh/
├── config                        ← 서버 별칭 설정 (oracle-server)
└── oracle-server.key             ← 🔒 오라클 서버 SSH 키

Windows 작업 스케줄러
└── GuroWeather                   ← 매일 08:00 scripts/weather.py 실행
```

---

## 📄 파일별 설명

| 파일 | 역할 | 수정해도 되나요? |
|---|---|---|
| `README.md` | 폴더 구조 안내 | ✅ 파일이 늘면 업데이트 |
| `CLAUDE.md` | Claude Code가 지켜야 할 규칙 | ✅ 규칙 추가·변경 시 |
| `SECURITY.md` | 키가 노출됐을 때 대응 순서 | ✅ 키 종류가 늘면 추가 |
| `.gitignore` | GitHub 업로드 제외 목록 | ⚠️ 민감 파일이 생기면 꼭 추가 |
| `tasks/todo.md` | 할 일 체크리스트 | ✅ 자유롭게 |
| `tasks/progress.md` | 작업 이력 | ➕ **추가만** (지우지 않기) |
| `scripts/weather.py` | 날씨·미세먼지 수집 + 디스코드 전송 (Open-Meteo, 키 불필요) | ✅ |
| `portfolio/index.html` | 포트폴리오 (연락처·경력은 예시 값) | ✅ 실제 정보로 교체 |
| `docs/DATA_DOWN_2608.csv` | 원본 데이터 | ❌ 원본은 그대로 두기 |
| `.env` | 비밀 값 저장소 (`NEIS_API_KEY`, `DISCORD_WEBHOOK_URL`) | 🔒 본인만 |

---

## ⚠️ 주의사항

1. **`DATA_DOWN_2608.csv`에는 회원 개인정보가 있어요** (`USER_ID`, `생년정보`, `지역` 등).
   - 외부 서비스(웹 업로드, 공유 링크, GitHub 등)에 올리지 마세요.
   - 결과를 공유할 때는 **집계된 숫자만** 사용하세요.
2. **`.env`, `*.key`, `*.pem` 파일은 절대 공유·업로드하지 마세요.** (`.gitignore`로 막혀 있음)
3. 새 민감 파일이 생기면 **커밋 전에 `.gitignore`에 먼저 추가**하세요.
4. 키가 노출된 것 같으면 → **[SECURITY.md](SECURITY.md)** 를 바로 여세요.

---

## 🔁 작업 흐름

```
작업 시작 → tasks/todo.md 확인 → 작업 → 결과 확인 → tasks/progress.md에 기록
```

---

*최종 업데이트: 2026-10-14*
