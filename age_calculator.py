from datetime import date, datetime

print("📅 Age Calculator")

# Get birthdate from user
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()

    # Calculate age
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # Adjust if needed
    if days < 0:
        months -= 1
        days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

    if months < 0:
        years -= 1
        months += 12

    print(f"🎉 You are {years} years, {months} months, and {days} days old.")

except ValueError:
    print("⚠️ Invalid date format! Please use YYYY-MM-DD.")
