# Intra-package referene via absolute path (best practise)
from ecommerce.customer import contact as abs_contact

# Intra-package referene via relative path
from ..customer import contact as rel_contact

abs_contact.contact_customer()
rel_contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass
