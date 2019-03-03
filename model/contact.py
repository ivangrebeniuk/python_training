# -*- coding: utf-8 -*-


class Contact:

    def __init__(self, first_name, middle_name, last_name, nickname, title, company, address, home_phone,
                          mobile_phone, work_phone, fax, email, email2, email3, home_page, b_day, b_month, b_year,
                          a_day, a_month, a_year, secondary_address, phone2, note, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.home_page = home_page
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year
        self.secondary_address = secondary_address
        self.phone2 = phone2
        self.note = note
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

