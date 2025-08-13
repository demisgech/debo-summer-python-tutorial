from secret_code import generate_code

def send_verification_email(fromm,to,message=f"{generate_code()}"):
    print(f"<{fromm}> to <{to}>")
    print(f"code : { message }")
    
    