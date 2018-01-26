import random
import string

def generate(size=6,chars=string.ascii_lowercase+string.digits):
	# return ''.join(random.choice(chars) for _ in range(size))
	new_code = ''
	for _ in range(size):
		new_code += random.choice(chars)
	return new_code

def create_shortcode(instance,size=6):
	new_code = generate(size=size)
	TempClass = instance.__class__
	qs = TempClass.objects.filter(shortcode=new_code).exists()
	if qs:
		return create_shortcode(size=size)
	return new_code