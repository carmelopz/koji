from __future__ import absolute_import

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from kojiweb.util import formatMode

class TestFormatMode(unittest.TestCase):
    def test_format_mode(self):
        formats = (
            ('drwxrwxr-x', 0x41fd), # dir
            ('-rw-------', 0x8180), # reg. file
            ('crw--w----', 0x2190), # /dev/tty0
            ('brw-rw----', 0x61b0), # /dev/sda
            ('lrwxrwxrwx', 0xa1ff), # symlink
            ('srwxr-xr-x', 0xc1ed), # socket
            ('-rwsrwsr--', 0x8db4), # suid
        )

        for s, mode in formats:
            self.assertEqual(formatMode(mode), s)
