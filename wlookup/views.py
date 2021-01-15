#This is my views.py file
from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST" :
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=5&API_KEY=C6D0CC62-BB4E-4D98-8139-904BD025D077")
        try:
            api = api_request.json()
        except Exception as e:
            api = "error......."

        if api[0]['Category']['Name'] == "Good":
            category_description = '(0-50)Air Quality is satisfactory, less or no risk.'
            category_color = 'good'
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = '(51-100)Air Quality is acceptable, moderate health concern.'
            category_color = 'moderate'

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = '(101-150)General public is not affected , people with lung disease have greater risk.'
            category_color = 'usg'
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = '(151-200)Everyone may begin to experience health effects, sennsitive people may be affected more.'
            category_color = 'unhealthy'

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = '(201-300)Health alert : everyone may experience more serious health effects.'
            category_color = 'veryunhealthy'

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = '(301-500)Health warnings of emergency conditions.The entire population affected.'
            category_color = 'hazardous'

            
        return render(request,'home.html', {'api': api, 'category_description' : category_description ,'category_color' : category_color})
        


    else:    
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C6D0CC62-BB4E-4D98-8139-904BD025D077")
        try:
            api = api_request.json()
        except Exception as e:
            api = "error......."

        if api[0]['Category']['Name'] == "Good":
            category_description = '(0-50)Air Quality is satisfactory, less or no risk.'
            category_color = 'good'
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = '(51-100)Air Quality is acceptable, moderate health concern.'
            category_color = 'moderate'

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = '(101-150)General public is not affected , people with lung disease have greater risk.'
            category_color = 'usg'
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = '(151-200)Everyone may begin to experience health effects, sennsitive people may be affected more.'
            category_color = 'unhealthy'

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = '(201-300)Health alert : everyone may experience more serious health effects.'
            category_color = 'veryunhealthy'

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = '(301-500)Health warnings of emergency conditions.The entire population affected.'
            category_color = 'hazardous'

            
        return render(request,'home.html', {'api': api, 'category_description' : category_description ,'category_color' : category_color})

def about(request):
    return render(request,'about.html', {})

