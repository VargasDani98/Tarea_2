import tkinter as tk

def dd_to_dms(degrees):
    d = int(degrees)
    m = int((degrees - d) * 60)
    s = (degrees - d - m / 60) * 3600
    return d, m, s

def dms_to_dd(degrees, minutes, seconds):
    dd = degrees + minutes / 60 + seconds / 3600
    return dd

def conversion_dd_to_dms():
    latitude_dd = float(entry_lat_dd.get())
    longitude_dd = float(entry_long_dd.get())

    latitude_dms = dd_to_dms(latitude_dd)
    longitude_dms = dd_to_dms(longitude_dd)

    label_result_lat.config(text=f"Latitud: {latitude_dms[0]}° {latitude_dms[1]}' {latitude_dms[2]:.4f}'' N")
    label_result_long.config(text=f"Longitud: {longitude_dms[0]}° {longitude_dms[1]}' {longitude_dms[2]:.4f}'' W")

def conversion_dms_to_dd():
    latitude_degrees = float(entry_lat_deg.get())
    latitude_minutes = float(entry_lat_min.get())
    latitude_seconds = float(entry_lat_sec.get())
    
    longitude_degrees = float(entry_long_deg.get())
    longitude_minutes = float(entry_long_min.get())
    longitude_seconds = float(entry_long_sec.get())

    latitude_dd = dms_to_dd(latitude_degrees, latitude_minutes, latitude_seconds)
    longitude_dd = dms_to_dd(longitude_degrees, longitude_minutes, longitude_seconds)

    label_result_lat.config(text=f"Latitud en DD: {latitude_dd}")
    label_result_long.config(text=f"Longitud en DD: {longitude_dd}")

root = tk.Tk()
root.title("Conversor de coordenadas");
root.geometry("600x400")  # Tamaño de la ventana

frame = tk.Frame(root, bg="red")
frame.place(x=20, y=20, width=600, height=400)  # Coordenadas x, y y dimensiones del frame

titulo = tk.Label(frame, text="CONVERSOR DE COORDENADAS", width=30, font=("Arial", 12, "bold"))
titulo.place(x=150, y=20)  # Coordenadas de la etiqueta


label_lat_dd = tk.Label(frame, text="Latitud en DD:")
label_lat_dd.place(x=20, y=70)  # Coordenadas de la etiqueta
entry_lat_dd = tk.Entry(frame)
entry_lat_dd.place(x=150, y=70, width=190)

label_long_dd = tk.Label(frame, text="Longitud en DD:")
label_long_dd.place(x=20, y=100)
entry_long_dd = tk.Entry(frame)
entry_long_dd.place(x=150, y=100, width=190)

button_dd_to_dms = tk.Button(frame, text="DD a DMS", command=conversion_dd_to_dms)
button_dd_to_dms.place(x=20, y=130)



label_lat_deg = tk.Label(frame, text="Grados");
label_lat_deg.place(x=150, y=180)

label_lat_min = tk.Label(frame, text="MInutos");
label_lat_min.place(x=250, y=180)

label_lat_seg = tk.Label(frame, text="Segundos");
label_lat_seg.place(x=350, y=180)

label_lat_deg = tk.Label(frame, text="Latitud en grados:")
label_lat_deg.place(x=20, y=220)

'''Horas'''
entry_lat_deg = tk.Entry(frame)
entry_lat_deg.place(x=150, y=220, width=90)  # Se agrega la coma después de la coordenada x

'''Minutos'''
entry_lat_min = tk.Entry(frame)
entry_lat_min.place(x=250, y=220, width=90)  # Se agrega la coma después de la coordenada x

'''Segundos'''
entry_lat_sec = tk.Entry(frame)
entry_lat_sec.place(x=350, y=220, width=90)  # Se agrega la coma después de la coordenada x


label_long_deg = tk.Label(frame, text="Longitud en grados:")
label_long_deg.place(x=20, y=250)

'''Horas'''
entry_long_deg = tk.Entry(frame)
entry_long_deg.place(x=150, y=250, width=90)

'''Minutos'''
entry_long_min = tk.Entry(frame)
entry_long_min.place(x=250, y=250, width=90)

'''Segundos'''
entry_long_sec = tk.Entry(frame)
entry_long_sec.place(x=350, y=250, width=90)

button_dms_to_dd = tk.Button(frame, text="DMS a DD", command=conversion_dms_to_dd)
button_dms_to_dd.place(x=20, y=280)

label_result_lat = tk.Label(frame, text="")
label_result_lat.place(x=20, y=330)

label_result_long = tk.Label(frame, text="")
label_result_long.place(x=20, y=350)


root.mainloop()
