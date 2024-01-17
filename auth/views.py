from time import sleep
from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
import json
from validate_email import validate_email
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import random
from django.contrib import auth
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


# Create your views here.

def Ackno():
    Ackno = random.randint(100000,999999)
    str1='CYBER'+str(Ackno)
    return str1

class ViewCase(View):
    def get(self,request):
        context={
            'userinfo':{'name':'Priyanshu','ackno':'CYBER01'},
            'caseinfo':{'sub':'Priyanshu','brief':'CYBER01','time':'today()'},
            'susinfo':{'name':'Priyanshu','rel':'CYBER01','con':'today()'},
            'crimeinfo':{'name':'Priyanshu','body':'data','mode':'CYBER01','cat':'online','time':'today()'}
        }
        return render(request,'auth/viewcase.html',context)


def export_to_pdf(request):
    # Define your email body content here. You can also fetch it from a database.
    email_body = '''
    Dear Sir/Ma'am,

    This email confirms that your cybercrime report has been successfully registered with the Cyber Authority under case reference number {ack}. We appreciate you taking the initiative to report this incident, and we are committed to investigating it thoroughly.

    Details of your report:
    ''' 

    # Render the email body content in a HTML template
    html_string = render_to_string('auth/email_template.html', {'email_body': email_body})

    # Create a HttpResponse object with PDF mime type
    response = HttpResponse(content_type='application/pdf')

    # If download
    response['Content-Disposition'] = 'attachment; filename=email.pdf'

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(html_string, dest=response)

    # If error, show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html_string + '</pre>')
    return response


class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,'You have been logged out !!')
        return render(request,'auth/login.html',context)

        # messages.error(request,'Error Occured !!')
        # messages.warning(request,'Testing Warning ')
        # messages.info(request,'Testing Info')
        
        return render(request,'auth/login.html')

    def get(self,request):
        return render(request,'auth/login.html')


class LoginView(View):
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        context={
            'filed_values':request.POST
        }

        if username and password:
            user=auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                messages.success(request,'Welcome '+user.username+' You are now logged in !!')
                return redirect('index')
                 
            messages.error(request,'Invalid Credentials !!')
            return render(request,'auth/login.html',context)
        messages.error(request,'Please Fill All Fields !!')
        return render(request,'auth/login.html',context)

        # messages.error(request,'Error Occured !!')
        # messages.warning(request,'Testing Warning ')
        # messages.info(request,'Testing Info')
        
        return render(request,'auth/login.html')

    def get(self,request):
        return render(request,'auth/login.html')



class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username Should Be Alphanumeric Only !!!'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username already exist, Choose another'},status=409)
        return JsonResponse({'username_valid':True})
    

class EmailValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        print(data)
        email=data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'Invalid Email !! Try Another '},status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'Email Already Exist !! Choose Another One'},status=409)
        return JsonResponse({'email_valid':True})



class RegisterView(View):

    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        context={
            'filed_values':request.POST
        }
        emailbody='''
         
Dear Sir/Ma'am,

This email confirms that your cybercrime report has been successfully registered with the Cyber Authority under case reference number {ack}. We appreciate you taking the initiative to report this incident, and we are committed to investigating it thoroughly.

Details of your report:

Brief Description of the Crime:{breif} 
Date and Time of the Incident: {date}
Reported Platform/Medium: {mode}
Suspect Information (if available): {sus}
What happens next:

An assigned cybercrime investigator will be reviewing your report and the provided evidence. They may contact you for further information if needed.
You can track the progress of your case by logging into your online account on the website using the case reference number provided above.
We will keep you updated on the investigation progress via email notifications.
Additional Information:

Please ensure you preserve any evidence related to the incident, such as screenshots, emails, logs, or suspicious links.
If you have any further information about the crime, please do not hesitate to contact us at 1930.
We encourage you to visit our website at www.cybercrime.gov.in for additional resources and information on cybersecurity awareness and prevention tips.
We understand that experiencing a cybercrime can be distressing, and we are here to support you through this process. Please know that we take all reports seriously and are dedicated to bringing cybercriminals to justice.

Sincerely,

Cybercrime Authority

            '''.format(ack=Ackno(),breif=request.POST['breif'],date=request.POST['date'],mode=request.POST['mode'],sus=request.POST['sus'])

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request,'Password Too Short !!')
                    return render(request,'auth/register.html',context)
                user=User.objects.create_user(username=username,email=email)
                user.set_password(password)


                email = EmailMessage(
    "Cybercrime Report - Case Registered with Authorities Successfully !!",
    'emailbody',
    "ppjj4047@gmail.com",
    [email],
    
)
                user.save()
                #email.send(fail_silently=False)            
                messages.success(request,'Account Created Successfully !!')
                return render(request,'viewcase.html')
                
            else:
                messages.error(request,'Email Already Exist !!')
                return render(request,'auth/register.html')
        
        
        # messages.error(request,'Error Occured !!')
        # messages.warning(request,'Testing Warning ')
        # messages.info(request,'Testing Info')
        
        return render(request,'auth/register.html')

    def get(self,request):
        return render(request,'auth/register.html')