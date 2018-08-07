# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test1", footer="test2"))
    old_groups = app.group.get_group_list()
    group = Group(name="New name")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_header_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="test1", footer="test2"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(header='New header'))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_footer_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="test1", footer="test2"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(footer='New footer'))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)