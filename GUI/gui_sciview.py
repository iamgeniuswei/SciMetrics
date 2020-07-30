from GUI.gui_listview import *
from GUI.gui_networkview import *
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import networkx as nx




class SciViewController(QWidget):
    signal_zoomout_clicked = Signal()
    singal_zoomin_clicked = Signal()
    singal_remove_clicked = Signal()
    singal_core_clicked = Signal()
    def __init__(self, parent=None):
        super(SciViewController, self).__init__(parent)
        self.initUI()
        self.initSignal()

    def initSignal(self):
        self._zoom_in.clicked.connect(self.singal_zoomin_clicked)
        self._zoom_out.clicked.connect(self.signal_zoomout_clicked)
        self._remove_low.clicked.connect(self.singal_remove_clicked)
        self._core_author.clicked.connect(self.singal_core_clicked)

    def initUI(self):
        self._layout = QHBoxLayout(self)
        self._layout.setMargin(1)

        self._group_node = QGroupBox(self)
        self._group_node.setTitle('节点选择')
        self._group_node_layout = QGridLayout(self._group_node)
        self._rb_select_all = QRadioButton('全选', self._group_node)
        self._rb_select_none = QRadioButton('反选', self._group_node)
        self._rb_select_threshold = QRadioButton('阈值', self._group_node)
        self._lb_first_author = QLabel('第一作者文章：', self._group_node)
        self._slide_first_author = QSlider(Qt.Horizontal, self._group_node)
        self._slide_co_author = QSlider(Qt.Horizontal, self._group_node)
        self._lb_co_author = QLabel('共同作者文章：', self._group_node)
        self._group_node_layout.addWidget(self._rb_select_all, 0, 0, 1, 2)
        self._group_node_layout.addWidget(self._rb_select_none, 0, 2, 1, 2)
        self._group_node_layout.addWidget(self._rb_select_threshold, 0, 4, 1, 2)
        self._group_node_layout.addWidget(self._lb_first_author, 1, 0, 1, 2)
        self._group_node_layout.addWidget(self._slide_first_author, 1, 2, 1, 4)
        self._group_node_layout.addWidget(self._lb_co_author, 2, 0, 1, 2)
        self._group_node_layout.addWidget(self._slide_co_author, 2, 2, 1, 4)
        self._group_node.setLayout(self._group_node_layout)

        self._group_auto = QGroupBox(self)
        self._group_auto.setTitle('数据控制')
        self._group_auto_layout = QGridLayout(self._group_auto)
        self._remove_low = QPushButton('移除挂名作者', self._group_auto)
        self._group_auto_layout.addWidget(self._remove_low, 0, 0, 1, 1)
        self._core_author = QPushButton('核心作者筛选', self._group_node)
        self._group_auto_layout.addWidget(self._core_author, 0, 1, 1, 1)
        self._group_auto.setLayout(self._group_auto_layout)

        self._group_network = QGroupBox(self)
        self._group_network.setTitle('网络图控制')
        self._group_network_layout = QGridLayout(self._group_network)
        self._zoom_in = QPushButton('放大', self._group_network)
        self._zoom_out = QPushButton('缩小', self._group_network)
        self._slide_zoom = QSlider(Qt.Horizontal, self._group_network)
        self._group_network_layout.addWidget(self._zoom_out, 0, 0, 1, 2)
        self._group_network_layout.addWidget(self._slide_zoom, 0, 2, 1, 4)
        self._group_network_layout.addWidget(self._zoom_in, 0, 6, 1, 2)
        self._group_network.setLayout(self._group_network_layout)


        self._layout.addWidget(self._group_node)
        self._layout.addWidget(self._group_auto)
        self._layout.addStretch()
        self._layout.addWidget(self._group_network)
        self._layout.addStretch()
        self.setLayout(self._layout)





class SciView(QWidget):
    def __init__(self, parent=None):
        super(SciView, self).__init__(parent)
        self.initUI()
        self.initSignal()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self._controller = SciViewController(self)
        self.split = QSplitter(self)
        self.list = SciListView(self.split)
        self.network = NetworkDrawer(self.split)
        self.split.addWidget(self.list)
        self.split.addWidget(self.network)
        self.split.setStretchFactor(0, 2)
        self.split.setStretchFactor(1, 8)
        self.layout.addWidget(self._controller, 0)
        self.layout.addWidget(self.split, 1)
        self.setLayout(self.layout)

    def initSignal(self):
        self.list.clicked.connect(self.network.highlight_item)
        self._controller.singal_zoomin_clicked.connect(self.network.zoom_in_view)
        self._controller.signal_zoomout_clicked.connect(self.network.zoom_out_view)
        self._controller.singal_remove_clicked.connect(self.network.hide_nodes)

    @Slot()
    def say_hello(self):
        print("tree clicked")





    def setData(self, data):
        self.graph = nx.Graph()
        try:
            for key, value in data.items():
                self.graph.add_node(key, first=value['articleAsFirst'], co=value['articleAsCo'])
                for key_co, value_co in value['CoOccur'].items():
                    self.graph.add_edge(key, key_co, weight=value_co)
        except Exception as e:
            self.graph.clear()
            print(str(e))
        print('OK')

        # nodes = self

        headers = ['name', 'freq', 'co']
        model = []
        for key, value in data.items():
           item = []
           try:
              item.append(key)
              if 'articleAsFirst' in value:
                 item.append(value['articleAsFirst'])
              else:
                 item.append(0)
              if 'articleAsCo' in value:
                 item.append(value['articleAsCo'])
              else:
                 item.append(0)
              model.append(item)
           except Exception as e:
              print(str(e))
        self.list.setData(headers, model)
        self.network.setGraph(self.graph)