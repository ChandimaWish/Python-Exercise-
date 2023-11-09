
Details = {
    'Store Name':'Food City',
    'Address':'Alawwa',
    'Contact Number':'0714127171'
}
print(Details)
Number = int(input('Enter Contact Number'))
Details.update({f'Contact Number':{Number}})
print(Details)