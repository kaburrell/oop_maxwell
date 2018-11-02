'''

10/27/18 Ken
My first solution at the classesandmethods_extra.py hw. Trying to build classes
by following a doctest is not the easiest task. It took an iteration to figure
out the desired class interactions.

+ I rewrote a solution
+ RUN this as a regular PyCharm Run configuration and NOT in the doctest mode


Let's create a class to manage invoices. Its constructor will take
an invoice number, the customer name, and the amount of money owed.

>>> invoice = Invoice(12, 'Mark Smith', 42.50)
>>> type(invoice)
<class '__main__.Invoice'>
>>> invoice.number
12
>>> invoice.customer
'Mark Smith'
>>> invoice.amount
42.5

And we'll keep track too of the total payments made. At first, this
will be zero.

>>> invoice.total_payments
0

Now, the customer may make payments in stages (rather than paying all
at once).  So let's create methods to add payments, check whether the
invoice is fully paid off, etc.

>>> invoice.add_payment(20)
>>> invoice.is_fully_paid()
False
>>> invoice.total_payments
20
>>> invoice.amount_due()
22.5

>>> invoice.add_payment(22.50)
>>> invoice.is_fully_paid()
True
>>> invoice.amount_due()
0.0

Sometimes, a customer will submit one large payment for several
invoices. And it may only partially cover one of them. Create a
CustomerAccount class to manage the nuances of this.

>>> customer_name = 'James Jones'
>>> account = CustomerAccount(customer_name)
>>> type(account)
<class '__main__.CustomerAccount'>

Did you know Python class objects have a __name__ attribute?
>>> type(account).__name__
'CustomerAccount'
>>> account.name
'James Jones'

The add_invoice() method takes an instance of the Invoice class.

>>> account.add_invoice(Invoice(1, customer_name, 20.0))
>>> len(account.invoices)
1
>>> account.total_due()
20.0
>>> account.add_invoice(Invoice(2, customer_name, 25.0))
>>> len(account.invoices)
2
>>> account.total_due()
45.0
>>> account.add_invoice(Invoice(3, customer_name, 30.0))
>>> len(account.invoices)
3
>>> account.total_due()
75.0

>>> unpaid = account.unpaid_invoices()
>>> len(unpaid)
3
>>> type(unpaid[0]).__name__
'Invoice'
>>> unpaid[0].number
1
>>> unpaid[0].amount
20.0

>>> account.apply_payment(20)
>>> now_unpaid = account.unpaid_invoices()
>>> len(now_unpaid)
2
>>> now_unpaid[0].number
2
>>> account.total_due()
55.0

>>> account.apply_payment(10)
>>> account.total_due()
45.0
>>> len(account.unpaid_invoices())
2

>>> account.apply_payment(45)
>>> len(account.unpaid_invoices())
0

'''

# Write your code here:

class Invoice(object):

    """
    An invoice that supports multiple payments
    """

    def __init__(self, number, customer, amount):
        # invoice number
        self.number = number

        # customer name
        self.customer = customer

        # invoice amount
        self.amount = amount

        # sum of payments made
        self.total_payments = 0

    def add_payment(self, payment):
        self.total_payments += payment

    def is_fully_paid(self):
        return True if self.total_payments >= self.amount else False

    def amount_due(self):
        return self.amount - self.total_payments


class CustomerAccount(object):
    """
    Account that tracks invoices
    Supports payments that can be applied to multiple invoices
    """

    def __init__(self, name):
        self.name = name
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)


    def total_due(self):
        total_due = 0

        for invoice in self.invoices:
            total_due += invoice.amount_due()

        return total_due


    def unpaid_invoices(self):
        unpaid = []
        for invoice in self.invoices:
            if not invoice.is_fully_paid():
                unpaid.append(invoice)
        return unpaid


    def apply_payment(self, amount):
        unpaid = self.unpaid_invoices()
        while amount > 0:
            invoice = unpaid.pop(0)
            partial = min(amount, invoice.amount_due())
            invoice.add_payment(partial)
            amount -= partial

# Do not edit any code below this line!


if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
