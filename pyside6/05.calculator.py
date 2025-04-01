from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Qt
from calculator_ui import Ui_Calculator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.result = ""  # 储存计算结果

        self.calculator = Ui_Calculator()
        self.calculator.setupUi(self)

    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.addNumber("0"))
        self.pushButton_1.clicked.connect(lambda: self.addNumber("1"))
        self.pushButton_2.clicked.connect(lambda: self.addNumber("2"))
        self.pushButton_3.clicked.connect(lambda: self.addNumber("3"))
        self.pushButton_4.clicked.connect(lambda: self.addNumber("4"))
        self.pushButton_5.clicked.connect(lambda: self.addNumber("5"))
        self.pushButton_6.clicked.connect(lambda: self.addNumber("6"))
        self.pushButton_7.clicked.connect(lambda: self.addNumber("7"))
        self.pushButton_8.clicked.connect(lambda: self.addNumber("8"))
        self.pushButton_9.clicked.connect(lambda: self.addNumber("9"))

        self.pushButton_add.clicked.connect(lambda: self.addNumber("+"))
        self.pushButton_reduce.clicked.connect(lambda: self.addNumber("-"))
        self.pushButton_multiply.clicked.connect(lambda: self.addNumber("*"))
        self.pushButton_divide.clicked.connect(lambda: self.addNumber("/"))

        # self.pushButton_equal.clicked.connect(self.calculate_result)
        # self.pushButton_clear.clicked.connect(self.clear_result)
        # self.pushButton_delete.clicked.connect(self.delete_last_character)

    def addNumber(self, number):
        self.lineEdit.clear()
        self.result += number
        self.calculator.lineEdit.setText(self.result)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
