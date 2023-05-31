# QDesktopWidget
import sys

from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
from PyQt5.QtGui import QIcon

# 解决设计UI与运行结果不一致问题
from PyQt5 import QtCore

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class CenterForm(QMainWindow):  # CenterForm类继承QMainWindow类
    def __init__(self, parent=None):
        super(CenterForm, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle("让窗口居中")

        # 设置窗口的尺寸
        self.resize(400, 300)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        self.move(newLeft,newTop)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建类
    main = CenterForm()

    # 显示窗口
    main.show()

    sys.exit(app.exec_())
