import json
from collections import OrderedDict
from PySide6.QtWidgets import QLineEdit, QSpinBox, QComboBox, QCheckBox, QListWidget


class ConfigManager:
    def __init__(self):
        # Inicializar la estructura de la configuración con las secciones requeridas
        # fmt: off
        self.config_structure = OrderedDict([
            ('HEADER', OrderedDict()),
            ('GRID', OrderedDict()),
            ('VARIABLES', OrderedDict([
                ('cb_tipoflujo', 'Difusivo'),
                ('le_var_title5', 'Temperatura'),
                ('cb_tsimu', 'Permanente'),
                ('cb_trataborde', 'Esquema de bajo orden')
                ])),
            ('BOUND', OrderedDict([
                ('X Max', OrderedDict([('Borde base', OrderedDict())])),
                ('X Min', OrderedDict([('Borde base', OrderedDict())])),
                ('Y Max', OrderedDict([('Borde base', OrderedDict())])),
                ('Y Min', OrderedDict([('Borde base', OrderedDict())])),
                ('Z Max', OrderedDict([('Borde base', OrderedDict())])),
                ('Z Min', OrderedDict([('Borde base', OrderedDict())])),
            ]))])
        # fmt: on

    ################################################################################
    ##
    ## Slots usados por señales
    ##
    ################################################################################

    def save_to_json(self, filename):
        # Guardar la configuración en un archivo JSON
        with open(filename, "w", encoding="utf8") as f:
            json.dump(self.config_structure, f, indent=4)

    def load_from_json(self, filename):
        # Cargar la configuración desde un archivo JSON
        with open(filename, "r", encoding="utf8") as f:
            self.config_structure = json.load(f, object_pairs_hook=OrderedDict)

    def load_config(self, window):
        # Carga la configuración de una ventana desde config_manager
        config = window.config_manager.config_structure[window.config_name]
        for widget_name, value in config.items():
            widget = getattr(window, widget_name)
            if isinstance(widget, QLineEdit):
                widget.setText(value)
            elif isinstance(widget, QComboBox):
                widget.setCurrentText(value)
            elif isinstance(widget, QSpinBox):
                widget.setValue(value)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(value == 2)
            else:
                continue

    def connect_config(self, window):
        for widget_name in window.widgets:
            widget = getattr(window, widget_name)
            if isinstance(widget, QLineEdit):
                signal = widget.textChanged
            elif isinstance(widget, QComboBox):
                signal = widget.currentTextChanged
            elif isinstance(widget, QSpinBox):
                signal = widget.valueChanged
            elif isinstance(widget, QCheckBox):
                signal = widget.stateChanged
            elif isinstance(widget, QListWidget):
                signal = widget.currentRowChanged
            else:
                continue
            signal.connect(window.value_changed)

    def set_patch_config(self, border, patch, key, value):
        """
        Establece la configuración para un parche específico.

        :param border: str - El nombre del borde (ejemplo: "X Max").
        :param patch: str - El nombre del parche (ejemplo: "Borde Base").
        :param config: key - El nombre de la variable a guardar.
        :param config: value - El valor de la variable a guardar.
        """
        if value is not None:
            # Asegurarse de que la estructura de borde y parche exista
            if border not in self.config_structure["BOUND"]:
                self.config_structure["BOUND"][border] = OrderedDict()
            if patch not in self.config_structure["BOUND"][border]:
                self.config_structure["BOUND"][border][patch] = OrderedDict()
            self.config_structure["BOUND"][border][patch][key] = value
        else:
            self.config_structure["BOUND"][border][patch].pop(key, None)
            if len(self.config_structure["BOUND"][border][patch]) == 0 and patch != "Borde base":
                self.config_structure["BOUND"][border].pop(patch, None)
