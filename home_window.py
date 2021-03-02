from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QScrollArea, QLabel, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QStackedWidget
from PyQt5.QtGui import QIcon, QFont
import sys

# TODO: make person class and make storage class
# TODO: make add person window (also contains list of all people and allows user
# TODO: to delete people from list)


class HeaderFrame(QFrame):
    """
    Frame for header of home window containing labels
    for name, birthday, and "Add Person" button
    """

    def __init__(self):
        super().__init__()
        self.init_frame()

    def init_frame(self):

        self.create_frame_content()

    def create_frame_content(self):

        self.name_label = QLabel("Birthday Tracker App")
        font = QFont("Arial", 10)
        font.setBold(True)
        self.name_label.setFont(font)

        self.list_all_button = QPushButton("List All")
        self.list_all_button.clicked.connect(self.go_to_list_all_window)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.name_label)
        self.hbox.addStretch()
        self.hbox.addWidget(self.list_all_button)

        self.setLayout(self.hbox)

    def go_to_list_all_window(self):
        parent = self.parentWidget()
        while True:
            if type(parent) == QStackedWidget:
                break
            parent = parent.parentWidget()
        parent.setCurrentIndex(1)


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


class TodayBirthdayFrame(QFrame):
    """
    Frame containing information about a person whose
    birthday is in the current day
    """

    def __init__(self, name, birthday):
        super().__init__()
        self.name = name
        self.birthday = birthday
        self.init_frame()

    def init_frame(self):
        self.setFrameStyle(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Plain)
        self.create_frame_content()

    def create_frame_content(self):

        self.birthday_frame = BirthdayFrame(self.name, self.birthday)

        self.message_label = QLabel(f"It's {self.name}'s birthday today!")
        self.greet_button = QPushButton("Greet him!")
        self.greet_button.clicked.connect(self.go_to_greet_window)

        self.hbox = QHBoxLayout()
        self.hbox.addSpacing(10)
        self.hbox.addWidget(self.message_label)
        self.hbox.addStretch()
        self.hbox.addWidget(self.greet_button)
        self.hbox.addSpacing(10)

        self.vbox = QVBoxLayout()
        # TODO: Understand how .setContentsMargins affects other widgets
        self.vbox.setContentsMargins(0, 0, 0, 4)
        self.vbox.addWidget(self.birthday_frame)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

    def go_to_greet_window(self):
        parent = self.parentWidget()
        while True:
            if type(parent) == QStackedWidget:
                break
            parent = parent.parentWidget()
        parent.setCurrentIndex(3)



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


class BirthdayFrame(QFrame):
    """
    most basic birthday frame containing name, birthday,
    and categorical icon of person
    """

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

        # HEADER FRAME
        self.header_frame = HeaderFrame()

        # TODAY BIRTHDAY FRAMES
        self.today_birthday_frame1 = TodayBirthdayFrame("Jeremy Bearimy", "February 27")
        self.today_birthday_frame2 = TodayBirthdayFrame("Tom the Cat", "February 27")

        self.bday_vbox = QVBoxLayout()
        self.bday_vbox.addWidget(self.today_birthday_frame1)
        self.bday_vbox.addWidget(self.today_birthday_frame2)

        self.birthday_groupbox = BirthdayGroupBox()
        self.birthday_groupbox.setLayout(self.bday_vbox)

        # UPCOMING BIRTHDAY FRAMES
        self.upcoming_bday_frame1 = BirthdayFrame("Elon Musk", "June 28")
        self.upcoming_bday_frame2 = BirthdayFrame("Bill Gates", "October 28")

        self.upcoming_bday_vbox = QVBoxLayout()
        self.upcoming_bday_vbox.addWidget(self.upcoming_bday_frame1)
        self.upcoming_bday_vbox.addWidget(self.upcoming_bday_frame2)

        self.upcoming_bday_groupbox = UpcomingBirthdayGroupBox()
        self.upcoming_bday_groupbox.setLayout(self.upcoming_bday_vbox)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.header_frame)
        self.vbox.addWidget(self.birthday_groupbox)
        self.vbox.addWidget(self.upcoming_bday_groupbox)
        self.vbox.addStretch()

        self.center_widget = QWidget()
        self.center_widget.setLayout(self.vbox)

        self.setWidget(self.center_widget)
