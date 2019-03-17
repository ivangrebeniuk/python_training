# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, home_phone=None,
                 mobile_phone=None, work_phone=None, fax=None, email=None, email2=None, email3=None, home_page=None, b_day=None, b_month=None, b_year=None,
                 a_day=None, a_month=None, a_year=None, secondary_address=None, phone2=None, note=None, id=None):
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

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
