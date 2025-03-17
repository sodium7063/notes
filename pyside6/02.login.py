# 本节中使用Designer设计UI界面并进行导出和保存
# 具体来说，第一步：在Designer设计好界面，保存为.ui文件
# 第二步：使用pyside6-uic 将 .ui 文件转为 .py 文件 （其实也可以直接在vsc的资源管理器右键 .ui 文件实现）
# 第三步：在代码中导入该.py文件，即本文件的内容
from PySide6.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow  # 从转化的login.py中导入Ui_MainWindow类


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()  # 创建Ui_MainWindow类的实例
        self.ui.setupUi(self)  # 调用setupUi方法，将UI布局添加到主窗口中


# 下面展示一个使用了多继承方法的示例
class second_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


def main_m1():
    app = QApplication([])
    window = main_window()
    window.show()
    app.exec()


def main_m2():
    app = QApplication([])
    window = second_window()
    window.show()
    app.exec()


if __name__ == "__main__":
    main_m1()
