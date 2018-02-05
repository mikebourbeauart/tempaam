css = '''
	QDialog{
		background-color: #141414;
	}

	QSplashScreen{
		background-color: #141414;
	}

	QLabel{
		color: #DADADA;
		font:12px;
	}

	QTabBar::tab::selected{
		Background: #2c998e;
		color: #E8E8E8;
		font-weight:bold;
	}
	QTabBar::tab::!selected{
		Background: #222222;
		color: #E8E8E8;
	}
	QTabBar::tab::hover{
		Background: #29C2B2;
		color: #FFFFFF;
		font-weight:bold;
	}

	QLineEdit{
		background: #404040;
		color:rgb(218,218,218);
		font:12px;
		height: 30px;
	}
	QLineEdit:focus{
		background: #404040;
		color:rgb(218,218,218);
		font:12px;
		border: 2px solid #2c998e;
		height: 30px;
	}

	QPushButton{
		background-color: #5a5a5a;
		color: #DADADA;
		height: 20px
	}

	QComboBox{
		background-color: #404040;
		font:12px;
	}

	QComboBox QAbstractItemView{
		selection-background-color: #2c998e;
		font:12px;
		border-left-style:solid;
		border-top-style: none;
		border-bottom-style: none;
		border-right-style: none;

	}

	QListWidget{
		background-color: #404040;
		color:rgb(218,218,218);
		font:12px;
	}
	QListWidget:focus{
		background-color: #404040;
		border: 2px solid #2c998e;
	}

	QPushButton{
		Background:#636363;
		height: 30px
	}
	QPushButton:hover{
		Background: #2c998e;
	}
	QPushButton:hover:pressed{
		Background: #2c998e;
	}
	QPushButton:pressed{
		Background:  #22A194;
'''