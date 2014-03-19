
#Function to get a calendar / dictonary entry
curl -i  http://127.0.0.1:5000/api/1/getCalendar
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 351
Server: Werkzeug/0.9.4 Python/2.7.4
Date: Wed, 19 Mar 2014 23:24:45 GMT

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
}
