#!/usr/bin/env bash

venv_dir="./venv_assurity_test"

if [ ! -d $venv_dir ]
then
  printf "Setting up the virtual environment...\n"
  python3 -m venv $venv_dir
  source $venv_dir/bin/activate
  pip3 install -r requirements.txt
else
  source $venv_dir/bin/activate
fi

printf "\nRunning tests...\n"
pytest
deactivate
printf "Finished.\n"
