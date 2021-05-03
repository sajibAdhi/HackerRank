if __name__ == '__main__':
    n = int(input())
    if (n < 2 or n > 10): exit()
    
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total_mark = 0;
    num_of_subject = 0;
    
    for mark in student_marks[query_name]:
        total_mark = total_mark + mark
        num_of_subject = num_of_subject + 1
    
        float_formate =  "{:.2f}"
    print(float_formate.format(total_mark / num_of_subject))