#!/usr/bin/env python

import datetime
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class PaceCalculatorGTK:
    """This is an Hello World GTK application"""

    def __init__(self):
        # Set the Glade file
        self.gladefile = "pacecalculator.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)

        # Get the Main Window, and connect the "destroy" event
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("pacecalculator")
        self.window.connect("delete-event", Gtk.main_quit)
        self.submitobj = self.builder.get_object("submit")
        self.paceobj = self.builder.get_object("pace")
        self.distanceobj = self.builder.get_object("distance")
        self.pacekmmileobj = self.builder.get_object("pacekmmile")
        self.distancekmmileobj = self.builder.get_object("distancekmmile")
        self.resultobj = self.builder.get_object("result")
        self.pacecalculator_filequitobj = \
            self.builder.get_object("pacecalculator_filequit")
        self.pacecalculator_filequitobj.connect("activate", Gtk.main_quit)
        self.submitobj.connect("clicked", self.calculate)
        self.window.show_all()
        self.pacekmmileobj.hide()
        self.distancekmmileobj.hide()

    def calculate(self, button):
        pace = self.paceobj.get_text()
        pace_time_struct = time.strptime(pace, '%M:%S')
        pace_seconds = datetime.timedelta(minutes=pace_time_struct.tm_min,
                                          seconds=pace_time_struct.tm_sec)\
            .total_seconds()
        distance = self.distanceobj.get_text()
        time_seconds = float(pace_seconds) * float(distance)
        m, s = divmod(time_seconds, 60)
        h, m = divmod(m, 60)
        time_str = "%d hour %02d minutes %02d seconds" % (h, m, s)
        self.resultobj.set_markup('<b>%s</b>' % time_str)

if __name__ == "__main__":
    hwg = PaceCalculatorGTK()
    Gtk.main()
