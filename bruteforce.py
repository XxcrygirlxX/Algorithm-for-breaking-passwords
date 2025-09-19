import time
import turtle

pwd = "abc" 
alfabeto = ("abcdefghijklmnopqrstuvwxyz" + "ABCDEFFHIJKLMNOPQRSTUVWXYZ" +
            "0123456789" + "!?.,;:-—()[]{}'\"…+×÷=<>≠≈%°√∞$€£¥¢©®™@#&*§¶")
SAMPLE_EVERY = 1 
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
PADDING = 60

intentos = 0
datos = []
inicio_tiempo = time.time()

def gen_combinaciones_longitud(pwd, alfabeto, longitud, intento_pwd=""):
    global intentos, datos
    if len(intento_pwd) == longitud:
        intentos += 1
        tiempo_actual = time.time() - inicio_tiempo
        if intentos % SAMPLE_EVERY == 0:
            datos.append((intentos, tiempo_actual))
        if intento_pwd == pwd:
            print(f"contraseña '{intento_pwd}' encontrada :3")
            print(f"vas {intentos} intentos")
            return True
        else:
            return False
    for letra in alfabeto:
        encontrado = gen_combinaciones_longitud(pwd, alfabeto, longitud, intento_pwd + letra)
        if encontrado:
            return True
    return False

def buscar_contraseña(pwd, alfabeto):
    encontrado = gen_combinaciones_longitud(pwd, alfabeto, len(pwd))
    tiempo_total = time.time() - inicio_tiempo
    print(f"el tiempo en encontrar fue de {tiempo_total:.6f} segundos")
    return encontrado, tiempo_total

def draw_plot(datos, tiempo_total):
    if not datos:
        print("No hay datos para dibujar.")
        return

    screen = turtle.Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    screen.title("Intentos vs Tiempo (gráfico) - presiona click para cerrar")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    max_intentos = max(p for p, _ in datos)
    max_tiempo = max(t for _, t in datos + [(0, tiempo_total)])
    min_intentos = 0
    min_tiempo = 0

    plot_w = WINDOW_WIDTH - 2 * PADDING
    plot_h = WINDOW_HEIGHT - 2 * PADDING

    def to_screen_coords(intentos_val, tiempo_val):

        x = (-WINDOW_WIDTH/2 + PADDING +
             (intentos_val - min_intentos) / max(1, (max_intentos - min_intentos)) * plot_w)
        y = (-WINDOW_HEIGHT/2 + PADDING +
             (tiempo_val - min_tiempo) / max(1e-9, (max_tiempo - min_tiempo)) * plot_h)
        return x, y

    t.penup()

    x0, y0 = to_screen_coords(min_intentos, min_tiempo)
    x1, y1 = to_screen_coords(max_intentos, min_tiempo)
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)

    t.penup(); t.goto(x1, y1); t.pendown()
    t.setheading(0)
    t.right(30); t.forward(10); t.penup(); t.backward(10); t.left(60); t.pendown(); t.forward(10)
    t.penup(); t.home(); t.setheading(0)

    x0, y0 = to_screen_coords(min_intentos, min_tiempo)
    x1, y1 = to_screen_coords(min_intentos, max_tiempo)
    t.penup(); t.goto(x0, y0); t.pendown(); t.goto(x1, y1)

    t.penup(); t.goto(x1, y1); t.pendown()
    t.left(150); t.forward(10); t.penup(); t.backward(10); t.right(300); t.pendown(); t.forward(10)
    t.penup(); t.home(); t.setheading(0)

    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(0, WINDOW_HEIGHT/2 - PADDING/2)
    label.write(f"Intentos vs Tiempo (s) — Contraseña: '{pwd}' — Intentos: {max_intentos} — Tiempo: {tiempo_total:.4f}s",
                align="center", font=("Arial", 12, "normal"))

    marks = 8
    mark_turtle = turtle.Turtle()
    mark_turtle.hideturtle()
    mark_turtle.penup()
    for i in range(marks + 1):

        val = min_intentos + i * (max_intentos - min_intentos) / max(1, marks)
        x, y = to_screen_coords(val, min_tiempo)
        mark_turtle.goto(x, y - 8)
        mark_turtle.write(f"{int(val)}", align="center", font=("Arial", 9, "normal"))
        # eje Y marcas
        valy = min_tiempo + i * (max_tiempo - min_tiempo) / max(1, marks)
        x, y = to_screen_coords(min_intentos, valy)
        mark_turtle.goto(x - 40, y - 4)
        mark_turtle.write(f"{valy:.3f}", align="right", font=("Arial", 9, "normal"))

    plotter = turtle.Turtle()
    plotter.hideturtle()
    plotter.pensize(2)
    plotter.penup()

    first = True
    for intento_num, tiempo in datos:
        x, y = to_screen_coords(intento_num, tiempo)
        if first:
            plotter.goto(x, y)
            plotter.pendown()
            first = False
        else:
            plotter.goto(x, y)

    dotter = turtle.Turtle()
    dotter.hideturtle()
    dotter.penup()
    for intento_num, tiempo in datos:
        x, y = to_screen_coords(intento_num, tiempo)
        dotter.goto(x, y)
        dotter.dot(4) 

    ultimo_intento, ultimo_tiempo = datos[-1]
    x_last, y_last = to_screen_coords(ultimo_intento, ultimo_tiempo)

    tip = turtle.Turtle()
    tip.hideturtle()
    tip.penup()
    tip.goto(x_last, y_last)
    tip.dot(14, "red") 

    et.hideturtle()
    et.penup()
    etiqueta_x = x_last + 12
    etiqueta_y = y_last + 8
    et.goto(etiqueta_x, etiqueta_y)
    et.write(f"Intentos: {ultimo_intento}", align="left", font=("Arial", 11, "bold"))

    et2 = turtle.Turtle()
    et2.hideturtle()
    et2.penup()
    et2.goto(x_last + 12, y_last - 10)
    et2.write(f"{ultimo_tiempo:.3f}s", align="left", font=("Arial", 9, "normal"))

    footer = turtle.Turtle()
    footer.hideturtle()
    footer.penup()
    footer.goto(0, -WINDOW_HEIGHT/2 + PADDING/4)
    footer.write("Haz clic en la ventana para cerrarla.", align="center", font=("Arial", 10, "italic"))

    screen.exitonclick()

if __name__ == "__main__":
    encontrado, tiempo_total = buscar_contraseña(pwd, alfabeto)
    if datos and datos[-1][0] != intentos:
        datos.append((intentos, time.time() - inicio_tiempo))
    draw_plot(datos, time.time() - inicio_tiempo)
    if not encontrado:
        print("no se encontró la contraseña :c")
