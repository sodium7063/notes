# 信号与槽 signal and slot

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import Qt


class Main_Window(QWidget):
    def __init__(self):
        super().__init__()

        btn = QPushButton("click me", self)
        btn.clicked.connect(self.hello)  # connect signal and slot

    def hello(self):
        print("hello world")


def main():
    app = QApplication([])
    window = Main_Window()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
