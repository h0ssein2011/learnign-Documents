
def covert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None
