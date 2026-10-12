"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    return record[1]
    


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    return (coordinate[0], coordinate[1])    
    

def compare_records(azara_record, rui_record):

    rui_coord = rui_record[1][0] + rui_record[1][1]

    return azara_record[1] == rui_coord


def create_record(azara_record, rui_record):

    rui_coord = rui_record[1][0] + rui_record[1][1]

    if azara_record[1] == rui_coord:
        return azara_record + rui_record
    else:
        return "not a match"
    


def clean_up(combined_record_group):
    report = ""
    for record in combined_record_group:
        cleaned_record = (record[0], record[2], record[3], record[4])
        report += f"{cleaned_record}\n"

    return report

    


