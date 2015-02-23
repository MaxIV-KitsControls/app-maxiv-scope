"""Contain the patch for the Taurus status bug."""

# Constant

CORRECTED = "3.3.0"

# Use this patch

def check_and_patch(verbose=False):
    from taurus import Release
    current = versiontuple(Release.version)
    limit = versiontuple(CORRECTED)
    if current < limit:
        patch_taurus_status_bug()
        if verbose: print("Patched!")
    elif verbose: print("No patch needed.")

# Other functions

def versiontuple(v):
    return tuple(map(int, (v.split("."))))

def patch_taurus_status_bug():
    """ Patch the taurus status bug."""
    from taurus.qt.qtgui.base import TaurusBaseController
    old_func = TaurusBaseController.handleEvent
    def patchedHandleEvent(self, *args):
        """Patched version of handle events"""
        if args[0] != self.modelObj():
            return self.update()
        return old_func(self, *args)
    TaurusBaseController.handleEvent = patchedHandleEvent

# Main execution

if __name__ == '__main__':
    check_and_patch(True)
