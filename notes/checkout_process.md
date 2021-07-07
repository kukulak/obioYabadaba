<!-- CheckOUt Process -->

1. Cart --> CheckOUt View
  ?
  -Login/Register or enter an email (as guest)
  -shipping address
  -billing info
      -billing address
      -credit card/payment

2. Billing App/Component
  -Billing profile
    -user or email (guest email)
    -generating payment Processor token (stripe or Braintee)

3. orders/invoices Component
  -connencting the Billing profile
  -shipping / billing address
  -Cart
  -status - dilivered shipped cancelled?

4. Backup Fixtures
  C:\Users\user\ecom\src>python manage.py dumpdata products --format json --indent 4 > products/fixtures/products.json
