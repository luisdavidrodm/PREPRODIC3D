from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal

from malla_window.ui.malla_window_ui import Ui_malla_window


class MallaWindow(qtw.QDialog, Ui_malla_window):

    longitudes_actualizadas_signal = Signal(list)

    def __init__(self, config_manager):
        super().__init__()
        self.setupUi(self)
        self.ui = Ui_malla_window()
        self.config_manager = config_manager

        self.sb_dirx_numz.setMinimum(2)
        self.sb_dirx_numz.setMaximum(10)
        self.sb_diry_numz.setMinimum(2)
        self.sb_diry_numz.setMaximum(10)
        self.sb_dirz_numz.setMinimum(2)
        self.sb_dirz_numz.setMaximum(10)
        self.sb_dirtita_numz.setMinimum(2)
        self.sb_dirtita_numz.setMaximum(10)
        self.sb_dirr_numz.setMinimum(2)
        self.sb_dirr_numz.setMaximum(10)
        self.sb_dirzcil_numz.setMinimum(2)
        self.sb_dirzcil_numz.setMaximum(10)

        self.cb_tipocoord.currentTextChanged.connect(self.changeZonas)
        self.cb_tipozonas.currentTextChanged.connect(self.changeZonas)

        self.cb_tipocoord.currentTextChanged.connect(self.on_coordinate_system_changed)

        self.cb_tipozonas.currentTextChanged.connect(self.on_zones_system_changed)

        self.le_xlon.textChanged.connect(self.actualizar_longitudes)
        self.le_ylon.textChanged.connect(self.actualizar_longitudes)
        self.le_zlon.textChanged.connect(self.actualizar_longitudes)
        self.le_titalon.textChanged.connect(self.actualizar_longitudes)
        self.le_rlon.textChanged.connect(self.actualizar_longitudes)
        self.le_rini.textChanged.connect(self.actualizar_longitudes)
        self.le_zloncil.textChanged.connect(self.actualizar_longitudes)

        for i in range(1, 11):
            line_edit_name_x_vz = f"le_dirx_lon_zon{i}"
            line_edit_object_x_vz = getattr(self, line_edit_name_x_vz)
            line_edit_object_x_vz.textChanged.connect(self.actualizar_longitudes)

        for i in range(1, 11):
            line_edit_name_y_vz = f"le_diry_lon_zon{i}"
            line_edit_object_y_vz = getattr(self, line_edit_name_y_vz)
            line_edit_object_y_vz.textChanged.connect(self.actualizar_longitudes)

        for i in range(1, 11):
            line_edit_name_z_vz = f"le_dirz_lon_zon{i}"
            line_edit_object_z_vz = getattr(self, line_edit_name_z_vz)
            line_edit_object_z_vz.textChanged.connect(self.actualizar_longitudes)

        for i in range(1, 11):
            line_edit_name_tita_vz = f"le_dirtita_lon_zon{i}"
            line_edit_object_tita_vz = getattr(self, line_edit_name_tita_vz)
            line_edit_object_tita_vz.textChanged.connect(self.actualizar_longitudes)

        for i in range(1, 11):
            line_edit_name_r_vz = f"le_dirr_lon_zon{i}"
            line_edit_object_r_vz = getattr(self, line_edit_name_r_vz)
            line_edit_object_r_vz.textChanged.connect(self.actualizar_longitudes)

        for i in range(1, 11):
            line_edit_name_zcil_vz = f"le_dirzcil_lon_zon{i}"
            line_edit_object_zcil_vz = getattr(self, line_edit_name_zcil_vz)
            line_edit_object_zcil_vz.textChanged.connect(self.actualizar_longitudes)

        self.le_dirr_inidom.textChanged.connect(self.actualizar_longitudes)

        self.sb_dirx_numz.valueChanged.connect(self.handle_dirx_numz_change)
        self.sb_diry_numz.valueChanged.connect(self.handle_diry_numz_change)
        self.sb_dirz_numz.valueChanged.connect(self.handle_dirz_numz_change)
        self.sb_dirtita_numz.valueChanged.connect(self.handle_dirtita_numz_change)
        self.sb_dirr_numz.valueChanged.connect(self.handle_dirr_numz_change)
        self.sb_dirzcil_numz.valueChanged.connect(self.handle_dirzcil_numz_change)

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CARTESIANA

        self.le_xlon.textChanged.connect(lambda text: self.update_config("CART_XL", text))
        self.le_nvcx.textChanged.connect(lambda text: self.update_config("CART_NVCX", text))
        self.le_potenciax.textChanged.connect(lambda text: self.update_config("CART_POWERX", text))
        self.le_ylon.textChanged.connect(lambda text: self.update_config("CART_YL", text))
        self.le_nvcy.textChanged.connect(lambda text: self.update_config("CART_NVCY", text))
        self.le_potenciay.textChanged.connect(lambda text: self.update_config("CART_POWERY", text))
        self.le_zlon.textChanged.connect(lambda text: self.update_config("CART_ZL", text))
        self.le_nvcz.textChanged.connect(lambda text: self.update_config("CART_NVCZ", text))
        self.le_potenciaz.textChanged.connect(lambda text: self.update_config("CART_POWERZ", text))

        ##############################################################################################
        # CONEXION DE WIDGETS ZONA UNICA - CILINDRICA

        self.le_titalon.textChanged.connect(lambda text: self.update_config("CIL_TITAL", text))
        self.le_nvctita.textChanged.connect(lambda text: self.update_config("CIL_NVCTITA", text))
        self.le_potenciatita.textChanged.connect(lambda text: self.update_config("CIL_POWERTITA", text))
        self.le_rini.textChanged.connect(lambda text: self.update_config("CIL_R(1)_ZU", text))
        self.le_rlon.textChanged.connect(lambda text: self.update_config("CIL_RL", text))
        self.le_nvcr.textChanged.connect(lambda text: self.update_config("CIL_NVCR", text))
        self.le_potenciar.textChanged.connect(lambda text: self.update_config("CIL_POWERR", text))
        self.le_zloncil.textChanged.connect(lambda text: self.update_config("CIL_ZL", text))
        self.le_nvczcil.textChanged.connect(lambda text: self.update_config("CIL_NVCZ", text))
        self.le_potenciazcil.textChanged.connect(lambda text: self.update_config("CIL_POWERZ", text))

        #####################################################################################
        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA X (CARTESIANA)

        self.sb_dirx_numz.textChanged.connect(lambda text: self.update_config("CART_NZX", text))

        for i in range(1, 11):
            getattr(self, f"le_dirx_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"XZONE({i})", text)
            )
            getattr(self, f"le_dirx_nvcx_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"NCVX({i})", text)
            )
            getattr(self, f"le_dirx_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"POWERX({i})", text)
            )

        # -COORDENADA Y (CARTESIANA)

        self.sb_diry_numz.textChanged.connect(lambda text: self.update_config("CART_NZY", text))

        for i in range(1, 11):
            getattr(self, f"le_diry_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"YZONE({i})", text)
            )
            getattr(self, f"le_diry_nvcy_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"NCVY({i})", text)
            )
            getattr(self, f"le_diry_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"POWERY({i})", text)
            )

        # -COORDENADA Z (CARTESIANA)

        self.sb_dirz_numz.textChanged.connect(lambda text: self.update_config("CART_NZZ", text))

        for i in range(1, 11):
            getattr(self, f"le_dirz_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"ZZONE({i})", text)
            )
            getattr(self, f"le_dirz_nvcz_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"NCVZ({i})", text)
            )
            getattr(self, f"le_dirz_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"POWERZ({i})", text)
            )

        #####################################################################################

        # CONEXION DE WIDGETS VARIAS ZONAS - CARTESIANA

        # -COORDENADA TITA (CILINDRICA) - VARIAS ZONAS

        self.sb_dirtita_numz.textChanged.connect(lambda text: self.update_config("CIL_NZX", text))

        for i in range(1, 11):
            getattr(self, f"le_dirtita_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_XZONE({i})", text)
            )
            getattr(self, f"le_dirtita_nvctita_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_NCVX({i})", text)
            )
            getattr(self, f"le_dirtita_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_POWERX({i})", text)
            )

        #####################################################################################

        # -COORDENADA RADIO (CILINDRICA) - VARIAS ZONAS

        self.sb_dirr_numz.textChanged.connect(lambda text: self.update_config("CIL_NZY", text))

        self.le_dirr_inidom.textChanged.connect(lambda text: self.update_config("CIL_R(1)_VZ", text))

        for i in range(1, 11):
            getattr(self, f"le_dirr_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_YZONE({i})", text)
            )
            getattr(self, f"le_dirr_nvcr_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_NCVY({i})", text)
            )
            getattr(self, f"le_dirr_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_POWERY({i})", text)
            )

        #####################################################################################

        # -COORDENADA Z (CILINDRICA) - VARIAS ZONAS

        self.sb_dirzcil_numz.textChanged.connect(lambda text: self.update_config("CIL_VZ_NZZ", text))

        for i in range(1, 11):
            getattr(self, f"le_dirzcil_lon_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_VZ_ZZONE({i})", text)
            )
            getattr(self, f"le_dirzcil_nvczcil_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_VZ_NCVZ({i})", text)
            )
            getattr(self, f"le_dirzcil_poten_zon{i}").textChanged.connect(
                lambda text, i=i: self.update_config(f"CIL_VZ_POWERZ({i})", text)
            )

        #####################################################################################

    def changeZonas(self):
        current_text_coord = self.cb_tipocoord.currentText()
        current_text_zona = self.cb_tipozonas.currentText()

        # Determina el índice de la capa basado en la selección actual
        if current_text_zona == "Zona única" and current_text_coord == "Cartesianas":
            capaIndex = 0
        elif current_text_zona == "Zona única" and current_text_coord == "Cilindricas":
            capaIndex = 1
        elif current_text_zona == "Varias zonas" and current_text_coord == "Cartesianas":
            capaIndex = 2
        elif current_text_zona == "Varias zonas" and current_text_coord == "Cilindricas":
            capaIndex = 3

        # Resetear widgets de la capa actual antes de cambiar
        self.resetearWidgetsDeCapa(capaIndex)

        # Cambia el índice del QStackedWidget
        self.gbsw_malla2.setCurrentIndex(capaIndex)

    def on_coordinate_system_changed(self, selection):
        mode = 1 if selection == "Cartesianas" else 2
        self.config_manager.config_structure["GRID"]["MODE"] = mode

    def on_zones_system_changed(self, selection):
        zone = "zgrid" if selection == "Varias zonas" else "ezgrid"
        self.config_manager.config_structure["GRID"]["ZONEGRID"] = zone

    def update_config(self, config_key, text):
        # Actualiza el valor de la configuración en el ConfigManager
        self.config_manager.config_structure["GRID"][config_key] = text

    def actualizar_longitudes(self):

        tipocoord = self.cb_tipocoord.currentText()
        tipozonas = self.cb_tipozonas.currentText()

        longitud_x_cart_zu = self.le_xlon.text()
        longitud_y_cart_zu = self.le_ylon.text()
        longitud_z_cart_zu = self.le_zlon.text()
        longitud_tita_cil_zu = self.le_titalon.text()
        longitud_r_cil_zu = self.le_rlon.text()
        rini_cil_zu = self.le_rini.text()
        longitud_zcil_cil_zu = self.le_zloncil.text()

        longitud_x_cart_vz = 0
        longitud_y_cart_vz = 0
        longitud_z_cart_vz = 0

        longitud_tita_cil_vz = 0
        longitud_r_cil_vz = 0
        rini_cil_vz = self.le_dirr_inidom.text()
        longitud_zcil_cil_vz = 0

        for i in range(1, 11):
            # X
            attr_name_x_vz = f"le_dirx_lon_zon{i}"
            line_edit_object_x = getattr(self, attr_name_x_vz)
            try:
                valor_numerico_x_cart_vz = float(line_edit_object_x.text())
                longitud_x_cart_vz += valor_numerico_x_cart_vz
            except ValueError:
                print(f"El valor de {attr_name_x_vz} no es un número válido")

            # Y
            attr_name_y_vz = f"le_diry_lon_zon{i}"
            line_edit_object_y = getattr(self, attr_name_y_vz)
            try:
                valor_numerico_y_cart_vz = float(line_edit_object_y.text())
                longitud_y_cart_vz += valor_numerico_y_cart_vz
            except ValueError:
                print(f"El valor de {attr_name_y_vz} no es un número válido")

            # Z
            attr_name_z_vz = f"le_dirz_lon_zon{i}"
            line_edit_object_z = getattr(self, attr_name_z_vz)
            try:
                valor_numerico_z_cart_vz = float(line_edit_object_z.text())
                longitud_z_cart_vz += valor_numerico_z_cart_vz
            except ValueError:
                print(f"El valor de {attr_name_z_vz} no es un número válido")

        # Itera para las coordenadas en el sistema cilíndrico
        for i in range(1, 11):
            # Tita
            attr_name_tita_vz = f"le_dirtita_lon_zon{i}"
            line_edit_object_tita = getattr(self, attr_name_tita_vz)
            try:
                valor_numerico_tita_cil_vz = float(line_edit_object_tita.text())
                longitud_tita_cil_vz += valor_numerico_tita_cil_vz
            except ValueError:
                print(f"El valor de {attr_name_tita_vz} no es un número válido")

            # R
            attr_name_r_vz = f"le_dirr_lon_zon{i}"
            line_edit_object_r = getattr(self, attr_name_r_vz)
            try:
                valor_numerico_r_cil_vz = float(line_edit_object_r.text())
                longitud_r_cil_vz += valor_numerico_r_cil_vz
            except ValueError:
                print(f"El valor de {attr_name_r_vz} no es un número válido")

            # Zcil
            attr_name_zcil_vz = f"le_dirzcil_lon_zon{i}"
            line_edit_object_zcil = getattr(self, attr_name_zcil_vz)
            try:
                valor_numerico_zcil_cil_vz = float(line_edit_object_zcil.text())
                longitud_zcil_cil_vz += valor_numerico_zcil_cil_vz
            except ValueError:
                print(f"El valor de {attr_name_zcil_vz} no es un número válido")

        if tipocoord == "Cartesianas" and tipozonas == "Zona única":
            self.longitudes_actualizadas_signal.emit([longitud_x_cart_zu, longitud_y_cart_zu, longitud_z_cart_zu, 0])

        elif tipocoord == "Cilindricas" and tipozonas == "Zona única":
            self.longitudes_actualizadas_signal.emit(
                [longitud_tita_cil_zu, longitud_r_cil_zu, longitud_zcil_cil_zu, rini_cil_zu]
            )

        elif tipocoord == "Cartesianas" and tipozonas == "Varias zonas":
            self.longitudes_actualizadas_signal.emit([longitud_x_cart_vz, longitud_y_cart_vz, longitud_z_cart_vz, 0])

        elif tipocoord == "Cilindricas" and tipozonas == "Varias zonas":
            self.longitudes_actualizadas_signal.emit(
                [longitud_tita_cil_vz, longitud_r_cil_vz, longitud_zcil_cil_vz, rini_cil_vz]
            )

    def handle_generic_numz_change(self, value, prefix, ncv_prefix):
        for i in range(1, 11):
            le_lon = getattr(self, f"{prefix}_lon_zon{i}", None)
            le_ncv = getattr(self, f"{prefix}_{ncv_prefix}_zon{i}", None)
            le_pot = getattr(self, f"{prefix}_poten_zon{i}", None)

            if i <= value:
                if le_lon:
                    le_lon.setEnabled(True)
                if le_ncv:
                    le_ncv.setEnabled(True)
                if le_pot:
                    le_pot.setEnabled(True)
            else:
                if le_lon:
                    le_lon.setEnabled(False)
                if le_ncv:
                    le_ncv.setEnabled(False)
                if le_pot:
                    le_pot.setEnabled(False)

    def handle_dirx_numz_change(self, value):
        self.handle_generic_numz_change(value, "le_dirx", "nvcx")

    def handle_diry_numz_change(self, value):
        self.handle_generic_numz_change(value, "le_diry", "nvcy")

    def handle_dirz_numz_change(self, value):
        self.handle_generic_numz_change(value, "le_dirz", "nvcz")

    def handle_dirtita_numz_change(self, value):
        self.handle_generic_numz_change(value, "le_dirtita", "nvctita")

    def handle_dirr_numz_change(self, value):
        self.handle_generic_numz_change(value, "le_dirr", "nvcr")

    def handle_dirzcil_numz_change(self, value):
        self.handle_generic_numz_change(value, "le_dirzcil", "nvczcil")

    def resetearWidgetsDeCapa(self, capaIndex):
        # Obtén el widget (capa) actual del QStackedWidget basado en el índice
        capa = self.gbsw_malla2.widget(capaIndex)

        # Encuentra todos los QLineEdit en esta capa y limpia su texto
        lineEdits = capa.findChildren(qtw.QLineEdit)
        for lineEdit in lineEdits:
            lineEdit.clear()

        # Encuentra todos los QSpinBox en esta capa y restablece su valor al mínimo
        spinBoxes = capa.findChildren(qtw.QSpinBox)
        for spinBox in spinBoxes:
            spinBox.setValue(spinBox.minimum())
