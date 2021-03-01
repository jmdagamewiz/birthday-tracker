from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton, QLineEdit, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QFormLayout, QStackedWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys


class PersonFrame(QFrame):

    def __init__(self, name, birthday):
        super().__init__()

        self.name = name
        self.birthday = birthday

        self.init_frame()

    def init_frame(self):
        self.setFrameStyle(QFrame.StyledPanel)
        self.create_frame_content()

    def create_frame_content(self):

        self.name_label = QLabel(self.name)
        self.birthday_label = QLabel(self.birthday)
        self.blank_label = QLabel("")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.name_label, stretch=2)
        self.hbox.addWidget(self.birthday_label, stretch=2)
        self.hbox.addWidget(self.blank_label, stretch=1)
        self.setLayout(self.hbox)


class ListAllGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()

        self.init_groupbox()

    def init_groupbox(self):
        self.setTitle("All Persons")
        self.create_groupbox_content()

    def create_groupbox_content(self):
        self.person_frame1 = PersonFrame("Jay Hara", "October 1, 1000")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.person_frame1)

        self.setLayout(self.vbox)


class ListAllWindow(QWidget):
    """
    window for showing list of all persons and adding a person
    """

    def __init__(self):
        super().__init__()

        self.title = "List All Window"

        self.init_window()

    def init_window(self):
        self.setGeometry(100, 100, 420, 450)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("assets/icon.png"))

        self.create_window_content()

    def create_window_content(self):

        self.add_person_button = QPushButton("Add Person")
        self.add_person_button.clicked.connect(self.go_to_add_person_window)

        self.options_hbox = QHBoxLayout()
        self.options_hbox.addStretch()
        self.options_hbox.addWidget(self.add_person_button)

        self.list_all_groupbox = ListAllGroupBox()

        self.go_back_button = QPushButton("Go Back")
        self.go_back_button.setFixedWidth(100)
        self.go_back_button.clicked.connect(self.go_back_to_home_window)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.options_hbox)
        self.vbox.addWidget(self.list_all_groupbox)
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

    def go_to_add_person_window(self):
        parent = self.parentWidget()
        while True:
            if type(parent) == QStackedWidget:
                break
            parent = parent.parentWidget()
        parent.setCurrentIndex(2)

