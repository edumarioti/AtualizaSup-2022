#-------------------------------------------------------------------------------
#
# By: Eduardo Marioti Vargas
# Project made with: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
#-------------------------------------------------------------------------------

# Import Modules
import shutil, sys, os

# Import Qt
from qt_core import *

# Import Windows 
from windows.ui_main_window import Ui_MainWindow

NORMAL = 0
WARNING = 1
SUCCESS = 2



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AtualizaSup")
        self.setWindowIcon(QIcon("gui/images/logo/logo-2000px-2000px.png"))
        
        # Setup main window
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        # Show First Page
        self.show_page_home()

        self.show_button_update()

        # ------------------------------ Buttons Left Menu ---------------------------------
        # Toggle menu
        self.ui.toggle_button.clicked.connect(self.animation_toggle_menu)

        # Button home
        self.ui.button_home.clicked.connect(self.show_page_home)

        # Button link
        self.ui.button_settings.clicked.connect(self.show_page_link)

        # Button home
        self.ui.button_about.clicked.connect(self.show_page_settings)

        # ------------------------------ Buttons Update -----------------------------------

        # Button Update All
        self.ui.ui_pages.check_uptade_all.clicked.connect(self.enable_disable_other_options)

        self.ui.ui_pages.button_uptade.clicked.connect(self.show_confirmation_message)

        self.ui.ui_pages.button_cancel_uptade.clicked.connect(self.show_button_update)

        self.ui.ui_pages.button_confirm_uptade.clicked.connect(self.select_folders_for_copy)

        # ------------------------------ Buttons Settings ----------------------------------

        # Button save settings
        self.ui.ui_pages.button_save.clicked.connect(self.save_links)


        # ------------------------------ Show aplication ----------------------------------
        self.show()

    def enable_disable_other_options(self):
        checked = self.ui.ui_pages.check_uptade_all.isChecked()

        self.ui.ui_pages.check_datalog.setDisabled(checked)
        self.ui.ui_pages.check_gfx.setDisabled(checked)
        self.ui.ui_pages.check_tag.setDisabled(checked)
        self.ui.ui_pages.check_users.setDisabled(checked)
    
    def show_confirmation_message(self):

        self.ui.ui_pages.button_uptade.setHidden(True)
        self.ui.ui_pages.frame_confirmation.setHidden(False)
    
    def show_button_update(self):
        self.ui.ui_pages.button_uptade.setHidden(False)
        self.ui.ui_pages.frame_confirmation.setHidden(True)


    def reset_selection_left_menu(self):
        for button in self.ui.left_menu.findChildren(QPushButton):
            try:
                button.set_active(False)
            except:
                pass
    
    def show_page_home(self):
        self.reset_selection_left_menu()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_home)
        self.ui.top_left_label.setText("| PÁGINA INICIAL")
        self.ui.button_home.set_active(True)

    def show_page_link(self):
        self.reset_selection_left_menu()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_settings)
        self.ui.top_left_label.setText("| CONFIGURAÇÕES")
        self.ui.button_settings.set_active(True)

    def show_page_settings(self):
        self.reset_selection_left_menu()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_about)
        self.ui.top_left_label.setText("| SOBRE")
        self.ui.button_about.set_active(True)

    def animation_toggle_menu(self):

        # get width left menu
        menu_width = self.ui.left_menu.width()

        new_width = self.ui.left_menu_standard_width
        if menu_width == self.ui.left_menu_standard_width:
            new_width = self.ui.left_menu_extend_width
        
        # Animation
        self.animation_menu = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation_menu.setStartValue(menu_width)
        self.animation_menu.setEndValue(new_width)
        self.animation_menu.setDuration(500)
        self.animation_menu.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation_menu.start()

    def save_links(self):

        source = self.ui.ui_pages.line_edit_source.text()
        destination = self.ui.ui_pages.line_edit_destination.text()
        
        uninformed_paths = len(source) == 0 or len(destination) == 0

        source_not_found = not os.path.exists(source)

        if uninformed_paths:
            self.message_in_bottom_bar("Verifique o preenchimento dos campos", WARNING)

        elif source_not_found:
            self.message_in_bottom_bar("Origem não encontrada! Verifique o preenchimento dos campos", WARNING)
    
        else:
            with open("file_settings.txt", "w", encoding = "utf-8")as file_settings:
                file_settings.write(source + "\n" + destination)
                

            self.message_in_bottom_bar("Endereços salvos com sucesso!", SUCCESS)
                


    def select_folders_for_copy(self):
        
        with open("file_settings.txt", "r", encoding = "utf-8") as file_settings:
            source = file_settings.readline().strip()
            destination  = file_settings.readline().strip()
        
        uninformed_paths = len(source) == 0 or len(destination) == 0

        source_not_found = not os.path.exists(source)

        if uninformed_paths:
            self.message_in_bottom_bar("Verifique o preenchimento dos campos", WARNING)

        elif source_not_found:
            self.message_in_bottom_bar("Origem não encontrada! Verifique o preenchimento dos campos", WARNING)
       
        else:

            update_all_is_checked = self.ui.ui_pages.check_uptade_all.isChecked()
            gfx_is_checked = self.ui.ui_pages.check_gfx.isChecked()
            datalog_is_checked = self.ui.ui_pages.check_datalog.isChecked()
            tag_is_checked = self.ui.ui_pages.check_tag.isChecked()
            users_is_checked = self.ui.ui_pages.check_users.isChecked()

            no_option_selected = not (update_all_is_checked or gfx_is_checked or datalog_is_checked or tag_is_checked or users_is_checked)
            
            if no_option_selected: 
                self.message_in_bottom_bar("Selecione pelo menos uma opção!", WARNING)
                self.show_button_update()
            else:
                if update_all_is_checked:
                    self.copy_subfolders_and_files(source, destination)
        

    def copy_subfolders_and_files(self, source_path, destination_path):
        
        
        items_for_transfer = list()

        # Lista os caminho, as subpastas e aquivos da origem
        for path, subfolders, files in os.walk(source_path):
            
            # Nome da subpastas no destino
            path_of_destination_file = path.replace(source_path, destination_path)

            # Cria a subpasta se necessário no destino
            if not os.path.exists(path_of_destination_file):
                os.mkdir(path_of_destination_file)
            
            for file in files:

                # Get path from each file in souce and destination
                source = os.path.join(os.path.realpath(path), file)
                destination = source.replace(source_path, destination_path)
                
                items_for_transfer.append([source, destination])
                
        # Numero total de arquivos
        total_files = len(items_for_transfer)

        self.chage_bottom_label_in_progress_bar()

        # Copia ou substitui cada arquivo da lista para o destino
        for actual_number, files in enumerate(items_for_transfer):

            souce_file, destination_file = files

            if os.path.exists(destination_file):
                os.remove(destination_file)

            shutil.copy2(souce_file, destination_file)

            percentage_of_completion = int(actual_number * 100 / total_files)

            self.ui.bottom_progress_bar.setValue(percentage_of_completion)
        
        self.message_in_bottom_bar("Atualização concluida!", SUCCESS)
        self.return_standard_options()

    
    def message_in_bottom_bar(self, message, type=NORMAL):

        self.change_progress_bar_in_bottom_label()

        if type == WARNING:
            self.ui.bottom_left_label.setStyleSheet("font: 10pt 'Consolas'; color: red")
        elif type == SUCCESS:
            self.ui.bottom_left_label.setStyleSheet("font: 10pt 'Consolas'; color: #6EF0D2")
        else:
            self.ui.bottom_left_label.setStyleSheet("font: 10pt 'Consolas'; color: #D0D0D0")

        self.ui.bottom_left_label.setText(message)


    def change_progress_bar_in_bottom_label(self):
        self.ui.bottom_progress_bar.hide()
        self.ui.bottom_left_label.show()
    

    def chage_bottom_label_in_progress_bar(self):
        self.ui.bottom_left_label.hide()
        self.ui.bottom_progress_bar.show()

    
    def return_standard_options(self):

        self.ui.ui_pages.check_datalog.setChecked(False)
        self.ui.ui_pages.check_gfx.setChecked(False)
        self.ui.ui_pages.check_tag.setChecked(False)
        self.ui.ui_pages.check_uptade_all.setChecked(False)
        self.ui.ui_pages.check_users.setChecked(False)

        self.show_button_update()
        self.enable_disable_other_options()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

