import codecs

subjects_dict = {}
with codecs.open("Lessons.txt", "r", "utf-8") as f:
    lines = f.readlines()
    for line in lines:
        subject, *lessons = line.split(":")
        total_lessons = sum(int(lesson.split("(")[0]) for lesson in lessons)
        subjects_dict[subject] = total_lessons

print(subjects_dict)
