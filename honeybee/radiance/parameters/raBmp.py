# coding=utf-8


from ._advancedparametersbase import AdvancedRadianceParameters
from ._frozen import frozen


@frozen
class RaBmpParameters(AdvancedRadianceParameters):
    def __init__(self, createGrayscale=None, reverseConversion=None, exposure=None,
                 gamma=None, crtPrimaries=None):

        AdvancedRadianceParameters.__init__(self)

        self.addRadianceBoolFlag('b', 'create an 8-bit gray scale image',
                                 attributeName='createGrayscale')
        self.createGrayscale = createGrayscale
        """Create an eight bit grayscale image instead of a color image."""

        self.addRadianceBoolFlag('r', 'convert a bitmap to hdr',
                                 attributeName='reverseConversion')
        self.reverseConversion = reverseConversion
        """Do a reverse conversion and convert bitmap to hdr"""

        self.addRadianceValue('e', 'exposure value', attributeName='exposure')
        self.exposure = exposure
        """Specify tonemapping method or exposure value. Accepted tone mapping methods
        are 'auto', 'human' or 'linear. Accepted exposure values are any number prefixed
        with a + or - sign (e.g. -1.2, +1.4, -3.4 etc)."""

        self.addRadianceNumber('g', 'gamma correction', attributeName='gamma')
        self.gamma = gamma
        """Gamma correction for the monitor. Default value is 2.2"""

        self.addRadianceTuple('p', 'crt primaries', attributeName='crtPrimaries')
        self.crtPrimaries = crtPrimaries
        """CRT color output primaries."""
