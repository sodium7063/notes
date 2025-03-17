from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from login import Ui_MainWindow


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()  # 创建Ui_MainWindow类的实例
        self.ui.setupUi(self)  # 调用setupUi方法，将UI布局添加到主窗口中


def main():
    app = QApplication([])
    window = Main_Window()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
