from PySide2 import QtWidgets as qtw
from PySide2.QtCore import Qt

from bordes_window.ui.bordes_window_ui import Ui_bordes_window


class BordesWindow(qtw.QDialog, Ui_bordes_window):

    def __init__(self, config_manager):
        # fmt: off
        super().__init__()
        self.setupUi(self)
        self.config_manager = config_manager
        self.config_name = "BOUND"
        self.load_borders_list()

        self.pb_addpatch.clicked.connect(self.add_patch)
        self.pb_rempatch.clicked.connect(self.remove_patch)

        self.lw_bordes.currentRowChanged.connect(self.load_patch_list)
        self.lw_patchlist.currentRowChanged.connect(self.load_patch_config)
        self.lw_variables.currentRowChanged.connect(self.load_current_config)

        # Definir widgets de parches y listas de widgets
        self.patch_widgets = [
            "chb_wall", "chb_inmass", "chb_outmass", "le_transversal_start", "le_transversal_end", 
            "le_vertical_start", "le_vertical_end", "chb_exclude_borders", "cb_ex_transversal_start", 
            "cb_ex_transversal_end", "cb_ex_vertical_start", "cb_ex_vertical_end"
        ]
        self.variable_widgets = [
            "chb_value", "chb_flux", "chb_convec", "le_value", "chb_ex_value", 
            "le_tempamb", "le_k", "chb_ex_k"]
        self.widgets = self.patch_widgets + self.variable_widgets

        for chb_name in ['wall', 'inmass', 'outmass', 'value', 'flux', 'convec']:
            checkbox = getattr(self, f'chb_{chb_name}')
            checkbox.stateChanged.connect(self.handle_checkbox_state_changed)

        self.chb_outmass.stateChanged.connect(self.handle_chb_mass_state_changed)
        self.chb_inmass.stateChanged.connect(self.handle_chb_mass_state_changed)

        self.config_manager.connect_config(self)
        self.lw_bordes.setCurrentItem(self.lw_bordes.item(0))
        self.load_variables_list()
        self.initialize_patch_labels()
        # fmt: on

    def toggle_widget_list(self, widgets, toggle):
        """"""
        for widget_name in widgets:
            widget = getattr(self, widget_name, None)
            if widget:
                widget.setEnabled(toggle)
                if not toggle:
                    if isinstance(widget, qtw.QLineEdit):
                        widget.clear()
                    elif isinstance(widget, qtw.QComboBox):
                        widget.setCurrentText(None)
                    elif isinstance(widget, qtw.QCheckBox):
                        widget.setChecked(False)
            else:
                print(f"ERROR AL LIMPIAR: {widget_name} en {widgets}")

    def value_changed(self, value):
        """"""
        sender = self.sender()
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        variable = self.lw_variables.currentItem()
        if value is not None and value != "":
            # Si hay un valor nuevo válido
            if border and patch and variable and sender.objectName() in self.variable_widgets:
                variable_key = variable.data(Qt.UserRole)
                self.le_tempamb.setEnabled(self.chb_convec.isChecked() or self.chb_flux.isChecked())
                border_text = border.data(Qt.UserRole)
                if border_text not in self.config_manager.bound:
                    self.config_manager.bound[border_text] = {}
                if patch.text() not in self.config_manager.bound[border_text]:
                    self.config_manager.bound[border_text][patch.text()] = {}
                if variable_key not in self.config_manager.bound[border_text][patch.text()]:
                    self.config_manager.bound[border_text][patch.text()][variable_key] = {}
                self.config_manager.bound[border_text][patch.text()][variable_key][sender.objectName()] = value
            elif border and patch and sender.objectName() in self.patch_widgets:
                border_text = border.data(Qt.UserRole)
                if border_text not in self.config_manager.bound:
                    self.config_manager.bound[border_text] = {}
                if patch.text() not in self.config_manager.bound[border_text]:
                    self.config_manager.bound[border_text][patch.text()] = {}
                self.config_manager.bound[border_text][patch.text()][sender.objectName()] = value
        else:
            if border and patch and variable and sender.objectName() in self.variable_widgets:
                variable_key = variable.data(Qt.UserRole)
                border_text = border.data(Qt.UserRole)
                self.config_manager.bound[border_text][patch.text()][variable_key].pop(sender.objectName(), None)
                # if not self.config_manager.bound[border_text][patch.text()][variable_key]:
                #     del self.config_manager.bound[border_text][patch.text()][variable_key]
                # if not self.config_manager.bound[border_text][patch.text()]:
                #     del self.config_manager.bound[border_text][patch.text()]
            elif border and patch and sender.objectName() in self.patch_widgets:
                border_text = border.data(Qt.UserRole)
                self.config_manager.bound[border_text][patch.text()].pop(sender.objectName(), None)
                # if not self.config_manager.bound[border_text][patch.text()]:
                #     del self.config_manager.bound[border_text][patch.text()]

    def get_configured_widgets(self, border, patch, variable):
        """"""
        # Esta función busca en la configuración y recoge todos los widgets configurados
        if border and patch:
            border_text = border.data(Qt.UserRole)
            patch_text = patch.text()
            if border_text not in self.config_manager.bound:
                self.config_manager.bound[border_text] = {}
            if patch_text not in self.config_manager.bound[border_text]:
                self.config_manager.bound[border_text][patch_text] = {}
            config = self.config_manager.bound[border_text][patch_text]
            configured_widgets = set()
            configured_widgets.update(key for key, value in config.items() if not isinstance(value, dict))
            if variable:
                variable_key = variable.data(Qt.UserRole)
                if variable_key not in config:
                    config[variable_key] = {}
                variable_config = config[variable_key]
                configured_widgets.update(key for key in variable_config.keys())
            return configured_widgets
        return []

    def load_current_config(self):
        """"""
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        variable = self.lw_variables.currentItem()
        configured_widgets = self.get_configured_widgets(border, patch, variable)
        not_configured_widgets = [widget for widget in self.widgets if widget not in configured_widgets]
        self.toggle_widget_list(not_configured_widgets, False)
        if border and patch:
            border_text = border.data(Qt.UserRole)
            config = self.config_manager.bound[border_text][patch.text()]
            self.toggle_widget_list(self.patch_widgets, True)
            self.config_manager.load_config(self, config)
            self.lw_variables.setEnabled(True)
            if patch.text() == "Borde base":
                self.le_transversal_start.setEnabled(False)
                self.le_transversal_end.setEnabled(False)
                self.le_vertical_start.setEnabled(False)
                self.le_vertical_end.setEnabled(False)
                self.cb_ex_transversal_start.setEnabled(False)
                self.cb_ex_transversal_end.setEnabled(False)
                self.cb_ex_vertical_start.setEnabled(False)
                self.cb_ex_vertical_end.setEnabled(False)
                if self.config_manager.is_mesh_info_complete:
                    patch_data = self.initialize_patch_data()
                    self.le_transversal_start.setText(patch_data["transversal_start"])
                    self.le_transversal_end.setText(patch_data["transversal_end"])
                    self.le_vertical_start.setText(patch_data["vertical_start"])
                    self.le_vertical_end.setText(patch_data["vertical_end"])
            if self.config_manager.has_out_mass and not self.chb_outmass.isChecked():
                self.chb_outmass.setEnabled(False)
            if variable is not None:
                variable_key = variable.data(Qt.UserRole)
                self.toggle_widget_list(self.variable_widgets, True)
                self.config_manager.load_config(self, config[variable_key])
                variable_number = int(variable_key[len("le_var_title") :])
                if variable_number in [1, 2, 3, 4, 11, 12]:
                    self.chb_convec.setEnabled(False)
                if variable_number in [1, 2, 3]:
                    self.lb_cond.setText("Viscosidad")
                elif variable_number == 5:
                    self.lb_cond.setText("k/Cp")
                else:
                    self.lb_cond.setText("Coef. Difusión")
                self.le_tempamb.setEnabled(self.chb_convec.isChecked() or self.chb_flux.isChecked())
                if self.chb_inmass.isChecked() or self.chb_outmass.isChecked():
                    if (
                        variable_key in [f"le_var_title{i}" for i in range(1, 4)]
                        and self.chb_ex_value not in config[variable_key]
                    ):
                        self.chb_ex_value.setChecked(True)
                if not any(config[variable_key].get(chb) == 2 for chb in ["chb_value", "chb_convec", "chb_flux"]):
                    self.chb_value.setChecked(True)
            else:
                self.toggle_widget_list(self.variable_widgets, False)
        else:
            self.lw_variables.setEnabled(False)

    def load_patch_list(self):
        """"""
        border = self.lw_bordes.currentItem()
        if border is not None:
            self.lw_patchlist.clear()
            border_text = border.data(Qt.UserRole)
            config = self.config_manager.bound[border_text]
            for key, value in config.items():
                if isinstance(value, dict):
                    self.lw_patchlist.addItem(key)
            self.load_current_config()
            self.initialize_patch_labels()

    def load_patch_config(self):
        """"""
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        if border is not None and patch is not None:
            border_text = border.data(Qt.UserRole)
            patch_text = patch.text()
            if self.config_manager.is_mesh_info_complete and patch_text != "Borde base":
                patch_data = self.initialize_patch_data()
                # Verificar si alguno de los valores ya está definido
                keys = ["le_transversal_start", "le_transversal_end", "le_vertical_start", "le_vertical_end"]
                if not any(key in self.config_manager.bound[border_text][patch_text] for key in keys):
                    self.config_manager.bound[border_text][patch_text]["le_transversal_start"] = patch_data[
                        "transversal_start"
                    ]
                    self.config_manager.bound[border_text][patch_text]["le_transversal_end"] = patch_data[
                        "transversal_end"
                    ]
                    self.config_manager.bound[border_text][patch_text]["le_vertical_start"] = patch_data[
                        "vertical_start"
                    ]
                    self.config_manager.bound[border_text][patch_text]["le_vertical_end"] = patch_data["vertical_end"]
            self.lw_variables.clearSelection()
            self.load_variables_list()

    def load_variables_list(self):
        """Carga y actualiza la lista de variables considerando el orden y permitiendo duplicados."""
        excluded_keys = {"le_var_title4", "le_var_title11", "le_var_title12"}
        new_items = []
        for key, value in self.config_manager.variables.items():
            if key.startswith("le_var_title") and key not in excluded_keys:
                number = int(key[len("le_var_title") :])
                new_items.append((number, value, key))
        new_items.sort()
        self.lw_variables.clear()
        for _, name, tech_name in new_items:
            item = qtw.QListWidgetItem(name)
            item.setData(Qt.UserRole, tech_name)
            self.lw_variables.addItem(item)
        self.load_current_config()

    def handle_checkbox_state_changed(self, state: int):
        sender = self.sender()
        if state == 2:
            if sender in [self.chb_wall, self.chb_inmass, self.chb_outmass]:
                if sender == self.chb_wall:
                    self.chb_wall.setChecked(True)
                    if self.chb_inmass.isChecked():
                        self.chb_inmass.setChecked(False)
                    if self.chb_outmass.isChecked():
                        self.chb_outmass.setChecked(False)
                elif sender == self.chb_inmass:
                    self.chb_inmass.setChecked(True)
                    if self.chb_wall.isChecked():
                        self.chb_wall.setChecked(False)
                    if self.chb_outmass.isChecked():
                        self.chb_outmass.setChecked(False)
                elif sender == self.chb_outmass:
                    self.chb_outmass.setChecked(True)
                    if self.chb_wall.isChecked():
                        self.chb_wall.setChecked(False)
                    if self.chb_inmass.isChecked():
                        self.chb_inmass.setChecked(False)
            elif sender in [self.chb_value, self.chb_flux, self.chb_convec]:
                if sender == self.chb_value:
                    self.chb_value.setChecked(True)
                    self.lb_value.setText("Valor")
                    self.lb_variable.setText("")
                    if self.chb_flux.isChecked():
                        self.chb_flux.setChecked(False)
                    if self.chb_convec.isChecked():
                        self.chb_convec.setChecked(False)
                elif sender == self.chb_flux:
                    self.chb_flux.setChecked(True)
                    self.lb_value.setText("Fc")
                    self.lb_variable.setText("Fp")
                    if self.chb_value.isChecked():
                        self.chb_value.setChecked(False)
                    if self.chb_convec.isChecked():
                        self.chb_convec.setChecked(False)
                elif sender == self.chb_convec:
                    self.chb_convec.setChecked(True)
                    self.lb_value.setText("Coeficiente")
                    self.lb_variable.setText("Temp. Amb.")
                    if self.chb_value.isChecked():
                        self.chb_value.setChecked(False)
                    if self.chb_flux.isChecked():
                        self.chb_flux.setChecked(False)

    def handle_chb_mass_state_changed(self, state):
        if state == 2:
            self.chb_exclude_borders.setChecked(True)
            variable = self.lw_variables.currentItem()
            if variable:
                if variable.data(Qt.UserRole) in [f"le_var_title{i}" for i in range(1, 4)]:
                    self.chb_ex_value.setChecked(True)

    def add_patch(self):
        """"""
        border = self.lw_bordes.currentItem()
        if border:
            border_text = border.data(Qt.UserRole)
            patch_number = self.lw_patchlist.count()
            self.lw_patchlist.addItem(f"Parche {patch_number}")
            self.config_manager.bound[border_text][f"Parche {patch_number}"] = {"chb_wall": 2}

    def remove_patch(self):
        """"""
        border = self.lw_bordes.currentItem()
        if border:
            patch_count = self.lw_patchlist.count()
            if patch_count > 1:
                border_text = border.data(Qt.UserRole)
                last_patch = self.lw_patchlist.item(patch_count - 1)
                self.lw_patchlist.takeItem(patch_count - 1)
                self.config_manager.bound[border_text].pop(last_patch.text(), None)

    def load_borders_list(self):
        """"""
        self.lw_bordes.clear()
        if self.config_manager.is_cartesian:
            new_items = [
                (1, "X Max", "X Max"),
                (2, "X Min", "X Min"),
                (3, "Y Max", "Y Max"),
                (4, "Y Min", "Y Min"),
                (5, "Z Max", "Z Max"),
                (6, "Z Min", "Z Min"),
            ]
        else:
            new_items = [
                (1, "θ Max", "X Max"),
                (2, "θ Min", "X Min"),
                (3, "R Max", "Y Max"),
                (4, "R Min", "Y Min"),
                (5, "Z Max", "Z Max"),
                (6, "Z Min", "Z Min"),
            ]
        new_items.sort()
        for _, name, tech_name in new_items:
            item = qtw.QListWidgetItem(name)
            item.setData(Qt.UserRole, tech_name)
            self.lw_bordes.addItem(item)

    def initialize_patch_labels(self):
        """
        Initialize patch labels based on the selected patch.
        """
        transversal_label = ""
        vertical_label = ""
        border = self.lw_bordes.currentItem()
        if border is not None:
            border_text = border.data(Qt.UserRole)
            if self.config_manager.is_cartesian:
                if border_text in {"X Max", "X Min"}:
                    transversal_label = "Y"
                    vertical_label = "Z"
                elif border_text in {"Y Max", "Y Min"}:
                    transversal_label = "X"
                    vertical_label = "Z"
                elif border_text in {"Z Max", "Z Min"}:
                    transversal_label = "X"
                    vertical_label = "Y"
            else:
                if border_text in {"X Max", "X Min"}:
                    transversal_label = "R"
                    vertical_label = "Z"
                elif border_text in {"Y Max", "Y Min"}:
                    transversal_label = "θ"
                    vertical_label = "Z"
                elif border_text in {"Z Max", "Z Min"}:
                    transversal_label = "θ"
                    vertical_label = "R"
        self.lb_transversal.setText(transversal_label)
        self.lb_vertical.setText(vertical_label)

    def initialize_patch_data(self):
        """
        Initialize patch data based on the selected patch.
        """
        patch_data = {}
        border = self.lw_bordes.currentItem()
        patch = self.lw_patchlist.currentItem()
        if border is not None and patch is not None:
            border_text = border.data(Qt.UserRole)
            if self.config_manager.is_cartesian and self.config_manager.is_ezgrid:
                if border_text in {"X Max", "X Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_ylon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zlon"],
                    }
                elif border_text in {"Y Max", "Y Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_xlon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zlon"],
                    }
                elif border_text in {"Z Max", "Z Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_xlon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_ylon"],
                    }
            elif not self.config_manager.is_cartesian and self.config_manager.is_ezgrid:
                if border_text in {"X Max", "X Min"}:
                    patch_data = {
                        "transversal_start": self.config_manager.grid["le_rini"],
                        "transversal_end": self.config_manager.grid["le_rlon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zloncil"],
                    }
                elif border_text in {"Y Max", "Y Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_titalon"],
                        "vertical_start": "0",
                        "vertical_end": self.config_manager.grid["le_zloncil"],
                    }
                elif border_text in {"Z Max", "Z Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": self.config_manager.grid["le_titalon"],
                        "vertical_start": self.config_manager.grid["le_rini"],
                        "vertical_end": self.config_manager.grid["le_rlon"],
                    }
            elif self.config_manager.is_cartesian and not self.config_manager.is_ezgrid:
                x_end = sum(
                    float(self.config_manager.grid.get(f"le_dirx_lon_zon{i}", 0))
                    for i in range(1, self.config_manager.grid["sb_dirx_numz"] + 1)
                )
                y_end = sum(
                    float(self.config_manager.grid.get(f"le_diry_lon_zon{i}", 0))
                    for i in range(1, self.config_manager.grid["sb_diry_numz"] + 1)
                )
                z_end = sum(
                    float(self.config_manager.grid.get(f"le_dirz_lon_zon{i}", 0))
                    for i in range(1, self.config_manager.grid["sb_dirz_numz"] + 1)
                )
                if border_text in {"X Max", "X Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": str(y_end),
                        "vertical_start": "0",
                        "vertical_end": str(z_end),
                    }
                elif border_text in {"Y Max", "Y Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": str(x_end),
                        "vertical_start": "0",
                        "vertical_end": str(z_end),
                    }
                elif border_text in {"Z Max", "Z Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": str(x_end),
                        "vertical_start": "0",
                        "vertical_end": str(y_end),
                    }
            else:  # if not self.config_manager.is_cartesian and not self.config_manager.is_ezgrid
                x_end = sum(
                    float(self.config_manager.grid.get(f"le_dirtita_lon_zon{i}", 0))
                    for i in range(1, self.config_manager.grid["sb_dirtita_numz"] + 1)
                )
                y_end = sum(
                    float(self.config_manager.grid.get(f"le_dirr_lon_zon{i}", 0))
                    for i in range(1, self.config_manager.grid["sb_dirr_numz"] + 1)
                )
                z_end = sum(
                    float(self.config_manager.grid.get(f"le_dirzcil_lon_zon{i}", 0))
                    for i in range(1, self.config_manager.grid["sb_dirzcil_numz"] + 1)
                )
                y_start = self.config_manager.grid.get("le_dirr_inidom", 0)
                if border_text in {"X Max", "X Min"}:
                    patch_data = {
                        "transversal_start": str(y_start),
                        "transversal_end": str(y_end),
                        "vertical_start": "0",
                        "vertical_end": str(z_end),
                    }
                elif border_text in {"Y Max", "Y Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": str(x_end),
                        "vertical_start": "0",
                        "vertical_end": str(z_end),
                    }
                elif border_text in {"Z Max", "Z Min"}:
                    patch_data = {
                        "transversal_start": "0",
                        "transversal_end": str(x_end),
                        "vertical_start": str(y_start),
                        "vertical_end": str(y_end),
                    }
        return patch_data
