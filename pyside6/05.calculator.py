from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Qt
from calculator_ui import Ui_Calculator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = Ui_Calculator()
        self.calculator.setupUi(self)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
