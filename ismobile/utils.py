import re

def get_is_mobil(http_user_agent):
    if http_user_agent is None:
        # Default to assuming desktop if no user-agent header is
        # present.
        return False

    is_mobile_re=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
    return is_mobile_re.match(http_user_agent) != None
