# coding=utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import QString


class ContentWidget(QDialog):
    def __init__(self, parent=None):
        super(ContentWidget, self).__init__(parent)
        self.setStyleSheet("background: black")


class IndexWidget(QDialog):
    def __init__(self, parent=None):
        super(IndexWidget, self).__init__(parent)
        self.setStyleSheet("background: red")


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.resize(400, 300)
        self.mContent = ContentWidget()
        self.mIndex = IndexWidget()
        self.addTab(self.mContent, u"内容")
        self.addTab(self.mIndex, u"索引")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    t = TabWidget()
    t.show()
    app.exec_()