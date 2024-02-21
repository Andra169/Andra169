import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = st.slider('Pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai',0.0, 100.0, 25.0)
st.write('nilai y:', y)

t = np.linspace(x[0]*np.pi,x[1]*np.pi,100)
u = np.sin(t)
#st.write('nilai t:', t)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='sin(t)', color='b') # Plotting sin(t) curva
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

# Input sliders for a, b, and c
a = st.slider('Masukkan nilai a', -10.0, 30.0, 1.0)
b = st.slider('Masukkan nilai b', -10.0, 30.0, 1.0)
c = st.slider('Masukkan nilai c', -10.0, 30.0, 0.0)

# Slider for x range
x_range = st.slider('Pilih rentang', -10.0, 30.0, (-2.0, 2.0))

# Generate x values
x_values = np.linspace(x_range[0], x_range[1], 400)

# Calculate y values for the quadratic function
y_values = a * x_values ** 2 + b * x_values - c

# Plot the quadratic function
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, y_values, label=f'f(x) = {a}x^2 + {b}x - {c}', color='r')
ax.set_title('Graph of Quadratic Function')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.grid(True)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.legend()
st.pyplot(fig)

# Function to calculate the integral of f(x) from x1 to x2
def calculate_integral(a, b, c, x1, x2):
    # Define the function f(x) = ax^2 + bx - c
    def f(x):
        return a*x**2 + b*x - c
    
    # Calculate the integral using scipy's quad function
    integral, _ = np.round(np.vectorize(f).integrate(x1, x2), 2)
    return integral

# Streamlit code
st.title('Integral and Function Plot')

# Sliders for a, b, c, x1, and x2
a = st.slider('Set a', -10.0, 10.0, 1.0)
b = st.slider('Set b', -10.0, 10.0, 1.0)
c = st.slider('Set c', -10.0, 10.0, 1.0)
x1 = st.slider('Set x1', -10.0, 10.0, -2.0)
x2 = st.slider('Set x2', -10.0, 10.0, 2.0)

# Display the integral value
integral_value = calculate_integral(a, b, c, x1, x2)
st.write(f'Integral of f(x) from {x1} to {x2}: {integral_value}')

# Plot the function f(x) = ax^2 + bx - c
x_values = np.linspace(x1, x2, 100)
y_values = a * x_values ** 2 + b * x_values - c

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x_values, y_values, label='f(x) = ax^2 + bx - c', color='r')
ax.fill_between(x_values, y_values, color='skyblue', alpha=0.4)
ax.set_ylabel("f(x)")
ax.set_xlabel("x")
ax.tick_params(axis='both', labelsize=12)
plt.grid(True)
st.pyplot(fig)
