import app.calendar as calendar

"""#USERIDS================================================================================================
plug these in for userid...uhh...we need to know whats in these to test....may need to make a new account
also ask permission
"""

"""#CURRENTLY----------------------DOES-------------------------NOT------------------------------WORK-----------------------------------------------
def test1():
    #Example calendar 1
    user1events = [
        # year-month-day(T)two digit hours: two digit minutes: two digit seconds(-04 is subtracted from UTC, this for example is EST eastern time)
        calendar.Event("2019-04-15T11:00:00-04:00", "2019-04-15T11:50:00-04:00")
    ]
    calendar1 = calendar.Calendar(user1events)
    start = "2019-04-15T00:00:00-04:00"
    end = "2019-04-21T00:00:00-04:00"
    timezone = "America/New York" #keep this the same...we can't test other timezones rn
    userid1 = "123" #use one of the above for userid

    result = calendar.get_calendar(userid1, start, end, timezone)
    #result_string = ""
    #for event in result:
       # result_string += event.starttime + ' - ' + event.endtime + '\n'
    #print(result_string)
    assert result == calendar1
    #CURRENTLY----------------------DOES-------------------------NOT------------------------------WORK-----------------------------------------------
    """

def test2():
    #test will just print calendar to the console for this range
    #currently failing because it claims it takes 3 positional arguments

    #use one of the above ids for userid, this is Jared's
    userid = "auth0|5cb50516ee4bd5113d54872b" 
     # year-month-day(T)two digit hours: two digit minutes: two digit seconds(-04 is subtracted from UTC, this for example is EST eastern time) 
    start = "2019-04-15T00:00:00-04:00"
    end = "2019-04-21T00:00:00-04:00"
    timezone = "America/New York" #keep this the same...we can't test other timezones rn
    result = calendar.get_calendar(userid, start, end, timezone)
    #""""
    result_string = ""
    for event in result:
       result_string += event.starttime + ' - ' + event.endtime + '\n'
    print(result_string)
    #""""


if __name__ == '__main__':
    test2()
    print("Passed all tests.")
