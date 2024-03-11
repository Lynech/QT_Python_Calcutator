all: build

# venv:
# 	. python -m venv ./.venv
# 	.venv/Scripts/Activate.ps1


# qt: venv
# 	pip install PyQt6

# qt-tools: venv
# 	pip install Pyqt-tools

# pyinstaller: venv
# 	pip install pyinstaller

calc_ui.py:
	pyuic6 -x src/calc.ui -o src/calc_ui.py

build:
	pyinstaller --onefile -w ./src/*.py
	cp ./dist/app.exe ./
	rm -rf ./build ./dist ./app.spec
	./app.exe

clean:
	rm -rf ./build ./dist ./app.spec ./app.exe

rebuild: clean build