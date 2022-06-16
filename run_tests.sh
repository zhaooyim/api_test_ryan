#!/usr/bin/env bash

venv_dir="./venv_assurity"

if [ ! -d $venv_dir ]
then
  printf "Setting up the virtual environment...\n"
  python3 -m venv $venv_dir
  $venv_dir/bin/pip install -r requirements.txt
fi

printf "\nRunning tests...\n"
$venv_dir/bin/pytest
printf "Finished.\n"
