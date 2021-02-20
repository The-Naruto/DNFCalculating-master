# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 9:09
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : DNFCalculating-master

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTreeWidget,QMainWindow,QTreeWidgetItem,QMessageBox,QPushButton,QVBoxLayout,QTextBrowser,QLabel,QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,pyqtSignal
import json
import os


class Example(QMainWindow):

    dialogSignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.initData()
        self.initUI()

    # 初始化角色数据
    def initData(self):
        if not os.path.exists('./ResourceFiles'):
            QMessageBox.information(self, "解压错误", "未找到资源文件，请将压缩包中ResourceFiles解压到同目录后打开计算器")
            self.close()
        self.adventures = []
        with open("ResourceFiles/Config/adventure_info.json", encoding='utf-8') as fp:
            self.adventures = json.load(fp)
        # 删掉小魔女,女圣职者
        # print(self.adventures[39],self.adventures[45])
        self.adventures.pop(45)
        self.adventures.pop(39)

        self.adventures_class = []
        for adv in self.adventures:
            dazhiye = adv.get("职业系")
            if dazhiye not in self.adventures_class:
                self.adventures_class.append(dazhiye)
        # print(self.adventures)
        self.big_class = {"鬼剑士":['鬼剑士(男)', '鬼剑士(女)'],"格斗家":['格斗家(男)', '格斗家(女)'],
                     "神枪手":['神枪手(男)', '神枪手(女)'],"魔法师":['魔法师(男)', '魔法师(女)'],
                     "圣职者":['圣职者(男)', '圣职者(女)'],"暗夜守护者":['暗夜使者','守护者'],
                     "其它":['魔枪士', '枪剑士', '外传']}


    def initUI(self):
        self.tree = QTreeWidget(self)
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["职业名","开发者"])
        self.setCentralWidget(self.tree)
        self.tree.setColumnWidth(0,270)

        # 创建根节点
        root = QTreeWidgetItem()
        root.setText(0,"全选")
        root.setCheckState(0, Qt.Unchecked)

        # 创建大类节点
        for name in self.big_class.keys():
            exec(name+' = QTreeWidgetItem(root)')
            exec(name+'.setText(0,''''name'''')')
            exec(name+'.setCheckState(0, Qt.Unchecked)')

        def replaceStr(str):
            return str.replace('(', '1').replace(')', '2')

        def recoverStr(str):
            return str.replace('1', '(').replace('2', ')')

        # 创建小类节点
        for name in self.big_class.items():
            for chd in name[1]:
                exec(replaceStr(chd)+' =QTreeWidgetItem('+name[0]+')')
                exec(replaceStr(chd)+'.setText(0,''''chd'''')')
                exec(replaceStr(chd)+'.setCheckState(0, Qt.Unchecked)')

        # 创建具体职业节点
        for adv in self.adventures:
            sub_class = replaceStr(adv.get("职业系"))
            zhiye = adv.get("类名2")
            if len(zhiye)==1:
                zhiye = adv.get("显示名称")

            var_name = replaceStr(adv.get("转职名称"))
            zuozhe = adv.get("作者")
            if len(var_name)==0:
                continue
            # print(sub_class,var_name)
            # 格斗和枪手追加性别字符
            if '格斗家' in sub_class or '神枪手' in sub_class:
                zhiye = zhiye+'·'+sub_class.split('1')[1][0]

            exec(var_name+' =QTreeWidgetItem(' +sub_class+ ')')
            exec(var_name+'.setText(0,''''zhiye'''')')
            exec(var_name+'.setText(1,''''zuozhe'''')')
            exec(var_name+'.setCheckState(0, Qt.Unchecked)')

        self.tree.addTopLevelItem(root)
        self.tree.expandAll()

        self.tree.itemChanged.connect(self.handleChanged)
        # print(self.tree.topLevelItem(0).text(0))

        self.setGeometry(300, 300, 500, 700)
        self.setWindowTitle('QTreeWidget')
        # self.show()



    # 根据选择
    def handleChanged(self, item, column):
        count = item.childCount()
        if item.checkState(column) == Qt.Checked:
            for index in range(count):
                item.child(index).setCheckState(0, Qt.Checked)
        if item.checkState(column) == Qt.Unchecked:
            for index in range(count):
                item.child(index).setCheckState(0, Qt.Unchecked)

    def getChecked(self,node):
        checked = []
        for cd_index in range(node.childCount()):
            item = node.child(cd_index)
            # 判断是否还有子分支
            if item.childCount():
                checked.extend(self.getChecked(item))
            else:
                if item.checkState(0) == Qt.Checked:
                    checked.append(item.text(0))
        # 由于计算多个职业的时候,前面的会丢失,故多计算一次前面的几个

        return checked


    def closeEvent(self,e):
        res = self.getChecked(self.tree.topLevelItem(0))
        self.dialogSignal.emit(res)
        self.destroy()
        # print(res)


class NewMainForm(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox =  QVBoxLayout()
        vbox.addStretch(1)
        btn1 = QPushButton("单职业计算/配置")
        # self.btn.move(50, 50)
        btn1.setMinimumWidth(120)
        btn1.clicked.connect(self.closeself)

        btn2 = QPushButton("多职业选择")
        # self.btn.move(50, 50)
        btn2.setMinimumWidth(120)
        btn2.clicked.connect(self.openDialog)

        self.textB =  QTextBrowser()
        self.textB.setText("尚未选择任何职业!")
        self.lable =QLabel()
        self.showResult(0)
        # self.lable.setText("当前选择了0个职业,预计需要0分钟!")

        calc_btn = QPushButton("开始计算")
        calc_btn.clicked.connect(self.calc)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(self.textB)
        vbox.addWidget(self.lable)
        vbox.addWidget(calc_btn)

        self.setLayout(vbox)

        self.setGeometry(30, 30, 380, 300)
        self.setWindowTitle('QTreeWidget')
        # self.show()

    def calc(self):

        pass



    def closeself(self):
        self.close()

    def showResult(self,changdu):
        self.lable.setText("当前选择了%d个职业,预计需要0分钟!"%(changdu))

    def openDialog(self):

        self.dialog = Example()

       # 连接【子窗口自定义消息和主窗口槽函数】
        self.dialog.dialogSignal.connect(self.slot_emit)
        self.dialog.show()

    def slot_emit(self,choose_list):
        # print("主窗口：method_2")
        changdu = len(choose_list)
        self.showResult(changdu)
        self.textB.setText(str(choose_list))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewMainForm()
    ex.show()
    sys.exit(app.exec_())






