from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("那我问你", self)
        btn.setGeometry(50, 50, 200, 50)
        btn.setToolTip("使用`setToolTip`方法设置按钮的提示信息")
        btn.setText("ciallo~")
        # 更多的属性设置可以直接在designer中检查

        # 接下来是Qlabel
        lb = QLabel("这是一个标签", self)
        lb.setText("使用`setText`方法设置标签的文本")
        # 当参数需要传入一个0x引导的十六进制数字的时候，需要导包`PySide6.QtCore`，参考本文件的第二行
        lb.setAlignment(Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()
