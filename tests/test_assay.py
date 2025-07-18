# -*- coding: utf-8 -*-
"""
test_assay
~~~~~~~~~~

Test assay object.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest

from pubchempy import *


@pytest.fixture(scope='module')
def a1():
    """Assay AID 1."""
    return Assay.from_aid(1)


def test_basic(a1):
    assert a1.aid == 1
    assert repr(a1) == 'Assay(1)'
    assert a1.record


def test_meta(a1):
    assert isinstance(a1.name, text_types)
    assert a1.project_category == ProjectCategory.OTHER
    assert isinstance(a1.description, list)
    assert isinstance(a1.comments, list)


def test_assay_equality():
    first = Assay.from_aid(1)
    second = Assay.from_aid(3)
    assert first == first
    assert second == second
    assert first != second


def test_assay_dict(a1):
    assert isinstance(a1.to_dict(), dict)
    assert a1.to_dict()

