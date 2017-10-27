def to24hourtime(hour, minute, period):
    if period == 'pm' and hour != 12:
        hour = 12 + hour
    
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    
    return str(hour) + str(minute)
