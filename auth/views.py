from time import sleep
from django.shortcuts import render, redirect
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
import requests
from bs4 import BeautifulSoup  # Install using: pip install beautifulsoup4

# Create your views here.

def Ackno():
    Ackno = random.randint(100000,999999)
    str1 = 'CYBER' + str(Ackno)
    return str1


def hdfcapi(request):
    apiexp='''
    <pre>
      CustomerInformation API Gateway Service URL's UAT Endpoint :-
      https://api-uat.hdfcbank.com/API/CustomerInformation PROD Endpoint :-
      https://api.hdfcbank.com/API/CustomerInformation API :
      https://api-tryitout-uat.hdfcbank.com/aHNDiZ5fj52HXscBQMBEJwdG3BBNjBNNaeCyKt5ff4DL6RmO
      Request :
      <?xml version="1.0" encoding="UTF-8"?>
      <soapenv:Envelope
        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:soas="soaserver.xsd.hdfcbank.com"
      >
        <soapenv:Header> </soapenv:Header>
        <soapenv:Body>
          <soas:AccountServiceRequest>
            <accountId> </accountId>
            <sourceId> </sourceId>
            <customerId> </customerId>
            <PanNo>BVVPM4039E</PanNo>
            <AadharNo> </AadharNo>
            <MobileNo>8440006083</MobileNo>
            <UCICNo> </UCICNo>
            <soaFillers>
              <filler1> </filler1>
              <filler2> </filler2>
              <filler3> </filler3>
              <filler4> </filler4>
              <filler5> </filler5>
            </soaFillers>
            <soaStandard>
              <service_user> </service_user>
              <service_password> </service_password>
              <consumer_name> </consumer_name>
              <unique_id> </unique_id>
              <time_stamp> </time_stamp>
            </soaStandard>
          </soas:AccountServiceRequest>
        </soapenv:Body>
      </soapenv:Envelope>

      response :

      <?xml version="1.0" encoding="UTF-8"?>
      <soapenv:Envelope
        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
      >
        <soapenv:Body>
          <a:ServiceResponse xmlns:a="soaserver.xsd.hdfcbank.com">
            <SAS_DIM_DEDUPE_OUTPUT>
              <ALL_ACCOUNT>
                <ACCOUNT_INFO>
                  <CUSTOMER_ID>56481406</CUSTOMER_ID>
                  <ACCOUNTID> </ACCOUNTID>
                  <SOURCE_ID>FINNESS</SOURCE_ID>
                  <SAS_ID>34241147</SAS_ID>
                  <FW_CUST_ID>34241147</FW_CUST_ID>
                  <FW_ACCNT_NUM>1681050195505</FW_ACCNT_NUM>
                  <V_D_CUST_FIRST_NAME>SANTOSH</V_D_CUST_FIRST_NAME>
                  <V_D_CUST_MIDDLE_NAME>KUMAR</V_D_CUST_MIDDLE_NAME>
                  <V_D_CUST_LAST_NAME>MAHTO</V_D_CUST_LAST_NAME>
                  <D_D_CUST_START_DATE>2017-04-05 00:00:00</D_D_CUST_START_DATE>
                  <D_D_CUST_CLOSED_DATE
                    >2020-02-29 00:00:00</D_D_CUST_CLOSED_DATE
                  >
                  <V_D_CUST_CHANNEL1_CODE>0007</V_D_CUST_CHANNEL1_CODE>
                  <V_D_CUST_CHANNEL2_CODE>24050</V_D_CUST_CHANNEL2_CODE>
                  <V_D_CUST_BRANCH_CODE>BWADI_RIICO</V_D_CUST_BRANCH_CODE>
                  <D_D_CUST_DATE_OF_BIRTH
                    >1985-08-15 00:00:00</D_D_CUST_DATE_OF_BIRTH
                  >
                  <V_D_CUST_PROFESSION>SALASERV</V_D_CUST_PROFESSION>
                  <V_D_CUST_GENDER>M</V_D_CUST_GENDER>
                  <F_D_CUST_STAFF_IND>N</F_D_CUST_STAFF_IND>
                  <V_D_CUST_MARITAL_STATUS>MS1</V_D_CUST_MARITAL_STATUS>
                  <N_D_CUST_DEPENDENTS>1</N_D_CUST_DEPENDENTS>
                  <V_D_CUST_EDUCATION>GRAD</V_D_CUST_EDUCATION>
                  <N_D_CUST_MONTHLY_INCOME>0</N_D_CUST_MONTHLY_INCOME>
                  <N_D_CUST_ANNUAL_INCOME>0</N_D_CUST_ANNUAL_INCOME>
                  <V_D_CUST_EMP_COMPANY
                    >JAQUAR AND COMPANY PVT LTD</V_D_CUST_EMP_COMPANY
                  >
                  <V_D_CUST_ADD1>JAQUAR AND COMPANY LTD</V_D_CUST_ADD1>
                  <V_D_CUST_ADD2>SP-53</V_D_CUST_ADD2>
                  <V_D_CUST_ADD3>RIICO IND AREA BHIWADI</V_D_CUST_ADD3>
                  <V_D_CUST_ZIP_CODE>301019</V_D_CUST_ZIP_CODE>
                  <V_D_CUST_JOB_TITLE> </V_D_CUST_JOB_TITLE>
                  <V_D_CUST_OFF_ADR1>SP 53 RIICO IND AREA</V_D_CUST_OFF_ADR1>
                  <V_D_CUST_OFF_ADR2>BHIWADI</V_D_CUST_OFF_ADR2>
                  <V_D_CUST_OFF_ADR3> </V_D_CUST_OFF_ADR3>
                  <V_D_CUST_OFF_ZIP_CODE>301019</V_D_CUST_OFF_ZIP_CODE>
                  <V_D_CUST_TYPE_ORIGIN> </V_D_CUST_TYPE_ORIGIN>
                  <V_D_CUST_RESIDENCE_TYPE>NOT AVAI</V_D_CUST_RESIDENCE_TYPE>
                  <N_D_CUST_JOINING_AGE>31</N_D_CUST_JOINING_AGE>
                  <F_D_CUST_MISSING_IND> </F_D_CUST_MISSING_IND>
                  <D_D_CUST_REESTB_DATE> </D_D_CUST_REESTB_DATE>
                  <V_D_CUST_TITLE>MR</V_D_CUST_TITLE>
                  <V_D_CUST_ADD4> </V_D_CUST_ADD4>
                  <V_D_CUST_CITY>BHIWADI</V_D_CUST_CITY>
                  <V_D_CUST_STATE>RAJASTHAN</V_D_CUST_STATE>
                  <V_D_CUST_COUNTRY> </V_D_CUST_COUNTRY>
                  <V_D_CUST_EMAIL_ADD> </V_D_CUST_EMAIL_ADD>
                  <V_D_CUST_MOBILE_PHONE>8440006083</V_D_CUST_MOBILE_PHONE>
                  <V_D_CUST_IT_NBR>BVVPM4039E</V_D_CUST_IT_NBR>
                  <V_D_CUST_NET_ANNUAL_INCOME>0</V_D_CUST_NET_ANNUAL_INCOME>
                  <V_D_CUST_FULL_NAME>SANTOSH KUMAR MAHTO</V_D_CUST_FULL_NAME>
                  <V_D_CUST_SPOUSE_NAME> </V_D_CUST_SPOUSE_NAME>
                  <V_D_CUST_NAME_SHORT>NULL</V_D_CUST_NAME_SHORT>
                  <V_D_CUST_SPOUSE_OCCU>NULL</V_D_CUST_SPOUSE_OCCU>
                  <V_D_CUST_RESI_PHONE> </V_D_CUST_RESI_PHONE>
                  <V_D_CUST_OFF_PHONE>8440006083</V_D_CUST_OFF_PHONE>
                  <V_D_CUST_NATL_ID>NULL</V_D_CUST_NATL_ID>
                  <V_D_CUST_OFF_EMAIL_ADD> </V_D_CUST_OFF_EMAIL_ADD>
                  <UPDATE_DT> </UPDATE_DT>
                  <STANDARDIZED_CITY> </STANDARDIZED_CITY>
                  <V_D_CUST_MTHR_MADN_NAME> </V_D_CUST_MTHR_MADN_NAME>
                  <V_D_SECOND_HOLDER> </V_D_SECOND_HOLDER>
                  <V_D_THIRD_HOLDER> </V_D_THIRD_HOLDER>
                  <V_D_CUST_IT_PAN2> </V_D_CUST_IT_PAN2>
                  <V_D_CUST_IT_PAN3> </V_D_CUST_IT_PAN3>
                  <V_D_CUST_TYPE> </V_D_CUST_TYPE>
                  <REL_TYPE> </REL_TYPE>
                  <DEBIT_SCORE_PL> </DEBIT_SCORE_PL>
                  <DEBIT_SCORE_BL> </DEBIT_SCORE_BL>
                  <DEBIT_SCORE_AL> </DEBIT_SCORE_AL>
                  <DEBIT_SCORE_CARDS> </DEBIT_SCORE_CARDS>
                  <CNC_BEHAV_SCORE> </CNC_BEHAV_SCORE>
                  <CARD_BEHAV_SCORE> </CARD_BEHAV_SCORE>
                  <BEHAV_SCORE1> </BEHAV_SCORE1>
                  <BEHAV_SCORE2> </BEHAV_SCORE2>
                  <TOTAL_UNSECURE_PA_AMT> </TOTAL_UNSECURE_PA_AMT>
                  <TOTAL_PA_AMT> </TOTAL_PA_AMT>
                  <BEHAVIORAL_SCORE3> </BEHAVIORAL_SCORE3>
                  <BEHAVIORAL_SCORE4> </BEHAVIORAL_SCORE4>
                  <BEHAVIORAL_SCORE5> </BEHAVIORAL_SCORE5>
                  <BEHAVIORAL_SCORE6> </BEHAVIORAL_SCORE6>
                  <BEHAVIORAL_SCORE7> </BEHAVIORAL_SCORE7>
                  <ETHNIC_CODE> </ETHNIC_CODE>
                  <PRODUCT_CODE> </PRODUCT_CODE>
                  <PRODUCT_DESCRIPTION> </PRODUCT_DESCRIPTION>
                  <PRODUCT_TYPE> </PRODUCT_TYPE>
                  <AadharNo> </AadharNo>
                </ACCOUNT_INFO>
                <ACCOUNT_INFO>
                  <CUSTOMER_ID>97762471</CUSTOMER_ID>
                  <ACCOUNTID> </ACCOUNTID>
                  <SOURCE_ID>FINNESS</SOURCE_ID>
                  <SAS_ID>34241147</SAS_ID>
                  <FW_CUST_ID>34241147</FW_CUST_ID>
                  <FW_ACCNT_NUM>01681050195505</FW_ACCNT_NUM>
                  <V_D_CUST_FIRST_NAME>SANTOSH</V_D_CUST_FIRST_NAME>
                  <V_D_CUST_MIDDLE_NAME>KUMAR</V_D_CUST_MIDDLE_NAME>
                  <V_D_CUST_LAST_NAME>MAHTO</V_D_CUST_LAST_NAME>
                  <D_D_CUST_START_DATE>2020-02-28 00:00:00</D_D_CUST_START_DATE>
                  <D_D_CUST_CLOSED_DATE> </D_D_CUST_CLOSED_DATE>
                  <V_D_CUST_CHANNEL1_CODE>9099</V_D_CUST_CHANNEL1_CODE>
                  <V_D_CUST_CHANNEL2_CODE>54395</V_D_CUST_CHANNEL2_CODE>
                  <V_D_CUST_BRANCH_CODE> </V_D_CUST_BRANCH_CODE>
                  <D_D_CUST_DATE_OF_BIRTH
                    >1984-07-01 00:00:00</D_D_CUST_DATE_OF_BIRTH
                  >
                  <V_D_CUST_PROFESSION>SALAMANU</V_D_CUST_PROFESSION>
                  <V_D_CUST_GENDER>M</V_D_CUST_GENDER>
                  <F_D_CUST_STAFF_IND>N</F_D_CUST_STAFF_IND>
                  <V_D_CUST_MARITAL_STATUS>MS1</V_D_CUST_MARITAL_STATUS>
                  <N_D_CUST_DEPENDENTS>1</N_D_CUST_DEPENDENTS>
                  <V_D_CUST_EDUCATION>GRAD</V_D_CUST_EDUCATION>
                  <N_D_CUST_MONTHLY_INCOME>0</N_D_CUST_MONTHLY_INCOME>
                  <N_D_CUST_ANNUAL_INCOME>0</N_D_CUST_ANNUAL_INCOME>
                  <V_D_CUST_EMP_COMPANY
                    >JAQUAR AND COMPANY PVT LTD</V_D_CUST_EMP_COMPANY
                  >
                  <V_D_CUST_ADD1>S/O SANTOSH KUMAR S/O TUNTUN M</V_D_CUST_ADD1>
                  <V_D_CUST_ADD2
                    >C/O RISHAL COLONY VILL SANTHALKA POST</V_D_CUST_ADD2
                  >
                  <V_D_CUST_ADD3>BHIWADI ALWAR RAJASTHAN 301019</V_D_CUST_ADD3>
                  <V_D_CUST_ZIP_CODE>301019</V_D_CUST_ZIP_CODE>
                  <V_D_CUST_JOB_TITLE> </V_D_CUST_JOB_TITLE>
                  <V_D_CUST_OFF_ADR1
                    >SP 53 RICO INDL AREA BHIWADI</V_D_CUST_OFF_ADR1
                  >
                  <V_D_CUST_OFF_ADR2> </V_D_CUST_OFF_ADR2>
                  <V_D_CUST_OFF_ADR3> </V_D_CUST_OFF_ADR3>
                  <V_D_CUST_OFF_ZIP_CODE>301019</V_D_CUST_OFF_ZIP_CODE>
                  <V_D_CUST_TYPE_ORIGIN> </V_D_CUST_TYPE_ORIGIN>
                  <V_D_CUST_RESIDENCE_TYPE>NOT AVAI</V_D_CUST_RESIDENCE_TYPE>
                  <N_D_CUST_JOINING_AGE>35</N_D_CUST_JOINING_AGE>
                  <F_D_CUST_MISSING_IND> </F_D_CUST_MISSING_IND>
                  <D_D_CUST_REESTB_DATE> </D_D_CUST_REESTB_DATE>
                  <V_D_CUST_TITLE>MR.</V_D_CUST_TITLE>
                  <V_D_CUST_ADD4> </V_D_CUST_ADD4>
                  <V_D_CUST_CITY>BHIWADI</V_D_CUST_CITY>
                  <V_D_CUST_STATE>RAJASTHAN</V_D_CUST_STATE>
                  <V_D_CUST_COUNTRY> </V_D_CUST_COUNTRY>
                  <V_D_CUST_EMAIL_ADD
                    >SSANTOSHKUMA4@GMAIL.COM</V_D_CUST_EMAIL_ADD
                  >
                  <V_D_CUST_MOBILE_PHONE>8440006083</V_D_CUST_MOBILE_PHONE>
                  <V_D_CUST_IT_NBR>BVVPM4039E</V_D_CUST_IT_NBR>
                  <V_D_CUST_NET_ANNUAL_INCOME>0</V_D_CUST_NET_ANNUAL_INCOME>
                  <V_D_CUST_FULL_NAME>SANTOSH KUMAR MAHTO</V_D_CUST_FULL_NAME>
                  <V_D_CUST_SPOUSE_NAME> </V_D_CUST_SPOUSE_NAME>
                  <V_D_CUST_NAME_SHORT>NULL</V_D_CUST_NAME_SHORT>
                  <V_D_CUST_SPOUSE_OCCU>NULL</V_D_CUST_SPOUSE_OCCU>
                  <V_D_CUST_RESI_PHONE> </V_D_CUST_RESI_PHONE>
                  <V_D_CUST_OFF_PHONE>246808</V_D_CUST_OFF_PHONE>
                  <V_D_CUST_NATL_ID>NULL</V_D_CUST_NATL_ID>
                  <V_D_CUST_OFF_EMAIL_ADD> </V_D_CUST_OFF_EMAIL_ADD>
                  <UPDATE_DT> </UPDATE_DT>
                  <STANDARDIZED_CITY> </STANDARDIZED_CITY>
                  <V_D_CUST_MTHR_MADN_NAME> </V_D_CUST_MTHR_MADN_NAME>
                  <V_D_SECOND_HOLDER> </V_D_SECOND_HOLDER>
                  <V_D_THIRD_HOLDER> </V_D_THIRD_HOLDER>
                  <V_D_CUST_IT_PAN2> </V_D_CUST_IT_PAN2>
                  <V_D_CUST_IT_PAN3> </V_D_CUST_IT_PAN3>
                  <V_D_CUST_TYPE> </V_D_CUST_TYPE>
                  <REL_TYPE> </REL_TYPE>
                  <DEBIT_SCORE_PL> </DEBIT_SCORE_PL>
                  <DEBIT_SCORE_BL> </DEBIT_SCORE_BL>
                  <DEBIT_SCORE_AL> </DEBIT_SCORE_AL>
                  <DEBIT_SCORE_CARDS> </DEBIT_SCORE_CARDS>
                  <CNC_BEHAV_SCORE> </CNC_BEHAV_SCORE>
                  <CARD_BEHAV_SCORE> </CARD_BEHAV_SCORE>
                  <BEHAV_SCORE1> </BEHAV_SCORE1>
                  <BEHAV_SCORE2> </BEHAV_SCORE2>
                  <TOTAL_UNSECURE_PA_AMT> </TOTAL_UNSECURE_PA_AMT>
                  <TOTAL_PA_AMT> </TOTAL_PA_AMT>
                  <BEHAVIORAL_SCORE3> </BEHAVIORAL_SCORE3>
                  <BEHAVIORAL_SCORE4> </BEHAVIORAL_SCORE4>
                  <BEHAVIORAL_SCORE5> </BEHAVIORAL_SCORE5>
                  <BEHAVIORAL_SCORE6> </BEHAVIORAL_SCORE6>
                  <BEHAVIORAL_SCORE7> </BEHAVIORAL_SCORE7>
                  <ETHNIC_CODE> </ETHNIC_CODE>
                  <PRODUCT_CODE> </PRODUCT_CODE>
                  <PRODUCT_DESCRIPTION> </PRODUCT_DESCRIPTION>
                  <PRODUCT_TYPE> </PRODUCT_TYPE>
                  <AadharNo> </AadharNo>
                </ACCOUNT_INFO>
              </ALL_ACCOUNT>
              <ERR_CODE>0</ERR_CODE>
              <ERR_MESSAGE>SUCCESS</ERR_MESSAGE>
              <soaFillers> </soaFillers>
            </SAS_DIM_DEDUPE_OUTPUT>
          </a:ServiceResponse>
        </soapenv:Body>
      </soapenv:Envelope>
    </pre>'''

    return HttpResponse(apiexp)

class ViewCase(View):
    def get(self, request):
        with open(r'D:\Projects\1930Hachathon\Helpline1930\output.json', 'r') as f:
            data = json.load(f)
        
        context = {
            'userinfo': {'name': 'Priyanshu', 'ackno': 'CYBER01'},
            'caseinfo': {'sub': 'Priyanshu', 'brief': 'CYBER01', 'time': 'today()'},
            'susinfo': {'name': 'Priyanshu', 'rel': 'CYBER01', 'con': 'today()'},
            'crimeinfo': {'name': 'Priyanshu', 'body': 'data', 'mode': 'CYBER01', 'cat': 'online', 'time': 'today()'}
        }
        return render(request, 'auth/viewcase.html', {'data': data})


def export_to_pdf(request):
    # Define your email body content here. You can also fetch it from a database.
    with open(r'D:\Projects\1930Hachathon\Helpline1930\output.json', 'r') as f:
            data = json.load(f)
        
    email_body = '''
         
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

            '''.format(ack=Ackno(), breif=data['OBJ']['brief2'], date=data['OBJ']['Date'], mode=data['OBJ']['SubCat'], sus=data['OBJ']['SuspectedPerson'])

    # Render the email body content in an HTML template
    html_string = render_to_string('auth/email_template.html', {'email_body': email_body})

    # Create an HttpResponse object with PDF mime type
    response = HttpResponse(content_type='application/pdf')

    # If download
    response['Content-Disposition'] = 'attachment; filename=email.pdf'

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(html_string, dest=response)

    # If error, show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html_string + '</pre>')
    return response


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out !!')
        return render(request, 'auth/login.html')

    def get(self, request):
        return render(request, 'auth/login.html')


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        context = {
            'filed_values': request.POST
        }

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Welcome ' + user.username + ' You are now logged in !!')
                return redirect('index')

            messages.error(request, 'Invalid Credentials !!')
            return render(request, 'auth/login.html', context)
        messages.error(request, 'Please Fill All Fields !!')
        return render(request, 'auth/login.html', context)

    def get(self, request):
        return render(request, 'auth/login.html')


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username Should Be Alphanumeric Only !!!'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already exist, Choose another'}, status=409)
        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        print(data)
        if not validate_email(email):
            return JsonResponse({'email_error': 'Invalid Email !! Try Another '}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email Already Exist !! Choose Another One'}, status=409)
        return JsonResponse({'email_valid': True})


class RegisterView(View):
    def post(self, request):
        with open(r'D:\Projects\1930Hachathon\Helpline1930\output.json', 'r') as f:
            data = json.load(f)
        username = data['OBJ']['LoginId']
        password = data['OBJ']['Password']
        email = data['OBJ']['EmailId']
        print(password)
        context = {
            'filed_values': request.POST
        }
        emailbody = '''
         
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

            '''.format(ack=Ackno(), breif=data['OBJ']['brief2'], date=data['OBJ']['Date'], mode=data['OBJ']['SubCat'], sus=data['OBJ']['SuspectedPerson'])
                            

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password Too Short !!')
                    return render(request, 'auth/register.html', context)
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)

                email = EmailMessage(
                    "Cybercrime Report - Case Registered with Authorities Successfully !!",
                    emailbody,
                    "ppjj4047@gmail.com",
                    [email],
                )
                user.save()
                email.send(fail_silently=False)
                messages.success(request, 'Account Created Successfully !!')
                return render(request, 'auth/register.html')

            else:
                messages.error(request, 'Email Already Exist !!')
                return render(request, 'auth/register.html')

        return render(request, 'auth/register.html',{'data': data})

    def get(self, request):
        with open(r'D:\Projects\1930Hachathon\Helpline1930\output.json', 'r') as f:
            data = json.load(f)
        print(data)
        # url = 'http://127.0.0.1:8000/auth/register/'  # Replace with the actual URL of your form

        # # Fetch the form page to get the CSRF token
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')

        # # Prepare form data with CSRF token
        # form_data = {
        #     'csrfmiddlewaretoken': csrf_token,
        #     'data': data
        # }

        # # Submit the form
        # response = requests.post(url, data=form_data)

        # print(response.text)   
        return render(request, 'auth/register.html', {'data': data})
