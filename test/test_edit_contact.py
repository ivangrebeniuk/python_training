from model.contact import Contact


def test_edit_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="John", middle_name="Doe", last_name="Doe", nickname="Sponge Bob", title="Mr",
                    company="Test company", address="Russia, Moscow", home_phone="123456",
                    mobile_phone="+7912000000", work_phone="222333", fax="2223334", email="test@email.com",
                    email2="test2@email.com",
                    email3="test3@email.com", home_page="https:/google.com", b_day="5", b_month="February",
                    b_year="1984", a_day="8", a_month="October", a_year="1999",
                    secondary_address="Test secondary address", phone2="55", note="Test note"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(first_name="Jane", middle_name="Zzz", last_name="Aaa", nickname="Patric Star", title="Ms", company="Updated company", address="Bikini bottom, World Ocean", home_phone="000111",
                               mobile_phone="000000", work_phone="000000", fax="00000", email="test@test.com", email2="test2@test.com",
                               email3="test3@test.com", home_page="https:/google.com", b_day="1", b_month="January", b_year="2019", a_day="2", a_month="January", a_year="2019",
                               secondary_address="Test secondary address", phone2="01", note="Hello world"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
