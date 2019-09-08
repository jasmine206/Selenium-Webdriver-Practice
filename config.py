class Config:
    # Expert
    EXPERT_BASE_URL = 'https://expert-excel.got-it.io/'
    EXPERT_EMAIL_LOGIN_FB = 'honghaijumili206@gmail.com'
    EXPERT_PASSWORD_LOGIN_FB = '123456Aa@'

    # Asker
    headers_asker = {
        # 'Origin': 'https://www.got-it.io',
        'X-GotIt-Product': 'excelchat',
        'Content-Type': 'application/json',
        'X-GotIt-Site': 'excelchat',
        'X-GotIt-Vertical': 'excel'
    }
    base_url_asker = 'https://api.got-it.io/'

    ASKER_EMAIL_LOGIN = 'jasmine+2@gotitapp.co'
    ASKER_PASSWORD_LOGIN = '1234Aa'
    SUBJECT_ID = -1000
    ASKER_QUESTION = '[Jasmine] I need a formula to combine column C with the numbers in columns L10 to L20'
    ASKER_MESSAGE = 'thank you, next'
    ASKER_IMAGE_PATH = '../Selenium-Webdriver-Practice/files/percent-change-formula.png'
    ASKER_EXCEL_FILE_PATH = '../Selenium-Webdriver-Practice/files/YSL.xlsx'

    # Admin
    headers_admin = {
        'Origin': 'https://www.got-it.io',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjMzOGNiN2Y0IiwiaWF0IjoxNTYyMDQzNjg'
                         '2LCJzdWIiOjg4LCJleHAiOjE1OTM1Nzk2ODYsImF1ZCI6ImFkbWluIn0.dB9YLRNozvu-Kwzr0rzaneYG8uvs9Xn1l'
                         'j9eirWT8ak',
        'Content-Type': 'application/json',
        'X-GotIt-Vertical': 'excel'
    }
    base_url_admin = 'https://api.got-it.io/admin/'
