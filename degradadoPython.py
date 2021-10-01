import tkinter as tk 

class Ventana(tk.Frame):

        def __init__(self,parent=None):
           
            self.master=parent          
            super().__init__(self.master)        
         
            self._ancho=self.winfo_screenwidth()
            self._alto=self.winfo_screenheight()
            self.master.geometry(f"{self._ancho}x{self._alto}")
                

if __name__=="__main__":
    root=tk.Tk()
    app=Ventana(parent=root)
    app.mainloop()
