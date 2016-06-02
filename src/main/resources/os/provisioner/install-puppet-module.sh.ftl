@echo off
puppet module install --color false ${moduleName}
if %errorlevel% neq 0 exit /b %errorlevel%