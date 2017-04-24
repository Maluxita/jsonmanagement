import datetime
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")


def date_handler(obj):
    # Function to manage date and datetime objects in json
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError