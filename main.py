import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

#what is after =, decode it first online
template = """ """

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def pig_latin_translator(fact):
    #analyze network traffice
    payload = {"input_text": fact}
    print(f"payload is {payload}")
    #form data
    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", allow_redirects=False, data=payload)
    #from the respones, from the response header get the value of the location header
    print(f"imitate a post request and get response: {response}")
    print(f"response.headers: {response.headers}")
    print(f"response.content: {response.content}")

    return response.headers['Location']


@app.route('/')
def home():
    fact = get_fact().strip()
    new_web_address = pig_latin_translator(fact)
    #ew web address shows fact translated with pig lattin
    return str(new_web_address)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

