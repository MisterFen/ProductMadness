from NPC import Dev

row_spacing = 265
column_spacing = 155

first_row_x = 25
second_row_x = 185

first_column_y = 10
second_column_y = 90

dev1 = Dev(first_row_x, first_column_y)
dev2 = Dev(first_row_x, second_column_y)
dev3 = Dev(second_row_x, first_column_y)
dev4 = Dev(second_row_x, second_column_y)

dev5 = Dev(first_row_x + row_spacing, first_column_y)
dev6 = Dev(first_row_x + row_spacing, second_column_y)
dev7 = Dev(second_row_x + row_spacing, first_column_y)
dev8 = Dev(second_row_x + row_spacing, second_column_y)

npcs = (dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8)


def on_tick():
    for x in npcs:
        x.on_tick()


def draw_npcs(display):
    for x in npcs:
        x.draw(display)