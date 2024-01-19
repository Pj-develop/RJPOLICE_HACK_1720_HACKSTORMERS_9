from django.shortcuts import render
from django.http import HttpResponse
from .models import AudioFile
import speech_recognition as sr
import json
from django.http import JsonResponse


# Create your views here.
from dash import Dash
import dash_html_components as html
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

import google.generativeai as genai
genai.configure(api_key="api key")
model = genai.GenerativeModel('gemini-pro')



def fact(user_input):
    
    data= user_input
    prompt='''Arrange the text in key: value pair like this 
    
  "OBJ": 
    "Login Id": "",
    "Suspected Person": "",
    "Name": "",
    "Mobile": "",
    "DOB": "",
    "Email Id": "",
    "Mobile No": "",
    "Transaction id": "",
    "Password": "",
    "Father/Mother/Spouse": "",
    "Present Address": 
      "Vill/Town/City": "",
      "Country": "",
      "State": "",
      "District": "",
      "Police Station": "",
      "Pincode": "find it"
        "Category of complaint": "",
    "Sub-Category of complaint": "",
    "Approximate date & time of Incident/receiving/viewing of content": "",
    "Is there any delay in reporting?": "",
    "Where did the incident occur?": "",
    "Please provide any additional information about the incident": ""
    for this dialogues {} and remove new line character?'''.format(data)
    #prompt2="".format(data)
    responseAI = model.generate_content(prompt)
    return responseAI.text


#bard

def text_to_json(text, delimiter=":"):
    json_data = {}

    # Split the text into lines and process each line
    for line in text.split('\n'):
        # Split each line into key and value based on the delimiter
        parts = line.split(delimiter, 1)
        
        # If both key and value are present, add them to the JSON data
        if len(parts) == 2:
            key, value = parts
            json_data[key.strip()] = value.strip()
        
        
    return json_data

def save_to_json_file(json_data, file_path):
    with open(file_path, 'w') as json_file:
        
        json.dump(json_data, json_file, indent=2)



def dash_plot(request):
    # Create a Dash app object
    app = Dash(__name__)

    # Define layout of the Dash app
    app.layout = html.Div(children=[
        html.H1(children='Dashboard'),
        # Add other components as needed
    ])

    # Run the Dash app
    return render(request, 'baseapp/index.html', {'baseapp': app})


def aichat(request):
    return render(request,'baseapp/aichat.html')

# speech_to_text/views.py
from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr

r = sr.Recognizer()

def addcase(request):
    if request.method == 'POST' and request.FILES['audio_file']:
        audio_file = request.FILES['audio_file']
        lang_code = request.POST.get('language', 'en-IN')

        with sr.AudioFile(audio_file) as source:
            audio_text = r.listen(source)
        
        try:
            text = r.recognize_google(audio_text, language=lang_code)
            text=fact(text)
            text=fact(text+"remove the all error JSON, make the code in JSON FILE")
            
            json_data = text_to_json(text)
            json_data=fact(str(json_data)+"remove the all Error from JSON FILE, make the code in JSON FILE")
            json_data = text_to_json(text)
            print(json_data)
            # Specify the desired output JSON file path
            output_json_path = "output.json"
            # Save JSON data to a file
            save_to_json_file(json_data, output_json_path)
            print("JSON file successfully created.")
            return JsonResponse({'text': text})
        except Exception as e:
            return JsonResponse({'error': f'Sorry, an error occurred: {e}'})
        
        

    return render(request, 'baseapp/addcase.html')





def home(request):
    return render(request,'index.html')
