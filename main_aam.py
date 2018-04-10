import sys

from Qt import QtWidgets

from packages import settings_aam
from packages.gui import MainAAM


def main():

	settings_aam.settings()

	app = QtWidgets.QApplication(sys.argv)
	window = MainAAM()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
