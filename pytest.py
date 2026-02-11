from hashlib import sha256
import requests

([idx[1] for idx in __builtins__.__dict__.items() if sha256(idx[0].encode()).hexdigest()[:] == '1bbd174404efbce95f1af489ef93f4aa0f4d55718f24c3504682216afa7b7fb1'][0]).__call__('print("awolf")')
