import math
import primes
import random

#primelist = []
#def prime_gen():
#	for a in range(10000,20000):
#		k=0
#		for i in range(2,a//2+1):
#			if(a%i==0):
#				k=k+1
#		if(k<=0):
#			primelist.append(a)
#prime_gen()
def invmod(a, p, maxiter=1000000):
    """The multiplicitive inverse of a in the integers modulo p:
         a * b == 1 mod p
       Returns b.
       (http://code.activestate.com/recipes/576737-inverse-modulo-p/)"""
    if a == 0:
        raise ValueError('0 has no inverse mod %d' % p)
    r = a
    d = 1
    for i in range(min(p, maxiter)):
        d = ((p // r + 1) * d) % p
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d

def modpow(base, exponent, modulus):
    """Modular exponent:
         c = b ^ e mod m
       Returns c.
       (http://www.programmish.com/?p=34)"""
    result = 1
    while exponent > 0:
        if exponent & 1 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)
	
class PrivateKey_P(object):

	def __init__(self, p, q, n):
		self.p = p
		self.q = q
		self.n_sq = n*n
		self.g = n + 1 #g should be random but zeel = n+1
		self.gL = int(lcm((p-1),(q-1)))
		self.l = (pow(self.g,self.gL,self.n_sq)-1)//n
		self.m = invmod(self.l, n)

	def __repr__(self):
		return '<PrivateKey: %s %s>' % (self.gL, self.m)


class PublicKey_P(object):

    @classmethod
    def from_n(cls, n):
        return cls(n)

    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1

    def __repr__(self):
        return '<PublicKey: %s %s>' % (self.n,self.g)


smallprimes = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
		
def generate_keypair_P(bits):
	#p = 43
	#q = 41
	#while True:
	#	i = random.randint(0,1032)
	#	p = primelist[i]
	#	j = random.randint(0,1032)
	#	q = primelist[j]
	#	if p != q:
	#		break
	p = primes.generate_prime(bits / 2)
	q = primes.generate_prime(bits / 2)
	n = p * q
	return PrivateKey_P(p, q, n), PublicKey_P(n)

def encrypt_P(pub,plain):
	if plain > pub.n:
		print("Condition not satisfied (0<plain<n)")
	else:
		while True:
			r  = primes.generate_prime(long(round(math.log(pub.n, 2))))
			if r > 0 and r < pub.n:
				break
		k1 = pow(pub.g,plain,pub.n_sq)
		k2 = pow(r,pub.n,pub.n_sq)
		cipher = k1*k2 % pub.n_sq
	return cipher,r

"""
def encrypt(pub, plain):
    while True:
        r  = primes.generate_prime(long(round(math.log(pub.n, 2))))
        if r > 0 and r < pub.n:
            break
    x = pow(r, pub.n, pub.n_sq)
    cipher = (pow(pub.g, plain, pub.n_sq) * x) % pub.n_sq
    return cipher
"""
def e_add_P(pub, a, b):
    """Add one encrypted integer to another"""
    return a * b % pub.n_sq
	
def e_mul_P(pub, a, b):
    """Add one encrypted integer to another"""
    return a + b % pub.n_sq
	
	
def e_add_const_P(pub, a, n):
    """Add constant n to an encrypted integer"""
    return a * modpow(pub.g, n, pub.n_sq) % pub.n_sq

def e_mul_const_P(pub, a, n):
    """Multiplies an ancrypted integer by a constant"""
    return modpow(a, n, pub.n_sq)

def decrypt_P(priv,pub,cipher):
    l_decr = (pow(cipher,priv.gL,pub.n_sq)-1)//pub.n
    plain = (l_decr*priv.m) % pub.n
    
    return plain
	
"""
def decrypt(priv, pub, cipher):
    x = pow(cipher, priv.l, pub.n_sq) - 1
    plain = ((x // pub.n) * priv.m) % pub.n
    return plain
	
"""

