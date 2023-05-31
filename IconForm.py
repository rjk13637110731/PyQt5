import sys

'''
窗口的setWindowIcon方法用于设置窗口的图标，只在Windows中可用

QApplication中的setWindowIcon方法用于设置主窗口的图标与应用程序的图标，
但是调用了窗口的setWindowIcon方法，QApplication中的setWindowIcon方法就只能用于设置应用程序图标了
'''

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

# 解决设计UI与运行结果不一致问题
from PyQt5 import QtCore

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class IconForm(QMainWindow):  # FirstMainWin类继承QMainWindow类
    def __init__(self, parent=None):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 同时设置窗口的位置和尺寸
        self.setGeometry(300, 300, 250, 250)

        # 设置主窗口的标题
        self.setWindowTitle("设置窗口图标")

        # 设置窗口图标
        self.setWindowIcon(QIcon('./imgs/AutoCAD-360.icon.png'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('./imgs/AutoCAD-360.icon.png'))

    # 创建类
    main = IconForm()

    # 显示窗口
    main.show()

    sys.exit(app.exec_())
