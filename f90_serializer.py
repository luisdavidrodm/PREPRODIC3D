import json
import subprocess
import os
from pathlib import Path

# I de identacion mayor, i de identación menor, s de separador
I = "      "  # 6 espacios de indentación para el código F90
i = "  "
s = "!______________________________________________________________________"


class F90Serializer:
    def __init__(self):
        self.f90_lines = ["! Generated by PrePRODIC3D"]
        self.loop_mapping = {
            "X Max": ("KBCI1", "J", "M1", "K", "N1", "T(L1,J,K)"),
            "X Min": ("KBCL1", "J", "M1", "K", "N1", "T(1,J,K)"),
            "Y Max": ("KBCJ1", "I", "L1", "K", "N1", "T(I,M1,K)"),
            "Y Min": ("KBCM1", "I", "L1", "K", "N1", "T(I,1,K)"),
            "Z Max": ("KBCK1", "I", "L1", "J", "M1", "T(I,J,N1)"),
            "Z Min": ("KBCN1", "I", "L1", "J", "M1", "T(I,J,1)"),
        }

    def serialize_grid_section(self, grid, header):
        """
        Serializa la sección GRID del JSON a líneas de código F90, incluyendo los datos de HEADER.

        :param grid: Diccionario con la información de la sección GRID del JSON.
        :param header: Diccionario con la información de la sección HEADER del JSON.
        :return: Lista de líneas de código F90 correspondientes a la sección GRID y HEADER.
        """
        f90_lines = ["ENTRY GRID"]
        # HEADER section with corrected variable names
        f90_lines.append(f"HEADER='{header.get('le_titulosimu')}'")
        f90_lines.append(f"PRINTF='{header.get('le_tituloimpre')}'")
        f90_lines.append(f"PLOTF='{header.get('le_titulograf')}'")
        mode = {"Cartesianas": 1, "Cilindricas": 2}.get(grid.get("cb_tipocoord"), 2)
        kcy = 1 if mode == 2 else 0
        f90_lines.append(f"MODE={mode} ; KCY={kcy}")
        f90_lines.append(
            f"NCVLX={grid.get('le_nvctita', '12')} ; NCVLY={grid.get('le_nvcr', '6')} ; NCVLZ={grid.get('le_nvczcil', '6')}; LAST=5"
        )
        f90_lines.append(
            f"XL={grid.get('le_titalon', '1.')}; R(1)={grid.get('le_rini', '1.')}; YL={grid.get('le_rlon', '1.5')}; ZL={grid.get('le_zloncil', '1.5')}"
        )
        grid_function = "ZGRID" if grid.get("cb_tipozonas") == "Varias zonas" else "EZGRID"
        f90_lines.append(f"CALL {grid_function}")
        f90_lines.append("RETURN")
        return f90_lines

    def serialize_begin_section(self, variables, bound):
        f90_lines = ["ENTRY BEGIN"]
        f90_lines.append(f"TITLE(5)='{variables.get('le_var_title5', '')}'")
        f90_lines.append(f"KSOLVE(5)={variables.get('chb_ksolve5', 0)} ; KPRINT(5)={variables.get('chb_kprint5', 0)}")
        f90_lines.append("IBORY(5)=1")
        for boundary, patchs in bound.items():
            for patch, values in patchs.items():
                value_condition = values.get("chb_value", None)
                border_value = values.get("le_value", None)
                if value_condition == 2 and border_value is not None:
                    _, loop_var_1, loop_limit_1, loop_var_2, loop_limit_2, assignment = self.loop_mapping[boundary]
                    f90_lines.extend(
                        [
                            f"DO {loop_var_1}=1,{loop_limit_1}",
                            f"{i}DO {loop_var_2}=1,{loop_limit_2}",
                            f"{i}{i}{assignment}={border_value}",
                            f"{i}ENDDO",
                            "ENDDO",
                        ]
                    )
        f90_lines.append("RETURN")
        return f90_lines

    def serialize_dense_section(self, dense):
        f90_lines = ["ENTRY DENSE"]
        f90_lines.append("RETURN")
        return f90_lines

    def serialize_bound_section(self, bound):
        f90_lines = ["ENTRY BOUND"]
        f90_lines.append("RETURN")
        return f90_lines

    def serialize_output_section(self, output):
        f90_lines = ["ENTRY OUTPUT"]
        f90_lines.append("RETURN")
        return f90_lines

    def serialize_phi_section(self, variables, bound):
        f90_lines = ["ENTRY PHI"]
        for boundary, patchs in bound.items():
            for patch, values in patchs.items():
                flux_condition = values.get("chb_flux", 0)
                if flux_condition == 2:
                    kbc_var, loop_var_1, loop_limit_1, loop_var_2, loop_limit_2, _ = self.loop_mapping[boundary]
                    f90_lines.extend(
                        [
                            f"DO {loop_var_1}=1,{loop_limit_1}",
                            f"{i}DO {loop_var_2}=1,{loop_limit_2}",
                            f"{i}{i}{kbc_var}({loop_var_1},{loop_var_2})=2",
                            f"{i}ENDDO",
                            "ENDDO",
                        ]
                    )
        f90_lines.append("RETURN")
        f90_lines.append("END")
        return f90_lines

    def generate_f90(self, config_structure):
        self.extend_f90(["SUBROUTINE ADAPT"])
        self.extend_f90(["INCLUDE '3DCOMMON.F90'", f"{i}COMMON QNOR,QSOU,QSUM,TCIN,TCEX"])

        # HEADER y GRID section - Usando la función definida anteriormente
        grid_section_lines = self.serialize_grid_section(
            config_structure.get("GRID", {}), config_structure.get("HEADER", {})
        )
        self.extend_f90(grid_section_lines)
        begin_section_lines = self.serialize_begin_section(
            config_structure.get("VARIABLES", {}), config_structure.get("BOUND", {})
        )
        self.extend_f90(begin_section_lines)
        dense_section_lines = self.serialize_dense_section("")
        self.extend_f90(dense_section_lines)
        bound_section_lines = self.serialize_bound_section("")
        self.extend_f90(bound_section_lines)
        output_section_lines = self.serialize_output_section("")
        self.extend_f90(output_section_lines)
        phi_section_lines = self.serialize_phi_section(
            config_structure.get("VARIABLES", {}), config_structure.get("BOUND", {})
        )
        self.extend_f90(phi_section_lines)

        print(self.f90_lines)
        return "\n".join(self.f90_lines)

    def extend_f90(self, new_f90_lines):
        new_f90_lines = [f"{I}{line}" for line in new_f90_lines]
        self.f90_lines.extend([s] + new_f90_lines)


if __name__ == "__main__":
    working_directory = Path("C:/PRODIC3D/Utilidades/F90/dona")
    os.chdir(working_directory)
    with open("dona.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
    serializer = F90Serializer()
    f90_code = serializer.generate_f90(json_data)
    with open(working_directory / "output.f90", "w", encoding="utf-8") as f:
        f.write(f90_code)
    exe_path = working_directory / "myprogram.exe"
    if exe_path.exists():
        exe_path.unlink()
    compile_command = "gfortran -o myprogram.exe prodic3d.f90 output.f90"
    subprocess.run(compile_command, check=True, shell=True, cwd=working_directory)
    subprocess.run(str(exe_path), shell=True, check=False)
    ruta_paraview = "C:/Program Files/ParaView 5.12.0/bin/paraview.exe"
    script_path = "C:/PREPRODIC3D/tecplot.py"
    subprocess.run([ruta_paraview, "--script=" + script_path], check=True)
