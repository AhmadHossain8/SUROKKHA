from msilib.schema import CheckBox
from urllib import response
from click import confirm
from django.http import HttpResponse
from django.shortcuts import render
from pandas import value_counts
import requests
import json
import datetime as DT
from Home_Page.models import Chart_Data

# Bangladesh Live Update
url = "https://worldometers.p.rapidapi.com/api/coronavirus/country/Bangladesh"
headers = {
    "X-RapidAPI-Host": "worldometers.p.rapidapi.com",
    "X-RapidAPI-Key": "43442304b8mshd3e52abe82d6647p13c505jsn0eac43c951b5"
}


def Home_page(request):

    cap = Chart_Data.objects.filter().count()
    obj = Chart_Data()
    if cap == 0:
        obj.Houndred_Days_Info()


    x = "Date"
    y = "Deaths"
    graph_data = [[x, y]]

    obj = Chart_Data.objects.all()
    for v in obj.iterator():
        m = v.date
        m = m.strftime('%Y/%m/%d')
        graph_data.append([m, v.deaths])

    x_json = json.dumps(x)
    y_json = json.dumps(y)
    graph_data_json = json.dumps(graph_data)

    temp = requests.request("GET", url, headers=headers).json()
    response = {'Active_Cases': [], 'Country': [], 'Critical': [], 'Deaths_Per_M': [], 'Population': [], 'Region': [
    ], 'Tests_Per_M': [], 'Total_Cases': [], 'Total_Cases_Per_M': [], 'Total_Deaths': [], 'Total_Recovered': [], 'Total_Tests': []}
    response['Active_Cases'] = temp['data']['Active Cases']
    response['Country'] = temp['data']['Country']
    response['Critical'] = temp['data']['Critical']
    response['Deaths_Per_M'] = temp['data']['Deaths/1M pop']
    response['Population'] = temp['data']['Population']
    response['Region'] = temp['data']['Region']
    response['Tests_Per_M'] = temp['data']['Tests/1M pop']
    response['Total_Cases'] = temp['data']['Total Cases']
    response['Total_Cases_Per_M'] = temp['data']['Total Cases/1M pop']
    response['Total_Deaths'] = temp['data']['Total Deaths']
    response['Total_Recovered'] = temp['data']['Total Recovered']
    response['Total_Tests'] = temp['data']['Total Tests']

    return render(request, 'Home_Page.html', {'values': graph_data_json, 'h_title': x_json, 'v_title': y_json, 'response': response})
