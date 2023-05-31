# 显式控件提示信息

import sys

# 导入QToolTip类
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

# 解决设计UI与运行结果不一致问题
from PyQt5 import QtCore

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("Sans-Serif", 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300, 200, 300)
        self.setWindowTitle("设置控件提示消息")

        self.button1 = QPushButton("我的按钮")
        self.button1.setToolTip("这是一个按钮，Are You OK？")
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建类
    main = TooltipForm()

    # 显示窗口
    main.show()

    sys.exit(app.exec_())
