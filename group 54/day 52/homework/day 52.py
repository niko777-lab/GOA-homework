# Transportation on vacation
def rental_car_cost(n):
    daily_rate = 40
    if n >= 7:
        return n * daily_rate - 50
    elif n >= 3:
        return n * daily_rate - 20
    else:
        return n * daily_rate
# Quarter of the year
def quarter_of(month):
    return (month - 1) // 3 + 1
# Remove exclamation marks
def remove_exclamation_marks(s):
    return s.replace('!', '')
# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height
# Total amount of points
def points(games):
    total_points = 0
    for game in games:
        team_score, opponent_score = map(int, game.split(":"))
        if team_score > opponent_score:
            total_points += 3
        elif team_score == opponent_score:
            total_points += 1
    return total_points
# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
# Area or Perimeter
def area_or_perimeter(length, width):
    if length == width:
        return length * width  # Area of square
    else:
        return 2 * (length + width)  # Perimeter of rectangle
