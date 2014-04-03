from taurus.qt import QtCore, QtGui
from taurus import Database


class ScopeSelector(QtGui.QComboBox):

    def __init__(self, parent=None):
        QtGui.QComboBox.__init__(self, parent)
        self._addItems()
    
    def _addItems(self):
        db = Database()
        for item in db.get_device_exported_for_class('RohdeSchwarzRTO').value_string:
            self.addItem(item)


def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication(sys.argv)

    form = ScopeSelector()
    form.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
