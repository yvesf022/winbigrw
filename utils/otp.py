import random
from config import OTP_LENGTH

def generate_otp():
    return str(random.randint(10**(OTP_LENGTH-1), 10**OTP_LENGTH - 1))
