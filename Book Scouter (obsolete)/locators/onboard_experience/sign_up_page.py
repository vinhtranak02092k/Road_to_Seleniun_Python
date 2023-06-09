class SignUpPage:
    # some locators have not been given the value
    TXT_EMAIL: str = "//input[contains(@name, 'email')]"
    TXT_PASSWORD: str = "//input[contains(@name, 'password')]"
    BTN_SHOW = ""
    CHK_NEWSLETTER: str = \
        "//div[contains(@class, 'SignUpCheckbox')]//span[following-sibling::span[contains(text(), 'Newsletter')]]"
    CHK_BECOME_PRO: str = \
        "//div[contains(@class, 'SignUpCheckbox')]//span[following-sibling::span[contains(text(), 'Become a Pro')]]"
    BTN_SIGN_UP: str = "//button[@type = 'submit' and contains(@name, 'Sign Up')]"
    BTN_CONTINUE_AMAZON = ""
    BTN_CONTINUE_FACEBOOK = ""
    BTN_CONTINUE_TWITTER = ""
    BTN_CONTINUE_GOGGLE = ""
    BTN_CLOSE = ""
    BTN_FORGOT_PASSWORD = ""
    BTN_LOG_IN = "//button[@name = 'Log in']"

    # sign-up combined with becoming a pro flow
    LBL_PRO: str = "//h2[parent::div[contains(@class, 'ModalHeader')]]"
    IMG_HANDSHAKE: str = \
        "//div[contains(@class, 'SignUpProPreviewCards')]//img[parent::div[contains(@aria-label, 'handshake')]]"
    IMG_COUNT: str = \
        "//div[contains(@class, 'SignUpProPreviewCards')]//img[parent::div[contains(@aria-label, 'count')]]"
    IMG_CLOCK: str = \
        "//div[contains(@class, 'SignUpProPreviewCards')]//img[parent::div[contains(@aria-label, 'clock')]]"
    IMG_MONEY: str = \
        "//div[contains(@class, 'SignUpProPreviewCards')]//img[parent::div[contains(@aria-label, 'money')]]"
    IMG_CALENDAR: str = \
        "//div[contains(@class, 'SignUpProPreviewCards')]//img[parent::div[contains(@aria-label, 'calendar')]]"
    TXT_CC_NUMBER: str = "//input[contains(@name, 'cardnumber') and contains(@inputmode, 'numeric')]"
    TXT_EXPIRED_DATE: str = "//input[contains(@name, 'exp-date') and contains(@inputmode, 'numeric')]"
    TXT_CVC: str = "//input[contains(@name, 'cvc') and contains(@inputmode, 'numeric')]"
    LBL_INVALID_CC_NUMBER: str = \
        "//span[contains(@class, 'PaymentInputErrorMsg')][preceding-sibling::label[contains(text(), 'Credit Card')]]"
    LBL_INVALID_EXPIRED_DATE: str = \
        "//span[contains(@class, 'PaymentInputErrorMsg')][preceding-sibling::label[contains(text(), 'Expiration Date')]]"
    LBL_INVALID_CVC: str = \
        "//span[contains(@class, 'PaymentInputErrorMsg')][preceding-sibling::label[contains(text(), 'CVC')]]"
    BTN_REGISTER_CARD: str = "//button[@type = 'button' and contains(text(), 'Sign up!')]"
    LBL_INPUT_EMAIL_ERR_MSG: str = \
        "//span[contains(@class, 'ErrorMsg')][preceding-sibling::label[contains(text(), 'Email')]]"
    LBL_INPUT_PWD_ERR_MSG: str = \
        "//span[contains(@class, 'ErrorMsg')][preceding-sibling::label[contains(text(), 'Password')]]"
    LBL_INVALID_EMAIL_ERR_MSG: str = LBL_INPUT_EMAIL_ERR_MSG
    LBL_INVALID_PWD_ERR_MSG: str = LBL_INPUT_PWD_ERR_MSG
    ALE_TOAST_EXISTED_EMAIL: str = \
        "//div[@role = 'alert']//div[contains(@class, 'toast-icon')]//following-sibling::div"
