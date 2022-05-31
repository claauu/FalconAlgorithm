
from common import q, sqnorm
from fft import add, sub, mul, div, neg, fft, ifft
from ntt import mul_zq, div_zq
from samplerz import samplerz, MAX_SIGMA
from ffsampling import ffldl, ffldl_fft, ffnp, ffnp_fft
from ffsampling import gram
from random import randint, random, gauss, uniform
from math import sqrt, ceil
from ntrugen import karamul, ntru_gen, gs_norm
from falcon import SecretKey, PublicKey, Params
from falcon import SALT_LEN, HEAD_LEN, SHAKE256
from encoding import compress, decompress
from scripts import saga
from scripts.samplerz_KAT512 import sampler_KAT512
from scripts.sign_KAT import sign_KAT
from scripts.samplerz_KAT1024 import sampler_KAT1024
# https://stackoverflow.com/a/25823885/4143624
from timeit import default_timer as timer

"""Generate the complex roots of x ** 2 + 1."""
phi4 = cyclotomic_polynomial(4)
phi4_roots = phi4.complex_roots()
phi4_roots.reverse()

"""Generate the complex roots of x ** n + 1, for n = 4, 8, 16, ..., 1024."""
phi8_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi4_roots], [])
phi16_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi8_roots], [])
phi32_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi16_roots], [])
phi64_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi32_roots], [])
phi128_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi64_roots], [])
phi256_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi128_roots], [])
phi512_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi256_roots], [])
phi1024_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi512_roots], [])
phi2048_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi1024_roots], [])
phi4096_roots = sum([[sqrt(elt), - sqrt(elt)] for elt in phi2048_roots], [])
print (phi4096_roots)

"""Generate the roots of x ** n + 1 in Z_q,
	for q = 12 * 1024 + 1 and n = 4, 8, 16, ..., 1024."""
q = 12 * 1024 + 1
Zq = Integers(q)
phi4_roots_Zq = [sqrt(R(- 1)), - sqrt(R(- 1))]
phi8_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi4_roots_Zq], [])
phi16_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi8_roots_Zq], [])
phi32_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi16_roots_Zq], [])
phi64_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi32_roots_Zq], [])
phi128_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi64_roots_Zq], [])
phi256_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi128_roots_Zq], [])
phi512_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi256_roots_Zq], [])
phi1024_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi512_roots_Zq], [])
phi2048_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi1024_roots_Zq], [])
phi4096_roots_Zq = sum([[sqrt(elt), - sqrt(elt)] for elt in phi2048_roots_Zq], [])

print (phi4096_roots_Zq)

