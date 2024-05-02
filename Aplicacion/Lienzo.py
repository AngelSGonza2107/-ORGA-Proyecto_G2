import math
from tkinter import *

class PixelArtEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Pixel Art Editor")

        self.canvas = Canvas(self.master, width=470, height=480, bg="white")
        self.canvas.place(x=750, y=200) 

        self.cell_size = 160
        self.cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(3):
            for j in range(3):
                x0 = i * self.cell_size  # Ajusta las coordenadas x
                y0 = j * self.cell_size  # Ajusta las coordenadas y
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="gray")

        self.canvas.bind("<B1-Motion>", self.draw_pixel)

        # Crear grupo de botones de colores
        self.create_color_button_group()

        # Crear grupo de botones de formas
        self.create_shape_button_group()

        # Botón para borrar solo las figuras
        clear_button = Button(self.master, text="Clear Table",width=22, height=2, command=self.clear_figures)
        clear_button.config(fg="Black", bg="#FC7643",
                     font=("Bahnschrift SemiBold", 12))
        clear_button.place(x=890, y=700)

    
        # Inicializar forma seleccionada
        self.selected_shape = "Tri"

    def create_color_button_group(self):
        # Definir los colores y sus nombres
        colors = [("Cyan", "#00BFFF"), ("Magenta", "#FF00FF"), ("Yellow", "yellow"), ("Black", "black")]

        # Crear marco para los botones de colores
        color_button_frame = Frame(self.master, bg="#96E8AE")
        color_button_frame.place(x=1050, y=90)

        # Crear botones para cada color
        for name, color in colors:
            if name == "Black":
                button = Button(color_button_frame, text=name, command=lambda c=color: self.set_selected_color(c), height=2, width=11)
                button.config(fg="White", bg="black",
                     font=("Bahnschrift SemiBold", 11))
            else:
                button = Button(color_button_frame, text=name, command=lambda c=color: self.set_selected_color(c), height=2, width=11)
                button.config(fg="Black", bg=color,
                     font=("Bahnschrift SemiBold", 11))
            button.pack(side=LEFT, padx=5, pady=5)

    def create_shape_button_group(self):
        # Crear marco para los botones de formas
        shape_button_frame = Frame(self.master, bg="#96E8AE")
        shape_button_frame.place(x=560, y=90)

        # Crear botones para cada forma
        shapes = [("Tri", "▲"), ("Star", "⭐"), ("Cross", "❌"), ("Circle", "⭕")]

        for shape, label in shapes:
            button = Button(shape_button_frame, text=label, command=lambda s=shape: self.set_selected_shape(s), height=2, width=12,font=("Segoe UI Emoji", 10))
            button.pack(side=LEFT, padx=5, pady=5)

    def set_selected_color(self, color):
        self.selected_color = color

    def set_selected_shape(self, shape):
        self.selected_shape = shape

    def draw_pixel(self, event):
        x = (event.x - 50) // self.cell_size  
        y = (event.y - 50) // self.cell_size  

        # Limitar a la matriz de 3x3
        if 0 <= x < 3 and 0 <= y < 3:
            if self.cells[y][x] == 0:  # Verificar si la celda está vacía
                self.cells[y][x] = 1
                if self.selected_shape == "Tri":
                    self.draw_triangle(x, y)
                elif self.selected_shape == "Star":
                    self.draw_star(x, y)
                elif self.selected_shape == "Cross":
                    self.draw_cross(x, y)
                elif self.selected_shape == "Circle":
                    self.draw_circle(x, y)

    def draw_triangle(self, x, y):
        # Dibujar un triángulo en el lienzo
        x0 = x * self.cell_size + self.cell_size // 2
        y0 = y * self.cell_size
        x1 = x0 - self.cell_size // 2
        y1 = y0 + self.cell_size
        x2 = x0 + self.cell_size // 2
        y2 = y0 + self.cell_size
        self.canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill=self.selected_color, tags=("figure",))

    def draw_star(self, x, y):
        # Dibujar una estrella en el lienzo
        x0 = x * self.cell_size + self.cell_size // 2
        y0 = y * self.cell_size + self.cell_size // 2
        r_outer = self.cell_size // 3
        r_inner = r_outer // 2

        points = []
        for i in range(10):
            angle_outer = math.pi + 2 * math.pi * i / 5
            angle_inner = angle_outer + math.pi / 5

            if i % 2 == 0:
                x_outer = x0 + r_outer * math.cos(angle_outer)
                y_outer = y0 + r_outer * math.sin(angle_outer)
                points.extend([x_outer, y_outer])
            else:
                x_inner = x0 + r_inner * math.cos(angle_inner)
                y_inner = y0 + r_inner * math.sin(angle_inner)
                points.extend([x_inner, y_inner])

        self.canvas.create_polygon(points, fill=self.selected_color, tags=("figure",))
        
    def draw_cross(self, x, y):
        # Dibujar una cruz (x) en el lienzo
        x0 = x * self.cell_size
        y0 = y * self.cell_size
        x1 = x0 + self.cell_size
        y1 = y0 + self.cell_size

        # Dibujar líneas más gruesas
        line_width = 6
        self.canvas.create_line(x0, y0, x1, y1, fill=self.selected_color, width=line_width, tags=("figure",))
        self.canvas.create_line(x1, y0, x0, y1, fill=self.selected_color, width=line_width, tags=("figure",))

    def draw_circle(self, x, y):
        # Dibujar un círculo en el lienzo
        x0 = x * self.cell_size + self.cell_size // 2
        y0 = y * self.cell_size + self.cell_size // 2
        r = self.cell_size // 3
        self.canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, fill=self.selected_color, tags=("figure",))

    def clear_figures(self):
        # Eliminar solo las figuras del lienzo
        figures = self.canvas.find_withtag("figure")
        for figure in figures:
            self.canvas.delete(figure)

        # Restablecer las celdas a vacías
        self.cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

