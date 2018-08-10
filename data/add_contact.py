# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string


constant = [
    Contact(firstname='firstname', middlename='middlename', lastname='lastname', nickname='nickname', title='title',
            company='company', address='address', home='home', mobile='mobile', work='work', fax='fax', email='email',
            email2='email2', email3='email3', homepage='homepage', byear='byear', ayear='ayear', address2='address2',
            phone2='phone2', notes='notes')

]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname='', middlename='', lastname='', nickname='', title='', company='', address='', home='',
            mobile='', work='', fax='', email='', email2='', email3='', homepage='', byear='', ayear='',
            address2='', phone2='', notes='')] + [Contact(firstname=random_string('firstname', 10),
            middlename=random_string('middlename', 10), lastname=random_string('lastname', 10),
            nickname=random_string('nickname', 10), title=random_string('title', 10), company=random_string('company', 10),
            address=random_string('address', 10), home=random_string('home', 10), mobile=random_string('mobile', 10),
            work=random_string('work', 10), fax=random_string('fax', 10), email=random_string('email', 10),
            email2=random_string('email2', 10), email3=random_string('email3', 10), homepage=random_string('homepage', 10),
            byear=random_string('byear', 10), ayear=random_string('ayear', 10), address2=random_string('address2', 10),
            phone2=random_string('phone2', 10), notes=random_string('notes', 10))
            for i in range(5)
]

