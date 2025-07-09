# Snake Game (Pygame)

Este es un juego clásico de la serpiente (Snake) implementado en Python usando la librería Pygame. El código está modularizado y organizado en carpetas para facilitar su mantenimiento y extensión.

## Características
- Control con flechas o teclas WASD
- Ventana y tablero configurables
- Colores y texturas personalizables
- Efecto de parpadeo al perder
- Código comentado y fácil de entender

## Estructura del proyecto

```
python_snake/
│   ejecutar_snake.bat         # Script para ejecutar el juego en Windows
│   main.py                    # Punto de entrada principal
│   requirements.txt           # Dependencias del proyecto
│
└───src/
    ├───core/
    │       logic.py           # Lógica del juego (SnakeGame)
    └───ui/
            draw.py            # Funciones de dibujo y UI
    └───assets/                # Imágenes y recursos (opcional)
```

## Requisitos
- Python 3.8+
- pygame

Instala las dependencias con:

```
pip install -r requirements.txt
```

## Cómo jugar

Ejecuta el juego con:

```
python main.py
```

- Usa las flechas o WASD para mover la serpiente.
- Come la manzana roja para crecer.
- No choques contra ti mismo ni contra los bordes.
- Cuando pierdas, pulsa **C** para continuar o **Q** para salir.

## Personalización
Puedes cambiar el tamaño de la ventana, los colores y la velocidad modificando las variables al inicio de `main.py`.

---

## Autor

DOS

¡Disfruta programando y jugando!
