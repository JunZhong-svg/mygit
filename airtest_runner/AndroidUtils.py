# -*- coding: utf-8 -*-


from MainWindow import *

from PyQt5.QtWidgets import QCheckBox, QListWidgetItem, QFileDialog
from airtest.core.android.adb import ADB


class AndroidUtils():
    def __init__(self):
        return

    def UiVariety(self,window):
        window.android_starter.setStyleSheet("background-color: red")
        window.pc_starter.setStyleSheet("background-color: (240,240,240)")
        window.web_starter.setStyleSheet("background-color: (240,240,240)")
        window.box_devices.setVisible(True)
        window.label_3.setVisible(False)
        window.box_devices.setVisible(True)
        window.box_runcase.setVisible(True)
        window.checkBox_devices.setVisible(True)
        window.btn_refresh.setVisible(True)
        window.label_2.setVisible(False)
        window.listWidget_devices.setVisible(True)
        window.textEdit.setVisible(False)
        window.box_runcase.setGeometry(QtCore.QRect(540, 110, 291, 451))
        _translate = QtCore.QCoreApplication.translate
        window.label_readme.setText(_translate("Form",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;  border:none;\n"
                                             "        border-bottom:1px solid white;  padding:2px 4px;border-radius:10px;\">\n"
                                             "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">安卓-Airtest启动器使用方法</p>\n"
                                             "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.选择执行设备和执行脚本</p>\n"
                                             "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.点击【启动脚本】按钮</p></body></html>"))

        return


    """设备"""

    def RefreshADB(self): #刷新ADB
        if len(self.buttonList) != 0:
            for index, but in enumerate(self.buttonList):
                but.deleteLater()
                self.itemList[index].deleteLater()

        self.GetValidDevices()

    def GetValidDevices(self,window):
        """获取本地连接的设备号列表"""
        #lData = ADB().devices('device')
        lData = ['设备1','设备2','设备3']
        #lPositiveDevices = [item[0] for item in lData]
        lPositiveDevices = [item for item in lData]
        self.GenerateDeviceIDButton(lPositiveDevices,window)
        return lPositiveDevices

    def GenerateDeviceIDButton(self, devices,window):
        window.listWidget_devices.clear()#清空内容
        self.selectedDevice = []  # 选中的设备列表
        """根据设备号列表生成按钮"""
        self.buttonList = [QCheckBox(device) for device in devices]
        self.itemList = [QListWidgetItem() for i in devices]
        for index, button in enumerate(self.buttonList):
            button.setChecked(False)
            window.listWidget_devices.addItem(self.itemList[index])
            button.stateChanged.connect(partial(self.SelectedDevice, button,window))
            window.listWidget_devices.setItemWidget(self.itemList[index], self.buttonList[index])

        # 全选按钮信号
        window.checkBox_devices.clicked.connect(partial(self.SelectAllDevice, self.buttonList,window))

    def SelectedDevice(self, dev,window):
        """选中的设备"""
        if dev.isChecked() == True:
            self.selectedDevice.append(dev.text())
        elif dev.isChecked() == False:
            window.checkBox_devices.setChecked(False)
            for i in self.selectedDevice:
                if dev.text() == i:
                    self.selectedDevice.remove(i)

        self.selectedDevice = list(set(self.selectedDevice))  # 清除重复的元素
        print(self.selectedDevice)

    def SelectAllDevice(self, buttonList,window):
        """全选设备和取消全选"""
        if window.checkBox_devices.isChecked() == True:
            for button in buttonList:
                button.setChecked(True)
                if button.text() in self.selectedDevice:
                    continue
                self.selectedDevice.append(button.text())

        elif window.checkBox_devices.isChecked() == False:
            for button in buttonList:
                button.setChecked(False)
                for i in self.selectedDevice:
                    if button.text() == i:
                        self.selectedDevice.remove(i)
        # print(self.selectedDevice)
        return

    """脚本"""

    def get_test_cases(self, path,main):
        # 空列表接收返回值
        self.case_paths = []
        # 遍历传入的路径
        for file in os.listdir(path):
            # 是已air尾缀结尾，并且不是二进制文件
            if file.endswith('.air') and not os.path.isfile(path):
                self.case_paths.append(os.path.basename(file))
        print(self.case_paths)
        self.caseButton(self.case_paths,main)
        return self.case_paths

    def caseButton(self, case_paths,main):
        main.listWidget_case.clear()  # 清空内容
        self.selectedCase = []  # 选中的脚本列表
        """生成按钮"""
        self.caseButtonList = [QCheckBox(case) for case in case_paths]
        self.caseItemList = [QListWidgetItem() for i in case_paths]
        for index, caseButton in enumerate(self.caseButtonList):
            caseButton.setChecked(False)
            main.listWidget_case.addItem(self.caseItemList[index])
            caseButton.stateChanged.connect(partial(self.SelectedCase, caseButton,main))
            main.listWidget_case.setItemWidget(self.caseItemList[index], self.caseButtonList[index])
            # 全选脚本信号
            main.checkBox_case.clicked.connect(partial(self.SelectAllCase, self.caseButtonList,main))

    def SelectedCase(self, caseButton,main):
        if caseButton.isChecked() == True:
            self.selectedCase.append(caseButton.text())
        elif caseButton.isChecked() == False:
            main.checkBox_devices.setChecked(False)
            for i in self.selectedCase:
                if caseButton.text() == i:
                    self.selectedCase.remove(i)

        self.selectedCase = list(set(self.selectedCase))  # 清除重复的元素
        print(self.selectedCase)

    def SelectAllCase(self, caseButtonList,main):

        """全选脚本和取消全选"""
        if main.checkBox_case.isChecked() == True:
            for button in caseButtonList:
                button.setChecked(True)
                if button.text() in self.selectedCase:
                    continue
                self.selectedCase.append(button.text())

        elif main.checkBox_devices.isChecked() == False:
            for button in caseButtonList:
                button.setChecked(False)
                for i in self.selectedCase:
                    if button.text() == i:
                        self.selectedCase.remove(i)
        # print(self.selectedDevice)
        return self.selectedCase

    def startUp(self,main):
        """一台设备创建一个线程"""
        if self.selectedDevice == []:
            print('请连接设备')
            main.messageDialog('警告', '请连接设备')
            return
        elif self.selectedCase == []:
            print('请选择脚本')
            main.messageDialog('警告', '请选择脚本')
            return
        threads = [threading.Thread(target=self.ran_case, args=(devID,)) for devID in self.selectedDevice]
        for t in threads:  # 开启线程
            print('子线程')
            t.start()
        for t in threads:  # 等待子线程结束
            t.join()
        main.messageDialog('测试结束', '请查看报告！')
        return

    def ran_case(self, devID,main):
        now_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        self.caseAbsolutePaths = []  # 脚本的地址列表
        caseAbsolutePath = os.path.abspath('scripts')  # 获取脚本所在的绝对目录
        for caseName in self.selectedCase:
            print(caseName)
            self.caseAbsolutePaths.append(os.path.join(caseAbsolutePath, caseName))
        print(self.caseAbsolutePaths)

        for index, case_name in enumerate(self.selectedCase):
            # 日志存放的地方
            self.log_path = os.path.abspath(
                'logs_root/{devices}/{now_time}/{case_name}/log'.format(devices=devID, case_name=case_name,
                                                                        now_time=now_time))
            # 报告地址以及报告的名称
            self.report_path = os.path.abspath(
                'report_pages/{devices}/{now_time}/{name}/report'.format(devices=devID, name=case_name,
                                                                         now_time=now_time))
            # 报告文件夹
            self.report_folder = 'report_pages'

            # 验证日志存放的地址是否已经存在
            if os.path.exists(self.log_path):
                shutil.rmtree(self.log_path)
            else:
                os.makedirs(self.log_path)
            # 验证存放报告的目录是否存在
            if not os.path.exists(self.report_path):
                os.makedirs(self.report_path)

            # 执行脚本
            command = 'python -m airtest run {testcase_path} --device Android:///{devID}  --log {log_path}'.format(
                testcase_path=self.caseAbsolutePaths[index],
                log_path=self.log_path, devID=devID)
            os.system(command)
            # 生成报告
            command_report = 'python -m airtest report {testcase_path} --log_root {log_path} --outfile log.html --lang zh --plugin airtest_selenium.report --export {report_path} '.format(
                testcase_path=self.caseAbsolutePaths[index], log_path=self.log_path, report_path=self.report_path)

            os.system(command_report)
        return



AndroidUtils = AndroidUtils()
