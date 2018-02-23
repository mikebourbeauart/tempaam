import sys

from Qt import QtWidgets

from packages import aam_settings
from gui import MainAAM


def main():

	aam_settings.settings()

	app = QtWidgets.QApplication(sys.argv)
	window = MainAAM()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
