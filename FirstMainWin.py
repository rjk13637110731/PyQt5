import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

# 解决设计UI与运行结果不一致问题
from PyQt5 import QtCore

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class FirstMainWin(QMainWindow):  # FirstMainWin类继承QMainWindow类
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")

        # 设置窗口的尺寸
        self.resize(400, 300)

        # 获得状态栏
        self.status = self.statusBar()

        # 在状态栏上显示消息
        self.status.showMessage("只存在5s消息", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./imgs/AutoCAD-360.icon.png'))

    # 创建类
    main = FirstMainWin()

    # 显示窗口
    main.show()

    sys.exit(app.exec_())
