#! /bin/sh

echo
echo "Run isort"
echo
isort --check

echo
echo "Run autopep8"
echo
autopep8 --exit-code --diff -r .

echo
echo "Run flake8"
echo
flake8

echo
echo "Run pylama"
echo
pylama
