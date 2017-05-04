import datetime
import sys
import time

from PyQt4 import QtGui

import pacecalculatorqtui


class PaceCalculator(QtGui.QMainWindow, pacecalculatorqtui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PaceCalculator, self).__init__(parent)
        self.setupUi(self)
        self.submit.clicked.connect(self.calculate)

    def calculate(self):
        pace = self.pace.text()
        pace_time_struct = time.strptime(pace, '%M:%S')
        pace_seconds = datetime.timedelta(minutes=pace_time_struct.tm_min,
                                          seconds=pace_time_struct.tm_sec)\
            .total_seconds()
        distance = self.distance.text()
        time_seconds = float(pace_seconds) * float(distance)
        m, s = divmod(time_seconds, 60)
        h, m = divmod(m, 60)
        time_str = "%d hour %02d minutes %02d seconds" % (h, m, s)
        self.result.setText('<b>%s</b>' % time_str)


def main():
    app = QtGui.QApplication(sys.argv)
    form = PaceCalculator()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
