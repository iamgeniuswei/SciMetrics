# This Python file uses the following encoding: utf-8
import sys
import PySide2
import typing
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsView, QGraphicsScene,\
QGraphicsRectItem, QGraphicsItem,QGraphicsEllipseItem,QStyle
from PySide2.QtCore import *
from PySide2.QtGui import *
import math
import networkx as nx
import random


class NetworkController(QWidget):
    def __init__(self, parent=None):
        super(NetworkController, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self._layout = QHBoxLayout(self)
        self._layout.setMargin(1)
        self._zoom_in = QPushButton('ZoomIn', self)
        self._zoom_out = QPushButton('ZoomOut', self)
        self._layout.addStretch()
        self._layout.addWidget(self._zoom_in)
        self._layout.addWidget(self._zoom_out)
        self._layout.addStretch()
        self.setLayout(self._layout)

class NetworkView(QGraphicsView):
    def __init__(self, parent=None):
        super(NetworkView, self).__init__(parent)
        # self.setScene(scene)

    def random_pos(self):
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        return QPointF(x, y)

    def hide_items(self):
        nodes = self.graph.nodes(data=True)
        for node in nodes:
            if node[1]['first'] == 0 and node[1]['co'] == 1:
                node = self.nodes[node[0]]
                node.hide_self()

    def draw_network(self, graph):
        self.graph = graph
        self._scene = QGraphicsScene(self)
        self.nodes = {}
        self.edges = []
        nodes = self.graph.nodes(data=True)
        # degrees = sorted(degrees, key=lambda x: (x[1]), reverse=True)
        for node in nodes:
            count = node[1]['first'] + node[1]['co']
            new_display_node = Node(100*count*10/100)
            self.nodes[node[0]] = new_display_node
            self._scene.addItem(new_display_node)
            new_display_node.setPos(self.random_pos())
        edges = self.graph.edges(data='weight')
        for edge in edges:
            node_start = self.nodes[edge[0]]
            node_end = self.nodes[edge[1]]
            new_display_edge = Edge(node_start, node_end)
            self._scene.addItem(new_display_edge)
        self.setScene(self._scene)







class Node(QGraphicsItem):
    def __init__(self, radius = 10):
        super(Node, self).__init__()
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(-1)
        self.egdes = []
        self.weights = []
        self.degree = 0
        self.radius = radius
        self._is_highlight = False
        self._text = None

    def set_text(self,text):
        self._text = text
        self.update()

    def hide_self(self):
        for edge in self.egdes:
            edge.hide()
        self.hide()

    def highlight(self):
        self._is_highlight = True
        self.update()


    def add_edge(self, edge):
        self.egdes.append(edge)
        edge.adjust()

    def type(self) -> int:
        return QGraphicsItem.UserType+1

    def paint(self, painter:PySide2.QtGui.QPainter, option:PySide2.QtWidgets.QStyleOptionGraphicsItem, widget:typing.Optional[PySide2.QtWidgets.QWidget]=...):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        # painter.setBrush(Qt.darkGray)
        # painter.drawEllipse(-7, -7, 20, 20)
        # gradient = QRadialGradient(-3, -3, 10)
        # if option.state and QStyle.State_Sunken:
        #     gradient.setCenter(3, 3)
        #     gradient.setFocalPoint(3, 3)
        #     gradient.setColorAt(1, QColor(Qt.yellow).lighter(120))
        #     gradient.setColorAt(0, QColor(Qt.darkYellow).lighter(120))
        # else:
        #     gradient.setColorAt(0, Qt.yellow)
        #     gradient.setColorAt(1, Qt.darkYellow)
        #
        # painter.setBrush(gradient)
        if self._is_highlight:
            painter.setBrush(QBrush(Qt.red))
        else:
            painter.setBrush(QBrush(QColor(200, 50, 50, 50)))

        # painter.drawEllipse(QPoint(0, 0), 40, 40)
        # painter.setBrush(Qt.darkGray)
        painter.drawEllipse(QPoint(0, 0), self.radius, self.radius)
        # painter.setPen(Qt.red)
        # painter.drawText(0,0,'100')

    def mouseDoubleClickEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        print('double clicked')
        print(event.pos())
        print(self.scenePos())
        print(self.pos())
        QGraphicsItem.mouseDoubleClickEvent(self,event)

    # def mousePressEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
    #     self.update()
    #     QGraphicsItem.mousePressEvent(self,event)
    #
    # def mouseReleaseEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
    #     self.update()
    #     QGraphicsItem.mousePressEvent(self,event)


    def boundingRect(self) -> PySide2.QtCore.QRectF:
        adjust = 2
        return QRectF(-self.radius-adjust, -self.radius-adjust, self.radius*2 + adjust, self.radius*2 + adjust)

    def shape(self) -> PySide2.QtGui.QPainterPath:
        path = QPainterPath()
        path.addEllipse(self.boundingRect())
        return path


    def itemChange(self, change:PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange, value:typing.Any) -> typing.Any:
        if change is QGraphicsItem.ItemPositionHasChanged:
            for edge in self.egdes:
                edge.adjust()
        return QGraphicsItem.itemChange(self, change, value)


class Edge(QGraphicsItem):
    def __init__(self, src, dst):
        super(Edge, self).__init__()
        self.src = src
        self.dst = dst
        src.add_edge(self)
        dst.add_edge(self)
        self.src_point = None
        self.dst_point = None
        self.adjust()
    def type(self) -> int:
        return QGraphicsItem.UserType+2

    def boundingRect(self) -> PySide2.QtCore.QRectF:
        if self.src is None or self.dst is None:
            return


        penWidth = 1
        extra = 1

        return QRectF(self.src_point, QSizeF(self.dst_point.x() - self.src_point.x(),
                                          self.dst_point.y() - self.src_point.y())).normalized().adjusted(-extra, -extra, extra, extra)

    def adjust(self):
        if self.src is None or self.dst is None:
            return
        line = QLineF(self.mapFromItem(self.src, 0, 0), self.mapFromItem(self.dst, 0, 0))
        length = line.length()
        self.prepareGeometryChange()
        self.src_point = line.p1()
        self.dst_point = line.p2()

    def paint(self, painter:PySide2.QtGui.QPainter, option:PySide2.QtWidgets.QStyleOptionGraphicsItem, widget:typing.Optional[PySide2.QtWidgets.QWidget]=...):
        if self.src is None or self.dst is None:
            return
        line = QLineF(self.src_point, self.dst_point)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.lightGray, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(line)




# class MainWindow(QWidget):
#     def __init__(self):
#
#
#         QWidget.__init__(self)
#         self.layout = QVBoxLayout(self)
#         # rect = QRectF(0, 0, 800, 800)
#         self.scene = QGraphicsScene()
#         items = {}
#         init_pos = QPointF(0, 0)
#         for i in range(100):
#             id = str(i)
#             node = Node()
#             items[id] = node
#             self.scene.addItem(node)
#             x = int(i/12)
#             y = i%12
#             if y == 0 and x==0:
#                 node.setPos(init_pos)
#             else:
#                 base = 100*(x+1)
#                 base_x = base* math.cos((y-1)*math.pi/6)
#                 base_y = base * math.sin((y-1)*math.pi/6)
#                 node.setPos(base_x, base_y)
#
#         node1 = items['1']
#         node2 = items['5']
#         node3 = items['15']
#         node4 = items['50']
#         edge1 = Edge(node1, node2)
#         edge2 = Edge(node1, node4)
#         self.scene.addItem(edge1)
#         self.scene.addItem(edge2)
#
#
#         # item = Node()
#         # self.scene.addItem(item)
#         # item1 = Node()
#         # item1.setPos(QPoint(50,50))
#         # self.scene.addItem(item1)
#         # item2 = QGraphicsRectItem(10,10,50,50)
#         # self.scene.addItem(item2)
#         # line = Edge(item, item1)
#         # self.scene.addItem(line)
#         self.view = NetworkView(self.scene, self)
#         self.view.setCacheMode(QGraphicsView.CacheBackground)
#         self.view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
#         self.layout.addWidget(self.view)
#         self.setLayout(self.layout)
#
#
#
#
#
# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#
#         self.button = QPushButton("Click me!")
#         self.text = QLabel("Hello World")
# #        self.text.setAlignment(Qt::AlignCenter)
#
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)
#
#
#         self.button.clicked.connect(self.magic)
#
#
#     def magic(self):
#         self.text.setText(random.choice(self.hello))
#
#
class NetworkDrawer(QWidget):
    def __init__(self, parent=None):
        super(NetworkDrawer, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self._layout = QVBoxLayout(self)
        self._layout.setMargin(0)
        # self._controller = NetworkController(self)
        self._viewer = NetworkView(self)
        # self._layout.addWidget(self._controller, 0)
        self._layout.addWidget(self._viewer, 1)
        self.setLayout(self._layout)

    def setGraph(self, graph):
        self._viewer.draw_network(graph)

    @Slot()
    def zoom_in_view(self):
        self._viewer.scale(1.2, 1.2)

    @Slot()
    def zoom_out_view(self):
        self._viewer.scale(1/1.2, 1/1.2)
    @Slot()
    def highlight_item(self, index:QModelIndex):
        if index.isValid():
            key = index.data()
            node = self._viewer.nodes[key]
            print(node)
            node.highlight()

    @Slot()
    def hide_nodes(self):
        self._viewer.hide_items()

