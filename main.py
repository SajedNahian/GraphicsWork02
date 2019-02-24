from display import *
from draw import *
from matrix import *
from random import randint

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(10, 10)

edges = new_matrix(4, 2)
for row in range(get_row_count(edges)):
	for col in range(get_col_count(edges)):
		set_value(edges, row, col, randint(0, 9))
print('---------Testing Add Edges---------')
print('Before add_edge((1, 2, 3), (4, 5, 6))')
print_matrix(edges)
add_edge(edges, 1, 2, 3, 4, 5, 6);
print('After add_edge((1, 2, 3), (4, 5, 6))')
print_matrix(edges)
print('---------Testing Matrix Multiplication---------')
print('Matrix1:')
print_matrix(edges)
m2 = new_matrix(4, 3)
for row in range(get_row_count(m2)):
	for col in range(get_col_count(m2)):
		set_value(m2, row, col, randint(0, 9))
print('Matrix2')
print_matrix(m2)
print('Matrix1 * Matrix2')
matrix_mult(edges, m2)
print_matrix(m2)

# Actual image
edges = new_matrix(4, 0)
print_matrix(edges)

add_edge(edges, 50 + randint(0, 9), 450 + randint(0, 9), 0, 100 + randint(0, 9), 450 + randint(0, 9), 0);
add_edge(edges, 50 + randint(0, 9), 450 + randint(0, 9), 0, 50 + randint(0, 9), 400 + randint(0, 9), 0);
add_edge(edges, 100 + randint(0, 9), 450 + randint(0, 9), 0, 100 + randint(0, 9), 400 + randint(0, 9), 0);
add_edge(edges, 100 + randint(0, 9), 400 + randint(0, 9), 0, 50 + randint(0, 9), 400 + randint(0, 9), 0);

add_edge(edges, 200 + randint(0,9), 450 + randint(0,9), 0, 250 + randint(0,9), 450 + randint(0,9), 0);
add_edge(edges, 200 + randint(0,9), 450 + randint(0,9), 0, 200 + randint(0,9), 400 + randint(0,9), 0);
add_edge(edges, 250 + randint(0,9), 450 + randint(0,9), 0, 250 + randint(0,9), 400 + randint(0,9), 0);
add_edge(edges, 250 + randint(0,9), 400 + randint(0,9), 0, 200 + randint(0,9), 400 + randint(0,9), 0);

add_edge(edges, 150 + randint(0,9), 400 + randint(0,9), 0, 130 + randint(0,9), 360 + randint(0,9), 0);
add_edge(edges, 150 + randint(0,9), 400 + randint(0,9), 0, 170 + randint(0,9), 360 + randint(0,9), 0);
add_edge(edges, 130 + randint(0,9), 360 + randint(0,9), 0, 170 + randint(0,9), 360 + randint(0,9), 0);

add_edge(edges, 100 + randint(0,9), 340 + randint(0,9), 0, 200 + randint(0,9), 340 + randint(0,9), 0);
add_edge(edges, 100 + randint(0,9), 320 + randint(0,9), 0, 200 + randint(0,9), 320 + randint(0,9), 0);
add_edge(edges, 100 + randint(0,9), 340 + randint(0,9), 0, 100 + randint(0,9), 320 + randint(0,9), 0);
add_edge(edges, 200 + randint(0,9), 340 + randint(0,9), 0, 200 + randint(0,9), 320 + randint(0,9), 0);

draw_lines( edges, screen, color )
display(screen)
