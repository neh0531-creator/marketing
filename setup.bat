@echo off
echo ===================================
echo  병원 카드뉴스 생성기 - 초기 설정
echo ===================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [오류] Python이 설치되지 않았습니다.
    echo https://www.python.org 에서 Python 3.10 이상을 설치해주세요.
    pause
    exit /b 1
)

echo [1/3] 패키지 설치 중...
pip install -r requirements.txt

echo.
echo [2/3] Playwright 브라우저 설치 중...
playwright install chromium

echo.
echo [3/3] 설정 완료!
echo.
echo 사용 방법:
echo   python generate_cards.py                         (대화형 모드)
echo   python generate_cards.py -H "병원명" -i 원고.txt
echo   python generate_cards.py -H "병원명" -i 원고.docx
echo.
pause
