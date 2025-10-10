"""
Project Title : Daily Calorie Tracker CLI Tool
Author : Ruhan Dogra
Date : October 7,2025
Description : This tool  helps track the user's daily calorie intake 
"""
def welcome():
    print("=================================================")
    print("    👋Welcome To The Daily Calorie Tracker!")
    print("=================================================")
    print("Still counting your calories on a notebook??")
    print("FEAR NOT!! This simple yet effective CLI Tool")
    print("helps you manage and count your calories easily")
    print("Lets make every CALORIE COUNT!🔥")
    print("-"*30)

def collecting_meal_data():
    meal_names=[]
    calorie_amounts=[]
    num_meals= int(input(" How many meals would you like to enter? : "))
    daily_limit=float(input("What is your Daily Calorie Limit? : "))



    print("\n----- Starting Data Entry-----")
    for i in range(num_meals):
        print(f"\n[+]Meal #{i+1} of {num_meals}")
        name=input("Enter meal name : ")
        calories=float(input("Enter amount of calories : "))

        meal_names.append(name)
        calorie_amounts.append(calories)

        print("-----Data Entry Complete-----")
    return meal_names, calorie_amounts ,daily_limit, num_meals
    
def calorie_maths(calorie_amounts,num_meals):
    total_calories=sum(calorie_amounts)
    average_calories= total_calories / num_meals
    return total_calories, average_calories

def print_summary(meal_names,calorie_amounts,total_calories,average_calories):
    print("\n"+ "="*35)
    print("       DAILY CALORIE SUMMARY")
    print("="*35)

    
    print(f"{'Meal Name':<15}{'Calories':>10}")
    print("-"*25)

    for i in range(len(meal_names)):
        meal = meal_names[i]
        calories = calorie_amounts[i]
        print(f"{meal:<15}{calories:>10.0f}")

    print("-"*25)
    print(f"{'Total :':<15}{total_calories :>10.2f}")
    print(f"[{'Average :':<15}{average_calories :>10.2f}]")
    print("="*35)

def intake_analysis(total_calories,daily_limit):
    print("\n" + "="*40)
    print("          Calorie Intake Analysis")
    print("="*40)

    if total_calories > daily_limit:
        print("⚠️  Warning!")
        print(f" You have exceeded your daily calorie limit by: {total_calories-daily_limit:.2f} kcal")
        print("Consider Taking a break!")

    else:
        calories_left=daily_limit-total_calories
        if daily_limit== total_calories:
            print("✨  A True Perfectionist!🎯")
            print("You have completed your calorie intake goal for today!")
        elif calories_left > 200:
            print("You are lacking Behind!⚠️")
            print(f"Your calorie intake today was {calories_left} kcal less than your calorie limit.")
            print("Its time to lock in!")

        elif calories_left <= 200 :
            print("👏 Good Job")
            print(f"You almost maxed out your calorie intake today with {calories_left:.2f} calories left!")
            print("Discipline is the Key to Success and you my friend,are on the right path.")




def main():
    welcome()
    meal_names , calorie_amounts,daily_limit,num_meals = collecting_meal_data()
    total_calories, average_calories = calorie_maths(calorie_amounts,num_meals)
    print_summary(meal_names,calorie_amounts,total_calories,average_calories)
    intake_analysis(total_calories,daily_limit)

main()
