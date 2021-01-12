import sys
from functools import partial

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from qtpy import QtCore
from AndroidUtils import *
from PcUtils import *
from WebUtils import *

from Ui_MainWindow import Ui_Form


class MainWindow(QMainWindow,Ui_Form):

    def __init__(self):
        super(MainWindow, self).__init__()
        sys.path.append(r'static\adb\windows')

        self.setupUi(self)
        self.connectionSlot()
        self.otherSignals()

    def connectionSlot(self):
        # 信号
        self.android_starter.clicked.connect(self.choose_android)
        self.web_starter.clicked.connect(self.choose_web)
        self.pc_starter.clicked.connect(self.choose_pc)


    def otherSignals(self):
        #self.btn_refresh.clicked.connect(self.choose_android)  # 刷新ADB
        self.btn_path.clicked.connect(partial(self.selectfolder))  # 选取文件夹
        self.btn_report.clicked.connect(partial(self.openfolder))
        return



    #警告弹窗
    def messageDialog(self,title,news):
        msg_box = QMessageBox(QMessageBox.Warning,title,news)
        msg_box.exec_()

    """选取文件夹"""

    def selectfolder(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        print(directory1)
        self.LScriptsRoot.setText(directory1)
        self.caseAbsolutePath = directory1

    """打开报告文件夹"""

    def openfolder(self):
        '''打开系统文件资源管理器的对应文件夹'''
        #folder = AndroidUtils.report_folder
        folder = 'report_pages'
        # 方法1：通过start explorer
        os.system("start explorer %s" % folder)
        # 方法2：通过startfile
        # os.startfile(folder)


    def choose_android(self):
        AndroidUtils.UiVariety(main)#页面变化
        """生成设备单选按钮列表"""
        AndroidUtils.GetValidDevices(main)
        """生成脚本单选按钮列表"""
        AndroidUtils.get_test_cases('scripts',main)
        self.btn_start.clicked.connect(partial(AndroidUtils.startUp,main))  #启动信号


        return

    def choose_pc(self):
        PcUtils.UiVariety(main)
        PcUtils.get_test_cases('scripts', main)
        self.btn_start.clicked.connect(partial(PcUtils.startUp, main))  # 启动信号

    def choose_web(self):
        WebUtils.UiVariety(main)
        WebUtils.get_test_cases('scripts', main)
        self.btn_start.clicked.connect(partial(WebUtils.ran_case, main))  # 启动信号






if __name__ == '__main__':
    #创建应用程序
    app = QApplication(sys.argv)
    #创建窗口
    main = MainWindow()
    #显示窗口
    main.show()
    #事件循环
    sys.exit(app.exec_())