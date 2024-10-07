@echo off
REM Створюємо віртуальне середовище, якщо його немає
python -m venv venv

REM Активуємо віртуальне середовище
call venv\Scripts\activate

REM Встановлюємо залежності
python -m pip install -r requirements.txt

REM Запускаємо тести
python -m unittest discover -s tests
python -m unittest discover > report.xml
