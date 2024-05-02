import re
from Movimiento import Movimiento

class Analizador:
    def __init__(self, codigo):
        self.contError = 0
        self.LisMovimiento = []
        self.codigo = codigo
        # Expresiones regulares para los tokens
        self.nombre_impresion = r'new_print\s+(\w+);'
        self.set_print = r'set_print_(x|o|triangulo|estrella)\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\w+)\s*\);'
        self.comentario = r'#.*'

        try:
            # Buscar tokens en el código
            self.impresion = re.findall(self.nombre_impresion, self.codigo)
            self.sets_print = re.findall(self.set_print, self.codigo)
            self.matches = re.findall(self.comentario, self.codigo)

            # Mostrar los resultados
            if self.impresion:
                print("Nombre de la impresión:", self.impresion[0])
            else:
                print("Error: No se encontró el nombre de la impresión")
                self.contError += 1

            if self.sets_print:
                for i, (set_print_type, fila, columna, color) in enumerate(self.sets_print, 1):
                    #print(f"Set de impresión {i}:")
                    newMovimiento = Movimiento(columna, fila, color, set_print_type)
                    self.LisMovimiento.append(newMovimiento)

                    # Verificar si alguno de los valores extraídos es None
                    if None in (set_print_type, fila, columna, color):
                        print("Error: El conjunto de impresión está incompleto")
                        self.contError += 1
            else:
                print("Error: No se encontraron sets de impresión")
                self.contError += 1
            
            '''
            if self.matches:
                print("Comentarios encontrados:")
                for match in self.matches:
                    print(match)
            '''        
        except Exception as e:
            print(f"Error al analizar el código: {str(e)}")
            self.contError += 1

    def obtener_contador_errores(self):
        return self.contError

    def obtener_movimientos(self):
        return self.LisMovimiento

