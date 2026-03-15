import time
import datetime
import os
from twilio.rest import Client

# Twilio Details
ACC_SID = 'AC66b7c69257effce1d41745c1232'
AUTH_TOKEN = 'PASTE_YOUR_AUTH_TOKEN_HERE' 
TWILIO_NUM = '+19046592298'
MY_NUM = '+92XXXXXXXXXX' # Apna mobile number likhein

def make_call():
    try:
        client = Client(ACC_SID, AUTH_TOKEN)
        client.calls.create(
            twiml='<Response><Say>Taha Sir, it is 9 PM. Please sleep now. Your watch is watching you!</Say></Response>',
            to=MY_NUM,
            from_=TWILIO_NUM
        )
        print("Jarvis: Call sent successfully!")
    except Exception as e:
        print(f"Jarvis Error: {e}")

print("Jarvis is standing by on Render Cloud...")

while True:
    # Render UTC time use karta hai (Pakistan UTC+5 hai)
    # 9:00 PM PKT = 4:00 PM UTC
    now = datetime.datetime.utcnow() 
    
    if now.hour == 16 and now.minute == 0: 
        make_call()
        time.sleep(60) # 1 minute wait
    
    time.sleep(30)
