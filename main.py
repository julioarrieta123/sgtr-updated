from tkinter import font
from typing import Optional, Tuple, Union
import customtkinter as ctk
import estilos
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import CTkImage
import os

carpeta_principal = os.path.dirname(__file__)

carpeta_imagen = os.path.join(carpeta_principal, "img")

class VentanaLogin():

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
        self.root.title("Iniciar Sesion")
        self.root.attributes('-fullscreen',True) 
		#-----------------------------------------------------------------
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
                messagebox.showinfo("Error", "Usuario y/o Contraseña Incorrecta")

            basedatos.close()
        
        def LoginARegristrar ():
            self.root.destroy()
            ventana_registrar = VentanaAdmin()
		
        entry_usuario = ctk.CTkEntry(self.root, placeholder_text="Ingrese Ususario",width=w/4, height=h/19)
        entry_usuario.pack(pady=10)
        entry_usuario.place(relx=0.68, rely=0.50)
		
        entry_constrasena = ctk.CTkEntry(self.root, placeholder_text="Ingrese Contraseña", show="*",width=w/4, height=h/19) 
        entry_constrasena.pack(pady=10)
        entry_constrasena.place(relx=0.68, rely=0.60)
	
        opciones=["Español", "Ingles"]
        cmbx_idioma = ctk.CTkComboBox(self.root, values=opciones, state="readonly", width=100)
        cmbx_idioma.set("idioma:")
        cmbx_idioma.place(x=685, y=10)
		
        self.img_entrar = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "logo_entrar.png")), size=(30, 30))

        boton_entrar= ctk.CTkButton(self.root, text="Entrar",width=w/4, height=h/19,
                                    cursor="hand2" , command=login_admin, image=self.img_entrar, compound="left")
        boton_entrar.pack(pady=20)
        boton_entrar.place(relx=0.68, rely=0.73)
		
        self.gregar_admin = ctk.CTkImage(Image.open(os.path.join(carpeta_imagen, "gregar_admin.png")), size=(30, 30))

        boton_registrar= ctk.CTkButton(self.root, text="Registrar Administrador", fg_color="#468189" ,width=w/4, height=h/19, 
                                       hover_color="#395462", cursor="hand2", image=self.gregar_admin, compound="left",command=LoginARegristrar)
        boton_registrar.pack(pady=0)
        boton_registrar.place(relx=0.68, rely=0.80)

        boton_salir= ctk.CTkButton(self.root, text="X", fg_color="Red",hover_color="#5e1914", cursor="hand2", 
                                   command=self.root.quit, width=30 , height=30, corner_radius=0)
        boton_salir.pack(pady=10, padx=10)
        boton_salir.place(x=w-30, y=0)

        boton_minimizar= ctk.CTkButton(self.root, text="-", font=("", 20), fg_color="#00a8f3",hover_color="#006593", cursor="hand2", 
                                   command=self.root.iconify, width=30 , height=30, corner_radius=0)
        boton_minimizar.pack(pady=10, padx=10)
        boton_minimizar.place(x=w-64, y=0)
        
		#----------------------------Imagen Login---------------------------------------

        
        img = Image.open(os.path.join(carpeta_imagen, "login_image.jpg"))
        img = img.resize((int(w/1.7),h))
        img_login = ImageTk.PhotoImage(img)
        img_login_lbl = ctk.CTkLabel(self.root, image=img_login, text="")
        img_login_lbl.pack()
        img_login_lbl.place(x=1, y=1)
		#-----------------------------imagen logo-------------------------------------------
        img = Image.open(os.path.join(carpeta_imagen, "logo_sgtr.png"))
        img = img.resize((int(w/4.5),int(h/3.5)))
        img_logo = ImageTk.PhotoImage(img)
        img_logo_lbl = ctk.CTkLabel(self.root, image=img_logo, text="")
        img_logo_lbl.pack()
        img_logo_lbl.place(relx=0.695, rely=0.15)
		
		#-----------------------------logo lenguaje---------------------
		
        

        #boton_admin=ctk.CTkButton(self.root, image=img_registrar_admin_tk, height="50", width="60", fg_color=estilos.background).place(x=410, y=290)

        self.root.mainloop()

class VentanaMenu():
    def __init__(self):
        super().__init__()

        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
		#---------------------Centrar-Ventana-----------------------------
        w = 800
        h = 349
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        w,h = ws,hs
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
        self.root.title("Menú")
        self.root.attributes('-fullscreen',True)
	    #self.root.iconbitmap("D:\\programacion IV\\proyecto final\\favicon.ico")
        self.navigation_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.navigation_frame.place(x=0, y=0)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)




        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        self.img_login = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_sgtr.png")), size=(100, 75))
        self.home_image = ctk.CTkImage(Image.open(os.path.join(image_path, "home_light.png")), size=(30, 30))
        self.client_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_clientes.png")), size=(30, 30))
        self.stock_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_stock.png")), size=(30, 30))

        img = Image.open(os.path.join(carpeta_imagen,"logo_lupa.png"))
        img = img.resize((20,20))
        lupa_img = ctk.CTkImage(img)
        img_lupa_lbl = ctk.CTkLabel(self.root, image=lupa_img, text="", fg_color="transparent",  bg_color="#2b2b2b")
        img_lupa_lbl.pack()
        img_lupa_lbl.place(x=10, rely=0.94)

        self.navigation_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(30, weight=2)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="", image=self.img_login,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=ws/15, pady=hs/40)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, font=ctk.CTkFont(size=15, weight="bold"),text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w")
        self.home_button.grid(row=1, column=0, sticky="ew")


        
        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,font=ctk.CTkFont(size=15, weight="bold"), text="Clientes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.client_image, anchor="w")
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, font=ctk.CTkFont(size=15, weight="bold"),text="Stock",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.stock_image, anchor="w")
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

    


        self.entry_buscar = ctk.CTkEntry(self.navigation_frame, placeholder_text="Buscar...",width=50, height=30)
        self.entry_buscar.grid(row=4, column=0, padx=(40, 10), pady=(440, 30), sticky="nsew")    

        boton_salir= ctk.CTkButton(self.root, text="X", fg_color="Red",hover_color="#5e1914", cursor="hand2", 
                                   command=self.root.quit, width=30 , height=30, corner_radius=0)
        boton_salir.grid(row=0, column=0, pady=10, padx=10)
        boton_salir.place(x=ws-30, y=0) 
		
        boton_minimizar= ctk.CTkButton(self.root, text="-", font=("", 20), fg_color="#00a8f3",hover_color="#006593", cursor="hand2", 
                                   command=self.root.iconify, width=30 , height=30, corner_radius=0)
        boton_minimizar.grid(row=0, column=0, pady=10, padx=10)
        boton_minimizar.place(x=w-64, y=0)

        # primer-frame
        self.home_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_lbl = ctk.CTkLabel(self.home_frame, text="Home", font=("bold", 15))
        self.home_lbl.grid(row=4, column=0, padx=20, pady=10)

        # segundo-frame
        self.segundo_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.segundo_frame.grid_columnconfigure(0, weight=1)

        self.clientes_lbl = ctk.CTkLabel(self.segundo_frame, text="Clientes", font=("bold", 15))
        self.clientes_lbl.grid(row=4, column=0, padx=20, pady=10)

        # tercer-frame
        self.tercer_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.tercer_frame.grid_columnconfigure(0, weight=1)

        self.stock_lbl = ctk.CTkLabel(self.tercer_frame, text="stock", font=("bold", 15))
        self.stock_lbl.grid(row=4, column=0, padx=20, pady=10)

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

            fcursor.execute(f"FROM Admin1 SELECT * WHERE Usuario = '{entry_usuario.get()}'")
            resultados = fcursor.fetchall()

            if resultados:
                messagebox.showinfo("Aviso", "Administrador ya registrado")
                print ("El dato ya se almacenó")
            else:
                sql=f"INSERT INTO Admin1 (Usuario, Mail, Contrasena) VALUES ('{entry_usuario.get()}','{entry_mail.get()}','{entry_constrasena.get()}')"
                fcursor.execute(sql)
                basedatos.commit()
                messagebox.showinfo("Registro", "Se registró el Administrador con éxito")
                print ("El dato no está almacenado")

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

ventana_iniciar = VentanaMenu()
