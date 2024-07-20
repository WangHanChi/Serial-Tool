.PHONY: install env run package clean

SRC := main.py
PY := python3 

# Get OS type
OS := $(shell uname -s)

# Install packaged
INSTALL_CMD := pip3 install -r requirements.txt
PACKAGE_CMD := pyinstaller --onefile $(SRC)

ifeq ($(OS),Linux)
    INSTALL_TK := sudo apt-get install -y python3-tk
    INSTALL_PYTHON := sudo apt-get update && sudo apt-get install -y python3
else ifeq ($(OS),Darwin)
    INSTALL_TK := brew install python-tk
    INSTALL_PYTHON := brew install python
else
    INSTALL_TK := echo "Please install tkinter manually on Windows"
    INSTALL_PYTHON := echo "Please install Python manually on Windows"
endif

install:
	@echo "Checking and installing Python packages..."
	$(INSTALL_CMD)
	@echo "Checking and installing tkinter..."
	$(INSTALL_TK)

env:
	@echo "Checking Python installation..."
	@if command -v python3 > /dev/null; then \
		echo "Python is already installed."; \
	else \
		echo "Python is not installed. Installing Python..."; \
		if [ "$(OS)" = "Linux" ]; then \
			sudo apt-get update && sudo apt-get install -y python3; \
		elif [ "$(OS)" = "Darwin" ]; then \
			brew install python; \
		else \
			echo "Please install Python manually on Windows"; \
		fi \
	fi

run:
	@echo "Running main.py..."
	$(PY) $(SRC)

package:
	@echo "Checking and installing PyInstaller..."
	$(INSTALL_CMD)
	@echo "Packaging main.py into an executable..."
	$(PACKAGE_CMD)
	@echo "Executable created in the dist/ directory."

clean:
	$(RM) -r build/ dist/ *.spec *.txt