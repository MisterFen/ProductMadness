from NPC import Dev

row_spacing = 265
column_spacing = 355

first_row_x = 25
second_row_x = 185

first_column_y = 10
second_column_y = 90
npcs = []

def set_devs():
    global npcs
    npcs = []
    dev1 = Dev(first_row_x, first_column_y, "right")
    dev2 = Dev(first_row_x, second_column_y, "right")
    dev3 = Dev(second_row_x, first_column_y, "left")
    dev4 = Dev(second_row_x, second_column_y, "left")

    dev5 = Dev(first_row_x + row_spacing, first_column_y, "right")
    dev6 = Dev(first_row_x + row_spacing, second_column_y, "right")
    dev7 = Dev(second_row_x + row_spacing, first_column_y, "left")
    #dev8 = Dev(second_row_x + row_spacing, second_column_y)

    dev9 = Dev(first_row_x + row_spacing * 2, first_column_y, "right")
    dev10 = Dev(first_row_x + row_spacing * 2, second_column_y, "right")
    dev11 = Dev(second_row_x + row_spacing * 2, first_column_y, "left")
    dev12 = Dev(second_row_x + row_spacing * 2, second_column_y, "left")

    dev13 = Dev(first_row_x, first_column_y + column_spacing, "right")
    dev14 = Dev(first_row_x, second_column_y + column_spacing,"right")
    dev15 = Dev(second_row_x, first_column_y + column_spacing, "left")
    dev16 = Dev(second_row_x, second_column_y + column_spacing, "left")

    dev17 = Dev(first_row_x + row_spacing, first_column_y + column_spacing, "right")
    dev18 = Dev(first_row_x + row_spacing, second_column_y + column_spacing, "right")
    dev19 = Dev(second_row_x + row_spacing, first_column_y + column_spacing, "left")
    dev20 = Dev(second_row_x + row_spacing, second_column_y + column_spacing, "left")

    dev21 = Dev(first_row_x + row_spacing * 2, first_column_y + column_spacing, "right")
    dev22 = Dev(first_row_x + row_spacing * 2, second_column_y + column_spacing, "right")
    dev23 = Dev(second_row_x + row_spacing * 2, first_column_y + column_spacing, "left")
    dev24 = Dev(second_row_x + row_spacing * 2, second_column_y + column_spacing, "left")

    npcs = (dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev9, dev10, dev11, dev12, dev13, dev14, dev15, dev16, dev17, dev18, dev19, dev20, dev21, dev22, dev23, dev24)


def on_tick():
    for x in npcs:
        x.on_tick()


def draw_npcs(display):
    for x in npcs:
        x.draw(display)


def reset():
    for x in npcs:
        x.on_start()


def on_shout():
    for x in npcs:
        x.on_shout()


set_devs()
