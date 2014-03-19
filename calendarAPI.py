from flask import Flask, jsonify, request
from datetime import date, time

app = Flask(__name__)

calendars = [
[
    {
	'Entry': 1,
        'Date': str(date(2014, 3, 18)),
	'Description': 'Paddys Wknd',
	'Start Time': str(time(9, 0)),
	'Finish Time': str(time(13, 30)),
	'Location URL': 'https://www.google.ie/maps/place/DIT-Kevin+Street/@53.3372301,-6.2684233,17z/data=!3m1!4b1!4m2!3m1!1s0x48670c2089d84a1d:0x6e1d03e3d62489ae'
    }
]
]
 
#cal_num is a parameter to specify which calendar to return
@app.route('/api/<int:cal_num>/getCalendar', methods=['GET'])
def get_calendar(cal_num):
    return jsonify({'calendar%d' % cal_num: calendars[cal_num - 1]})

@app.route('api/<int:cal_num>/getEntriesWithRange', method=['POST'])
def get_entries_with_range(cal_num)
    for entry['Date'] in calendars[cal_num - 1]:
    `

@app.route('/api/<int:cal_num>/createCalendarEntry', methods=['POST'])
def create_calendar_entry(cal_num):
    if not request.json or not 'Description' in request.json:
        abort(400)
    if len(calendars[cal_num - 1]) == 0:
        entry_num = 1
    else:
        entry_num = calendars[cal_num - 1][-1]['Entry'] + 1
    entry = {
	'Entry': entry_num,
	'Date': request.json['Date'],
	'Description': request.json['Description'],
	'Start Time': request.json.get('Start Time', ""),
	'Finish Time': request.json.get('Finish Time',"")
    }
    calendars[cal_num - 1].append(entry)
    return jsonify({'entry': entry}),201

@app.route('/api/<int:cal_num>/modifyCalendar/<int:entry_num>', methods=['PUT'])
def modify_calendar(cal_num, entry_num):
    """This method is for PUT """
    #Normal comment
    temp_entry = calendars[cal_num - 1][entry_num - 1]
    if request.json.get('Description') is not None:
        temp_entry['Description'] = request.json.get('Description')

    if request.json.get('Start Time') is not None:
        temp_entry['Start Time'] = request.json.get('Start Time')

    if request.json.get('Finish Time') is not None:
        temp_entry['Finish Time'] = request.json.get('Finish Time')
    
    # Don't need to put temp_entry back to the calander, because temp_entry points to the calendar[entry_num - 1],
    #calendars[entry_num - 1] = temp_entry
 
    return jsonify(temp_entry)

@app.route('/api/<int:cal_num>/deleteCalendarEntry/<int:entry_num>', methods=['DELETE'])
def delete_calendar_entry(cal_num, entry_num):
    """This method is for deleting entry """
    temp_entry = calendars[cal_num - 1][entry_num - 1]
    del calendars[cal_num - 1][entry_num - 1]
    
    return jsonify(temp_entry)   

@app.route('/api/createCalendar', methods=['POST'])
def create_calendar():
    new_calendar = []
    calendars.append(new_calendar)
    return "Your calendar number is %d\n" % len(calendars)

@app.route('/api/deleteCalendar/<int:cal_num>', methods=['DELETE'])
def delete_calendar(cal_num):
    del calendars[cal_num - 1]
    return "Deleted calendar number %d\n" % cal_num

if __name__ == '__main__':
    app.run(debug = True)

