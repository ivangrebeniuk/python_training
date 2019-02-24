from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    app.group.modify_first_group(Group(name="Modified group name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    app.group.modify_first_group(Group(header="Modified group header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group added in MODIFY test", header="Some test header", footer="Some test footer"))
    app.group.modify_first_group(Group(footer="Modified group footer"))

