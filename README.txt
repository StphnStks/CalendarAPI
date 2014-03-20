#Student: Stephen Stokes D12124062
#API call Heroku URL: http://agile-forest-7589.herokuapp.com/api/1/getCalendar 

#Function to get a calendar / dictonary entry
curl -i http://agile-forest-7589.herokuapp.com/api/1/getCalendar
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 20 Mar 2014 01:31:23 GMT
Server: gunicorn/18.0
Content-Length: 351
Connection: keep-alive

{
  "calendar1": [
    {
      "Date": "2014-03-18",
      "Description": "Paddys Wknd",
      "Entry": 1,
      "Finish Time": "13:30:00",
      "Location URL": "https://www.google.ie/maps/place/DIT-Kevin+Street/@53.3372301,-6.2684233,17z/data=!3m1!4b1!4m2!3m1!1s0x48670c2089d84a1d:0x6e1d03e3d62489ae",
      "Start Time": "09:00:00"
    }
  ]


#Function to create an empty calendar
curl -i -H "Content-Type: application/json" -X POST -d '' http://agile-forest-7589.herokuapp.com/api/createCalendar
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Date: Wed, 19 Mar 2014 23:52:20 GMT
Server: gunicorn/18.0
Content-Length: 26
Connection: keep-alive

Your calendar number is 4


#Function to modify a calendar entry
curl -i -H "Content-Type: application/json" -X PUT -d '{"Description": "Friday"}' http://agile-forest-7589.herokuapp.com/api/1/modifyCalendar/0
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 20 Mar 2014 01:41:21 GMT
Server: gunicorn/18.0
Content-Length: 289
Connection: keep-alive

{
  "Date": "2014-03-18",
  "Description": "Friday",
  "Entry": 1,
  "Finish Time": "13:30:00",
  "Location URL": "https://www.google.ie/maps/place/DIT-Kevin+Street/@53.3372301,-6.2684233,17z/data=!3m1!4b1!4m2!3m1!1s0x48670c2089d84a1d:0x6e1d03e3d62489ae",
  "Start Time": "09:00:00"


#Function to delete a calendar / Dictonary entry
curl -i -H "Accept: application/JSON" -X DELETE  http://agile-forest-7589.herokuapp.com/api/1/deleteCalendarEntry/1
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 20 Mar 2014 01:51:48 GMT
Server: gunicorn/18.0
Content-Length: 289
Connection: keep-alive

{
  "Date": "2014-03-18",
  "Description": "Friday",
  "Entry": 1,
  "Finish Time": "13:30:00",
  "Location URL": "https://www.google.ie/maps/place/DIT-Kevin+Street/@53.3372301,-6.2684233,17z/data=!3m1!4b1!4m2!3m1!1s0x48670c2089d84a1d:0x6e1d03e3d62489ae",
  "Start Time": "09:00:00"


#Function to create an empty Calendar
curl -i -H "Content-Type: application/json" -X POST -d '' http://agile-forest-7589.herokuapp.com/api/createCalendar
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Date: Thu, 20 Mar 2014 02:04:00 GMT
Server: gunicorn/18.0
Content-Length: 26
Connection: keep-alive

Your calendar number is 4


#Function to delete a Calendar
curl -i -H "Accept: application/JSON" -X DELETE  http://agile-forest-7589.herokuapp.com/api/deleteCalendar/4
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Date: Thu, 20 Mar 2014 02:07:39 GMT
Server: gunicorn/18.0
Content-Length: 26
Connection: keep-alive

Deleted calendar number 4
