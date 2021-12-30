all:
	pip3 install pyinstaller
	pyinstaller main.py -F --distpath './'

clean:
	rm -rf build/ main main.spec
