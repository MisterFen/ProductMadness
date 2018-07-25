from Object import Table

table_spacing_x = 200
table_spacing_y = 200

table1 = Table(50,0)
table2 = Table(table1.x+table1.width + table_spacing_x, 0)
table3 = Table(table2.x+table2.width + table_spacing_x, 0)
table4 = Table(table1.x, table1.y + table1.height + table_spacing_y)
table5 = Table(table2.x, table2.y + table1.height + table_spacing_y)
table6 = Table(table3.x, table3.y + table1.height + table_spacing_y)

objects = [table1, table2, table3, table4, table5, table6]



def draw_objects(display):
    for x in objects:
        x.draw(display)
