taurusgui-scope
===============
***

TaurusGUI for oscilloscopes.

Information
-----------

 - Package:       taurusgui-scope
 - Import:        scopegui
 - Compatbile DS: RTMScope, RTOScope
 - Repo:          [app-maxiv-scope][scopegui]

[scopegui]: https://github.com/MaxIV-KitsControls/app-maxiv-scope/

Requirement
-----------

 - [Taurus][taurus]
 - Device servers: [dev-maxiv-rohdescope][scopeds] >= 3.2.0

[taurus]:  https://pypi.python.org/pypi/taurus
[scopeds]: https://github.com/MaxIV-KitsControls/dev-maxiv-rohdescope

Installation
------------
    $ python setup.py install

Usage
-----

    $ python -m scopegui # OR
    $ ctscope

A server selector will look for scope instances running in the database.
Once a server is picked, the GUI creates a tab for each scope device 
handled by the server.

Tests
-----

Tested and deployed for:

 - RTM 2054 
 - RTO 1004

Contact
-------

- Vincent Michel: vincent.michel@maxlab.lu.se
- Paul Bell:      paul.bell@maxlab.lu.se
