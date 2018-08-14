# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test1", footer="test2"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_edition = Group(name="New name")
    group_edition.id = group.id
    app.group.edit_by_id(group.id, group_edition)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups.remove(group)
    old_groups.append(group_edition)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)