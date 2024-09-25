conda activate pyradar
conda env export --no-builds > environment.yml
conda list --export | grep -v '^#' | grep 'pypi' > requirements.txt
