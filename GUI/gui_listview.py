'''
@Author: your name
@Date: 2020-07-13 20:00:37
@LastEditTime: 2020-07-13 20:19:13
@LastEditors: Please set LastEditors
@Description: 构造一个ListView，用来显示与图对应的列表\

@FilePath: \SciMetrics\GUI\gui_listview.py
'''

import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import PySide2
import typing


class SciTreeItem(object):
    def __init__(self, data=list(), parent=None):
        self._children = []
        self._item_data = data
        self._parent = parent

    def parent(self):
        return self._parent

    def append_child(self, child):
        self._children.append(child)

    def child(self, row):
        if row < 0 or row >= len(self._children):
            return None
        return self._children[row]

    def children_count(self):
        return len(self._children)

    def column_count(self):
        return len(self._item_data)

    def data(self, column):
        if column < 0 or column > len(self._item_data):
            return None
        return self._item_data[column]

    def row(self):
        if not self.parent:
            return 0
        return self.parent._children.index(self)

class SciTreeModel(QAbstractItemModel):
    def __init__(self, headers, parent=None):
        super(SciTreeModel, self).__init__(parent)
        self.root_item = SciTreeItem(headers)

    def setup_model_data(self, data):
        for item in data:
            new_item = SciTreeItem(item, self.root_item)
            self.root_item.append_child(new_item)

    def parent(self, child: PySide2.QtCore.QModelIndex=...)-> PySide2.QtCore.QModelIndex:
        if not child.isValid():
            return QModelIndex()
        child_item = child.internalPointer()
        parent_item = child_item.parent()
        if (parent_item == self.root_item):
            return QModelIndex()
        return self.createIndex(parent_item.row(), 0, parent_item)


    def rowCount(self, parent:PySide2.QtCore.QModelIndex=...) -> int:
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()
        return parent_item.children_count()

    def columnCount(self, parent:PySide2.QtCore.QModelIndex=...) -> int:
        if parent.isValid():
            # print(parent.internalPointer().columnCount())
            return parent.internalPointer().columnCount()
        # print(self.root_item.column_count())
        return self.root_item.column_count()


    def data(self, index:PySide2.QtCore.QModelIndex, role:int=...) -> typing.Any:
        if index.isValid() is False:
            return None
        if role != Qt.DisplayRole:
            return None
        item = index.internalPointer()
        return item.data(index.column())

    def flags(self, index:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags:
        if not index.isValid():
            return Qt.NoItemFlags
        return QAbstractItemModel.flags(self,index)

    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...) -> typing.Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.root_item.data(section)
        return None

    def index(self, row:int, column:int, parent:PySide2.QtCore.QModelIndex=...) -> PySide2.QtCore.QModelIndex:
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)
        return QModelIndex()

    def sort(self, column:int, order:PySide2.QtCore.Qt.SortOrder=...):
        self.layoutAboutToBeChanged.emit()
        print('{}-{}-{}'.format(column, order, 'will be sorted'))
        self.layoutChanged.emit()


# class



class SciListView(QTreeView):
    def __init__(self, parent=None):
        super(SciListView, self).__init__(parent)
        self.initUI()
        self.initSignal()
        self.initData()

    def initUI(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setSortingEnabled(True)
        # self.layout = QVBoxLayout(self)
        # self.listview = QTreeView(self)
        # self.layout.addWidget(self.listview)
        # self.setLayout(self.layout)

    def initSignal(self):
        self.customContextMenuRequested.connect(self.slot_custom_context_menu)

    def initData(self):
        pass
        # headers = ['column1', 'column2']
        # data = [['item1','item1'], ['item2', 'item2']]
        # model = SciTreeModel(headers)
        # model.setup_model_data(data)
        # # model.setRootPath(QDir.currentPath())
        # self.listview.setModel(model)
    def setData(self, headers:list, data:list):
        model = SciTreeModel(headers)
        model.setup_model_data(data)
        proxy = QSortFilterProxyModel(self)
        proxy.setSourceModel(model)
        self.setModel(proxy)

    @Slot()
    def slot_custom_context_menu(self):
        print("Right clicked, Hello!")

