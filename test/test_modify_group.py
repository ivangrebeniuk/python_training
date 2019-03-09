from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(Group(name="Modified group name"), index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(Group(header="Modified group header"), index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(Group(footer="Modified group footer"), index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)




