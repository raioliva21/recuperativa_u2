import numbers
import gi
from regex import P
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.list_text = []
        self.count = 0
        self.set_border_width(10)
        self.set_default_size(400, 100)

        HB = Gtk.HeaderBar()
        HB.set_show_close_button(True)
        HB.props.title = "PROGRAMACION AVANZADA"
        self.set_titlebar(HB)

        self.button_about = Gtk.Button.new_from_icon_name(
            "gtk-about", Gtk.IconSize.MENU)
        #self.button_about.connect("clicked", self.button_about_clicked)
        HB.pack_start(self.button_about)

        label1 = Gtk.Label(label="Texto 1")
        entry1 = Gtk.Entry()
        label2 = Gtk.Label(label="Texto 2")
        entry2 = Gtk.Entry()
        label3 = Gtk.Label(label="Resultado")
        self.entry3 = Gtk.Entry()
        reset_button = Gtk.Button(label="Reiniciar")
        acept_button = Gtk.Button(label="Aceptar")
        save_button = Gtk.Button(label="Guardar")

        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        
        box = self.create_box(label1, label2, label3)
        row_1 = Gtk.ListBoxRow()
        row_1.add(box)
        self.listbox.add(row_1)

        self.box = self.create_box(entry1,entry2,self.entry3)
        row_2 = Gtk.ListBoxRow()
        row_2.add(self.box)
        self.listbox.add(row_2)
        
        box = self.create_box(reset_button,acept_button,save_button)
        row_3 = Gtk.ListBoxRow()
        row_3.add(box)
        self.listbox.add(row_3)

        self.add(self.listbox)
        self.list_text = []

        reset_button.connect("clicked", self.reset_button_clicked)
        acept_button.connect("clicked", self.accept_button_clicked)
        save_button.connect("clicked", self.save_button_clicked)
    
        self.connect("destroy", Gtk.main_quit)

        self.show_all()
    
    def create_box(self,widget1,widget2,widget3):
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box.set_homogeneous(True) 
        box.pack_start(widget1, True, True, 0)
        box.pack_start(widget2, True, True, 0)
        box.pack_start(widget3, True, True, 0)

        return box
    
    def get_sum(self):

        self.count = 0
        for text in self.list_text:
            if text.isdigit() == False:
                print("texto", text, "no es numerico")
                text = text.upper()
                if 'A' in text:
                    self.count = self.count + 1
                if 'E' in text:
                    self.count = self.count + 1
                if 'I' in text:
                    self.count = self.count + 1
                if 'O' in text:
                    self.count = self.count + 1
                if 'U' in text:
                    self.count = self.count + 1
            else:
                print("texto", text, "es numerico")
                self.count = self.count + int(text)

        self.entry3.set_text(f"{self.count}")
                

    def reset_button_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.OK_CANCEL,
            text="¡ADVERTENCIA!",
        )
        dialog.format_secondary_text(
            "Texto ingresado sera borrado ¿Deseas continuar con operacion?"
        )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Boton 'OK' ha sido presionado; se borrara texto no guardado.")
            for entry in self.box:
                entry.set_text("")
        elif response == Gtk.ResponseType.CANCEL:
            print("Boton 'CANCEL' ha sido presionado; se cancela operacion.")

        dialog.destroy()

    def accept_button_clicked(self, widget):

        self.list_text = []
        for text in self.box:
            self.list_text.append(text.get_text())
        del self.list_text[-1]

        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Mensaje Informativo",
        )
        dialog.format_secondary_text(
            f"Texto 1: {self.list_text[0]}"
            f"\nTexto 2: {self.list_text[1]}"
        )
        dialog.run()
        self.get_sum()
        dialog.destroy()

    def save_button_clicked(self, widget):

        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.SAVE
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE,
            Gtk.ResponseType.OK,
        )

        #self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            # Appending to file
            with open("pavanzada.txt", 'a') as file1:
                file1.write(self.entry3.get_text()+"\n")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()



win = GridWindow()
Gtk.main()