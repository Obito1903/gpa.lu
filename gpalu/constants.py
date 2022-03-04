import re

EMAILS_REGEX = re.compile(
    'collapse-(\d{7}).*\n.*title="(.*)".*\n.*\n.*&lt;([\.\-\w]+@[\-\w]+\.[\.\w\-]+)&'
)

GPALU_EMAIL_REGEX = re.compile('[a-zA-Z0-9\_\.\-]+@(les\.codes|gpa\.lu|yarien\.eu|saucent\.online)')

BASE_URL = 'https://gpa.lu/'
