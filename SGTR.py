import customtkinter as ctk
import os
from PIL import Image, ImageTk
import webbrowser
import tkinter as tk
from tkinter import ttk
from typing import Optional, Tuple, Union
import pymysql
from tkinter import messagebox
from fpdf import FPDF


carpeta_principal = os.path.dirname(__file__)

carpeta_imagen = os.path.join(carpeta_principal, "img")

class VentanaLogin():

    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        w = 2000
        h = 1080
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        w,h = ws,hs
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
        self.root.title("Iniciar Sesion")
        #self.root.attributes('-fullscreen', True)
        
		#-----------------------------------------------------------------

#----------------------------Imagen Login---------------------------------------

        
        img = Image.open(os.path.join(carpeta_imagen, "login_diseño.png"))
        img = img.resize((int(w/1),h))
        img_login = ImageTk.PhotoImage(img)
        img_login_lbl = ctk.CTkLabel(self.root, image=img_login, text="")
        img_login_lbl.pack()
        img_login_lbl.place(x=1, y=1)

        def login_admin():
            if(entry_usuario.get() == ""):
                entry_usuario.focus()
                messagebox.showinfo("Faltan datos", "Ingrese Usuario")
                return
            elif(entry_constrasena.get()==""):
                messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
                entry_constrasena.focus()
                return
			
            basedatos = pmydb = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            fcursor.execute("SELECT Usuario FROM Admin1 WHERE Usuario='" + entry_usuario.get() + "' and Contrasena='" + entry_constrasena.get() + "'")

            if fcursor.fetchall():
                self.root.destroy()
                ventana_menu = VentanaMenu()
            else:
                messagebox.showerror("Error", "Usuario y/o Contraseña Incorrecta")

            basedatos.close()
        
        def LoginARegristrar ():
            self.root.destroy()
            ventana_registrar = VentanaAdmin()
        
        
		
        entry_usuario = ctk.CTkEntry(self.root, placeholder_text="Ingrese Ususario",fg_color="#233B49",border_color="#048BA0", text_color="white",bg_color="white",width=w/4, height=h/19)
        entry_usuario.pack(pady=10)
        entry_usuario.place(relx=0.70, rely=0.50)
		
        entry_constrasena = ctk.CTkEntry(self.root, placeholder_text="Ingrese Contraseña",fg_color="#233B49",border_color="#048BA0", text_color="white", bg_color="white", show="*",width=w/4, height=h/19) 
        entry_constrasena.pack(pady=10)
        entry_constrasena.place(relx=0.70, rely=0.57)
	
        #opciones=["Español", "Ingles"]
        #cmbx_idioma = ctk.CTkComboBox(self.root, values=opciones, state="readonly", width=100)
        #cmbx_idioma.set("idioma:")
        #cmbx_idioma.place(x=685, y=10)

        self.img_entrar = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "logo_entrar.png")), size=(30, 30))

        boton_entrar= ctk.CTkButton(self.root, text="Entrar",width=w/4, height=h/19,
                                    cursor="hand2", bg_color="white" , command=login_admin, image=self.img_entrar, compound="left")
        boton_entrar.pack(pady=20)
        boton_entrar.place(relx=0.70, rely=0.65)
		
        self.gregar_admin = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "gregar_admin.png")), size=(30, 30))

        boton_registrar= ctk.CTkButton(self.root, text="Registrar Administrador", fg_color="#468189" ,width=w/4, height=h/19, 
                                       hover_color="#395462", bg_color="white", cursor="hand2", image=self.gregar_admin, compound="left",command=LoginARegristrar)
        boton_registrar.pack(pady=20)
        boton_registrar.place(relx=0.70, rely=0.72)

        
        
		
		#-----------------------------imagen logo-------------------------------------------

		
		

        

        #boton_admin=ctk.CTkButton(self.root, image=img_registrar_admin_tk, height="50", width="60", fg_color=estilos.background).place(x=410, y=290)

        self.root.mainloop()

class VentanaAdmin():
	
    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        w = 800
        h = 400
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        w,h = ws,hs
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
        self.root.title("Registrar Admin")
        self.root.attributes('-fullscreen',True) 
		#---------------------------------------------------------------------
        def limpiar_caja_admin():
            entry_usuario.delete(0, "end")
            entry_mail.delete(0, "end")
            entry_constrasena.delete(0, "end")
            entry_constrasena2.delete(0, "end")

        def volver_login():
            self.root.destroy()
            ventana_login = VentanaLogin ()
        
        def minimizar_ventana():
            self.root.iconify()

        def registrar_admin():
            if(entry_usuario.get() == ""):
                entry_usuario.focus()
                messagebox.showinfo("Faltan datos", "Ingrese Usuario")
                return
            elif (entry_mail.get()==""):
                messagebox.showinfo("Faltan datos", "Ingrese Mail")
                entry_mail.focus()
                return
            elif(entry_constrasena.get()==""):
                messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
                entry_constrasena.focus()
                return
            elif (entry_constrasena2.get()==""):
                messagebox.showinfo("Faltan datos", "Repita Contraseña")
                entry_constrasena2.focus()
                return
            elif (entry_constrasena.get() != entry_constrasena2.get()):
                messagebox.showinfo("Error","La contraseña no Coinciden")
                return

            basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            nombre_usuario = entry_usuario.get()
            
            fcursor.execute(f"SELECT Usuario FROM Admin1 WHERE Usuario = '{nombre_usuario}'")
            resultado = fcursor.fetchone()

            if resultado:
                messagebox.showinfo("Aviso", "Administrador ya registrado")
                print("El dato no se pudo almacenar")
            else:
                sql = "INSERT INTO Admin1 (Usuario, Mail, Contrasena) VALUES (%s, %s, %s)"
                values = (entry_usuario.get(), entry_mail.get(), entry_constrasena.get())
                fcursor.execute(sql, values)
                basedatos.commit()
                messagebox.showinfo("Registro", "Se registró el Administrador con éxito")
                print("El dato ya se almacenó")


                limpiar_caja_admin()
                basedatos.close()
		#----------------------------------------------------------------
        marco = ctk.CTkFrame (self.root, width=425, height=500)
        marco.pack()
        marco.place(relx=0.37, rely=0.12)

        entry_usuario = ctk.CTkEntry(self.root, placeholder_text="Ingrese el Ususario", width=w/4, height=h/19)
        entry_usuario.pack()
        entry_usuario.place(relx=0.40,rely=0.30)

        entry_mail = ctk.CTkEntry(self.root, placeholder_text="Ingrese el Mail", width=w/4, height=h/19)
        entry_mail.pack()
        entry_mail.place(relx=0.40,rely=0.37)

        entry_constrasena = ctk.CTkEntry(self.root, placeholder_text="Ingrese su Contraseña", width=w/4, height=h/19)
        entry_constrasena.pack()
        entry_constrasena.place(relx=0.40,rely=0.44)

        entry_constrasena2 = ctk.CTkEntry(self.root, show="*", placeholder_text="Reingrese su Contraseña",width=w/4, height=h/19)
        entry_constrasena2.pack()
        entry_constrasena2.place(relx=0.40,rely=0.51)

        self.img_save = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "logo_guardar.png")), size=(30, 30))

        guardar_btn = ctk.CTkButton(self.root, text="Guardar",fg_color="#468189", width=w/4, height=h/19,
                      hover_color="#395462", cursor="hand2", image=self.img_save, compound="left", command=registrar_admin)
        guardar_btn.pack(pady=10, padx=10)
        guardar_btn.place(relx=0.40, rely=0.60)

        boton_salir= ctk.CTkButton(self.root, text="X", fg_color="Red",hover_color="#5e1914", cursor="hand2", 
                                   command=self.root.quit, width=30 , height=30, corner_radius=0)
        boton_salir.pack(pady=10, padx=10)
        boton_salir.place(x=w-30, y=0)

        boton_minimizar= ctk.CTkButton(self.root, text="-", font=("", 20), fg_color="#00a8f3",hover_color="#006593", cursor="hand2", 
                                   command=self.root.iconify, width=30 , height=30, corner_radius=0)
        boton_minimizar.pack(pady=10, padx=10)
        boton_minimizar.place(x=w-64, y=0)
        
        self.img_cancel = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "logo_cancel.png")), size=(30, 30))

        cancelar_btn = ctk.CTkButton(self.root, text="Cancelar", fg_color="red" ,width=w/4, height=h/19, 
                                     hover_color="#5e1914", cursor="hand2", image=self.img_cancel, compound="left", command=limpiar_caja_admin)
        cancelar_btn.pack()
        cancelar_btn.place(relx=0.40, rely=0.67)

        self.img_volver = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "flecha_izquierda.png")), size=(20, 20))

        volver_btn = ctk.CTkButton(self.root, text="", fg_color="#62aea4" ,width=w/40, height=h/22, 
                                     hover_color="#467b74", cursor="hand2", image=self.img_volver, compound="left", command=volver_login)
        volver_btn.pack()
        volver_btn.place(relx=0.00, rely=0.00)
        

        img = Image.open(os.path.join(carpeta_imagen, "logo_sgtr.png"))
        img = img.resize((int(w/8),int(h/7)))
        img_logo = ImageTk.PhotoImage(img)
        img_logo_lbl = ctk.CTkLabel(self.root, image=img_logo, text="",  bg_color="#2b2b2b")
        img_logo_lbl.pack()
        img_logo_lbl.place(relx=0.46, rely=0.14)


        self.root.mainloop()

class Ventana_agregar_articulos():

    def __init__(self):
        super().__init__()

        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 390
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Agregar Artículos")
		#---------------------------------------------------------------
        def Salir_boton():
            self.root.destroy()

        def Cancelar_Boton ():
            entry_marca.delete(0, "end")
            entry_precio.delete(0, "end")
            entry_talle.delete(0, "end")
            cmbx_tipo_usuario.set("Tipo de usuario:")
            entry_tipo_prenda.delete(0, "end")
            cmbx_estado.set("Estado:")
            entry_marca.focus()

        def Guardar_Articulo():
            if entry_marca.get()=="":
                entry_marca.focus()
                messagebox.showinfo("Faltan Datos.","Ingrese la marca.")
                return
            elif entry_talle.get()=="":
                entry_talle.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el talle.")
                return
            elif entry_precio.get()=="":
                entry_precio.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el precio.")
                return
            elif cmbx_tipo_usuario.get()=="Tipo de usuario":
                cmbx_tipo_usuario.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el tipo de usuario.")
                return
            elif entry_tipo_prenda.get()=="":
                entry_tipo_prenda.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el tipo de prenda.")
                return
            elif cmbx_estado.get()=="Estado:":
                cmbx_estado.focus()
                messagebox.showinfo("Faltan Datos.", "Seleccione el estado.")
                return
            
            
            basedatos = mydb = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()
            
            sql="INSERT INTO articulos (marca, talle, estado, precio, tipo_usuario, tipo_prenda) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(entry_marca.get(), entry_talle.get(), cmbx_estado.get(), entry_precio.get(), cmbx_tipo_usuario.get(), entry_tipo_prenda.get())
            fcursor.execute(sql)
            basedatos.commit()
            messagebox.showinfo("Registro", "Se registró el articulo con éxito")

            self.root.destroy()
            basedatos.close()
		
		#----------------Labels, entry y botones-------------------------
		
        entry_marca= ctk.CTkEntry(self.root, placeholder_text="Marca", bg_color="transparent" )
        entry_marca.pack()
        entry_marca.place(relx=0.1,rely=0.1)
		
        entry_talle= ctk.CTkEntry(self.root, placeholder_text="Talle:" )
        entry_talle.pack()
        entry_talle.place(relx=0.1,rely=0.2)
		
        entry_precio= ctk.CTkEntry(self.root, placeholder_text="Precio:")
        entry_precio.pack()
        entry_precio.place(relx=0.1,rely=0.3)

        opciones_usu= ["Hombre", "Mujer", "Niños"]
        cmbx_tipo_usuario= ctk.CTkComboBox(self.root, values=opciones_usu, state="readonly")
        cmbx_tipo_usuario.set("Tipo de usuario")
        cmbx_tipo_usuario.place(relx=0.55,rely=0.1)
		
        entry_tipo_prenda= ctk.CTkEntry(self.root, placeholder_text="Tipo de prenda:" )
        entry_tipo_prenda.pack()
        entry_tipo_prenda.place(relx=0.55,rely=0.2)
		
        opciones= ["Nuevo", "Usado"]
        cmbx_estado= ctk.CTkComboBox(self.root, values=opciones, state="readonly", width=140)
        cmbx_estado.set("Estado:")
        cmbx_estado.place(relx=0.55,rely=0.3)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        self.img_save = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_guardar.png")), size=(30, 30))
        self.img_cancel = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_cancel.png")), size=(30, 30))
        self.img_salir = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_salir.png")), size=(30, 30))

        btn_guardar= ctk.CTkButton(self.root, text="Guardar", fg_color="#24838a", hover_color="#0d565c", width=w/1.25,height=h/10, cursor="hand2" ,command=Guardar_Articulo)#, image=self.img_save, compound="left")
        btn_guardar.place(relx=0.1,rely=0.45)

        btn_cancelar= ctk.CTkButton(self.root, text="Cancelar",fg_color="#ec1c24",hover_color="#b0060c", width=w/1.25,height=h/10, cursor="hand2", command=Cancelar_Boton)#, image=self.img_cancel, compound="left")
        btn_cancelar.place(relx=0.1,rely=0.58)

        btn_salir= ctk.CTkButton(self.root, text="Salir", fg_color="#62aea4", hover_color="#2c7b71",width=w/1.25,height=h/10, cursor="hand2", command=Salir_boton)#,image=self.img_salir, compound="left")
        btn_salir.place(relx=0.1,rely=0.71)

        

        self.root.mainloop()

class Ventana_agregar_cliente():
    def __init__(self):
        super().__init__()

        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 390
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Agregar Cliente")
		#---------------------------------------------------------------
        def Cancelar_boton():
            nombre_entry.delete(0,"end")
            numero_tel_entry.delete(0, "end")
            direccion_entry.delete(0, "end")
            nombre_entry.focus()

        def Salir_boton():
            self.root.destroy()

        def Guardar_Cliente():
            if nombre_entry.get()=="":
                nombre_entry.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el nombre y apellido.")
                return
            elif numero_tel_entry.get()=="":
                numero_tel_entry.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el número de teléfono.")
                return
            elif direccion_entry.get()=="":
                direccion_entry.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese la dirección.")
                return
            
            basedatos  = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            sql="INSERT INTO clientes (NombreyApellido, Numero_Tel, Direccion) VALUES ('{0}','{1}','{2}')".format(nombre_entry.get(), numero_tel_entry.get(), direccion_entry.get())
            fcursor.execute(sql)
            basedatos.commit()
            messagebox.showinfo("Registro", "Se registró el cliente con éxito")

            self.root.destroy()
            basedatos.close()


        #----------------------------- Entrys, Labels, etc.----------------------------------


        nombre_entry = ctk.CTkEntry(self.root, placeholder_text="Nombre y Apellido:" )
        nombre_entry.pack()
        nombre_entry.place(relx=0.3, rely=0.1)
		
        numero_tel_entry=ctk.CTkEntry(self.root,placeholder_text="Número de teléfono:" )
        numero_tel_entry.pack()
        numero_tel_entry.place(relx=0.3,rely=0.2)
		
        direccion_entry= ctk.CTkEntry(self.root,placeholder_text="Dirección:" )
        direccion_entry.pack()
        direccion_entry.place(relx=0.3,rely=0.3)
		
        btn_guardar= ctk.CTkButton(self.root, text="Guardar", fg_color="#24838a", hover_color="#0d565c", width=w/1.25,height=h/10, cursor="hand2" , command=Guardar_Cliente)
        btn_guardar.place(relx=0.1,rely=0.45)

        btn_cancelar= ctk.CTkButton(self.root, text="Cancelar",fg_color="#ec1c24",hover_color="#b0060c", width=w/1.25,height=h/10, cursor="hand2", command=Cancelar_boton)
        btn_cancelar.place(relx=0.1,rely=0.58)

        btn_salir= ctk.CTkButton(self.root, text="Salir", fg_color="#62aea4", hover_color="#2c7b71",width=w/1.25,height=h/10, cursor="hand2", command=Salir_boton)
        btn_salir.place(relx=0.1,rely=0.71)

        self.root.mainloop()

class Ventana_registrar_venta():
    def __init__(self):
        super().__init__()

        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 390
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Registrar Venta")
		#--------------------------------------------------------------------------------------------------------------------------------

        def Salir_registrar_venta():
            self.root.destroy()

        def Cancelar_venta ():
            entry_prendas_compradas.delete(0,"end")
            entry_entrega.delete(0,"end")
            entry_total.delete(0,"end")
            cmbx_nombre.set("Selecione el cliente:")
            cmbx_metodo_pago.set("Método de pago:")
            cmbx_cuotas.set("Cuotas:")
            cmbx_nombre.focus()

        
        def Ventas_button ():
            if cmbx_nombre.get() == "Selecione el cliente:" or entry_prendas_compradas.get() == "" or cmbx_metodo_pago.get() == "Método de pago:" or cmbx_cuotas.get() == "Cuotas:" or entry_total.get() == "":
                messagebox.showinfo("Faltan Datos.", "Por favor, complete todos los campos.")
                return
            
            if lbl_total_final.cget("text").startswith("Total final: "):
                total_final = lbl_total_final.cget("text")[12:]
            else:
                total_final = "No se ha calculado el total final"

            basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()
            
            sql="INSERT INTO ventas (nombreyapellido, prendas_compradas, metedo_pago, entrega, cuotas, total, total_final) VALUES ('{0}','{1}','{2}','{3}','{4}', '{5}', '{6}')".format(cmbx_nombre.get(), entry_prendas_compradas.get(),  cmbx_metodo_pago.get(), entry_entrega.get(), cmbx_cuotas.get(), entry_total.get(), total_final)
            fcursor.execute(sql)
            basedatos.commit()
            messagebox.showinfo("Registro", "Se registró la compra con éxito")

            

            self.root.destroy()
            
            actualizar_tabla_ventas()
            basedatos.close()
        
        def cal_total_final():
            if entry_entrega.get()=="" or entry_total.get() == "":
                messagebox.showinfo("Faltan Datos.", "Por favor, complete todos los campos.")
                return
                
            
            total1_str= entry_total.get()
            total2_str= entry_entrega.get()
            
            total1= float(total1_str)
            total2= float(total2_str)
            total_final= str(total1 - total2)

            lbl_total_final.configure(text=f"Total final: {total_final}")

        
        basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
        fcursor = basedatos.cursor()

        fcursor.execute("SELECT nombreyapellido FROM clientes")
        productos = fcursor.fetchall()

        basedatos.close()

        productos = [producto[0] for producto in productos]
        cmbx_nombre=ctk.CTkComboBox(self.root, values=productos, state="readonly", width=140)
        cmbx_nombre.set("Selecione el cliente:")
        cmbx_nombre.place(relx=0.1, rely=0.05)

        entry_prendas_compradas=ctk.CTkEntry(self.root, placeholder_text="Prendas compradas:")
        entry_prendas_compradas.pack()
        entry_prendas_compradas.place(relx=0.1, rely=0.15)

        opciones=["Efectivo", "Tarjeta"]
        cmbx_metodo_pago=ctk.CTkComboBox(self.root, values=opciones, state="readonly", width=140)
        cmbx_metodo_pago.set("Método de pago:")
        cmbx_metodo_pago.place(relx=0.1, rely=0.25)

        entry_entrega=ctk.CTkEntry(self.root, placeholder_text="Entrega (solo en efectivo):")
        entry_entrega.pack()
        entry_entrega.place(relx=0.1, rely=0.35)

        opciones=["De contado","En veces","1 cuota", "3 cuotas", "6 cuotas", "12 cuotas"]
        cmbx_cuotas=ctk.CTkComboBox(self.root, values=opciones, width=140, state="readonly")
        cmbx_cuotas.set("Cuotas:")
        cmbx_cuotas.place(relx=0.55, rely=0.05)

        entry_total=ctk.CTkEntry(self.root, placeholder_text="Total:")
        entry_total.pack()
        entry_total.place(relx=0.55, rely=0.15)

        lbl_total_final=ctk.CTkLabel(self.root, text="")
        lbl_total_final.place(relx=0.55, rely=0.35)

        btn_calcular_totalfinal=ctk.CTkButton(self.root, text="Calcular total final", fg_color="#62aea4", hover_color="#3b6963",width=140, cursor="hand2", command=cal_total_final )
        btn_calcular_totalfinal.place(relx=0.55, rely=0.25)



        btn_guardar= ctk.CTkButton(self.root, text="Guardar", fg_color="#24838a", hover_color="#0d565c", width=w/1.25,height=h/10, cursor="hand2", command=Ventas_button )#, image=self.img_save, compound="left")
        btn_guardar.place(relx=0.1,rely=0.55)

        btn_cancelar= ctk.CTkButton(self.root, text="Cancelar",fg_color="#ec1c24",hover_color="#b0060c", width=w/1.25,height=h/10, cursor="hand2", command=Cancelar_venta)#, image=self.img_cancel, compound="left")
        btn_cancelar.place(relx=0.1,rely=0.68)

        btn_salir= ctk.CTkButton(self.root, text="Salir", fg_color="#62aea4", hover_color="#2c7b71",width=w/1.25,height=h/10, cursor="hand2", command=Salir_registrar_venta)#,image=self.img_salir, compound="left")
        btn_salir.place(relx=0.1,rely=0.81)





        self.root.mainloop()


class Boleta(FPDF):
    def header(self):
        self.set_font('Times', 'B', 16)
        self.cell(60)
        self.cell(80, 12, 'Comprobante de compra', 1, 0, 'C')
        self.ln(25)

        self.cell(5)
        self.cell(180, 120, '', 1,0,'C')
        self.ln(25)

        

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Esta boleta fue creada a traves de SGTR® %s' % self.page_no(), 0, 0, 'C')

    def create_boleta(self, data):
        self.set_font('Arial', 'B', 12)
        self.cell(20)
        self.cell(40, 10, 'Nombre y Apellido:', 0)
        self.set_x(80)
        self.cell(0, 10, data['nombreyapellido'], 0, 1)
        self.ln(10)

        self.set_font('Arial', 'B', 12)
        self.cell(20)
        self.cell(40, 10, 'Prendas compradas:', 0)
        self.set_x(80)
        self.cell(0, 10, str(data['prendas_compradas']), 0, 1)
        self.ln(10)

        self.set_font('Arial', 'B', 12)
        self.cell(20)
        self.cell(40, 10, 'Método de Pago:', 0)
        self.set_x(80)
        self.cell(0, 10, data['metedo_pago'], 0, 1)
        self.ln(10)

        self.set_font('Arial', 'B', 12)
        self.cell(20)
        self.cell(40, 10, 'Entregó', 0)
        self.set_x(80)
        self.cell(0, 10, str(data['entrega']), 0, 1)
        self.ln(10)

        self.set_font('Arial', 'B', 12)
        self.cell(20)
        self.cell(40, 10, 'Cuotas:', 0)
        self.set_x(80)
        self.cell(0, 10, str(data['cuotas']), 0, 1)
        self.ln(10)

        self.set_y(155)

        self.set_font('Arial', 'B', 12)
        self.cell(140)
        self.cell(40, 10, 'Total:', 0)
        self.set_x(162)
        self.cell(0, 10, str(data['total']), 0, 1)
        self.ln(20)

        self.set_y(160)

        self.set_font('Arial', 'B', 12)
        self.cell(140)
        self.cell(40, 10, 'Total final:', 0)
        self.set_x(168)
        self.cell(0, 10, str(data['total_final']), 0, 1)
        self.ln(20)

        

        self.set_y(155)

        self.cell (135)
        self.cell(50, 15, '', 1, 0, 'C')
        self.ln(20)


class Ventana_crear_boleta():
    def __init__(self):
        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
        self.root.title("Crear Boleta")

        w = 390
        h = 150
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)

        self.entry_numero_compra = ctk.CTkEntry(self.root, placeholder_text="Núm. de Compra:")
        self.entry_numero_compra.pack()
        self.entry_numero_compra.place(relx=0.1, rely=0.1)

        self.entry_guardar_nombre = ctk.CTkEntry(self.root, placeholder_text="Guardar cómo:")
        self.entry_guardar_nombre.pack()
        self.entry_guardar_nombre.place(relx=0.55, rely=0.1)

        btn_guardar = ctk.CTkButton(self.root, text="Guardar",hover_color="#0f5b61", fg_color="#24838a",  width=w/1.24, height=h/2.55, cursor="hand2", command=self.Abrir_Crear_Boleta)
        btn_guardar.place(relx=0.1, rely=0.4)

        self.root.mainloop()

    def Abrir_Crear_Boleta(self):
        

        id_boleta = int(self.entry_numero_compra.get())
        nombre_archivo = self.entry_guardar_nombre.get() + ".pdf"

        boleta = Boleta()
        boleta.add_page()

        basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
        fcursor = basedatos.cursor()

        query = "SELECT nombreyapellido, prendas_compradas, metedo_pago, entrega, cuotas, total, total_final FROM ventas WHERE id_ventas = %s"
        fcursor.execute(query, (id_boleta,))
        data = fcursor.fetchone()

        if data is not None and len(data) >= 7:
            boleta.create_boleta({'nombreyapellido': data[0],
                                   'prendas_compradas': data[1],
                                     'metedo_pago': data[2],
                                     'entrega': data[3], 
                                     'cuotas': data[4], 
                                     'total': data[5],
                                     'total_final': data[6],
                                     })
            boleta.output(nombre_archivo)
            messagebox.showinfo("Exito", "La boleta se guardó con éxito.")
            print("Se guardó correctamente la boleta")
        else:
            print("Error: No se encontraron datos para crear la boleta.")
            messagebox.showerror("Error", "La boleta no se pudo crear, verifica los datos.")
        fcursor.close()
        basedatos.close()
        self.root.destroy()

class Ventana_eliminar_cliente():
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 150
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Eliminar Cliente")

        def sacar_lista():
            id_boleta = int(self.entry_numero_cliente.get())
        
            if self.entry_numero_cliente.get() == "":
                self.entry_numero_cliente.focus()
                messagebox.showerror("Error", "Coloca el número de compra")
                print("No escribio el N° de venta.")
                return
        
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            try:
                fcursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_boleta,))
                basedatos.commit()
                messagebox.showinfo("Listo", "El cliente se ha borrado correctamente.")
                self.root.destroy()
                print("La venta se ha eliminado sin problemas.")
            except Exception as e:
                basedatos.rollback()
                messagebox.showerror("Error", "Ocurrió un error al eliminar la venta.")
                print("Error al eliminar la venta:", e)
        
            basedatos.close()

#------------------------------------------------------------------------------------------------

        self.entry_numero_cliente= ctk.CTkEntry(self.root, placeholder_text="N° de Cliente:" )
        self.entry_numero_cliente.pack()
        self.entry_numero_cliente.place(x=125, y=30)

        self.btn_eliminar= ctk.CTkButton(self.root, text="Eliminar", width=150, height=60, command=sacar_lista)
        self.btn_eliminar.place(x=120, y=75)

        self.root.mainloop()

class Ventana_eliminar_venta():
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 150
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Eliminar Venta")

        def sacar_lista():
            id_boleta = int(self.entry_numero_venta.get())
        
            if self.entry_numero_venta.get() == "":
                self.entry_numero_venta.focus()
                messagebox.showerror("Error", "Coloca el número de compra")
                print("No escribio el N° de venta.")
                return
        
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            try:
                fcursor.execute("DELETE FROM ventas WHERE id_ventas = %s", (id_boleta,))
                basedatos.commit()
                messagebox.showinfo("Listo", "La venta se ha borrado correctamente.")
                self.root.destroy()
                print("La venta se ha eliminado sin problemas.")
            except Exception as e:
                basedatos.rollback()
                messagebox.showerror("Error", "Ocurrió un error al eliminar la venta.")
                print("Error al eliminar la venta:", e)
        
            basedatos.close()

#------------------------------------------------------------------------------------------------

        self.entry_numero_venta= ctk.CTkEntry(self.root, placeholder_text="N° de venta:" )
        self.entry_numero_venta.pack()
        self.entry_numero_venta.place(x=125, y=30)

        self.btn_eliminar= ctk.CTkButton(self.root, text="Eliminar", width=150, height=60, command=sacar_lista)
        self.btn_eliminar.place(x=120, y=75)

        self.root.mainloop()

class Ventana_eliminar_proovedor():
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 150
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Eliminar Proovedor")

        def sacar_lista():
            id_boleta = int(self.entry_numero_proovedor.get())
        
            if self.entry_numero_proovedor.get() == "":
                self.entry_numero_proovedor.focus()
                messagebox.showerror("Error", "Coloca el número de compra")
                print("No escribio el N° de proovedor.")
                return
        
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            try:
                fcursor.execute("DELETE FROM proovedores WHERE id_proovedor = %s", (id_boleta,))
                basedatos.commit()
                messagebox.showinfo("Listo", "El proovedor se ha borrado correctamente.")
                self.root.destroy()
                print("La venta se ha eliminado sin problemas.")
            except Exception as e:
                basedatos.rollback()
                messagebox.showerror("Error", "Ocurrió un error al eliminar la venta.")
                print("Error al eliminar la venta:", e)
        
            basedatos.close()

#------------------------------------------------------------------------------------------------

        self.entry_numero_proovedor= ctk.CTkEntry(self.root, placeholder_text="N° de Proovedor:" )
        self.entry_numero_proovedor.pack()
        self.entry_numero_proovedor.place(x=125, y=30)

        self.btn_eliminar= ctk.CTkButton(self.root, text="Eliminar", width=150, height=60, command=sacar_lista)
        self.btn_eliminar.place(x=120, y=75)

        self.root.mainloop()

class Ventana_eliminar_stock():
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 150
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Eliminar Stock")

        def sacar_lista():
            id_boleta = int(self.entry_numero_stock.get())
        
            if self.entry_numero_stock.get() == "":
                self.entry_numero_stock.focus()
                messagebox.showerror("Error", "Coloca el número de compra")
                print("No escribio el N° de venta.")
                return
        
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            try:
                fcursor.execute("DELETE FROM articulos WHERE id_articulos = %s", (id_boleta,))
                basedatos.commit()
                messagebox.showinfo("Listo", "El Artículo se ha borrado correctamente.")
                self.root.destroy()
                print("El artículo se ha eliminado sin problemas.")
            except Exception as e:
                basedatos.rollback()
                messagebox.showerror("Error", "Ocurrió un error al eliminar la venta.")
                print("Error al eliminar la venta:", e)
        
            basedatos.close()

#------------------------------------------------------------------------------------------------

        self.entry_numero_stock= ctk.CTkEntry(self.root, placeholder_text="N° de Artículo:" )
        self.entry_numero_stock.pack()
        self.entry_numero_stock.place(x=125, y=30)

        self.btn_eliminar= ctk.CTkButton(self.root, text="Eliminar", width=150, height=60, command=sacar_lista)
        self.btn_eliminar.place(x=120, y=75)

        self.root.mainloop()

#------------------------------------------------------------------------------------------------

        

    

    

class Ventana_registrar_proveedor():
    def __init__(self):
        super().__init__()

        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 390
        h = 390
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(False, False)
		#-----------------------------------------------------------------
        self.root.title("Registrar Proveedor")

        
        #--------------------------FUNCIONES-------------------------------------
        def Cancelar_boton():
            nombre_entry.delete(0,"end")
            marcas_entry.delete(0, "end")
            tipo_prenda_entry.delete(0, "end")
            nro_telefono_entry.delete(0, "end")

        def Guardar_proovedor():
            if entry_nombre.get()=="":
                entry_nombre.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el nombre.")
                return
            elif entry_apellido.get()=="":
                entry_apellido.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el apellido.")
                return
            elif entry_empresa.get()=="":
                entry_empresa.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el tipo de producto.")
                return
            elif entry_num_tel.get()=="":
                entry_num_tel.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el N° de teléfono.")
                return
            elif entry_tipo_producto.get()=="":
                entry_tipo_producto.focus()
                messagebox.showinfo("Faltan Datos.", "Ingrese el tipo de producto")
                return
            elif entry_marca.get()=="":
                entry_marca.focus()
                messagebox.showinfo("Faltan datos.", "Ingrese las marcas.")
            
            basedatos  = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            sql="INSERT INTO proovedores (nombre, apellido, empresa, num_telefono, tipo_producto, marca) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(entry_nombre.get(), entry_apellido.get(), entry_empresa.get(), entry_num_tel.get(), entry_tipo_producto.get(), entry_marca.get())
            fcursor.execute(sql)
            basedatos.commit()
            messagebox.showinfo("Registro", "Se registró el proovedor con éxito")

            self.root.destroy()
            basedatos.close()

        def Salir_boton():
            self.root.destroy()
		#---------------------------------------------------------------

        entry_nombre=ctk.CTkEntry(self.root, placeholder_text="Nombre:")
        entry_nombre.pack()
        entry_nombre.place(relx=0.1, rely=0.1)

        entry_apellido=ctk.CTkEntry(self.root, placeholder_text="Apellido:")
        entry_apellido.pack()
        entry_apellido.place(relx=0.1, rely=0.2)

        entry_empresa=ctk.CTkEntry(self.root, placeholder_text="Empresa:")
        entry_empresa.pack()
        entry_empresa.place(relx=0.1, rely=0.3)

        entry_num_tel=ctk.CTkEntry(self.root, placeholder_text="Número de telefono:")
        entry_num_tel.pack()
        entry_num_tel.place(relx=0.55, rely=0.1)
        
        entry_tipo_producto=ctk.CTkEntry(self.root, placeholder_text="Tipo de producto:")
        entry_tipo_producto.pack()
        entry_tipo_producto.place(relx=0.55, rely=0.2)

        entry_marca=ctk.CTkEntry(self.root, placeholder_text="Marca:")
        entry_marca.pack()
        entry_marca.place(relx=0.55, rely=0.3)

        btn_guardar= ctk.CTkButton(self.root, text="Guardar", fg_color="#24838a", hover_color="#0d565c", width=w/1.25,height=h/10, cursor="hand2", command=Guardar_proovedor )#, image=self.img_save, compound="left")
        btn_guardar.place(relx=0.1,rely=0.45)

        btn_cancelar= ctk.CTkButton(self.root, text="Cancelar",fg_color="#ec1c24",hover_color="#b0060c", width=w/1.25,height=h/10, cursor="hand2", command=Cancelar_boton )#, image=self.img_cancel, compound="left")
        btn_cancelar.place(relx=0.1,rely=0.58)

        btn_salir= ctk.CTkButton(self.root, text="Salir", fg_color="#62aea4", hover_color="#2c7b71",width=w/1.25,height=h/10, cursor="hand2", command=Salir_boton )#,image=self.img_salir, compound="left")
        btn_salir.place(relx=0.1,rely=0.71)

        self.root.mainloop()


class VentanaMenu():
    def __init__(self):
        super().__init__()

        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 2000
        h = 1080
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        w,h = ws,hs
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
        self.root.title("Menú")
	    #self.root.iconbitmap("D:\\programacion IV\\proyecto final\\favicon.ico")
        self.navegacion_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.navegacion_frame.place(x=0, y=0)

        # set grid layout 1x2
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        def Abrir_Agregar_Articulos():
            ventana_agregar_articulos = Ventana_agregar_articulos()
        def Abrir_Agregar_Clientes():
            ventana_agregar_cliente = Ventana_agregar_cliente()
        def Abrir_registrar_ventas():
            ventana_registrar_venta = Ventana_registrar_venta()
        def Abrir_Registrar_Proveedor():
            ventana_registrar_proveedor = Ventana_registrar_proveedor()
        def Abrir_Crear_Boleta():
            ventana_crear_boleta = Ventana_crear_boleta()
        def Abrir_Eliminar_Venta():
            ventana_eliminar_venta = Ventana_eliminar_venta()
        def Abrir_Eliminar_Cliente():
            ventana_eliminar_cliente = Ventana_eliminar_cliente()
        def Abrir_Eliminar_Proovedor():
            ventana_eliminar_proovedor = Ventana_eliminar_proovedor()
        def Abrir_Editar_Articulo():
            ventana_editar_articulo = Ventana_editar_articulo()

        def actualizar_tabla_cliente():
            basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            fcursor.execute("SELECT id_cliente, NombreyApellido, Numero_tel, Direccion FROM clientes")
            rows = fcursor.fetchall()
            for child in self.tablaclientes.get_children():
                self.tablaclientes.delete(child)
            for row in rows:
                self.tablaclientes.insert("","end",values=row)

        def actualizar_tabla_ventas():
            basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            fcursor.execute("SELECT id_ventas, nombreyapellido, prendas_compradas, metedo_pago, entrega,  cuotas, total, total_final FROM ventas")
            rows = fcursor.fetchall()
            for child in self.tablaventas.get_children():
                self.tablaventas.delete(child)
            for row in rows:
                self.tablaventas.insert("","end",values=row)

        def actualizar_tabla_proovedor():
            basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            fcursor.execute("SELECT id_proovedor, nombre, apellido, empresa, num_telefono, tipo_producto, marca FROM proovedores")
            rows = fcursor.fetchall()
            for child in self.tablaproovedores.get_children():
                self.tablaproovedores.delete(child)
            for row in rows:
                self.tablaproovedores.insert("","end",values=row)

        def actualizar_tabla_stock():
            basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()

            for child in self.tablahombre.get_children():
                self.tablahombre.delete(child)

            fcursor.execute("SELECT id_articulos, marca, talle, estado, precio, tipo_usuario, tipo_prenda FROM articulos WHERE tipo_usuario = 'hombre'")
            rows_hombre = fcursor.fetchall()
            for row in rows_hombre:
                self.tablahombre.insert("", "end", values=row)

            for child in self.tablamujer.get_children():
                self.tablamujer.delete(child)

            fcursor.execute("SELECT id_articulos, marca, talle, estado, precio, tipo_usuario, tipo_prenda FROM articulos WHERE tipo_usuario = 'mujer'")
            rows_mujer = fcursor.fetchall()
            for row in rows_mujer:
                self.tablamujer.insert("", "end", values=row)

            for child in self.tablaninios.get_children():
                self.tablaninios.delete(child)

            fcursor.execute("SELECT id_articulos, marca, talle, estado, precio, tipo_usuario, tipo_prenda FROM articulos WHERE tipo_usuario = 'niños'")
            rows_ninios = fcursor.fetchall()
            for row in rows_ninios:
                self.tablaninios.insert("", "end", values=row)

            basedatos.close()


            

        def buscar_cliente ():
            texto_busqueda = self.entry_buscar_cliente.get()
    
            for row in self.tablaclientes.get_children():
                self.tablaclientes.delete(row)
    
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()
    
            query = "SELECT id_cliente, NombreyApellido, Numero_tel, Direccion FROM clientes WHERE NombreyApellido LIKE %s"
            fcursor.execute(query, ("%" + texto_busqueda + "%",))
            rows = fcursor.fetchall()
    
            for row in rows:
                self.tablaclientes.insert("", "end", values=row)
    
            basedatos.close()

        def buscar_stock ():
            texto_busqueda = self.entry_buscar_articulo.get()
    
            for row in self.tablahombre.get_children():
                self.tablahombre.delete(row)

            for row in self.tablamujer.get_children():
                self.tablamujer.delete(row)

            for row in self.tablaninios.get_children():
                self.tablaninios.delete(row)

            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()
            query_hombre = "SELECT id_articulos, marca, talle, estado, precio, tipo_usuario, tipo_prenda FROM articulos WHERE tipo_usuario = 'hombre' AND marca LIKE %s"
            fcursor.execute(query_hombre, ("%" + texto_busqueda + "%",))
            rows_hombre = fcursor.fetchall()

            for row in rows_hombre:
                self.tablahombre.insert("", "end", values=row)

            query_mujer = "SELECT id_articulos, marca, talle, estado, precio, tipo_usuario, tipo_prenda FROM articulos WHERE tipo_usuario = 'mujer' AND marca LIKE %s"
            fcursor.execute(query_mujer, ("%" + texto_busqueda + "%",))
            rows_mujer = fcursor.fetchall()

            for row in rows_mujer:
                self.tablamujer.insert("", "end", values=row)

            query_ninios = "SELECT id_articulos, marca, talle, estado, precio, tipo_usuario, tipo_prenda FROM articulos WHERE tipo_usuario = 'niños' AND marca LIKE %s"
            fcursor.execute(query_ninios, ("%" + texto_busqueda + "%",))
            rows_ninios = fcursor.fetchall()

            for row in rows_ninios:
                self.tablaninios.insert("", "end", values=row)
    
            basedatos.close()


                
        def buscar_venta ():
            texto_busqueda = self.entry_buscar_venta.get()
    
            for row in self.tablaventas.get_children():
                self.tablaventas.delete(row)
    
            
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()
    
            query = "SELECT id_ventas, nombreyapellido, prendas_compradas, metedo_pago, entrega, cuotas, total, total_final FROM ventas WHERE nombreyapellido LIKE %s"
            fcursor.execute(query, ("%" + texto_busqueda + "%",))
            rows = fcursor.fetchall()
    
            for row in rows:
                self.tablaventas.insert("", "end", values=row)
    
            basedatos.close()
        
        def buscar_proovedor ():
            texto_busqueda = self.entry_buscar_proovedor.get()
    
            for row in self.tablaproovedores.get_children():
                self.tablaproovedores.delete(row)
    
            
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()
    
            query = "SELECT id_proovedor, nombre, apellido, empresa, num_telefono, tipo_producto, marca FROM proovedores WHERE nombre LIKE %s"
            fcursor.execute(query, ("%" + texto_busqueda + "%",))
            rows = fcursor.fetchall()
    
            for row in rows:
                self.tablaproovedores.insert("", "end", values=row)
    
            basedatos.close()


        

        


        
        

        # CARGAR IMÁGENES
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        self.img_login = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_sgtr.png")), size=(125, 85))
        self.home_image = ctk.CTkImage(Image.open(os.path.join(image_path, "home_light.png")), size=(30, 30))
        self.client_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_clientes.png")), size=(30, 30))
        self.stock_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_stock.png")), size=(30, 30))
        self.ventas_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_ventas.png")), size=(30, 30))
        self.proveedor_image= ctk.CTkImage(Image.open(os.path.join(image_path, "logo_proovedor.png")), size=(30,30))


        # FRAME DE NAVEGACIÓN
        self.navegacion_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.navegacion_frame.grid(row=0, column=0, sticky="nsew")
        self.navegacion_frame.grid_rowconfigure(30, weight=2)


        self.navegacion_frame_label = ctk.CTkLabel(self.navegacion_frame, text="", image=self.img_login,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navegacion_frame_label.grid(row=0, column=0,padx=ws/15, pady=hs/40)

        self.home_button = ctk.CTkButton(self.navegacion_frame, corner_radius=0, height=40, border_spacing=10, text="Acerca de nosotros",font=ctk.CTkFont(size=15, weight="bold"),
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=6, column=0, sticky="ew")

        self.clientes_button = ctk.CTkButton(self.navegacion_frame, corner_radius=0, height=40, border_spacing=10, text="Clientes",font=ctk.CTkFont(size=15, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.client_image, anchor="w", command=self.clientes_button_event)
        self.clientes_button.grid(row=2, column=0, sticky="ew")

        self.stock_button = ctk.CTkButton(self.navegacion_frame, corner_radius=0, height=40, border_spacing=10, text="Stock",font=ctk.CTkFont(size=15, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.stock_image, anchor="w", command=self.stock_button_event)
        self.stock_button.grid(row=3, column=0, sticky="ew")

        self.ventas_button = ctk.CTkButton(self.navegacion_frame, corner_radius=0, height=40, border_spacing=10, text="Ventas",font=ctk.CTkFont(size=15, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.ventas_image, anchor="w", command=self.ventas_button_event)
        self.ventas_button.grid(row=4, column=0, sticky="ew")

        self.proveedor_button = ctk.CTkButton(self.navegacion_frame, corner_radius=0, height=40, border_spacing=10, text="proveedores", font=ctk.CTkFont(size=15, weight="bold"),
                                              fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                              image=self.proveedor_image, anchor="w", command=self.proveedores_button_event)
        self.proveedor_button.grid(row=5, column=0, sticky="ew")

        

        


        # FRAME HOME
        self.home_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        
        empresa_titulo = "Desarrollado por Neuron: Smart develop"

        empresa_label = ctk.CTkLabel(self.home_frame, text=empresa_titulo, font=("Helvetica", 15))
        empresa_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        def abrir_pagina_web():
            webbrowser.open("file:///D:/Julio%20Arrieta/Proyecto%20Final%20CUSTOM/SGTR%20html/sgtr.html")

        web_button = ctk.CTkButton(self.home_frame, text="Sitio Web", command=abrir_pagina_web)
        web_button.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="w")

        empresa_info = """Historia:
        Fundada en 2023, Neuron surge como una respuesta a la creciente necesidad de soluciones tecnológicas innovadoras en el ámbito comercial.
        Nuestra misión es impulsar el crecimiento de las empresas a través del desarrollo de programas inteligentes y adaptativos.

Compromiso con la Innovación:
        En Neuron, abrazamos la filosofía de la innovación constante.
        Nuestro equipo altamente calificado de desarrolladores trabaja incansablemente para crear soluciones que no solo cumplen con las demandas 
        actuales, sino que también anticipan las necesidades futuras del mundo empresarial.

Visión:
        En Neuron: Smart Develop, visualizamos un futuro donde cada empresa, independientemente de su tamaño, tenga acceso a soluciones tecnológicas de vanguardia. 
        Nos esforzamos por ser líderes en la industria, impulsando la transformación digital y contribuyendo al éxito de nuestros clientes.
        
Únete a la Revolución Tecnológica con Neuron: Smart Develop:
        Si buscas llevar tu empresa al siguiente nivel con soluciones tecnológicas inteligentes y centradas en el futuro, ¡Neuron: Smart Develop es tu socio 
        ideal!"""


        info_text = ctk.CTkTextbox(self.home_frame, wrap="word", height=350, width=1010, font=("Helvetica", 14))
        info_text.insert("1.0", empresa_info)
        info_text.configure(state="disabled")
        info_text.grid(row=3, column=0, padx=20, pady=10, sticky="w")


        # FRAME CLIENTES
        self.segundo_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.segundo_frame.grid_columnconfigure(0, weight=1)       

        self.btn_agregar_cliente = ctk.CTkButton(self.segundo_frame, text="Agregar Cliente", command=Abrir_Agregar_Clientes)
        self.btn_agregar_cliente.grid(row=0, column=0, padx=10, pady=5, sticky="nsew") 

        self.btn_eliminar_cliente = ctk.CTkButton(self.segundo_frame, text="Eliminar Cliente", command=Abrir_Eliminar_Cliente)
        self.btn_eliminar_cliente.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        self.btn_actualizar_tabla_cli = ctk.CTkButton(self.segundo_frame, text="Actualizar Tabla", command=actualizar_tabla_cliente)
        self.btn_actualizar_tabla_cli.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")

        #--------------------------------------------Buscar-----------------------------------------------------------------

        self.frame_buscar = ctk.CTkFrame(self.segundo_frame)
        self.frame_buscar.grid(row=0, column=3, padx=5, pady=10, sticky="nsew")

        self.entry_buscar_cliente = ctk.CTkEntry(self.frame_buscar, placeholder_text="Buscar", width=400)
        self.entry_buscar_cliente.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="nsew")

        self.search_icon = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "search.png")), size=(20, 20))

        self.btn_buscar = ctk.CTkButton(self.frame_buscar, text="", width=20,cursor="hand2", image=self.search_icon, command=buscar_cliente)
        self.btn_buscar.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

 #--------------------------------------------Tabla-----------------------------------------------------------------

        self.tablaclientes = ttk.Treeview(self.segundo_frame)
        self.tablaclientes["columns"] = ("N° de cliente", "Nombre y Apellido", "Número de teléfono", "Dirección") 
        
        self.tablaclientes.heading("#0", text="")
        self.tablaclientes.column("#0", width=0, stretch=tk.NO)

        self.tablaclientes.heading("#1", text="N° de cliente")
        self.tablaclientes.column("#1", width=120, minwidth=120, stretch="no")

        self.tablaclientes.heading("#2", text="Nombre y Apellido")
        self.tablaclientes.column("#2", width=200, minwidth=200, stretch="no")

        self.tablaclientes.heading("#3", text="Número de teléfono")
        self.tablaclientes.column("#3", width=120, minwidth=120, stretch="no")

        self.tablaclientes.heading("#4", text="Dirección")
        self.tablaclientes.column("#4", width=120, minwidth=120, stretch="no")

        self.tablaclientes.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ns")

        basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
        fcursor = basedatos.cursor()

        fcursor.execute("SELECT id_cliente, NombreyApellido, Numero_tel, Direccion FROM clientes")
        rows = fcursor.fetchall()

        for row in rows:
            self.tablaclientes.insert("","end",values=row)



        # FRAME STOCK

        def cargar_articulos(frame, genero):
            basedatos = pymysql.connect(host="localhost", user="root", passwd="", db="sistemproa")
            fcursor = basedatos.cursor()
    
            query = "SELECT id_articulos, marca, talle, estado, precio, tipo_usuario, tipo_prenda FROM articulos WHERE tipo_usuario = %s"
            fcursor.execute(query, (genero,))
            rows = fcursor.fetchall()
    
            for row in rows:
                frame.insert("", "end", values=row)
    
        basedatos.close()
        self.tercer_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.tercer_frame.grid_columnconfigure(0, weight=1)

        self.agregar_articulo_button_1 = ctk.CTkButton(self.tercer_frame, text="Agregar Artículo", command= Abrir_Agregar_Articulos)
        self.agregar_articulo_button_1.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.agregar_articulo_button_1.configure(width=155)

        self.actualizar_tabla= ctk.CTkButton(self.tercer_frame, text="Actualizar tabla", command=actualizar_tabla_stock)
        self.actualizar_tabla.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")

        self.eliminar_stock= ctk.CTkButton(self.tercer_frame, text="Eliminar stock", command=Ventana_eliminar_stock)
        self.eliminar_stock.grid(row=0, column=3, padx=10, pady=5, sticky="nsew")

        #--------------------------------------------Buscar-----------------------------------------------------------------

        self.frame_buscar = ctk.CTkFrame(self.tercer_frame)
        self.frame_buscar.grid(row=0, column=4, padx=5, pady=10, sticky="nsew")

        self.entry_buscar_articulo = ctk.CTkEntry(self.frame_buscar, placeholder_text="Buscar", width=400)
        self.entry_buscar_articulo.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="nsew")

        self.search_icon = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "search.png")), size=(20, 20))

        self.btn_buscar = ctk.CTkButton(self.frame_buscar, text="", width=20,cursor="hand2", image=self.search_icon, command=buscar_stock)
        self.btn_buscar.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

#--------------------------------------------TABLA-----------------------------------------------------------------


        self.tabview = ctk.CTkTabview(self.tercer_frame, width=250)
        self.tabview.grid(row=1, column=0, padx=(30, 0), pady=(30, 0), columnspan=5, sticky="nsew")
        self.tabview.add("Hombre")
        self.tabview.add("Mujer")
        self.tabview.add("Niños")
        self.tabview.tab("Hombre").grid_columnconfigure(0, weight=1)  
        self.tabview.tab("Mujer").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Niños").grid_columnconfigure(0, weight=1)


        
        self.lblhombre = ctk.CTkLabel(self.tabview.tab("Hombre"), text="Ropa de Hombre")
        self.lblhombre.grid(row=0, column=0, padx=20, pady=20)

        self.tablahombre = ttk.Treeview(self.tabview.tab("Hombre"))
        self.tablahombre["columns"] = ("N° Artículo", "Marca", "Talle", "Estado", "Precio", "Tipo de Usuario", "Tipo de Prenda")
        self.tablahombre.grid(row=0, column=0)
        cargar_articulos(self.tablahombre, "Hombre")

        self.tablahombre.heading("#0", text="")
        self.tablahombre.column("#0", width=0, stretch=tk.NO)

        self.tablahombre.heading("#1", text="N° Artículo")
        self.tablahombre.column("#1", width=120, minwidth=120, stretch="no")
    
        self.tablahombre.heading("#2", text="Marca")
        self.tablahombre.column("#2", width=120, minwidth=120, stretch="no")

        self.tablahombre.heading("#3", text="Talle")
        self.tablahombre.column("#3", width=120, minwidth=120, stretch="no")

        self.tablahombre.heading("#4", text="Estado")
        self.tablahombre.column("#4", width=120, minwidth=120, stretch="no")

        self.tablahombre.heading("#5", text="Precio")
        self.tablahombre.column("#5", width=120, minwidth=120, stretch="no")

        self.tablahombre.heading("#6", text="Tipo de Usuario")
        self.tablahombre.column("#6", width=120, minwidth=120, stretch="no")

        self.tablahombre.heading("#7", text="Tipo de Prenda")
        self.tablahombre.column("#7", width=120, minwidth=120, stretch="no")
        self.tablahombre.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


        self.lblmujer = ctk.CTkLabel(self.tabview.tab("Mujer"), text="Ropa de Mujer")
        self.lblmujer.grid(row=0, column=0, padx=20, pady=20)
        
        self.tablamujer = ttk.Treeview(self.tabview.tab("Mujer"))
        self.tablamujer["columns"] = ("N° Artículo", "Marca", "Talle", "Estado", "Precio", "Tipo de Usuario", "Tipo de Prenda")
        self.tablamujer.grid(row=0, column=0)
        cargar_articulos(self.tablamujer, "Mujer")
        
        self.tablamujer.heading("#0", text="")
        self.tablamujer.column("#0", width=0, stretch=tk.NO)

        self.tablamujer.heading("#1", text="N° Artículo")
        self.tablamujer.column("#1", width=120, minwidth=120, stretch="no")
        
        self.tablamujer.heading("#2", text="Marca")
        self.tablamujer.column("#2", width=120, minwidth=120, stretch="no")

        self.tablamujer.heading("#3", text="Talle")
        self.tablamujer.column("#3", width=120, minwidth=120, stretch="no")

        self.tablamujer.heading("#4", text="Estado")
        self.tablamujer.column("#4", width=120, minwidth=120, stretch="no")

        self.tablamujer.heading("#5", text="Precio")
        self.tablamujer.column("#5", width=120, minwidth=120, stretch="no")

        self.tablamujer.heading("#6", text="Tipo de Usuario")
        self.tablamujer.column("#6", width=120, minwidth=120, stretch="no")

        self.tablamujer.heading("#7", text="Tipo de Prenda")
        self.tablamujer.column("#7", width=120, minwidth=120, stretch="no")

        self.tablamujer.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.lblninio = ctk.CTkLabel(self.tabview.tab("Niños"), text="Ropa de niños")
        self.lblninio.grid(row=0, column=0, padx=20, pady=20)

        self.tablaninios = ttk.Treeview(self.tabview.tab("Niños"))
        self.tablaninios["columns"] = ("N° Artículo", "Marca", "Talle", "Estado", "Precio", "Tipo de Usuario", "Tipo de Prenda")
        self.tablaninios.grid(row=0, column=0)
        cargar_articulos(self.tablaninios, "Niños")

        self.tablaninios.heading("#0", text="")
        self.tablaninios.column("#0", width=0, stretch=tk.NO)

        self.tablaninios.heading("#1", text="N° Artículo")
        self.tablaninios.column("#1", width=120, minwidth=120, stretch="no")
    
        self.tablaninios.heading("#2", text="Marca")
        self.tablaninios.column("#2", width=120, minwidth=120, stretch="no")

        self.tablaninios.heading("#3", text="Talle")
        self.tablaninios.column("#3", width=120, minwidth=120, stretch="no")

        self.tablaninios.heading("#4", text="Estado")
        self.tablaninios.column("#4", width=120, minwidth=120, stretch="no")

        self.tablaninios.heading("#5", text="Precio")
        self.tablaninios.column("#5", width=120, minwidth=120, stretch="no")

        self.tablaninios.heading("#6", text="Tipo de Usuario")
        self.tablaninios.column("#6", width=120, minwidth=120, stretch="no")

        self.tablaninios.heading("#7", text="Tipo de Prenda")
        self.tablaninios.column("#7", width=120, minwidth=120, stretch="no")
        self.tablaninios.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


        #FRAME VENTAS
        self.cuarto_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.cuarto_frame.grid_columnconfigure(0, weight=1)

        self.agregar_venta_button_1 = ctk.CTkButton(self.cuarto_frame, text="Registrar Venta", command= Abrir_registrar_ventas)
        self.agregar_venta_button_1.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.guardar_boleta = ctk.CTkButton(self.cuarto_frame, text="Crear boleta", command= Abrir_Crear_Boleta)
        self.guardar_boleta.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        self.actualizar_tabla= ctk.CTkButton(self.cuarto_frame, text="Actualizar Tabla", command=actualizar_tabla_ventas)
        self.actualizar_tabla.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")

        self.eliminar_venta= ctk.CTkButton(self.cuarto_frame, text="Eliminar Venta",command=Abrir_Eliminar_Venta)
        self.eliminar_venta.grid(row=0, column=3, padx=10, pady=5, sticky="nsew")

#--------------------------------------------Buscar-----------------------------------------------------------------

        self.frame_buscar = ctk.CTkFrame(self.cuarto_frame)
        self.frame_buscar.grid(row=0, column=4, padx=5, pady=10)

        self.entry_buscar_venta = ctk.CTkEntry(self.frame_buscar, placeholder_text="Buscar", width=400)
        self.entry_buscar_venta.grid(row=0, column=0, padx=5, pady=(10, 0))

        self.search_icon = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "search.png")), size=(20, 20))

        self.btn_buscar = ctk.CTkButton(self.frame_buscar, text="", width=20,cursor="hand2", image=self.search_icon, command=buscar_venta)
        self.btn_buscar.grid(row=0, column=1, padx=5, pady=10)


#------------------------------------------------------------------------------------------------------------------

        self.tablaventas = ttk.Treeview(self.cuarto_frame)
        self.tablaventas["columns"] = ("N° de compra", "Nombre y Apellido", "Prendas Compradas", "Método de pago", "Entregó", "Cuotas", "Total", "Total final") 
        self.tablaventas.heading("#0", text="")
        self.tablaventas.column("#0", width=0, stretch=tk.NO)

        self.tablaventas.heading("#1", text="N° de compra")
        self.tablaventas.column("#1", width=100, minwidth=100, stretch="no")

        self.tablaventas.heading("#2", text="Nombre y Apellido")
        self.tablaventas.column("#2", width=120, minwidth=120, stretch="no")

        self.tablaventas.heading("#3", text="Prendas Compradas")
        self.tablaventas.column("#3", width=120, minwidth=120, stretch="no")

        self.tablaventas.heading("#4", text="Método de pago")
        self.tablaventas.column("#4", width=120, minwidth=120, stretch="no")

        self.tablaventas.heading("#5", text="Entregó")
        self.tablaventas.column("#5", width=120, minwidth=120, stretch="no")

        self.tablaventas.heading("#6", text="Cuotas")
        self.tablaventas.column("#6", width=120, minwidth=120, stretch="no")

        self.tablaventas.heading("#7", text="Total")
        self.tablaventas.column("#7", width=120)

        self.tablaventas.heading("#8", text="Total Final")
        self.tablaventas.column("#8", width=120)

        self.tablaventas.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        actualizar_tabla_ventas()

        #FRAME proovedor
        self.quinto_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.quinto_frame.grid(row=1, column=0, padx=20, pady=10)

        self.btn_agregar_proveedor = ctk.CTkButton(self.quinto_frame, text="Registrar Proovedor", command= Abrir_Registrar_Proveedor)
        self.btn_agregar_proveedor.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.btn_eliminar_proveedor = ctk.CTkButton(self.quinto_frame, text="Eliminar Proovedor", command=Abrir_Eliminar_Proovedor)
        self.btn_eliminar_proveedor.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        self.btn_actualizar_tabla_proo = ctk.CTkButton(self.quinto_frame, text="Actualizar Tabla", command=actualizar_tabla_proovedor)
        self.btn_actualizar_tabla_proo.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")

        #--------------------------------------------Buscar-----------------------------------------------------------------

        self.frame_buscar = ctk.CTkFrame(self.quinto_frame)
        self.frame_buscar.grid(row=0, column=3, padx=5, pady=10, sticky="nsew")

        self.entry_buscar_proovedor = ctk.CTkEntry(self.frame_buscar, placeholder_text="Buscar", width=400)
        self.entry_buscar_proovedor.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="nsew")

        self.search_icon = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "search.png")), size=(20, 20))

        self.btn_buscar = ctk.CTkButton(self.frame_buscar, text="", width=20,cursor="hand2", image=self.search_icon, command=buscar_proovedor)
        self.btn_buscar.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
        
        self.tablaproovedores = ttk.Treeview(self.quinto_frame)
        self.tablaproovedores["columns"] = ( "N° Proovedor", "Nombre", "Apellido", "Empresa", "N° de teléfono", "Tipo de producto", "Marca") 
        self.tablaproovedores.heading("#0", text="")
        self.tablaproovedores.column("#0", width=0, stretch=tk.NO)

        self.tablaproovedores.heading("#1", text="N° Proovedor")
        self.tablaproovedores.column("#1", width=100, minwidth=100, stretch="no")

        self.tablaproovedores.heading("#2", text="Nombre")
        self.tablaproovedores.column("#2", width=100, minwidth=120, stretch="no")

        self.tablaproovedores.heading("#3", text="Apellido")
        self.tablaproovedores.column("#3", width=120, minwidth=120, stretch="no")

        self.tablaproovedores.heading("#4", text="Empresa")
        self.tablaproovedores.column("#4", width=120, minwidth=120, stretch="no")

        self.tablaproovedores.heading("#5", text="N° de teléfono")
        self.tablaproovedores.column("#5", width=120, minwidth=120, stretch="no")

        self.tablaproovedores.heading("#6", text="Tipo de producto")
        self.tablaproovedores.column("#6", width=120, minwidth=120, stretch="no")

        self.tablaproovedores.heading("#7", text="Marca")
        self.tablaproovedores.column("#7", width=120)

        self.tablaproovedores.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ns")

        basedatos = pmydb = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
        fcursor = basedatos.cursor()

        fcursor.execute("SELECT id_proovedor, nombre, apellido, empresa, num_telefono, tipo_producto, marca FROM proovedores")
        rows = fcursor.fetchall()

        for row in rows:
            self.tablaproovedores.insert("","end",values=row)



            




        # FRAME PREDETERMINADO
        self.select_frame_by_name("clientes")

        self.root.mainloop()
    
    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.clientes_button.configure(fg_color=("gray75", "gray25") if name == "clientes" else "transparent")
        self.stock_button.configure(fg_color=("gray75", "gray25") if name == "stock" else "transparent")
        self.ventas_button.configure(fg_color=("gray75", "gray25") if name == "ventas" else "transparent")
        self.proveedor_button.configure(fg_color=("gray75", "gray25") if name == "proveedor" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "clientes":
            self.segundo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.segundo_frame.grid_forget()
        if name == "stock":
            self.tercer_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.tercer_frame.grid_forget()
        if name == "ventas":
            self.cuarto_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.cuarto_frame.grid_forget()
        if name == "proveedor":
            self.quinto_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.quinto_frame.grid_forget()



    def home_button_event(self):
        self.select_frame_by_name("home")

    def clientes_button_event(self):
        self.select_frame_by_name("clientes")

    def stock_button_event(self):
        self.select_frame_by_name("stock")
    
    def ventas_button_event (self):
        self.select_frame_by_name("ventas")

    def proveedores_button_event (self):
        self.select_frame_by_name("proveedor")

ventana_iniciar = VentanaMenu()