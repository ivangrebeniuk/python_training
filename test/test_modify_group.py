from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Modified group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Modified group header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="Modified group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

