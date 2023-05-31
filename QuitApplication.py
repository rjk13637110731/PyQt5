import sys

from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

# 解决设计UI与运行结果不一致问题
from PyQt5 import QtCore
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle("退出应用程序")

        # 添加Button
        self.button1 = QPushButton("退出应用程序")

        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        # 发射信号
        sender = self.sender()
        print(sender.text() + "按钮被按下")
        # 实例化
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建类
    main = QuitApplication()

    # 显示窗口
    main.show()

    sys.exit(app.exec_())
