from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Hello world", header="Update group header AGAIN", footer="Update group footer AGAIN"))
    app.session.logout()

