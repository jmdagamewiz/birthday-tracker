from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QScrollArea, QLabel, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox, QStackedWidget
from PyQt5.QtGui import QIcon, QFont
import sys
from home_window import HomeWindow
from list_all_window import ListAllWindow
from add_person_window import AddPersonWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "Birthday Tracker"

        self.init_window()

    def init_window(self):
        self.setGeometry(100, 100, 420, 450)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("assets/icon.png"))

        self.create_stack_layout()

    def create_stack_layout(self):
        self.stack = QStackedWidget()
        self.stack.addWidget(HomeWindow())
        self.stack.addWidget(ListAllWindow())
        self.stack.addWidget(AddPersonWindow())

        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.addWidget(self.stack)

        self.center_widget = QWidget()
        self.center_widget.setLayout(self.vbox)
        self.setCentralWidget(self.center_widget)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(App.exec())
