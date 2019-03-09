# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(Contact(first_name="Zzzz", middle_name="Zzzz", last_name="Zzzz", nickname="Sponge Bob", title="Mr", company="Test company", address="Russia, Moscow", home_phone="123456",
                                        mobile_phone="+7912000000", work_phone="222333", fax="2223334", email="test@email.com", email2="test2@email.com",
                                        email3="test3@email.com", home_page="https:/google.com", b_day="5", b_month="February", b_year="1984", a_day="8", a_month="October", a_year="1999",
                                        secondary_address="Test secondary address", phone2="55", note="Test note"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()

