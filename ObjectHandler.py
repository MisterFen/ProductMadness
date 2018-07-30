from Object import Table, Computer

table_spacing_x = 165
table_spacing_y = 200

table1 = Table(75,0)
table2 = Table(table1.x+table1.width + table_spacing_x, 0)
table3 = Table(table2.x+table2.width + table_spacing_x, 0)
table4 = Table(table1.x, table1.y + table1.height + table_spacing_y)
table5 = Table(table2.x, table2.y + table1.height + table_spacing_y)
table6 = Table(table3.x, table3.y + table1.height + table_spacing_y)

computer1 = Computer(table2.x + table2.width/2 + 20, table2.y + table2.height/2 + 20)

objects = [table1, table2, table3, table4, table5, table6]
interactable_objects = [computer1]


def draw_objects(display):
    for x in objects:
        x.draw(display)
    for x in interactable_objects:
        x.draw(display)
