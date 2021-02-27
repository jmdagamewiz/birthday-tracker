from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QScrollArea, QLabel, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox
from PyQt5.QtGui import QIcon, QFont
import sys


class HeaderFrame(QFrame):
    """
    Frame for header of home window containing labels
    for name, birthday, and "Add Person" button
    """

    def __init__(self):
        super().__init__()
        self.init_frame()

    def init_frame(self):

        self.setFrameStyle(QFrame.StyledPanel)
        self.setMinimumHeight(75)
        self.setMinimumWidth(420)
        self.setContentsMargins(6, 10, 6, 10)

        self.create_frame_content()

    def create_frame_content(self):

        self.name_label = QLabel("Name")
        self.name_label.setStyleSheet("padding-left: 15")
        self.name_label.setFont(QFont("Arial", 10))

        self.birthday_label = QLabel("Birthday")
        self.birthday_label.setStyleSheet("padding-left: 15")
        self.birthday_label.setFont(QFont("Arial", 10))

        self.add_button = QPushButton("+")
        self.add_button.setStyleSheet("border: 10; border-radius: 20")
        self.add_button.setMinimumHeight(37.5)

        self.hbox = QHBoxLayout()
        self.hbox.setContentsMargins(0, 10, 0, 10)
        self.hbox.setSpacing(0)

        self.hbox.addWidget(self.name_label, stretch=2)
        self.hbox.addWidget(self.birthday_label, stretch=2)
        self.hbox.addWidget(self.add_button, stretch=1)

        self.setLayout(self.hbox)


class BirthdayGroupBox(QGroupBox):
    """
    Frame containing BirthdayFrame()'s in a vertical layout
    """

    def __init__(self):
        super().__init__()
        self.title = "Today's Birthdays"
        self.init_groupbox()

    def init_groupbox(self):
        self.setTitle(self.title)
        self.setContentsMargins(0, 0, 0, 0)


class TodayBirthdayFrame(QFrame):
    """
    Frame containing information about a person whose
    birthday is in the current day
    """

    def __init__(self):
        super().__init__()
        self.init_frame()

    def init_frame(self):
        self.setFrameStyle(QFrame.StyledPanel)
        self.setMaximumHeight(150)
        self.setMinimumHeight(150)
        self.setContentsMargins(6, 10, 6, 10)

    def create_frame_content(self):
        pass


class UpcomingBirthdayGroupBox(QGroupBox):
    """
    group box containing all birthday frames in a
    vertical layout
    """

    def __init__(self):
        super().__init__()
        self.title = "Upcoming Birthdays"
        self.init_groupbox()

    def init_groupbox(self):
        self.setTitle(self.title)
        self.setContentsMargins(0, 0, 0, 0)


class BirthdayFrame(QFrame):
    """
    most basic birthday frame containing name, birthday,
    and categorical icon of person
    """

    def __init__(self):
        super().__init__()
        self.init_frame()

    def init_frame(self):
        self.setFrameStyle(QFrame.StyledPanel)
        self.setMaximumHeight(150)
        self.setMinimumHeight(150)
        self.setContentsMargins(6, 10, 6, 10)

        self.create_frame_content()

    def create_frame_content(self):
        pass


class HomeWindow(QScrollArea):
    """
    window that shows the first thing a user sees
    when the app is opened
    """

    def __init__(self):
        super().__init__()

        self.title = "Home Window"

        self.init_window()

    def init_window(self):
        self.setGeometry(100, 100, 420, 450)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setWidgetResizable(True)

        self.header_frame = HeaderFrame()

        self.birthday_frame1 = TodayBirthdayFrame()

        self.bday_vbox = QVBoxLayout()
        self.bday_vbox.setContentsMargins(0, 10, 0, 0)
        self.bday_vbox.addWidget(self.birthday_frame1)

        self.birthday_groupbox = BirthdayGroupBox()
        self.birthday_groupbox.setLayout(self.bday_vbox)

        self.upcoming_birthday_frame = BirthdayFrame()

        self.upcoming_bday_vbox = QVBoxLayout()
        self.upcoming_bday_vbox.setContentsMargins(0, 10, 0, 0)
        self.upcoming_bday_vbox.addWidget(self.upcoming_birthday_frame)

        self.upcoming_bday_groupbox = UpcomingBirthdayGroupBox()
        self.upcoming_bday_groupbox.setLayout(self.upcoming_bday_vbox)

        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.addWidget(self.header_frame)
        self.vbox.addWidget(self.birthday_groupbox)
        self.vbox.addWidget(self.upcoming_bday_groupbox)
        self.vbox.addStretch()

        self.center_widget = QWidget()
        self.center_widget.setLayout(self.vbox)

        self.setWidget(self.center_widget)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(App.exec())
