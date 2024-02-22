#Whose that Tennis Player?

gender = input("Is the player male or female? (Male/Female) ")

grand_slam = input("Has the player won a Grand Slam tournament? (Yes/No) ")

top_10 = input("Is the player currently ranked in the top 10? (Yes/No) ")

if gender == 'Male' and grand_slam == 'Yes' and top_10 == 'Yes':
         print("You might be thinking of Novak Djokovic!")
elif gender == 'Female' and grand_slam == 'Yes' and top_10 == 'Yes':
         print("You might be thinking of Naomi Osaka!")
elif gender == 'Male' and grand_slam == 'Yes' and top_10 == 'No':
         print("You might be thinking of Juan Martin del Potro!")
elif gender == 'Female' and grand_slam == 'No' and top_10 == 'Yes':
         print("You might be thinking of Simona Halep!")
else:
    print("I have no idea what you're thinking, I'm just a simple program!")
Proe
