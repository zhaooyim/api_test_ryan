@echo off

set venv_dir=.\venv_assurity

if not exist %venv_dir% (
	echo Setting up the virtual environment...
	python -m venv %venv_dir%
	%venv_dir%\Scripts\pip install -r .\requirements.txt
)

echo Running tests...
%venv_dir%\Scripts\pytest
echo Finished.