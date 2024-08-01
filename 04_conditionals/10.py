## 10 - Are we Moving?
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving) # True

# Parentheses are needed. Without parenthese the expression evaluates to:
# (breaking_force < acceleration and speed > 0) or acceleration > 0
