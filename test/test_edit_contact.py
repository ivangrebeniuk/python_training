from model.contact import Contact


def test_edit_first_contact(app):
    app.open_home_page()
    app.contact.edit_first_contact(Contact(first_name="Jane", middle_name="Zzz", last_name="Aaa", nickname="Patric Star", title="Ms", company="Updated company", address="Bikini bottom, World Ocean", home_phone="000111",
                               mobile_phone="000000", work_phone="000000", fax="00000", email="test@test.com", email2="test2@test.com",
                               email3="test3@test.com", home_page="https:/google.com", b_day="1", b_month="January", b_year="2019", a_day="2", a_month="January", a_year="2019",
                               secondary_address="Test secondary address", phone2="01", note="Hello world"))
