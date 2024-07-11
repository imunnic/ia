import numpy as np
import matplotlib.pyplot as plt

# Función para obtener los datos de entrada
def obtener_datos():
    v0 = float(input("Introduce la velocidad inicial (m/s): "))
    theta = float(input("Introduce el ángulo de lanzamiento (grados): "))
    coef_rozamiento = float(input("Introduce el coeficiente de rozamiento (kg/s): "))
    masa = float(input("Introduce la masa del proyectil (kg): "))
    return v0, theta, coef_rozamiento, masa

# Parámetros iniciales obtenidos del usuario
v0, theta, coef_rozamiento, masa = obtener_datos()
g = 9.81  # aceleración debido a la gravedad en m/s^2

# Convertir el ángulo a radianes
theta_rad = np.radians(theta)

# Inicializar las condiciones iniciales
dt = 0.01  # paso de tiempo
t_total = 2 * v0 * np.sin(theta_rad) / g  # tiempo estimado de vuelo
n_steps = int(t_total / dt)  # número de pasos de tiempo

# Inicializar arrays para la posición y la velocidad
x = np.zeros(n_steps)
y = np.zeros(n_steps)
vx = np.zeros(n_steps)
vy = np.zeros(n_steps)

# Condiciones iniciales
vx[0] = v0 * np.cos(theta_rad)
vy[0] = v0 * np.sin(theta_rad)

# Resolver las ecuaciones de movimiento usando el método de Euler
for i in range(1, n_steps):
    v = np.sqrt(vx[i-1]**2 + vy[i-1]**2)
    ax = -coef_rozamiento * v * vx[i-1] / masa
    ay = -g - (coef_rozamiento * v * vy[i-1] / masa)
    
    vx[i] = vx[i-1] + ax * dt
    vy[i] = vy[i-1] + ay * dt
    
    x[i] = x[i-1] + vx[i-1] * dt
    y[i] = y[i-1] + vy[i-1] * dt
    
    # Detener el cálculo si el proyectil toca el suelo
    if y[i] < 0:
        x = x[:i]
        y = y[:i]
        break

# Graficar el tiro parabólico
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Tiro Parabólico con Rozamiento')
plt.xlabel('Distancia horizontal (m)')
plt.ylabel('Altura (m)')
plt.grid(True)
plt.show()

