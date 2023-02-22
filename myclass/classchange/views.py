from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    {
  "type": "service_account",
  "project_id": "myclass-beta",
  "private_key_id": "f334a18f306e0885e1c6937a0a7a0dba3d20ac31",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCtUobckUVVZVoR\nRWAZUjTIt7CG479gIkKanXXlJDHWk0QnX49dEHq2YBzpwTfcdzgBMO6DMnX3ivlm\nAdGpHjauTTu1Oox5B4vAmlkw+ADeYTA3Er2/GpfWP8AmKoJS+yoQBpSCDW++iqEO\np0vyuG+q/yXP8fy5BN8YnVP2RGtMA/LRYq4PRj5/EuLKvWfYHGyS0biiAi+I5ouF\niaheIpyhlbuIS9rL1iVERlL5K02llE8J9FxFhHBzC9skNpuUjdX/2/mQpmbnQheA\nZONfziCGeKc+saMAYZxpWKiWQu+MOZe4FM1t90yhJU7ti3AQjno2QJj8YdUeYBLF\nonwhU/ShAgMBAAECggEABo3ZnDMhHlDSFlebgfGeHd32Xq9zj/DTuHGOYP8cpFrW\nx69hJjmGjml1hnBgSqW2eDMPveXVWKpIco9MjJrgIfi5Mon3gGck5YBgsY2bSM1/\ni4GZq8WXaspn23mdioJFbaw2BvH3oQqwevOgF1panKp/1Ux3DE8PGajvYR9muE3Y\n9Vjfr5MkBEmvH/GMyiH+GFkqXl0F8EeAYGXBGsVEIRUOT4PIIsOwGddk9wd2+cHA\ns12m6fFtSay7hz9o2WpSo+kneaEdST5tli7CdKp/ngpkCZ268WSYfKVILlTbShI4\n0T1vys1uLyGquMrb9pik5pDccc0rQDzzl3ZXjpoFzQKBgQDgItKUl72evBDaudYX\nTpNA4ymNc8wlkuhJ3Lk3Z23bWZzuOIzxszVIjUR0QnzaRC7T9IBCoCYJPOH6DiY0\nmV+BqPbKiL9mv0a+Vbe4U8Venj6NsyAcoVIkh8IHToWb0ReHXNlKlHd9wGBJBfu5\nW5t95/uF0PaN0q9lz1NI+McJzQKBgQDF9mYNsjmrKGaTdFYarIZiRSekhxXAsN3h\nzwVu68UPi6pBILw8K16Vif7RHKT/leZ0H+1/uJlJEE1x1eVrhMHO9OluRaPQRBvN\nNhtZBcoT2EQ3CUf4WUWOvKg8CSmY8tXxu3Rs5lZB8kSwiEko/FFFkxDHYhqfZKrh\n9pmtG7uyJQKBgAWN11oHSJOeZWyGHmAFenCpMGZo8C4eLdNmvNA6p+Y/mjvs+tEi\nd7eMiJ246A8gkWh/Lo54GXkxIQhpQVkcU9mKrlLmgJezNbWRujO/H6zwjuxD/A+5\nj6eIFa7Iq1bpH4QjMN9APpXHJpuookw9kOTV0s3GF9X72ozTTmUIhSYhAoGBAJ+2\nXTurkM8/9xH8CAPZMUpTVNpuieQ+TaUCqvWEjiYunhuRV4yLyPGItebr30q9G4KQ\nx8IFotXJq1GuKjwGjX51JWdsE+/RI0T65DF8dD5yewaUHFaHX5D7MBfPpJnbQTSX\n8iRx6SGnXje2nJ/OgZtKPX0+7w+t3hgUJoP9Hf9pAoGAfs4/ZtaSA78VkasoOYyW\nJkft59wlEJbJWJ6HS2mBP6Q5+ZMLvuln2INXCVNJV5Iix4Sk7x5tn3ff3Ursdyg7\niamr214/XJMGu6XU06zCFF5OuJNyKoKPjGT50pZYSVQiy+I//CIZ1y72b6Em8mJy\nS+3zc09IhWRZBi/US0G3h6o=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-8m4fl@myclass-beta.iam.gserviceaccount.com",
  "client_id": "109875984940575449447",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8m4fl%40myclass-beta.iam.gserviceaccount.com"
}
)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myclass-beta-default-rtdb.firebaseio.com'
},
)

ref = db.reference('Data')

def form(request):
    return render(request, 'form.html')

def submitform(request):

    oc = request.POST.get('suboc')
    nc = request.POST.get('subnc')
    teacher = request.POST.get('subteach')
    date = request.POST.get('subdate')
    session = request.POST.get('subsession')
    sub = request.POST.get('sub')
    major = request.POST.get('class')

    ref.push({
        'Teacher':teacher,
        'Major': major,
        'Subject': sub,
        'Date': date,
        'Session': session,
        'OldClassroom': oc,
        'NewClassroom': nc
    })

    return render(request, 'form.html')

def getchanges(request):
    changes = ref.get()
    return render(request, 'changes.html', {'changes': changes})

def deletechange(request, key):
    ref.child(str(key)).delete()
    return redirect('/logs')