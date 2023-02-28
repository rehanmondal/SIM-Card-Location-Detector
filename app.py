from flask import Flask,request,render_template
from phonenumbers import timezone,carrier,geocoder
import phonenumbers

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def tracker():
    if request.method =='POST':
        country_code = request.form.get('country_code')
        number =  request.form.get('con')

        final_number = '+' + country_code + number

        contact = phonenumbers.parse(final_number)
        zone = timezone.time_zones_for_number(contact)  # for loop front end
        provider = carrier.name_for_number(contact, "en")  # for getting in english
        registration = geocoder.description_for_number(contact, "en")

        return render_template('index.html',code=country_code, detail = final_number,phone = number,timezone= zone,service = provider,registered = registration)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
