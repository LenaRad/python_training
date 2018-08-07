# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test1", footer="test2"))
    app.group.edit_first(Group(name="New name"))


def test_edit_header_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test1", footer="test2"))
    app.group.edit_first(Group(header='New header'))


def test_edit_footer_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test1", footer="test2"))
    app.group.edit_first(Group(footer='New footer'))