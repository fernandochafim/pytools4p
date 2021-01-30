


class ListElementPositionError(Exception):
    """Exception raised for errors in list element.

    Attributes:
        result -- List with boolean values
    """
    def __init__(self, result):
        error_location = []
        for x in range(len(result)):
            if not result[x]:
                error_location.append(str(x+1))
        if len(error_location) == 1:
            message = 'The element number ' + ', '.join(error_location) + ' is not correct'
        else:
            message = 'The elements number ' + ', '.join(error_location) + ' are not correct'
        super().__init__(message)