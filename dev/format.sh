#!/bin/bash
set -e

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../
echo $PWD

# core
python3 -m isort -rc python/
python3 -m black --config pyproject.toml --line-length 88 python/
python3 -m docformatter -i -r python/