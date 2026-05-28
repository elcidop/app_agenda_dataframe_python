from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import logging
import logging.config


logging.config.fileConfig('logging.conf')
# Obtener un logger
logger = logging.getLogger('sampleLogger')

#PARTE I FUNCIONALIDAD DEL APLICATIVO
__agenda=pd.read_csv('contactos.csv',encoding='utf-8')
logger.debug(__agenda)


def __guardar_contacto():
    global __agenda
    #Validaciones
    if e_nombre.get().strip()=='':
       return messagebox.showerror('Formulario de Creación','El campo Nombre es obligatorio')
    
    if e_apellidos.get().strip()=='':
       return messagebox.showerror('Formulario de Creación','El campo Apellidos es obligatorio')
       
    if e_telefono.get().strip()=='':
       return messagebox.showerror('Formulario de Creación','El campo Teléfono es obligatorio')
   
    if not e_telefono.get().isnumeric():
       return messagebox.showerror('Formulario de Creación','El campo Teléfono debe ser numerico')
    if e_codpostal.get().strip()!='' and not e_codpostal.get().isnumeric():
       return messagebox.showerror('Formulario de Creación','El campo Código Postal debe ser numerico')
    
     
    if e_id.get():
        #UNA FORMA: ACTUALIZANDO LA FILA
        item_seleccionado = t_listado_contactos.selection()
        indice_a_editar = t_listado_contactos.index(item_seleccionado)
        
        logger.debug('indice a editar:')
        logger.debug(indice_a_editar)
        logger.debug('item_seleccionado:')
        logger.debug(item_seleccionado)
        logger.debug('__agenda inicial: ')
        logger.debug(__agenda)

        #CUIDADIN¡¡ DEBE COINCIDIR LA POSICION DE LA FILA EN EL TREEVIEW(indice_a_editar) CON EL INDICE DEL DATAFRAME
        
        cod_postal = None if e_codpostal.get().strip()=='' else int(e_codpostal.get())
        datos_actualizados = [int(e_id.get()), e_nombre.get(), e_apellidos.get(), int(e_telefono.get()), e_fec_nacimiento.get(), e_direccion.get(), cod_postal]        
        __agenda.loc[indice_a_editar, :] = datos_actualizados

        logger.debug('indice_a_editar:')
        logger.debug(indice_a_editar)       
        
        # item_id = t_listado_contactos.get_children()[indice_a_editar]
        # t_listado_contactos.item(item_id, values=datos_actualizados)
        
        # logger.debug('item_id:')
        # logger.debug(item_id)

        logger.debug('__agenda final: ')
        logger.debug(__agenda) 


        
        #OTRA FORMA: Eliminamos y creamos la fila del contacto
        # id_contacto=int(e_id.get())
        # logger.debug('id_contacto:')
        # logger.debug(id_contacto)
        # logger.debug('Agenda INICIAL:')
        # logger.debug(__agenda)
        # #Eliminamos la fila del contacto
        # df_seleccionado=__agenda[__agenda["id"] == id_contacto]
        # logger.debug('DataFrame Seleccionado:')
        # logger.debug(df_seleccionado)
        # indice=df_seleccionado.index[0]
        # __agenda=__agenda.drop(indice)
        # logger.debug('Agenda SIN CONTACTO:')
        # logger.debug(__agenda)
        # #Creamos la fila del contacto
        # #fecha = datetime.strptime(e_fec_nacimiento.get(), "%d/%m/%Y").date()
        # __agenda.loc[indice]=[id_contacto,
        #                              e_nombre.get(),
        #                              e_apellidos.get(),
        #                              int(e_telefono.get()),
        #                              e_fec_nacimiento.get(),
        #                              e_direccion.get(),
        #                              int(e_codpostal.get())]
        # logger.debug('Agenda CON EL NUEVO CONTACTO')
        # logger.debug(__agenda)
        # __agenda=__agenda.sort_index()

    else:
     #el indice máximo que tenemos
     id_contacto=__agenda['id'].max()+1
     cod_postal = None if e_codpostal.get().strip()=='' else int(e_codpostal.get())
     __agenda.loc[len(__agenda)]=[id_contacto,
                                     e_nombre.get(),
                                     e_apellidos.get(),
                                     int(e_telefono.get()),
                                     e_fec_nacimiento.get(),
                                     e_direccion.get(),
                                     cod_postal]
     logger.debug('Agenda CON EL NUEVO CONTACTO')
     logger.debug(__agenda)
     __agenda=__agenda.sort_index()
              
    
    __limpiar_form_contacto()
    __actualizar_listado()
    messagebox.showinfo('Formulario de Contacto','El contacto se ha guardado')

def __limpiar_form_contacto():
    #borramos el texto de cada una de las Entry del formulario
    e_id.delete(0,"end") 
    e_nombre.delete(0,"end") 
    e_apellidos.delete(0,"end")
    e_telefono.delete(0,"end")
    e_fec_nacimiento.delete(0,"end")
    e_direccion.delete(0,"end")
    e_codpostal.delete(0,"end")

    e_nombre.focus()
  
   
def __actualizar_listado():
    #Primero quito los seleccionados
    seleccionados=t_listado_contactos.selection()
    if seleccionados:
        t_listado_contactos.selection_remove(seleccionados)

    #Despues limpiamos el t_listado de contactos
    for i_contacto in t_listado_contactos.get_children():
        t_listado_contactos.delete(i_contacto)
    #Inserto una fila por cada contacto que tengo en la agenda (DataFrame)
    for _, row in __agenda.iterrows(): 
        datos=[row['id'],row['nombre'],row['apellidos'],row['telefono']] 
        t_listado_contactos.insert("", "end", values=datos)
        

def __cargar_datos_contacto():
    #Conseguir el id del contacto desde el elemento seleccionado del TreeView(t_listado_contactos)
    seleccionados=t_listado_contactos.selection() #Devuelve una tupla con el codigo interno del TreeView de la fila ('I0001',)
   #Conseguimos el diccionario de la fila del primer valor de la tupla que es el identificador interno 'I0001'
    dict_item = t_listado_contactos.item(seleccionados[0]) 
    #Lista de valores de la fila seleccionada del listado contactos, mediante la clave 'values' en el diccionario de la fila
    lista_valores=dict_item['values'] 
    logger.debug(f'lista_valores seleccionados del TreeView: {lista_valores}')
    id_contacto=lista_valores[0]
    #Recuperar toda la información del contacto para colocarla en el formulario de contacto
    e_id.delete(0,"end")
    e_id.insert(0,id_contacto)
    
    row=__agenda.loc[__agenda['id'] == id_contacto].iloc[0] #Conseguimos la fila de agenda(DataFrame) por el id
    e_nombre.delete(0,"end")
    e_nombre.insert(0,row['nombre'])
    e_apellidos.delete(0,"end")
    e_apellidos.insert(0,row['apellidos'])
    e_telefono.delete(0,"end")
    e_telefono.insert(0,row['telefono'])
    e_fec_nacimiento.delete(0,"end")
    if row['fec_nacimiento']:
        e_fec_nacimiento.insert(0,str(row['fec_nacimiento']))
    e_direccion.delete(0,"end")
    e_direccion.insert(0,row['direccion'])
    e_codpostal.delete(0,"end")
    e_codpostal.insert(0,row['codpostal'])

   

  

def __eliminar_contacto():
    global __agenda
    seleccionados=t_listado_contactos.selection()
    posicion_fila = t_listado_contactos.index(seleccionados) 
    indice_dataframe=posicion_fila #COINCIDE EL INDICE DEL DATAFRAME CON LA POSICION DE LA FILA EN EL TREEVIEW
    
    __agenda=__agenda.drop(indice_dataframe)
    __agenda=__agenda.sort_index() #REESCRIBEN LOS INDICES DEL DATAFRAME
    __limpiar_form_contacto() #Limpiamos el formulario porque se ha seleccionado la información
    __actualizar_listado() #Actualizacion de la vista
    messagebox.showinfo('Contactos','El contacto se ha eliminado')
     
def pintar_pantalla():    
    root.mainloop()

def on_select_listado_contactos(event):
    __cargar_datos_contacto()
    return "break"

#PARTE II. CONFIGURACION DE LOS ELEMENTOS
root = tk.Tk()
root.title('Agenda de Contactos')
root.geometry('800x600+50+50')

fr_contacto=ttk.LabelFrame(root,text="Formulario de creación de Contacto")

e_id=ttk.Entry(fr_contacto,width=0)

l_nombre=ttk.Label(fr_contacto,text='Nombre:')
e_nombre=ttk.Entry(fr_contacto)

l_apellidos=ttk.Label(fr_contacto,text='Apellidos:')
e_apellidos=ttk.Entry(fr_contacto)

l_telefono=ttk.Label(fr_contacto,text='Telefono:')
e_telefono=ttk.Entry(fr_contacto)

l_fec_nacimiento=ttk.Label(fr_contacto,text='Fecha Nacimiento:')
e_fec_nacimiento=ttk.Entry(fr_contacto)

l_direccion=ttk.Label(fr_contacto,text='Dirección:')
e_direccion=ttk.Entry(fr_contacto)

l_codpostal=ttk.Label(fr_contacto,text='Código Postal:')
e_codpostal=ttk.Entry(fr_contacto)

b_limpiar=ttk.Button(fr_contacto,text="Reset",command=__limpiar_form_contacto)
b_guardar=ttk.Button(fr_contacto,text="Guardar",command=__guardar_contacto)

fr_listado_contactos=ttk.LabelFrame(root,text="Listado de Contactos")

t_listado_contactos = ttk.Treeview(fr_listado_contactos, columns=['id','nombre','apellidos','telefono'],
                    show="headings", height=8, selectmode="extended")
t_listado_contactos["displaycolumns"] = ("nombre", "apellidos","telefono")
#t_listado_contactos.heading('id', text='Id')
#t_listado_contactos.column('id', width=0) #Ponemos el ancho a 0 para ocultarla

t_listado_contactos.heading('nombre', text='Nombre')
t_listado_contactos.column('nombre', width=150, anchor="center")

t_listado_contactos.heading('apellidos', text='Apellidos')
t_listado_contactos.column('apellidos', width=150, anchor="center")

t_listado_contactos.heading('telefono', text='Teléfono')
t_listado_contactos.column('telefono', width=150, anchor="center")

sb_y = ttk.Scrollbar(fr_listado_contactos, orient="vertical",   command=t_listado_contactos.yview)
t_listado_contactos.configure(yscrollcommand=sb_y.set)

t_listado_contactos.bind("<ButtonRelease-1>",on_select_listado_contactos)




b_eliminar=ttk.Button(fr_listado_contactos,text="Eliminar",command=__eliminar_contacto)

root.after(0, __actualizar_listado) 

# PARTE III. VISUALIZACION DE LOS ELEMENTOS
fr_contacto.grid(row=0,column=0)


l_nombre.grid(row=2,column=0)
e_nombre.grid(row=2,column=1)
l_apellidos.grid(row=2,column=2)
e_apellidos.grid(row=2,column=3)
l_telefono.grid(row=2,column=4)
e_telefono.grid(row=2,column=5)
l_fec_nacimiento.grid(row=3,column=0)
e_fec_nacimiento.grid(row=3,column=1)
l_direccion.grid(row=3,column=2)
e_direccion.grid(row=3,column=3)
l_codpostal.grid(row=3,column=4)
e_codpostal.grid(row=3,column=5)
b_limpiar.grid(row=4,column=4)
b_guardar.grid(row=4,column=5)


fr_listado_contactos.grid(row=10,column=0)
t_listado_contactos.grid(row=11,column=0)
sb_y.grid(row=11,column=1,sticky='ns')
b_eliminar.grid(row=12,column=0)






if __name__=='__main__':
    pintar_pantalla()