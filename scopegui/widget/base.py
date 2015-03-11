"""Contain enhanced base widgets for the scope widget."""

from taurus.qt.qtgui.panel.taurusform import TaurusCommandsForm
from taurus.qt.qtgui.panel.taurusform import TaurusForm
from taurus.qt.qtgui.input import TaurusValueCheckBox
from taurus.qt.qtgui.table import TaurusValuesTable, TaurusPropTable
from taurus.qt.qtgui.base.taurusbase import TaurusBaseWidget, TaurusBaseComponent
from taurus.qt.qtgui.plot import TaurusPlot
from taurus.qt.qtgui.plot import TaurusXValues

from PyQt4.QtGui import QDialogButtonBox, QAbstractItemView


class FilteredTaurusCommandsForm(TaurusCommandsForm):
    """Taurus commands forms that filters some of the commands."""

    base_ignore = ["state", "status"]

    def __init__(self, *args, **kwargs):
        # Get keywords
        self.ignore = self.base_ignore
        self.ignore.extend(kwargs.pop("ignore", ()))
        self.include = kwargs.pop("include", None)
        self.show_output = kwargs.pop("show_output", False)
        # Init
        TaurusCommandsForm.__init__(self, *args, **kwargs)
        # Show output
        self._outputTE.setVisible(self.show_output)
        # Filter commands
        if self.include is None:
            filt = lambda arg: arg.cmd_name.lower() not in self.ignore
        else:
            filt = lambda arg: arg.cmd_name.lower() in self.include
        self.setViewFilters([filt])

    def _updateCommandWidgets(self, *args):
        # Hack: Forced update of the software state
        try:
            self.getModelObj().getSWState(cache=False)
        except AttributeError:
            pass
        return TaurusCommandsForm._updateCommandWidgets(self, *args)

class NoButtonTaurusValuesTable(TaurusValuesTable):
    """Taurus values table without the buttons."""

    def __init__(self, *args, **kwargs):
        TaurusValuesTable.__init__(self, *args, **kwargs)
        self._applyBT.hide()
        self._cancelBT.hide()
        self._label.hide()
        self._tableView.setSelectionMode(QAbstractItemView.NoSelection)
        self._tableView.horizontalHeader().setStretchLastSection(True)
        self._tableView.horizontalHeader().hide()
        self._tableView.resizeColumnsToContents = lambda *args: None


class NoButtonNorIndexTaurusValuesTable(NoButtonTaurusValuesTable):
    """Taurus values table without the buttons."""

    def __init__(self, *args, **kwargs):
        NoButtonTaurusValuesTable.__init__(self, *args, **kwargs)
        self._tableView.verticalHeader().hide()

class TestTaurusPropTable(TaurusPropTable):
    """Taurus values table without the buttons."""

    def __init__(self, *args, **kwargs):
        TaurusPropTable.__init__(self, *args, **kwargs)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().hide()
        self.resizeColumnsToContents = lambda *args: None
        self.setModel = self.setTable


class PatchedTaurusValueCheckBox(TaurusValueCheckBox):
    """Patched taurus value check box."""

    def __init__(self, *args, **kwargs):
        TaurusValueCheckBox.__init__(self, *args, **kwargs)
        self.autoApply = True
        self.setShowText(False)

    def getModelValueObj(self):
        res = TaurusValueCheckBox.getModelValueObj(self)
        if res is not None:
            res.w_value = res.value
        return res

    def getModelObj(self):
        res = TaurusValueCheckBox.getModelObj(self)
        if res is not None:
            value = res.getValueObj()
            if value:
                value.w_value = value.value
        return res


class NoButtonTaurusForm(TaurusForm):
    """Taurus form without buttons."""

    def __init__(self, *args, **kwargs):
        kwargs['buttons'] = QDialogButtonBox.NoButton
        TaurusForm.__init__(self, *args, **kwargs)

    def event(self, event):
        # Lame. Should find a better place for this piece of code.
        for item in self:
            widget = item.writeWidget()
            if widget: widget.setForcedApply(True)
        return TaurusForm.event(self, event)


class PatchedTaurusPlot(TaurusPlot):
    """Patched Taurus plot."""

    def __init__(self, *args, **kwargs):
        """Get the scale attribute as a keyword."""
        attr = kwargs.pop('scale')
        TaurusPlot.__init__(self, *args, **kwargs)
        self.scale = PatchedTaurusXValues(attr, self)
        self.registerCurves()
        # Set margins
        engine = self.axisScaleEngine(self.xBottom)
        engine.setMargins(0,0)
        engine.setAttribute(engine.Floating)

    def registerCurves(self):
        """Update the link between the scale and the curve."""
        for curve in self.curves.values():
            self.scale.registerDataChanged(curve)
            curve.setXValuesBuilder(self.scaleValues)

    def scaleValues(self, arg=None):
        """Get the scale values."""
        value = self.scale.getValues()
        try: len(value)
        except: value = []
        return value

    def getModelObj(self, idx=None):
        """Patch to use the parent model."""
        if idx is None:
            return self.parent().getModelObj()
        return TaurusPlot.getModelObj(self, idx)

    def updateCurves(self, names):
        """Use parent model for the scale"""
        TaurusPlot.updateCurves(self, names)
        self.scale.setUseParentModel(self.getUseParentModel())

    def parentModelChanged(self, parentmodel_name):
        """Update the scale when the parent has changed."""
        TaurusPlot.parentModelChanged(self, parentmodel_name)
        self.scale.setModelCheck(self.scale.getModel(), False)
        self.registerCurves()


class PatchedTaurusXValues(TaurusXValues):
    """Patched version of the taurus plot."""

    def __init__(self, name, parent=None):
        """Register the parent as the taurus parent."""
        TaurusXValues.__init__(self, name, parent)
        self.parent = parent

    def getParentTaurusComponent(self):
        """Return the taurus parent."""
        return self.parent
