"""Test the Dictionary class methods."""
import ee
import pytest

import geetools


class TestFromPairs:
    """Test the fromPairs method."""

    def test_from_pairs_with_list(self):
        d = ee.Dictionary.geetools.fromPairs([["foo", 1], ["bar", 2]])
        assert d.getInfo() == {"foo": 1, "bar": 2}

    def test_from_pairs_with_ee_list(self):
        d = ee.Dictionary.geetools.fromPairs(ee.List([["foo", 1], ["bar", 2]]))
        assert d.getInfo() == {"foo": 1, "bar": 2}

    def test_deprecated_method(self):
        with pytest.deprecated_call():
            d = geetools.tools.dictionary.fromList([["foo", 1], ["bar", 2]])
            assert d.getInfo() == {"foo": 1, "bar": 2}
