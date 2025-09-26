import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5
    step = 20

    if state == "down":
        t.setheading(270)  # Движение вниз
        t.forward(step * turn)  # Действие t.forward

        if turn <= num_turns:
            state = "left"
            return state, turn
        if turn > num_turns:
            state = "done"
            return state, turn
        return state, turn
    if state == "left":
        t.setheading(180)  # Движение влево
        t.forward(step * turn)  # Действие t.forward
        turn += 1  # turn += 1

        if turn <= num_turns:
            state = "up"
            return state, turn
        return state, turn
    if state == "up":
        t.setheading(90)  # движение вверх
        t.forward(step * turn)  # Действие t.forward

        if turn <= num_turns:
            state = "right"
            return state, turn
        return state, turn
    if state == "right":
        t.setheading(0)  # Движение вправо
        t.forward(step * turn)  # Действие t.forward
        turn += 1  # turn += 1

        if turn <= num_turns:
            state = "down"
            return state, turn
        return state, turn
    if state == "init":

        if turn <= num_turns:
            state = "down"
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "init"
    end_state = "done"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()