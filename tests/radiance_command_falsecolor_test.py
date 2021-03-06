# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from honeybee.radiance.command.falsecolor import Falsecolor
from honeybee.radiance.parameters.falsecolor import FalsecolorParameters
import os


class FalseColorTestCase(unittest.TestCase):
    """Test for (honeybee/radiance/command/false_color.py)."""

    # test prep
    def setUp(self):
        false_color_para = FalsecolorParameters()
        false_color_para.contourLines = True

        self.false_color = Falsecolor()
        self.false_color.inputImageFile = 'assets/sample.hdr'
        self.false_color.false_color_parameters = false_color_para
        self.false_color.outputFile = 'assets/sampleFalse.hdr'

    def tearDown(self):
        # cleanup
        os.remove('assets/sampleFalse.hdr')

    def test_default_values(self):
        # Two tests will be conducted:
        #   First one checks if false_color created the file correctly.
        #   Second one checks if the file size is greater than zero.
        self.false_color.execute()
        self.assertTrue(os.path.exists('assets/sampleFalse.hdr'),
                        'The file that should have been created by false_color was not'
                        'found.')

        file_size = os.stat('assets/sampleFalse.hdr').st_size

        self.assertGreater(file_size, 10,
                           'The size of the file created by false_color does not appear'
                           ' to be correct')


if __name__ == "__main__":
    unittest.main()
