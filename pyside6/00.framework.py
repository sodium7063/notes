from PySide6.QtWidgets import QApplication, QMainWindow  # 导入两个必要的模块


class MyWindow(QMainWindow):  # 定义窗口，集成QMainWindow并实现其构造函数
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
