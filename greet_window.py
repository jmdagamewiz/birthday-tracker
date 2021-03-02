from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton, QLineEdit, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QFormLayout, QStackedWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys


class GreetPersonGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        self.title = "Greet Person"
        self.init_groupbox()

    def init_groupbox(self):
        self.setTitle(self.title)
        self.create_groupbox_content()

    def create_groupbox_content(self):

        self.to_label = QLabel("To: ")
        self.to_input = QLineEdit()

        self.to_hbox = QHBoxLayout()
        self.to_hbox.addWidget(self.to_label)
        self.to_hbox.addWidget(self.to_input)

        self.message_label = QLabel("Your Message: ")
        self.message_input = QLineEdit()
        self.message_input.setMinimumHeight(225)
        self.message_input.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.from_label = QLabel("From: ")
        self.from_input = QLineEdit()

        self.from_hbox = QHBoxLayout()
        self.from_hbox.addWidget(self.from_label)
        self.from_hbox.addWidget(self.from_input)

        self.send_button = QPushButton("Send Greetings")
        self.send_button.setFixedWidth(200)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.to_hbox)
        self.vbox.addSpacing(10)
        self.vbox.addWidget(self.message_label)
        self.vbox.addWidget(self.message_input)
        self.vbox.addSpacing(10)
        self.vbox.addLayout(self.from_hbox)
        self.vbox.addSpacing(10)
        self.vbox.addWidget(self.send_button, alignment=Qt.AlignCenter)

        self.setLayout(self.vbox)


class GreetPersonWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "Greet Person Window"

        self.init_window()

    def init_window(self):
        self.setGeometry(100, 100, 420, 450)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("assets/icon.png"))

        self.create_window_content()

    def create_window_content(self):

        self.greet_person_groupbox = GreetPersonGroupBox()

        self.go_back_button = QPushButton("Go Back")
        self.go_back_button.setFixedWidth(100)
        self.go_back_button.clicked.connect(self.go_back_to_home_window)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.greet_person_groupbox)
        self.vbox.addStretch()
        self.vbox.addWidget(self.go_back_button, alignment=Qt.AlignLeft)
        self.setLayout(self.vbox)

    def go_back_to_home_window(self):
        parent = self.parentWidget()
        while True:
            if type(parent) == QStackedWidget:
                break
            parent = parent.parentWidget()
        parent.setCurrentIndex(0)

