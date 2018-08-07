# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_name_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="New name"))
    app.session.logout()


def test_edit_header_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(header='New header'))
    app.session.logout()


def test_edit_footer_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(footer='New footer'))
    app.session.logout()