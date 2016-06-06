Unicode to RTF command code conversion
======================================

This module implements an encoder for unicode to RTF 1.5 command sequences; it
can be used to generate valid RTF output with international characters.

Importing this module adds a new `rtfunicode` codec, allowing you to encode
unicode strings to valid RTF bytecode sequences:

>>> import rtfunicode
>>> u'RTF and unicode mix just fine! \u263A'.encode('rtfunicode')
'RTF and unicode mix just fine! \\u9786?'

The RTF command code for a unicode character is `\uN?`, where N is a signed
16-bit integer and the ? is a placeholder character for older RTF readers. This
module sets the latter to the '?' literal for simlicity's sake.

Requirements
------------

* Python 2.4-2.7, 3.3-3.5


Development
-----------

.. image:: https://travis-ci.org/mjpieters/rtfunicode.svg?branch=master
    :target: https://travis-ci.org/mjpieters/rtfunicode

The project code is hosted on GitHub_, feel free to report issues,
fork the code and issue pull requests.

.. _GitHub: https://github.com/mjpieters/rtfunicode


License
-------

BSD (simplified), see: LICENSE.txt


Author
------

Martijn Pieters <mj@zopatista.com>
