"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    
    
    rounded_list = []
    for score in student_scores:
        rounded_list.append(round(score))
    return rounded_list

    


def count_failed_students(student_scores):

    count = 0
    for i in student_scores:
        if i <= 40:
            count += 1
        else:
            count = count
    return count


def above_threshold(student_scores, threshold):
    
    new_list = []
    for score in student_scores:
        if score >= threshold:
            new_list.append(score)
    return new_list
    


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    lowest = 40
    step = (highest - 40) // 4
    thresholds = []

    for k in range(4):
        thresholds.append(41 + k * step)
    return thresholds
    
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    list = []
    for i, name in enumerate(student_names, start=1):
        item = f"{i}. {name}: {student_scores[i-1]}"
        list.append(item)
    return list

def perfect_score(student_info):
    

    list = []
    for score in student_info:
         if score[1] == 100:
             list.append(score)
             break
         else:
             continue
             
    if not list:
        return list
    else:
        return list[0]
             
         
        




         
         
