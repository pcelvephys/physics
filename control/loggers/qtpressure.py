# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pressure.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_P_window(object):
    def setupUi(self, P_window):
        P_window.setObjectName(_fromUtf8("P_window"))
        P_window.resize(1584, 1019)
        self.centralwidget = QtGui.QWidget(P_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.P_exp = QtGui.QLCDNumber(self.centralwidget)
        self.P_exp.setSmallDecimalPoint(False)
        self.P_exp.setNumDigits(2)
        self.P_exp.setObjectName(_fromUtf8("P_exp"))
        self.P_exp.setLineWidth(0)
        self.gridLayout.addWidget(self.P_exp, 0, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 7, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 4, 1, 3)
        self.x10_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.x10_label.setFont(font)
        self.x10_label.setObjectName(_fromUtf8("x10_label"))
        self.gridLayout.addWidget(self.x10_label, 0, 5, 2, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 7, 1, 1)
        self.P_dec = QtGui.QLCDNumber(self.centralwidget)
        self.P_dec.setProperty("value", 2.445)
        self.P_dec.setObjectName(_fromUtf8("P_dec"))
        self.P_dec.setLineWidth(0)
        self.gridLayout.addWidget(self.P_dec, 0, 4, 2, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 7, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 8, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 7, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(600, 0, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 8, 4, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(200, 0, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 8, 6, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 6, 7, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 7, 7, 1, 1)


        self.plotView_fig = Figure() #QtGui.QGraphicsView(self.centralwidget)
        self.plotView = FigureCanvas(self.plotView_fig)
        self.plotView.setObjectName(_fromUtf8("plotView"))
        self.gridLayout.addWidget(self.plotView, 4, 4, 4, 3)


        self.log_browser = QtGui.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.log_browser.setFont(font)
        self.log_browser.setObjectName(_fromUtf8("log_browser"))
        self.gridLayout.addWidget(self.log_browser, 0, 0, 8, 2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 2, 8, 1)
        P_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(P_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1584, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuLog = QtGui.QMenu(self.menubar)
        self.menuLog.setObjectName(_fromUtf8("menuLog"))
        self.menuGraph = QtGui.QMenu(self.menubar)
        self.menuGraph.setObjectName(_fromUtf8("menuGraph"))
        self.menuTime_scale = QtGui.QMenu(self.menuGraph)
        self.menuTime_scale.setObjectName(_fromUtf8("menuTime_scale"))
        self.menuStatus = QtGui.QMenu(self.menuGraph)
        self.menuStatus.setObjectName(_fromUtf8("menuStatus"))
        P_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(P_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        P_window.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(P_window)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.triggered.connect(sys.exit)
        self.actionClear = QtGui.QAction(P_window)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionClear.triggered.connect(self.log_browser.clear)

        def set_graph_timescale(GT):
            global graph_time
            graph_time = GT

        self.action20_secs = QtGui.QAction(P_window)
        self.action20_secs.setObjectName(_fromUtf8("action20_secs"))
        self.action20_secs.triggered.connect(lambda: set_graph_timescale(20))

        self.action1_min = QtGui.QAction(P_window)
        self.action1_min.setObjectName(_fromUtf8("action1_min"))
        self.action1_min.triggered.connect(lambda: set_graph_timescale(1*60))

        self.action3_min = QtGui.QAction(P_window)
        self.action3_min.setObjectName(_fromUtf8("action3_min"))
        self.action3_min.triggered.connect(lambda: set_graph_timescale(3*60))

        self.action5_min = QtGui.QAction(P_window)
        self.action5_min.setObjectName(_fromUtf8("action5_min"))
        self.action5_min.triggered.connect(lambda: set_graph_timescale(5*60))

        self.action15_min = QtGui.QAction(P_window)
        self.action15_min.setObjectName(_fromUtf8("action15_min"))
        self.action15_min.triggered.connect(lambda: set_graph_timescale(15*60))

        self.action30_min = QtGui.QAction(P_window)
        self.action30_min.setObjectName(_fromUtf8("action30_min"))
        self.action30_min.triggered.connect(lambda: set_graph_timescale(30*60))

        self.action1_hour = QtGui.QAction(P_window)
        self.action1_hour.setObjectName(_fromUtf8("action1_hour"))
        self.action1_hour.triggered.connect(lambda: set_graph_timescale(1*60*60))

        self.action3_hours = QtGui.QAction(P_window)
        self.action3_hours.setObjectName(_fromUtf8("action3_hours"))
        self.action3_hours.triggered.connect(lambda: set_graph_timescale(3*60*60))

        self.action12_hours = QtGui.QAction(P_window)
        self.action12_hours.setObjectName(_fromUtf8("action12_hours"))
        self.action12_hours.triggered.connect(lambda: set_graph_timescale(12*60*60))

        self.action1_day = QtGui.QAction(P_window)
        self.action1_day.setObjectName(_fromUtf8("action1_day"))
        self.action1_day.triggered.connect(lambda: set_graph_timescale(1*24*60*60))

        self.action3_days = QtGui.QAction(P_window)
        self.action3_days.setObjectName(_fromUtf8("action3_days"))
        self.action3_days.triggered.connect(lambda: set_graph_timescale(3*24*60*60))

        self.action7_days = QtGui.QAction(P_window)
        self.action7_days.setObjectName(_fromUtf8("action7_days"))
        self.action7_days.triggered.connect(lambda: set_graph_timescale(1*7*24*60*60))

        self.action2_weeks = QtGui.QAction(P_window)
        self.action2_weeks.setObjectName(_fromUtf8("action2_weeks"))
        self.action2_weeks.triggered.connect(lambda: set_graph_timescale(2*7*24*60*60))

        self.action1_month = QtGui.QAction(P_window)
        self.action1_month.setObjectName(_fromUtf8("action1_month"))
        self.action1_month.triggered.connect(lambda: set_graph_timescale(4*7*24*60*60))

        self.actionEnable = QtGui.QAction(P_window)
        self.actionEnable.setObjectName(_fromUtf8("actionEnable"))

        def enable_graph():
            global graph_state
            graph_state = True

        def disable_graph():
            global graph_state
            graph_state = False

        self.actionEnable.triggered.connect(enable_graph)
        self.actionDisable = QtGui.QAction(P_window)
        self.actionDisable.setObjectName(_fromUtf8("actionDisable"))
        self.actionDisable.triggered.connect(disable_graph)

        self.menuFile.addAction(self.actionQuit)
        self.menuLog.addAction(self.actionClear)
        self.menuTime_scale.addAction(self.action20_secs)
        self.menuTime_scale.addAction(self.action1_min)
        self.menuTime_scale.addAction(self.action3_min)
        self.menuTime_scale.addAction(self.action5_min)
        self.menuTime_scale.addAction(self.action15_min)
        self.menuTime_scale.addAction(self.action30_min)
        self.menuTime_scale.addAction(self.action1_hour)
        self.menuTime_scale.addAction(self.action3_hours)
        self.menuTime_scale.addAction(self.action12_hours)
        self.menuTime_scale.addAction(self.action1_day)
        self.menuTime_scale.addAction(self.action3_days)
        self.menuTime_scale.addAction(self.action7_days)
        self.menuTime_scale.addAction(self.action2_weeks)
        self.menuTime_scale.addAction(self.action1_month)
        self.menuStatus.addAction(self.actionEnable)
        self.menuStatus.addAction(self.actionDisable)
        self.menuGraph.addAction(self.menuTime_scale.menuAction())
        self.menuGraph.addAction(self.menuStatus.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())

        self.retranslateUi(P_window)
        QtCore.QMetaObject.connectSlotsByName(P_window)

    def retranslateUi(self, P_window):
        P_window.setWindowTitle(_translate("P_window", "Chamber Pressure", None))
        self.x10_label.setText(_translate("P_window", " x 10", None))
        self.menuFile.setTitle(_translate("P_window", "File", None))
        self.menuLog.setTitle(_translate("P_window", "Log", None))
        self.menuGraph.setTitle(_translate("P_window", "Graph", None))
        self.menuTime_scale.setTitle(_translate("P_window", "Time scale", None))
        self.menuStatus.setTitle(_translate("P_window", "Status", None))
        self.actionQuit.setText(_translate("P_window", "Quit", None))
        self.actionClear.setText(_translate("P_window", "Clear", None))
        self.action20_secs.setText(_translate("P_window", "20 secs", None))
        self.action1_min.setText(_translate("P_window", "1 min", None))
        self.action3_min.setText(_translate("P_window", "3 min", None))
        self.action5_min.setText(_translate("P_window", "5 min", None))
        self.action15_min.setText(_translate("P_window", "15 min", None))
        self.action30_min.setText(_translate("P_window", "30 min", None))
        self.action1_hour.setText(_translate("P_window", "1 hour", None))
        self.action3_hours.setText(_translate("P_window", "3 hours", None))
        self.action12_hours.setText(_translate("P_window", "12 hours", None))
        self.action1_day.setText(_translate("P_window", "1 day", None))
        self.action3_days.setText(_translate("P_window", "3 days", None))
        self.action7_days.setText(_translate("P_window", "1 week", None))
        self.action2_weeks.setText(_translate("P_window", "2 weeks", None))
        self.action1_month.setText(_translate("P_window", "1 month", None))
        self.actionEnable.setText(_translate("P_window", "Enable", None))
        self.actionDisable.setText(_translate("P_window", "Disable", None))


if __name__ == "__main__":
    import sys
    #import random
    import time as t
    import numpy as np
    import datetime
    import irc
    import leybold
    from collections import deque

    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else: mode = "irc"

    print("Mode: {}".format(mode))

    N = str(t.time())[-4:]
    irclog = irc.irc('Pressure_{}_{}'.format(mode, N), 'pressure_{}_{}'.format(mode, N), 'Leybold ITR90 {} {}'.format(mode, N))

    if mode == "local":
        itr90 = leybold.itr90(address="/dev/ttyUSB0")


    app = QtGui.QApplication(sys.argv)
    P_window = QtGui.QMainWindow()
    ui = Ui_P_window()
    ui.setupUi(P_window)
    P_window.show()

    pressures = deque([], maxlen=3000)
    times = deque([], maxlen=3000)

    graph_state = True
    graph_time = 120
    clear_time = datetime.datetime.now()

    def update():
        global pressures
        global times
        global clear_time

        if mode == "irc":
            for line in irclog.readlines():
                    try:
                            msg = {'message': line[line.index('>')+1:].strip(), 'nick': line[line.index('<')+1:line.index('>')].strip()}
                            #print(msg)
                    except:
                            continue
                    if msg['nick'].startswith('Pressure_local'):
                            P = float(msg['message'].split()[2])
        else:
            P = itr90.pressure()


        if "P" in locals():
            pressures.append(P)
            times.append(datetime.datetime.now())

            if mode == "local":
                message = "Pressure is %g mBar" % P
                irclog.write(message)


            s_P = "%1.3e"%P
            s_P = s_P.split("e")

            dec = s_P[0]
            ui.P_dec.display(dec)
            exp = int(s_P[1]) #int(np.log10(P))-1
            ui.P_exp.display(exp)
            #print("{} {}".format(dec,exp))




            if graph_state:
                ax = ui.plotView_fig.add_subplot(111)
                ax.clear()
                deltas = [datetime.datetime.now() - ti for ti in times]
                deltas = np.array([d.seconds for d in deltas])
                #print("D: {}".format(deltas))
                locs = np.where(deltas < graph_time)[0]
                #print("L: {}".format(locs))

                ax.plot([times[l] for l in locs], [pressures[l] for l in locs], "+-", color = "black")
                #ax.set_ylim(0,2)
                ax.set_yscale("log")
                ui.plotView_fig.autofmt_xdate()
                ax.grid(True)
                #ui.plotView_fig.tight_layout()
                ui.plotView.draw()

        ui.log_browser.clear()

        log_length = 100

        if len(pressures) < log_length:
            log_text = "\n".join(["{:.5g}\t\t{}".format(pressures[m], times[m].strftime("%Y-%m-%d\t%H:%M:%S")) for m in range(len(pressures))])
        else:
            log_text = "\n".join(["{:.5g}\t\t{}".format(pressures[m], times[m].strftime("%Y-%m-%d\t%H:%M:%S")) for m in range(-log_length,0)])
        ui.log_browser.append(log_text)

        if irc:
            ui.statusbar.showMessage("IRC: Connected\t\t\t\t{}\t|\tpressures length: {}\t|\ttimes length: {}\t|\tlog_text length: {}".format(t.strftime("%Y-%m-%d\t%H:%M:%S"), len(pressures), len(times), len(log_text)))
        else:
            ui.statusbar.showMessage("IRC: Disconnected!\t\t\t\t{}".format(t.strftime("%Y-%m-%d\t%H:%M:%S")))

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    if mode == "local":
        timer.start(5*1000)
    else:
        timer.start(2*1000)
    sys.exit(app.exec_())

