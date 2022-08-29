#!/bin/bash
set -e
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../

echo $PWD
echo "=== test.sh ==="

python3 -m isort python/ && echo "- isort:         done" &&
python3 -m docformatter -rc python/  && echo "- docformatter:  done" &&
python3 -m black  --check --line-length 88 python/     && echo "- black:         done" &&
python3 -m mypy  --config-file mypy.ini python/     && echo "- mypy:          done" &&
python3 -m flake8 python/ && echo "- flake8:        done" &&
echo "- All Python checks passed"