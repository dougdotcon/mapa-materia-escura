@echo off
echo [TARDIS] Switching to Native CURL Download... > download.log
echo [TARDIS] Target: assets/act_dr6_lens.fits (Source Archive) >> download.log
echo. >> download.log

if not exist assets mkdir assets
cd assets

:: Download with Resume (-C -) 
:: Using -k (insecure) just in case of cert issues, -L follow redirects
curl -L -C - -o act_data_v2.tar.gz "https://lambda.gsfc.nasa.gov/data/suborbital/ACT/ACT_dr6/dr6_lensing_release.tar.gz" >> ..\download.log 2>&1

echo. >> ..\download.log
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Download Finished. >> ..\download.log
) else (
    echo [ERROR] Download Failed with code %ERRORLEVEL% >> ..\download.log
)
cd ..
type download.log
