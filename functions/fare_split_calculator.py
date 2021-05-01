def schedule_classes(classes, times):
    schedule = []

    index = 0
    while index < len(classes):
        schedule_classes = classes[index] + ": " + times[index]
        schedule.append(schedule_classes)
        index += 1

    return schedule

classes = ["Algebra", "History", "Biology", "Swimming"]
times = ["9a.m.", "11a.mm", "1p.m.", "3p.m"]
schedule = schedule_classes(classes, times)
print(f"Monday's schedule: {schedule}")