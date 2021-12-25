# Function VAT
def get_vat(payment, percent=20):
	try:
		peyment = float(payment)
		vat = payment * percent / 100
		return "Sum VAT: {}".format(vat)
	except TypeError:
		return "Can't count. Check data!"	

result =get_vat(400, 15)

print(result)