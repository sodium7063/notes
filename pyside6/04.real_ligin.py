from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from login import Ui_Login_UI


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Login_UI()  # 创建Ui_MainWindow类的实例
        self.ui.setupUi(self)  # 调用setupUi方法，将UI布局添加到主窗口中
        self.ui.pushButton.clicked.connect(self.loginFunc)

    def loginFunc(self):
        username = self.ui.userNameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        print(f"用户名：{username}，密码：{password}")
        if username == "admin" and password == "123456":
            print("登录成功")
        else:
            print("登录失败")


def main():
    app = QApplication([])
    window = Main_Window()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
