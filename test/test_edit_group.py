# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_name_first_group(app):
    app.group.edit_first(Group(name="New name"))


def test_edit_header_first_group(app):
    app.group.edit_first(Group(header='New header'))


def test_edit_footer_first_group(app):
    app.group.edit_first(Group(footer='New footer'))