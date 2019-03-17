# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name=random_string("first name", 10), middle_name=random_string("Middle name", 10), last_name=random_string("Last name", 10), nickname=random_string("Nickname", 10), title=random_string("Title", 5), company=random_string("Company", 15), address=random_string("Address", 20), home_phone=random_string("Home", 10),
                                        mobile_phone=random_string("Mobile", 12), work_phone=random_string("Work", 15), fax=random_string("Fax", 10), email=random_string("Email", 20), email2=random_string("Email2", 20),
                                        email3="", home_page="", b_day="5", b_month="February", b_year="1984", a_day="8", a_month="October", a_year="1999",
                                        secondary_address=random_string("Addres2", 20), phone2=random_string("Phone2", 10), note=random_string("Note", 20)) for i in range(2)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    #old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)

