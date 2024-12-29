from anticaptchaofficial.imagecaptcha import imagecaptcha

solver = imagecaptcha()
solver.set_verbose(0)
#solver.set_key("123")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

captcha_text = solver.solve_and_return_solution("image.png")
if captcha_text != 0:
    print("captcha text "+ captcha_text)
else:
    print("task finished with error "+ solver.error_code)


def xevil_request():
    solver = imagecaptcha()
    solver.set_verbose(0)
    #solver.set_key("123")
    # Specify softId to earn 10% commission with your app.
    # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
    solver.set_soft_id(0)
    captcha_text = solver.solve_and_return_solution("./captcha.png")
    if captcha_text != 0:
        return captcha_text
    else:
        print("task finished with error "+ solver.error_code)


captcha_text = xevil_request()
if "*" in captcha_text or "XEvil" in captcha_text or "ERROR_NO_SLOT_AVAILABLE" in captcha_text:
    print("XEvil")
    captcha_text = xevil_request()
