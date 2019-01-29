import random
import primes

primelist = []
def prime_gen():
	for a in range(0,200):
		k=0
		for i in range(2,a//2+1):
			if(a%i==0):
				k=k+1
		if(k<=0):
			primelist.append(a)
prime_gen()


def mul_inv(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Keys(object):

	def __init__(self, p, q, n):
		self.p = p
		self.q = q
		self.n = n
		self.phi = (p-1)*(q-1)
		self.e = random.randint(1,self.phi)
		
		while gcd(self.e,self.phi) != 1:
			self.e = random.randint(1,self.phi)
		
		self.d = mul_inv(self.e,self.phi)
		

	def __repr__(self):
		return '<Key: %s %s %s>' % (self.e, self.d, self.n)

def generate_keypair_R(bits):
	#p = 43
	#q = 41
	"""
	while True:
		i = random.randint(0,len(primelist))
		p = primelist[i]
		j = random.randint(0,len(primelist))
		q = primelist[j]
		if p != q:
			break
	"""
	p = primes.generate_prime(bits / 2)
	q = primes.generate_prime(bits / 2)
	n = p * q
	return Keys(p, q, n)

def encrypt_R(pubkey,plain,n):
	cipher = pow(plain,pubkey,n)
	return cipher	

def decrypt_R(privkey,cipher,n):
	plain = pow(cipher,privkey,n)
	return plain

def e_mul_R(a, b, n):
		return a * b % n

#keys = generate_keypair_R(16)
#x=10
#y=5

#cx = encrypt_R(keys.e, x, keys.n)
#print(cx)
#dx = decrypt_R(keys.d, cx, keys.n)
#print(dx)



#print(keys.p)
#print(keys.q)
#print(keys.e)
#print(keys.d)