import re
import unicodedata


USERNAME_MAX_SPACES_RE= re.compile(r"\s+")

def normalize_username(username:str)->str:
    if username==None:
        return username
    
    normalize_username= username.strip()
    normalize_username= USERNAME_MAX_SPACES_RE.sub(" ", normalize_username)
    normalize_username = unicodedata.normalize("NFKC", normalize_username)
    return normalize_username.lower()




