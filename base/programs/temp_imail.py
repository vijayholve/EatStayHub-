
# send email using python
import smtplib
from django.contrib.auth.models import User
def send_email():
    email="vijucode@gmail.com"
    user=User.objects.all()
    subject="how are you"
    body="hello "
    text=f"subject {subject} {body}"
    for i,single_user in enumerate(user):
        try:
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(email,"iemk dqsj ejqj zcop")
            server.sendmail(email,single_user.email,text)
            print("user are",i)
        except:
            print("error in ",i)
    print("done")