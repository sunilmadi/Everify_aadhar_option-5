def sendsms(aadharnum,bank):
    import datetime as dt
    from twilio.rest import Client
    number='+917507483508'
    account_sid = 'AC9ca57309561dff05e457f51f0d40370a'
    auth_token = 'd5a27293ea20119e6a61f540983efb30'
    client = Client(account_sid, auth_token)
    body1="Your e-verification is complete for aadhar number : '{0}' by {1} bank at {2}"
    body2=body1.format(aadharnum,bank,dt.datetime.today())
    message = client.messages.create(
                body=body2,
                from_='+17065100684',
                to=number,
                )