import tkinter as tk 

class Ventana(tk.Frame):

        def __init__(self,parent=None):
           
            self.master=parent          
            super().__init__(self.master)        
         
            self._ancho=self.winfo_screenwidth()
            self._alto=self.winfo_screenheight()
            self.master.geometry(f"{self._ancho}x{self._alto}")
        #creamos un objeto de Degradado
            self.d1=Degradado(self.master,ancho=self._ancho+1)
            self.d1.place(x=-1,y=-1,width=self._ancho+2,height=400)
        #añadimos un boton sencillo (yo uso tk pero use ttk recomendable)
        #con self.d1 hacemos que el boton pertenezca al canvas (d1)
            btn=tk.Button(self.d1,text="inicio")
            btn.place(x=100,y=100,width=150,height=70)
        #añadimos otro degradado
            self.d2=Degradado(self.master,color1="green",color2="#CCAA14",ancho=self._ancho+1,alto=400)
            self.d2.place(x=300,y=500,width=self._ancho/4,height=400)
        
class Degradado(tk.Canvas):
        
        def __init__(self,parent,color1="red4",color2="red",ancho=500,alto=400):
            tk.Canvas   .__init__(self,parent,background="white")
            self.color1=color1
            self.color2=color2
            self.__ancho=ancho
            self.__alto=alto       
            self.dibujarDegradado()
       
        def dibujarDegradado(self):
            
        
            (r_1,g_1,b_1)=self.winfo_rgb(self.color1)
            (r_2,g_2,b_2)=self.winfo_rgb(self.color2)
            constR=(r_2-r_1)/(self.__alto-1)
            constG=(g_2-g_1)/(self.__alto-1)
            constB=(b_2-b_1)/(self.__alto-1)

            for i in range(self.__alto):
                r=int(r_1+(constR*i))
                g=int(g_1+(constG*i))
                b=int(b_1+(constB*i))
                color="#%04x%04x%04x"%(r,g,b) 
                self.create_line(0,i,self.__ancho,i,fill=color)    
            
                    

if __name__=="__main__":
    root=tk.Tk()
    app=Ventana(parent=root)
    app.mainloop()
