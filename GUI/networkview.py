# This Python file uses the following encoding: utf-8
import sys
import PySide2
import typing
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGraphicsView, QGraphicsScene,\
QGraphicsRectItem, QGraphicsItem,QGraphicsEllipseItem,QStyle
from PySide2.QtCore import *
from PySide2.QtGui import *


class NetworkView(QGraphicsView):
    def __init__(self, scene = None, parent=None):
        super(NetworkView, self).__init__(scene, parent)
        self.setScene(scene)

class Node(QGraphicsItem):
    def __init__(self):
        super(Node, self).__init__()
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(-1)
        self.egdes = []
        self.weights = []
        self.degree = 0
        self.radius = 0


    # def


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
        painter.setBrush(QBrush(QColor(50,50,50,50)))
        painter.drawEllipse(QPoint(0, 0), 40, 40)
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(QPoint(0, 0), 20, 20)
        painter.setPen(Qt.red)
        painter.drawText(0,0,'100')

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
        return QRectF(-50, -50, 200 + adjust, 200 + adjust)

    # def shape(self) -> PySide2.QtGui.QPainterPath:
    #     path = QPainterPath()
    #     path.addEllipse(-10, -10, 20, 20)
    #     return path


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
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(line)

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout(self)
        rect = QRectF(0, 0, 800, 800)
        self.scene = QGraphicsScene(rect)
        item = Node()
        self.scene.addItem(item)
        item1 = Node()
        item1.setPos(QPoint(50,50))
        self.scene.addItem(item1)
        item2 = QGraphicsRectItem(10,10,50,50)
        self.scene.addItem(item2)
        line = Edge(item, item1)
        self.scene.addItem(line)
        self.view = NetworkView(self.scene, self)
        self.view.setCacheMode(QGraphicsView.CacheBackground)
        self.view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        print(item1.scenePos())
        print(item1.pos())
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)





class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
#        self.text.setAlignment(Qt::AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))