class Config:
    # Expert
    EXPERT_BASE_URL = 'https://expert-excel.got-it.io/'
    EXPERT_EMAIL_LOGIN_FB = 'honghaijumili206@gmail.com'
    EXPERT_PASSWORD_LOGIN_FB = '123456Aa@'

    # Asker
    headers = {
        'Origin': 'https://www.got-it.io',
        'X-GotIt-Product': 'excelchat',
        'Content-Type': 'application/json',
        'X-GotIt-Site': 'excelchat',
        'X-GotIt-Vertical': 'excel'
    }
    base_url = 'https://api.got-it.io/'

    ASKER_EMAIL_LOGIN = 'jasmine@gotitapp.co'
    ASKER_PASSWORD_LOGIN = '1234Aa'
    SUBJECT_ID = -1000
    ASKER_QUESTION = '[Jasmine] I need a formula to combine column C with the numbers in columns L10 to L20'
    ASKER_MESSAGE = 'thank you, next'
