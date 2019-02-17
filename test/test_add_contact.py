# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.fill_contact_data(Contact(first_name="John", middle_name="Doe", last_name="Doe", nickname="Sponge Bob", title="Mr", company="Test company", address="Russia, Moscow", home_phone="123456",
                               mobile_phone="+7912000000", work_phone="222333", fax="2223334", email="test@email.com", email2="test2@email.com",
                               email3="test3@email.com", home_page="https:/google.com", b_day="5", b_month="February", b_year="1984", a_day="8", a_month="October", a_year="1999",
                               secondary_address="Test secondary address", phone2="55", note="Test note"))

    app.session.logout()

