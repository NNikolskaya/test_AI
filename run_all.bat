@echo off
setlocal

REM ════════════════════════════════════
REM    Windows replacement for Makefile
REM ════════════════════════════════════

:menu
echo ================================
echo 🔧 News AI Project Utility Menu
echo ================================
echo 1. Run Full Pipeline (scrape + summarize + index)
echo 2. Run CLI Search
echo 3. Run Streamlit UI
echo 4. Stop Streamlit UI
echo 0. Exit
echo ================================
set /p choice=Choose an option:

if "%choice%"=="1" goto run_pipeline
if "%choice%"=="2" goto run_cli_search
if "%choice%"=="3" goto run_streamlit
if "%choice%"=="4" goto stop_streamlit
if "%choice%"=="0" goto end

goto menu

:run_pipeline
echo Running full ETL pipeline...
poetry run python scripts/process_and_index.py
goto end

:run_cli_search
echo Starting CLI search...
poetry run python scripts/lang_search.py
goto end

:run_streamlit
echo Launching Streamlit interface...
poetry run streamlit run scripts/streamlit_search.py
goto end

:stop_streamlit
echo Stopping Streamlit...
for /f "tokens=2" %%a in ('tasklist /fi "imagename eq python.exe" /v ^| findstr /i "streamlit"') do (
    taskkill /PID %%a /F >nul 2>&1
)
goto end

:end
echo Done.
pause
