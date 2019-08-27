"""
Fixed program to determine score status, with function
"""

def main():
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    if score < 0:
        print("Invalid score")
    # or
    if score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    elif score < 50:
        print("Bad")


main()