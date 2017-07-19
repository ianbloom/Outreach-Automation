import requests
import json
import webbrowser
import urllib2
from Tkinter import *

    
outreach_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpYW4uYmxvb21AbG9naWNtb25pdG9yLmNvbSIsImlhdCI6MTQ5ODg2MDM4OCwiZXhwIjoxNDk4ODY3NTg4LCJiZW50byI6ImFwcDJhIiwib3JnX3VzZXJfaWQiOjE1MiwiYXVkIjoiTG9naWNNb25pdG9yIiwic2NvcGVzIjoicHJvZmlsZSBlbWFpbCBjcmVhdGVfcHJvc3BlY3RzIHJlYWRfcHJvc3BlY3RzIHVwZGF0ZV9wcm9zcGVjdHMgcmVhZF9zZXF1ZW5jZXMgdXBkYXRlX3NlcXVlbmNlcyByZWFkX3RhZ3MgcmVhZF9hY2NvdW50cyBjcmVhdGVfYWNjb3VudHMgcmVhZF9hY3Rpdml0aWVzIHJlYWRfbWFpbGluZ3MgcmVhZF9tYXBwaW5ncyByZWFkX3BsdWdpbnMgcmVhZF91c2VycyBjcmVhdGVfY2FsbHMgcmVhZF9jYWxscyByZWFkX2NhbGxfcHVycG9zZXMgcmVhZF9jYWxsX2Rpc3Bvc2l0aW9ucyBBSkVBa2dEQkFNSUJBUUFSQUJJQVVRQmhBUEVBUVFCQ0FDRUFNUT09Iiwibm9uY2UiOiI5ZDlkZWJmMyJ9.Apn4t5FShDOZ8miQKovUMVEDcQTU3R6YCjXxaE3NyKg"

url_proto = 'https://api.outreach.io/1.0/prospects/'

def prospect_search(query):
    api_key = outreach_api_key
    url = url_proto + str(query)
    r = requests.get(url, headers = {"Authorization":"Bearer " + api_key})
    data = r.json()
    company_name = data['data']['attributes']['company']['name']
    linked_in = data['data']['attributes']['social']['linkedin']

    print("company name is: " + str(company_name))
    print("prospect linkedin is: " + str(linked_in))
    webbrowser.open(linked_in)
    

"""
def run_it():
    prospect_id = entry.get()
    prospect_search(prospect_id)
    print("poop")


root = Tk()
Label(root, text="Prospect ID").grid(row=0)

entry = Entry(root)
entry.insert(0, "103452")
entry.grid(row=0, column=1)

butt = Button(root, text='Open', command = run_it)
butt.grid(row=0, column=2)

root.mainloop()
"""





    
