PYTHON:=python3
VENV:=venv

export PYTHONPATH="$(VENV):."

test: compile
	$(PYTHON) -m pytest 

compile: $(VENV)
$(VENV): requirements.txt
	$(PYTHON) -m pip install -t $(VENV) -r requirements.txt 
	touch $(VENV)
