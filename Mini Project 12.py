month = 7
day = 17
year = 2022

daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

current_date = day
current_month = month - 1
current_year = year
start_day = 0

user_input = input("Enter the day you want (Sunday, Monday, ... Saturday): ")

if user_input in weekdays:
    target_day = weekdays.index(user_input)
    print("Here are the " + user_input + "s for the next year:")

    while start_day != target_day:
        current_date += 1
        start_day = (start_day + 1) % 7

        if current_date > daysinmonth[current_month]:
            current_date = 1
            current_month = (current_month + 1) % 12

    for _ in range(52):
        print("{:2}-{:2}-{}".format(current_date, current_month + 1, current_year), end=" ")

        current_date += 7
        while current_date > daysinmonth[current_month]:
            current_date -= daysinmonth[current_month]
            current_month = (current_month + 1) % 12
            if current_month == 0:
                current_year += 1

        if (_ + 1) % 3 == 0:
            print()

else:
    print("I'm sorry, What day of the week was that again? Never heard of that one!.")
