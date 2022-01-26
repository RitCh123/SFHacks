from flask import Flask, render_template, send_file, redirect, url_for, request, flash
import os

from bs4 import BeautifulSoup

import requests

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import re




app = Flask('app')

#secret key

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def homePage():
  return render_template("index.html")
  
@app.route('/favicon.ico')
def favicon():
  return send_file("static/assets/favicon/logo.png")
@app.route('/attendance')
def attendance_form():
  return redirect("https://tinyurl.com/sfhacksattendance")
@app.route('/admin/signin', methods = ['GET', 'POST'])
def admin_register():
  if request.method == 'POST':
    if request.form['username'] == os.environ['USERNAME'] and request.form['password'] == os.environ['PASSWORD']:
      return redirect(url_for('admin_page'))
    else:
      flash("Incorrect login credentails")
  return render_template("admin/form.html")

@app.route('/admin/home', methods = ['GET', "POST"])
def admin_page():
  #scrape calendar for admin dashboard
  url = 'https://www.sfhs.com/calendar'

  response = requests.get(url)
  html_soup = BeautifulSoup(response.text, 'html.parser')

  classes_event = html_soup.find_all('div', class_ = "fsCalendarDaybox")

  mon_calendar_date = []

  pass_list = []

  for event in classes_event:
    day = event.find('div', class_='fsCalendarDate')['data-day']
    year = event.find('div', class_='fsCalendarDate')['data-year']
    month = event.find('div', class_='fsCalendarDate')['data-month']

    if not event.find('a', class_='fsCalendarEventTitle'):
      continue
    else:
      event_holder = event.find_all('a', class_='fsCalendarEventTitle')
      event_holder = list(map(lambda x: x['title'], event_holder))

    day_of_date= event.find('span', class_='fsCalendarDay')

    if not("No Classes " in event_holder) and day_of_date.contents[0] == "Mon,":
      date = month + " " + day + " " + year + " " 
      mon_calendar_date.append(date)
    else:
      date = month + " " + day + " " + year
      mon_calendar_date.append(date)

  #filtering the data

  for mon in mon_calendar_date:
    split = mon.split(' ')
    if len(split) > 3:
      pass_list.append(str(int(split[0])+1)+"/"+split[1] + "/"+ split[2])
  #get attendance form information from google sheets api
  gc = gspread.service_account(filename='mycredentials.json')

  gsheet = gc.open("Programming Club Attendance Sheet (2021-2022)")

  mydata = gsheet.sheet1.get_all_records()

  labels = []
  attendance = []
  for data in mydata:
    m = re.search('/', data['Attendance Summary'])
    if m:
      labels.append(data['Attendance Summary'])
      attendance.append(data[''])

    return render_template("/admin/home.html", dates = pass_list, labels = labels, data = attendance)
  

app.run(host='0.0.0.0', port=8080, debug=True)



