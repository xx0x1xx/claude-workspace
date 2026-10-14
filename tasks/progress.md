# 📝 작업 기록 (progress)

> 한 일을 날짜별로 **아래에 계속 추가**합니다. (지우거나 고치지 않기)

---

## 2026-10-13

- `tasks/` 폴더 생성, `todo.md`·`progress.md` 만듦
- `SECURITY.md` 작성 — OpenRouter / 오라클 SSH / WordPress 키 노출 시 폐기→재발급→교체→이력 확인 절차, 예방 체크리스트
- `READ.md` 작성 — 폴더 구조 트리, 파일별 설명, 주의사항
- 확인 사항: `.env`, `~/.ssh/oracle-server.key`, `~/.ssh/config` 아직 없음
- 참고: `DATA_DOWN_2608.csv`에 개인정보 칸(USER_ID, 생년정보, 지역) 있음 → 외부 업로드 금지
- `docs/자기소개서_IT마케팅_초안.md` 작성 — resume.pdf 기반 IT 마케팅 자기소개서(성장과정/지원동기/입사 후 포부), 공백 포함 881자
- 참고: Python 미설치(실행 시 MS Store 연결만 뜸) → 글자 수는 PowerShell로 확인
- `docs/DATA_DOWN_2608.csv` 분석 (1,560,865행, 원본 수정 없음) → `docs/analysis/`
  - 분류: 선생님·학원용·강사용→티칭 / 학생→러닝 / 포인트 / 기타 / 무료→CATEGORY2(협력학원·B2B·쿠폰)
  - 결과: 집계 TSV 2개, `다운로드분석_2608.md`(표+인사이트), `다운로드분석_2608.html`(시각화)
  - 검증: 분류별 다운로드 합계 = 전체 행 수 ✅, 브라우저 화면(다크·라이트·좁은 화면) 확인
  - 수정: 회원 비중 기준이 md(32,632명)와 html(33,587명)에서 달라 33,587명 기준으로 통일 (수정 전 md는 .bak 백업)

## 2026-10-14 — NEIS 시험일정 수집 (중단)
- NEIS 학사일정 API 사전 확인: 학교코드 필수, 키 없으면 5건 제한, **API에는 2025.03.01 이후 자료만 있음 (2023·2024 불가)**
- `.env` 생성 (NEIS_API_KEY) — 키가 파일 이름으로 저장돼 있던 것을 내용으로 옮김
- 계획 작성 후 사용자 요청으로 중단. 수집·결과 파일 없음
- 남은 정리: 키 이름으로 된 빈 파일 삭제 여부 미결정, NEIS 키 재발급 권장

## 2026-10-14 — Python 설치
- winget으로 Python 3.13.15 설치 (사용자 범위, `%LOCALAPPDATA%\Programs\Python\Python313`)
- 사용자 PATH에 Python이 WindowsApps(가짜 python)보다 앞에 등록됨 → 새 터미널에서 `python --version` = 3.13.15 확인
- 날씨 스크립트 계획을 Node.js → Python으로 변경

## 2026-10-14 — 구로구 날씨·미세먼지 자동 저장
- `scripts/weather.py` 작성: Open-Meteo(키 불필요)에서 날씨·PM10·PM2.5 받아 `weather.txt`에 이어 쓰기 (미세먼지는 모델 추정치)
- 작업 스케줄러 `GuroWeather` 등록: 매일 08:00, pythonw(창 없음), 놓친 실행은 PC 켜지면 실행
- 확인: 직접 실행 OK, 스케줄러 즉시 실행 결과 0(성공), weather.txt에 기록 2건(테스트) 확인

## 2026-10-14 — 날씨 디스코드 전송 추가
- `.env`에 DISCORD_WEBHOOK_URL 저장(사용자), 형식 확인
- `scripts/weather.py.bak` 백업 후 전송 기능 추가: 주소는 .env에서만 읽음, 실패해도 weather.txt 저장 유지, 결과를 weather.txt에 한 줄 기록
- 확인: 직접 실행 → 디스코드 204(성공) / 스케줄러 실행 → 결과 0, 디스코드 204

## 2026-10-14 — 포트폴리오 웹페이지
- `portfolio/index.html` 작성: 소개(CLAUDE.md 이름·직업 + 자기소개 초안), 경력 3개(임의 예시, ○○ 회사명), 보유 기술, 연락처(예시 주소)
- 반응형(640px 이하 1단) + 다크모드 자동 대응, 외부 업로드 없음
- 확인: Edge 헤드리스 스크린샷으로 PC(1280px)·휴대폰(390px) 폭 레이아웃 확인 → 기본 브라우저로 열기

## 2026-10-14 — GitHub CLI 설치
- winget으로 GitHub CLI 2.102.0 설치 (`C:\Program Files\GitHub CLI\gh.exe`)
- 새 PATH 기준 `gh --version` 실행 확인. 로그인(gh auth login)은 아직 안 함
- GitHub 로그인 완료: 계정 xx0x1xx, 웹 브라우저 인증, git 프로토콜 https, 토큰은 Windows 자격 증명(keyring)에 저장

## 2026-10-14 — claude-workspace GitHub 업로드
- `.gitignore` 작성(.env·키 파일·CSV·docs 개인문서/분석결과·*.bak·weather.txt 제외), READ.md → README.md (백업 READ.md.bak) 폴더 구조 정리
- git init(main), 작성자 xx0x1xx + GitHub noreply 이메일(이 폴더만)
- 커밋 e90658b "Initial setup" (8개 파일) → private 저장소 https://github.com/xx0x1xx/claude-workspace push
- 확인: visibility PRIVATE, GitHub 파일 8개 일치, 로컬=원격 e90658b
- 문제 해결: git fetch가 Git Credential Manager 로그인 대기로 멈춤 → `gh auth setup-git`으로 github.com 인증을 gh에 연결

## 2026-10-14 — 포트폴리오 Vercel 배포 준비
- 별도 폴더 `C:\OAXL\portfolio` 생성, index.html 복사 (workspace/portfolio 원본은 그대로)
- 추가: favicon.svg, 404.html, vercel.json(cleanUrls·보안 헤더), .gitignore, README.md(수정할 곳 + Vercel 배포 안내)
- index.html에 파비콘·OG 태그 추가
- 확인: 로컬 서버에서 / · favicon · 404 응답 200, 스크린샷 확인, vercel.json 형식 OK, 비밀 정보 검사 없음
- private 저장소 https://github.com/xx0x1xx/portfolio push (fa700a5), 로컬=원격 일치
- 남은 일(사용자): 예시 경력·연락처 교체 → Vercel Import·Deploy
