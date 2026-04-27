# Outer function
def classify_temperature(temp):

    # Inner function (validation)
    def validate_temperature(t):
        if not isinstance(t, (int, float)):
            return False
        if t < -100 or t > 100:   # realistic bounds
            return False
        return True

    # Use inner function
    if not validate_temperature(temp):
        return "Invalid temperature input"

    # Classification logic
    if temp < 10:
        return "Cold"
    elif 10 <= temp <= 25:
        return "Warm"
    else:
        return "Hot"


# Test
print(classify_temperature(5))     # Cold
print(classify_temperature(20))    # Warm
print(classify_temperature(35))    # Hot
print(classify_temperature(200))   # Invalid