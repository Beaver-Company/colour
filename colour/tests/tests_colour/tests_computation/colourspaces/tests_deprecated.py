# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_deprecated.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`colour.computation.colourspaces.deprecated` module.

**Others:**

"""

from __future__ import unicode_literals

import sys

import numpy


if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import colour.computation.colourspaces.deprecated

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["TestRGB_to_HSV",
           "TestHSV_to_RGB",
           "TestRGB_to_HSL",
           "TestHSL_to_RGB",
           "TestRGB_to_CMY",
           "TestCMY_to_RGB",
           "TestCMY_to_CMYK",
           "TestCMYK_to_CMY",
           "TestRGB_to_HEX",
           "TestHEX_to_RGB"]


class TestRGB_to_HSV(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.RGB_to_HSV` definition units tests methods.
    """

    def test_RGB_to_HSV(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.RGB_to_HSV` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_HSV(
                numpy.array([0.25, 0.60, 0.05])),
            numpy.array([0.27272727, 0.91666667, 0.6]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_HSV(
                numpy.array([0., 0., 0.])),
            numpy.array([0., 0., 0.]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_HSV(
                numpy.array([1., 1., 1.])),
            numpy.array([0., 0., 1.]).reshape((3, 1)),
            decimal=7)


class TestHSV_to_RGB(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.HSV_to_RGB` definition units tests methods.
    """

    def test_HSV_to_RGB(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.HSV_to_RGB` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HSV_to_RGB(
                numpy.array([0.27272727, 0.91666667, 0.6])),
            numpy.array([0.25, 0.60, 0.05]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HSV_to_RGB(
                numpy.array([0., 0., 0.])),
            numpy.array([0., 0., 0.]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HSV_to_RGB(
                numpy.array([0., 0., 1.])),
            numpy.array([1., 1., 1.]).reshape((3, 1)),
            decimal=7)


class TestRGB_to_HSL(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.RGB_to_HSL` definition units tests methods.
    """

    def test_RGB_to_HSL(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.RGB_to_HSL` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_HSL(
                numpy.array([0.25, 0.60, 0.05])),
            numpy.array([0.27272727, 0.84615385, 0.325]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_HSL(
                numpy.array([0., 0., 0.])),
            numpy.array([0., 0., 0.]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_HSL(
                numpy.array([1., 1., 1.])),
            numpy.array([0., 0., 1.]).reshape((3, 1)),
            decimal=7)


class TestHSL_to_RGB(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.HSL_to_RGB` definition units tests methods.
    """

    def test_HSL_to_RGB(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.HSL_to_RGB` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HSL_to_RGB(
                numpy.array([0.27272727, 0.84615385, 0.325])),
            numpy.array([0.25, 0.60, 0.05]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HSL_to_RGB(
                numpy.array([0., 0., 0.])),
            numpy.array([0., 0., 0.]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HSL_to_RGB(
                numpy.array([0., 0., 1.])),
            numpy.array([1., 1., 1.]).reshape((3, 1)),
            decimal=7)


class TestRGB_to_CMY(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.RGB_to_CMY` definition units tests methods.
    """

    def test_RGB_to_CMY(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.RGB_to_CMY` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_CMY(
                numpy.array([0.25, 0.60, 0.05])),
            numpy.array([0.75, 0.40, 0.95]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_CMY(
                numpy.array([0., 0., 0.])),
            numpy.array([1., 1., 1.]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.RGB_to_CMY(
                numpy.array([1., 1., 1.])),
            numpy.array([0., 0., 0.]).reshape((3, 1)),
            decimal=7)


class TestCMY_to_RGB(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.CMY_to_RGB` definition units tests methods.
    """

    def test_CMY_to_RGB(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.CMY_to_RGB` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMY_to_RGB(
                numpy.array([0.75, 0.40, 0.95])),
            numpy.array([0.25, 0.60, 0.05]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMY_to_RGB(
                numpy.array([1., 1., 1.])),
            numpy.array([0., 0., 0.]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMY_to_RGB(
                numpy.array([0., 0., 0.])),
            numpy.array([1., 1., 1.]).reshape((3, 1)),
            decimal=7)


class TestCMY_to_CMYK(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.CMY_to_CMYK` definition units tests methods.
    """

    def test_CMY_to_CMYK(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.CMY_to_CMYK` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMY_to_CMYK(
                numpy.array([0.75, 0.40, 0.95])),
            numpy.array([0.58333333, 0., 0.91666667, 0.4]).reshape((4, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMY_to_CMYK(
                numpy.array([0.15, 1., 1.])),
            numpy.array([0., 1., 1., 0.15]).reshape((4, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMY_to_CMYK(
                numpy.array([0.15, 0., 0.])),
            numpy.array([0.15, 0., 0., 0.]).reshape((4, 1)),
            decimal=7)


class TestCMYK_to_CMY(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.CMYK_to_CMY` definition units tests methods.
    """

    def test_CMYK_to_CMY(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.CMYK_to_CMY` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMYK_to_CMY(
                numpy.array([0.58333333, 0., 0.91666667, 0.4])),
            numpy.array([0.75, 0.40, 0.95]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMYK_to_CMY(
                numpy.array([0., 1., 1., 0.15])),
            numpy.array([0.15, 1., 1.]).reshape((3, 1)),
            decimal=7)

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.CMYK_to_CMY(
                numpy.array([0.15, 0., 0., 0.])),
            numpy.array([0.15, 0., 0.]).reshape((3, 1)),
            decimal=7)


class TestRGB_to_HEX(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.RGB_to_HEX` definition units tests methods.
    """

    def test_RGB_to_HEX(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.RGB_to_HEX` definition.
        """

        self.assertEqual(
            colour.computation.colourspaces.deprecated.RGB_to_HEX(
                numpy.array([0.25, 0.60, 0.05])),
            "#3f990c")
        self.assertEqual(
            colour.computation.colourspaces.deprecated.RGB_to_HEX(
                numpy.array([0., 0., 0.])),
            "#000000")
        self.assertEqual(
            colour.computation.colourspaces.deprecated.RGB_to_HEX(
                numpy.array([1., 1., 1.])),
            "#ffffff")


class TestHEX_to_RGB(unittest.TestCase):
    """
    Defines :func:`colour.computation.colourspaces.deprecated.HEX_to_RGB` definition units tests methods.
    """

    def test_HEX_to_RGB(self):
        """
        Tests :func:`colour.computation.colourspaces.deprecated.HEX_to_RGB` definition.
        """

        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HEX_to_RGB("#3f990c"),
            numpy.array([0.25, 0.60, 0.05]).reshape((3, 1)),
            decimal=2)
        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HEX_to_RGB("#000000"),
            numpy.array([0., 0., 0.]).reshape((3, 1)),
            decimal=2)
        numpy.testing.assert_almost_equal(
            colour.computation.colourspaces.deprecated.HEX_to_RGB("#ffffff"),
            numpy.array([1., 1., 1.]).reshape((3, 1)),
            decimal=2)


if __name__ == "__main__":
    unittest.main()