import sys
import os
import datetime
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
import importlib



from ui_functions.mail_ui_functions import update_preview_mail
from contact_functions.gs_contact_manager import get_sheet_names,get_data_dict
from ui_functions.color_theme import theme_dark,theme_light
from contact_functions.mail_sender_function import send_mail



class KanaMail(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    name = "K-Mail"
    version = " 1.2"

    def initUI(self):
        self.create_widgets()
        self.setup_layout()
        self.connection_to_functions()
        self.set_style_frame()
        self.set_default_styleSheet()
        self.setWindowTitle(self.name + self.version)

    def create_widgets(self) :

        # --- LAYOUTS
        self.main_layout = QVBoxLayout()
        self.inner_layout = QHBoxLayout()
        self.customization_layout = QVBoxLayout()
        self.preview_main_layout = QVBoxLayout()

        # --- WIDGET top_layout
        self.top_frame = QFrame()
        self.top_layout = QVBoxLayout()
        self.title = QLabel()
        self.title.setText("K-MAIL" + self.version)
        self.title.setStyleSheet("font-size : 40px;")
        self.title.setAlignment(Qt.AlignCenter)

        # --- WIDGETS customization_layout
        self.receivers_dropdown = QComboBox()
        self.receiver_items = self.update_receiver_items()
        self.receivers_dropdown.addItems(self.receiver_items)
        self.title_input = QLineEdit()
        self.content_greetings_input = QTextEdit()
        self.content_input = QTextEdit()
        self.content_question_input = QTextEdit()
        self.signature_input = QComboBox()
        self.signature_input.addItems(["Liam", "Tof", "Boris", "Lucas"])
        self.picture_input = QLineEdit()
        self.button_text_input = QLineEdit()
        self.button_link_input = QLineEdit()

        # --- WIDGETS text_preview_layout
        self.text_preview_frame = QFrame()
        self.text_preview_layout = QVBoxLayout()
        self.text_preview_infos = QLabel()
        self.update_text_preview()
        self.text_preview_infos.setAlignment(Qt.AlignCenter)
        self.text_preview_title = QLabel()
        self.update_title_mail()
        self.text_preview_title.setAlignment(Qt.AlignCenter)

        # --- WIDGETS preview_layout
        self.preview_frame = QFrame()
        self.preview_layout = QVBoxLayout()
        self.web_view = QWebEngineView()

        # --- WIDGETS button_send_layout
        self.button_send_layout = QVBoxLayout()
        self.button_send = QPushButton('📨 ENVOYER K-MAIL 📨')
        self.button_send.setStyleSheet('font-size : 20px;')

        # --- WIDGET dark_mode_switch
        self.dark_mode_switch = QCheckBox('MODE SOMBRE 💀')


    def setup_layout(self) :
        # --- SET LAYOUT top_layout
        self.top_frame.setLayout(self.top_layout)
        self.top_layout.addWidget(self.title)
        # --- SET LAYOUT customization_layout
        self.customization_layout.addWidget(self.dark_mode_switch)
        self.customization_layout.addWidget(QtWidgets.QLabel('Séléctionner les destinataires :'))
        self.customization_layout.addWidget(self.receivers_dropdown)
        self.customization_layout.addWidget(QtWidgets.QLabel('Objet du Mail :'))
        self.customization_layout.addWidget(self.title_input)
        self.customization_layout.addWidget(QtWidgets.QLabel('Complément de salutations :'))
        self.customization_layout.addWidget(self.content_greetings_input)
        self.customization_layout.addWidget(QtWidgets.QLabel('Contenu du Mail :'))
        self.customization_layout.addWidget(self.content_input)
        self.customization_layout.addWidget(QtWidgets.QLabel('Question :'))
        self.customization_layout.addWidget(self.content_question_input)
        self.customization_layout.addWidget(QtWidgets.QLabel('Signature :'))
        self.customization_layout.addWidget(self.signature_input)
        self.customization_layout.addWidget(QtWidgets.QLabel('Lien Image ( Imgur ) :'))
        self.customization_layout.addWidget(self.picture_input)
        self.customization_layout.addWidget(QtWidgets.QLabel('Texte du bouton :'))
        self.customization_layout.addWidget(self.button_text_input)
        self.customization_layout.addWidget(QtWidgets.QLabel('Lien du bouton :'))
        self.customization_layout.addWidget(self.button_link_input)

        # --- SET LAYOUT preview_layout
        self.text_preview_layout.addWidget(self.text_preview_infos)
        self.text_preview_layout.addWidget(self.text_preview_title)
        self.text_preview_frame.setLayout(self.text_preview_layout)
        self.preview_layout.addWidget(self.web_view)
        self.preview_frame.setLayout(self.preview_layout)

        self.preview_main_layout.addWidget(self.text_preview_frame)
        self.preview_main_layout.addWidget(self.preview_frame)

        self.customization_layout.addWidget(self.receivers_dropdown)

        # --- SET LAYOUT inner_layout
        self.inner_layout.addLayout(self.customization_layout)
        self.inner_layout.addLayout(self.preview_main_layout)

        # --- SET LAYOUT button_send_layout
        self.button_send_layout.addWidget(self.button_send)

        # --- SET LAYOUT main_layout
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addLayout(self.inner_layout)
        self.main_layout.addLayout(self.button_send_layout)
        self.setLayout(self.main_layout)

    def set_default_styleSheet(self):
        self.setStyleSheet("font-size: 16px; font-family: Quicksand;")

    def toggle_dark_mode(self):
        if self.dark_mode_switch.isChecked():
             self.old_styleSheet = self.styleSheet()
             self.new_styleSheet = f"background-color: {theme_dark["dark"]}; color:{theme_dark["light_grey"]};"
             self.setStyleSheet(self.old_styleSheet + self.new_styleSheet)
        else:
            self.set_default_styleSheet()

    def set_style_frame(self) :
        # --- STYLE text_preveiw_frame
        self.text_preview_frame.setMaximumHeight(100)

    def connection_to_functions(self):
        # --- CONNECTION customization_layout
        self.dark_mode_switch.clicked.connect(self.toggle_dark_mode)
        self.receivers_dropdown.currentIndexChanged.connect(self.update_preview)
        self.receivers_dropdown.currentIndexChanged.connect(self.update_text_preview)
        self.title_input.textChanged.connect(self.update_preview)
        self.title_input.textChanged.connect(self.update_title_mail)
        self.content_greetings_input.textChanged.connect(self.update_preview)
        self.content_input.textChanged.connect(self.update_preview)
        self.content_question_input.textChanged.connect(self.update_preview)
        self.signature_input.currentIndexChanged.connect(self.update_preview)
        self.picture_input.textChanged.connect(self.update_preview)
        self.button_text_input.textChanged.connect(self.update_preview)
        self.button_link_input.textChanged.connect(self.update_preview)
        self.button_send.clicked.connect(self.send_mail)



        # --- Set initial preview
        self.update_preview()

    def update_preview(self):
        html_content = update_preview_mail(
            self.receivers_dropdown,
            self.title_input,
            self.content_greetings_input,
            self.content_input,
            self.content_question_input,
            self.signature_input,
            self.picture_input,
            self.button_text_input,
            self.button_link_input,
            self.web_view
        )
        self.web_view.setHtml(html_content)
        return html_content   

    def update_text_preview(self):
        receiver_list = get_data_dict(self.receivers_dropdown.currentText())
        self.text_var = f"Ce message est envoyé à {len(receiver_list)} personnes qui sont dans la catégorie {self.receivers_dropdown.currentText()}. \n \n"
        self.text_preview_infos.setText(self.text_var)

    def update_title_mail(self):
        self.text_title = f"Objet du mail : {self.title_input.text()}"
        self.text_preview_title.setText(self.text_title)

    def update_receiver_items(self):
        self.receiver_group = get_sheet_names()
        self.removed_list = ['DATA_LIEUX','DATA_FESTIVALS','DATA_PRESSE','DATA_TEST','_OLD_LIEUX','_OLD_FESTIVALS','_OLD_VILLES','_OLD_TREMPLINS','_OLD_GROUPES','_OLD_AUTRES']
        self.good_receiver_items = [item for item in self.receiver_group if item not in self.removed_list] 
        return self.good_receiver_items
    
    def send_mail(self):
        html_content = self.update_preview()
        #print(html_content)
        receiver_list = get_data_dict(self.receivers_dropdown.currentText())
        print(receiver_list)
        send_mail(receiver_list,html_content)
        self.show_email_sent_message()

    def show_email_sent_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("K-Mail Envoyé")
        msg.setText("Les Mails ont tous été envoyés, tu peux fermer le K-Mail !")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
