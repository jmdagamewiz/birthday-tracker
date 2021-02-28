from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton, QLineEdit, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QFormLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys


class AddPersonGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        self.title = "Add Person"
        self.init_groupbox()

    def init_groupbox(self):
        self.setTitle(self.title)
        self.create_groupbox_content()

    def create_groupbox_content(self):

        self.first_name_label = QLabel("First Name: ")
        self.first_name_input = QLineEdit()

        self.last_name_label = QLabel("Last Name: ")
        self.last_name_input = QLineEdit()

        self.gender_label = QLabel("Gender: ")

        self.male_button = QRadioButton("Male")
        self.female_button = QRadioButton("Female")
        self.others_button = QRadioButton("Others")

        self.gender_vbox = QVBoxLayout()
        self.gender_vbox.addWidget(self.male_button)
        self.gender_vbox.addWidget(self.female_button)
        self.gender_vbox.addWidget(self.others_button)

        self.age_label = QLabel("Age: ")
        self.age_input = QLineEdit()

        self.birth_date_label = QLabel("Birth Date: ")
        self.birth_date_input = QLineEdit()

        self.email_label = QLabel("Email: ")
        self.email_input = QLineEdit()

        self.form = QFormLayout()
        self.form.addRow(self.first_name_label, self.first_name_input)
        self.form.addRow(self.last_name_label, self.last_name_input)
        self.form.addRow(self.gender_label, self.gender_vbox)
        self.form.addRow(self.age_label, self.age_input)
        self.form.addRow(self.birth_date_label, self.birth_date_input)
        self.form.addRow(self.email_label, self.email_input)

        self.add_person_button = QPushButton("Add Person")
        self.add_person_button.setFixedWidth(100)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.form)
        self.vbox.addWidget(self.add_person_button, alignment=Qt.AlignRight)
        self.setLayout(self.vbox)


class AddPersonWindow(QWidget):
    """
    window for adding person, showing list of all person,
    and
    """

    def __init__(self):
        super().__init__()

        self.title = "Add Person Window"

        self.init_window()

    def init_window(self):
        self.setGeometry(100, 100, 420, 450)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("assets/icon.png"))

        self.create_window_content()

    def create_window_content(self):

        self.add_person_groupbox = AddPersonGroupBox()

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.add_person_groupbox)
        self.vbox.addStretch()

        self.setLayout(self.vbox)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = AddPersonWindow()
    window.show()
    sys.exit(App.exec())