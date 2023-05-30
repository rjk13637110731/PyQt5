import sys  # 导入系统

from Designer import HorizontalVertical

from PyQt5.QtWidgets import QApplication, QMainWindow   # 导入两个重要类

# 解决设计UI与运行结果不一致问题
from PyQt5 import QtCore
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

if __name__ == "__main__":  # 只有从当前应用程序才能运行程序
    # 创建QApplication类的实例
    app = QApplication(sys.argv)

    # 创建一个窗口
    mainWindow = QMainWindow()

    # 创建UI对象
    ui = HorizontalVertical.Ui_MainWindow()

    # 向主窗口中添加控件，输入参数是主窗口对象
    ui.setupUi(mainWindow)

    # 显示窗口
    mainWindow.show()

    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())