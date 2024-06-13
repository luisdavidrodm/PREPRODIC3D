import json
import subprocess
import os
import sympy as sp
from pathlib import Path

# I de identacion mayor, i de identación menor, s de separador
I = "      "  # 6 espacios de indentación para el código F90
i = "  "
s = "!______________________________________________________________________"


class F90Translator:
    def __init__(self):
        self.f90_lines = ["! Generated by PrePRODIC3D"]
        self.variable_map = {"le_var_title1": "U", "le_var_title2": "V", "le_var_title3": "W", "le_var_title5": "T"}
        self.variables_map = {f"le_var_title{i}": i for i in range(1, 13)}
        self.volume_widgets = ["le_x_start", "le_x_end", "le_y_start", "le_y_end", "le_z_start", "le_z_end"]
        self.loop_mapping = {
            "X Max": ("L1", "J", "M1", "K", "N1", "(L1,J,K)"),
            "X Min": ("I1", "J", "M1", "K", "N1", "(1,J,K)"),
            "Y Max": ("M1", "I", "L1", "K", "N1", "(I,M1,K)"),
            "Y Min": ("J1", "I", "L1", "K", "N1", "(I,1,K)"),
            "Z Max": ("N1", "I", "L1", "J", "M1", "(I,J,N1)"),
            "Z Min": ("K1", "I", "L1", "J", "M1", "(I,J,1)"),
        }
        self.loop_mapping2 = {
            "X Max": ("J", "K", "(L1,J,K)"),
            "X Min": ("J", "K", "(1,J,K)"),
            "Y Max": ("I", "K", "(I,M1,K)"),
            "Y Min": ("I", "K", "(I,1,K)"),
            "Z Max": ("I", "J", "(I,J,N1)"),
            "Z Min": ("I", "J", "(I,J,1)"),
        }
        self.custom_titles = {
            1: " VEL U ",
            2: " VEL V ",
            3: " VEL W ",
            4: "CORRECCION",
            5: " TEMPERATURA ",
            11: "PRESION",
        }
        self.in_mass = """IF(ITER.NE.0) GO TO 350
      FLOWIN=0.
      DO I=2,L2
       DO J=2,M2
          FLOWIN=FLOWIN+RHO(I,J,1)*W(I,J,2)*ARZ(I,J)
       ENDDO
      ENDDO
  350 FL=0.
      AFL=0.
      WMIN=0.
      DO I=2,L2
       DO J=2,M2
         IF(W(I,J,N2).LT.0) WMIN=AMAX1(WMIN,-W(I,J,N2))
         AFL=AFL+RHO(I,J,N1)*ARZ(I,J)
         FL=FL+RHO(I,J,N1)*W(I,J,N2)*ARZ(I,J)
       ENDDO
      ENDDO
      FACTOR=FLOWIN/(FL+AFL*WMIN+SMALL)
      DO I=2,L2
       DO J=2,M2
        W(I,J,N1)=(W(I,J,N2)+WMIN)*FACTOR
       ENDDO
      ENDDO"""
        self.dimensionless = "DIMENSION  WSUM(25), TSUM(25), TB(25), WBAR(25), AREA(25)"
        self.dimensionless_common = "COMMON TW,TIN,WSUM,TSUM,TB,WBAR,AREA,FLOWIN,WMIN"
        self.dimensionless_output = """IF (ITER.EQ.LAST) THEN
        DO K=2,N2
         DO J=2,M2
           DO I=2,L2
              WSUM(K)=WSUM(K)+W(I,J,K)*ARZ(I,J)
              TSUM(K)=TSUM(K)+T(I,J,K)*W(I,J,K)*ARZ(I,J)
              AREA(K)=AREA(K)+ARZ(I,J)
              WBAR(K)=WSUM(K)/AREA(K)
           ENDDO
         ENDDO
        ENDDO
        DO K=2,N2
           TB(K)=TSUM(K)/(WSUM(K)+SMALL)
        ENDDO
        DO K=2,N2
          DO J=2,M2
            DO I=2,L2
               T(I,J,K)=(T(I,J,K)-TW)/(TB(K)-TW)
               T(I,J,N1)=T(I,J,N2)
               W(I,J,K)=W(I,J,K)/WBAR(K)
               W(I,J,N1)=W(I,J,N2)
            ENDDO
          ENDDO
        ENDDO
       ENDIF"""
        self.output_monitor = """IF (ITER.EQ.{iteration}) THEN
      DO N=1,4
      KSOLVE(N)=0
      END DO
      KSOLVE(5)=1
      END IF
      DO IUNIT=IU1,IU2
         IF(ITER.EQ.0) WRITE(IUNIT,210)
  210    FORMAT({format_string})
         {write_string}
  220    FORMAT(2X,I4,2X,1P{len_format_values}E10.2)
      ENDDO"""

    def translate_grid_section(self, grid, header):
        """
        Tranduce la sección GRID del JSON a líneas de código F90, incluyendo los datos de HEADER.

        :param grid: Diccionario con la información de la sección GRID del JSON.
        :param header: Diccionario con la información de la sección HEADER del JSON.
        :return: Lista de líneas de código F90 correspondientes a la sección GRID y HEADER.
        """
        f90_lines = ["ENTRY GRID"]
        # HEADER section
        for key, f90_key in [("le_titulosimu", "HEADER"), ("le_tituloimpre", "PRINTF"), ("le_titulograf", "PLOTF")]:
            if key in header:
                f90_lines.append(f"{f90_key}='{header[key]}'")
        mode = {"Cartesianas": 1, "Cilindricas": 2}.get(grid.get("cb_tipocoord", "Cartesianas"))
        kcy = 1 if grid.get("cb_tiposistema", "Cerrado") == "Abierto" else 0
        f90_lines.append(f"MODE={mode} ; KCY={kcy}")
        coord_vars = {
            1: {"XL": "le_xlon", "YL": "le_ylon", "ZL": "le_zlon"},
            2: {"XL": "le_titalon", "R(1)": "le_rini", "YL": "le_rlon", "ZL": "le_zloncil"},
        }
        nvc_vars = {
            1: {"NCVLX": "le_nvcx", "NCVLY": "le_nvcy", "NCVLZ": "le_nvcz"},
            2: {"NCVLX": "le_nvctita", "NCVLY": "le_nvcr", "NCVLZ": "le_nvczcil"},
        }
        for group in (coord_vars, nvc_vars):
            group_lines = []
            for var, key in group[mode].items():
                if key and key in grid:
                    group_lines.append(f"{var}={grid[key]}")
            if group_lines:
                f90_lines.append(" ; ".join(group_lines))
        grid_function = "ZGRID" if grid.get("cb_tipozonas", "") == "Varias zonas" else "EZGRID"
        f90_lines.append(f"CALL {grid_function}")
        f90_lines.append("RETURN")
        return f90_lines

    def translate_begin_section(self, grid, variables, bound, values, output):
        f90_lines = ["ENTRY BEGIN"]

        for num in range(1, 12):
            if num in self.custom_titles:
                var_title = self.custom_titles[num]
            else:
                var_title = variables.get(f"le_var_title{num}")
            if var_title is not None and var_title != "":
                f90_lines.append(f"TITLE({num})='{var_title}'")

        for num in range(1, 11):
            if variables.get(f"chb_ksolve{num}") == 2:
                f90_lines.append(f"KSOLVE({num})=1")

        for num in range(1, 12):
            if variables.get(f"chb_kprint{num}") == 2:
                f90_lines.append(f"KPRINT({num})=1")

        for num in range(1, 12):
            var_name = f"le_var_title{num}"
            if var_name in values:
                num = int("".join(filter(str.isdigit, var_name)))
                if values[var_name].get("chb_iborx") == 2:
                    f90_lines.append(f"IBORX({num})=1")
                if values[var_name].get("chb_ibory") == 2:
                    f90_lines.append(f"IBORY({num})=1")
                if values[var_name].get("chb_iborz") == 2:
                    f90_lines.append(f"IBORZ({num})=1")
                if values[var_name].get("chb_ipun") == 2:
                    f90_lines.append(f"IPUN({num})=1")
                ixyz = values[var_name].get("le_ixyz")
                if ixyz is not None and ixyz != "":
                    f90_lines.append(f"IXYZ({num})={ixyz}")
                kblock = values[var_name].get("le_kblock")
                if kblock is not None and kblock != "":
                    f90_lines.append(f"KBLOC({num})={kblock}")

        for num in range(1, 12):
            relax = variables.get(f"le_relax{num}")
            if relax is not None and relax != "":
                f90_lines.append(f"RELAX({num})={relax}")
        tolerance = variables.get("le_tol")
        if tolerance is not None and tolerance != "":
            f90_lines.append(f"TOL={tolerance}")
        kord = 2 if grid.get("cb_trataborde", "Esquema de bajo orden") == "Esquema de alto orden" else 1
        last = int(output.get("le_last", 5))
        f90_lines.append(f"KORD={kord}")
        f90_lines.append(f"LAST={last}")

        variables = {
            "le_var_title5": "T",
            "le_var_title1": "U",
            "le_var_title2": "V",
            "le_var_title3": "W",
        }
        #### le_general_value
        for var_title, var_name in variables.items():
            if var_title in values and "le_general_value" in values[var_title]:
                f90_lines.extend(
                    [
                        "DO I=1,L1",
                        f"{i}DO J=1,M1",
                        f"{i}{i}DO K=1,N1",
                        f"{i}{i}{i}{var_name}(I,J,K)={values[var_title]['le_general_value']}",
                        f"{i}{i}ENDDO",
                        f"{i}ENDDO",
                        "ENDDO",
                    ]
                )

        #### le_local_value
        for var_title, var_name in variables.items():
            if var_title in values:
                regions = {key: value for key, value in values[var_title].items() if isinstance(value, dict)}
                for region, region_values in regions.items():
                    if "le_local_value" in region_values:
                        volumes = {key: value for key, value in region_values.items() if isinstance(value, dict)}
                        for volume, volume_values in volumes.items():
                            if all(key in volume_values for key in self.volume_widgets):
                                x_start, x_end, y_start, y_end, z_start, z_end = self.adjust_volume_limits(
                                    volume_values
                                )
                                print(values[var_title])
                                f90_lines.extend(
                                    [
                                        f"DO I={x_start},{x_end}",
                                        f"{i}DO J={y_start},{y_end}",
                                        f"{i}{i}DO K={z_start},{z_end}",
                                        f"{i}{i}{i}{var_name}(I,J,K)={region_values['le_local_value']}",
                                        f"{i}{i}ENDDO",
                                        f"{i}ENDDO",
                                        "ENDDO",
                                    ]
                                )
                            else:
                                f90_lines.extend(
                                    [
                                        "DO I=1,L1",
                                        f"{i}DO J=1,M1",
                                        f"{i}{i}DO K=1,N1",
                                        f"{i}{i}{i}{var_name}(I,J,K)={region_values['le_local_value']}",
                                        f"{i}{i}ENDDO",
                                        f"{i}ENDDO",
                                        "ENDDO",
                                    ]
                                )

        for boundary, patchs in bound.items():
            for patch, patch_values in patchs.items():
                transversal_var, vertical_var, indexes = self.loop_mapping2[boundary]
                velocity_u = patch_values.get("le_value_veloc_u", None)
                velocity_v = patch_values.get("le_value_veloc_v", None)
                velocity_w = patch_values.get("le_value_veloc_w", None)

                if any([velocity_u, velocity_v, velocity_w]):
                    transversal_start = patch_values.get("le_transversal_start", 1)
                    transversal_end = patch_values.get("le_transversal_end", None)
                    vertical_start = patch_values.get("le_vertical_start", 1)
                    vertical_end = patch_values.get("le_vertical_end", None)
                    print("XXX", boundary, patch, transversal_start, transversal_end, vertical_start, vertical_end)
                    transversal_start, transversal_end, vertical_start, vertical_end = self.adjust_border_limits(
                        transversal_start, transversal_end, vertical_start, vertical_end, boundary
                    )
                    print("XXX", boundary, patch, transversal_start, transversal_end, vertical_start, vertical_end)
                    f90_lines.extend(
                        [
                            f"DO {transversal_var}={transversal_start},{transversal_end}",
                            f"{i}DO {vertical_var}={vertical_start},{vertical_end}",
                        ]
                    )
                    if velocity_u:
                        f90_lines.append(f"{i}{i}U{indexes}={velocity_u}")
                    if velocity_v:
                        f90_lines.append(f"{i}{i}V{indexes}={velocity_v}")
                    if velocity_w:
                        f90_lines.append(f"{i}{i}W{indexes}={velocity_w}")
                    f90_lines.extend(
                        [
                            f"{i}ENDDO",
                            "ENDDO",
                        ]
                    )

                variables = {key: value for key, value in patch_values.items() if isinstance(value, dict)}
                for variable, values in variables.items():
                    value_condition = values.get("chb_value", None)
                    border_value = values.get("le_value", None)
                    if value_condition == 2 and border_value and variable == "le_var_title5":
                        transversal_start = patch_values.get("le_transversal_start", 1)
                        transversal_end = patch_values.get("le_transversal_end", None)
                        vertical_start = patch_values.get("le_vertical_start", 1)
                        vertical_end = patch_values.get("le_vertical_end", None)
                        print("XXX", boundary, patch, transversal_start, transversal_end, vertical_start, vertical_end)
                        transversal_start, transversal_end, vertical_start, vertical_end = self.adjust_border_limits(
                            transversal_start, transversal_end, vertical_start, vertical_end, boundary
                        )
                        print("XXX", boundary, patch, transversal_start, transversal_end, vertical_start, vertical_end)
                        f90_lines.extend(
                            [
                                f"DO {transversal_var}={transversal_start},{transversal_end}",
                                f"{i}DO {vertical_var}={vertical_start},{vertical_end}",
                            ]
                        )
                        if border_value:
                            f90_lines.append(f"{i}{i}T{indexes}={border_value}")
                        f90_lines.extend(
                            [
                                f"{i}ENDDO",
                                "ENDDO",
                            ]
                        )
        # for boundary, patchs in bound.items():
        #     for patch, patch_values in patchs.items():
        #         velocity_u = patch_values.get("le_value_veloc_u", None)
        #         velocity_v = patch_values.get("le_value_veloc_v", None)
        #         velocity_w = patch_values.get("le_value_veloc_w", None)
        #         if any([velocity_u, velocity_v, velocity_w]):
        #             _, loop_var_1, loop_limit_1, loop_var_2, loop_limit_2, indexes = self.loop_mapping[boundary]
        #             f90_lines.extend(
        #                 [
        #                     f"DO {loop_var_1}=1,{loop_limit_1}",
        #                     f"{i}DO {loop_var_2}=1,{loop_limit_2}",
        #                 ]
        #             )
        #             if velocity_u:
        #                 f90_lines.append(f"{i}{i}U{indexes}={velocity_u}")
        #             if velocity_v:
        #                 f90_lines.append(f"{i}{i}V{indexes}={velocity_v}")
        #             if velocity_w:
        #                 f90_lines.append(f"{i}{i}W{indexes}={velocity_w}")
        #             f90_lines.extend(
        #                 [
        #                     f"{i}ENDDO",
        #                     "ENDDO",
        #                 ]
        #             )
        #         variables = {key: value for key, value in patch_values.items() if isinstance(value, dict)}
        #         for variable, variable_values in variables.items():
        #             value_condition = variable_values.get("chb_value", None)
        #             border_value = variable_values.get("le_value", None)
        #             if value_condition == 2 and border_value and variable == "le_var_title5":

        #                 x_start = int(sp.sympify(volume_values["le_x_start"]).evalf())
        #                 x_end = int(sp.sympify(volume_values["le_x_end"]).evalf())
        #                 y_start = int(sp.sympify(volume_values["le_y_start"]).evalf())
        #                 y_end = int(sp.sympify(volume_values["le_y_end"]).evalf())
        #                 z_start = int(sp.sympify(volume_values["le_z_start"]).evalf())
        #                 z_end = int(sp.sympify(volume_values["le_z_end"]).evalf())
        #                 f90_lines.append(f"{i}DO I={x_start},{x_end}")
        #                 f90_lines.append(f"{i}{i}DO J={y_start},{y_end}")
        #                 f90_lines.append(f"{I}DO K={z_start},{z_end}")

        #                 _, loop_var_1, loop_limit_1, loop_var_2, loop_limit_2, indexes = self.loop_mapping[boundary]
        #                 f90_lines.extend(
        #                     [
        #                         f"DO {loop_var_1}=1,{loop_limit_1}",
        #                         f"{i}DO {loop_var_2}=1,{loop_limit_2}",
        #                     ]
        #                 )
        #                 if border_value:
        #                     f90_lines.append(f"{i}{i}T{indexes}={border_value}")
        #                 f90_lines.extend(
        #                     [
        #                         f"{i}ENDDO",
        #                         "ENDDO",
        #                     ]
        #                 )
        f90_lines.append("RETURN")
        return f90_lines

    def translate_dense_section(self, dense):
        f90_lines = ["ENTRY DENSE"]
        f90_lines.append("RETURN")
        return f90_lines

    def translate_bound_section(self, bound):
        f90_lines = ["ENTRY BOUND"]
        for border_key, border_value in bound.items():
            for patch_key, patch_value in border_value.items():
                if isinstance(patch_value, dict) and patch_value.get("chb_inmass") == 2:
                    f90_lines.append(self.in_mass)
        f90_lines.append("RETURN")
        return f90_lines

    def translate_output_section(self, output):
        f90_lines = ["ENTRY OUTPUT"]
        monitored_variables = {}
        for key, value in output.items():
            if key in self.variable_map and all(k in value for k in ["le_x", "le_y", "le_z"]):
                var_name = self.variable_map[key]
                coords = f"({value['le_x']},{value['le_y']},{value['le_z']})"
                monitored_variables[var_name] = coords

        if monitored_variables:
            iteration = int(output.get("le_last", 5)) - 5
            standard_space = "5X"
            format_string = "3X,'ITER',"
            format_values = ["ITER"]
            for var, coords in monitored_variables.items():
                format_string += f"{standard_space},'{var}{coords}',"
                format_values.append(f"{var}{coords}")

            format_string += f"{standard_space},'SMAX',{standard_space},'SSUM'"
            format_values.extend(["SMAX", "SSUM"])
            format_string = format_string.rstrip(",")
            write_string = "WRITE(IUNIT,220) " + ",".join(format_values)
            f90_lines.append(
                self.output_monitor.format(
                    iteration=iteration,
                    format_string=format_string,
                    write_string=write_string,
                    len_format_values=len(format_values) - 1,
                )
            )

        if "checkBox_4" in output and output["checkBox_4"] == 2:
            f90_lines.append(self.dimensionless_output)
        f90_lines.append("RETURN")
        return f90_lines

    def translate_phi_section(self, bound, values):
        f90_lines = ["ENTRY PHI"]
        added_if = False

        for var, nf_value in self.variables_map.items():

            #### GAM(I,J,K)=le_k
            if var in values and "le_k" in values[var]:
                if not added_if:
                    f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                    added_if = True
                f90_lines.extend(
                    [
                        f"{i}DO I=2,L2",
                        f"{i}{i}DO J=2,M2",
                        f"{I}DO K=2,N2",
                        f"{I}{i}GAM(I,J,K)={values[var]['le_k']}",
                        f"{I}ENDDO",
                        f"{i}{i}ENDDO",
                        f"{i}ENDDO",
                    ]
                )

            #### SC(I,J,K)=le_local_sc y GAM(I,J,K)=le_local_k
            if var in values and "chb_local_value" in values[var]:
                regions = {key: value for key, value in values[var].items() if isinstance(value, dict)}
                for region, region_values in regions.items():
                    if "le_local_sc" in region_values or "le_local_k" in region_values:
                        volumes = {key: value for key, value in region_values.items() if isinstance(value, dict)}
                        for volume, volume_values in volumes.items():
                            if all(key in volume_values for key in self.volume_widgets):
                                if not added_if:
                                    f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                                    added_if = True
                                # x_start = int(sp.sympify(volume_values["le_x_start"]).evalf())
                                # x_end = int(sp.sympify(volume_values["le_x_end"]).evalf())
                                # y_start = int(sp.sympify(volume_values["le_y_start"]).evalf())
                                # y_end = int(sp.sympify(volume_values["le_y_end"]).evalf())
                                # z_start = int(sp.sympify(volume_values["le_z_start"]).evalf())
                                # z_end = int(sp.sympify(volume_values["le_z_end"]).evalf())
                                x_start, x_end, y_start, y_end, z_start, z_end = self.adjust_volume_limits(
                                    volume_values
                                )
                                f90_lines.append(f"{i}DO I={x_start},{x_end}")
                                f90_lines.append(f"{i}{i}DO J={y_start},{y_end}")
                                f90_lines.append(f"{I}DO K={z_start},{z_end}")
                                if "le_local_sc" in region_values:
                                    f90_lines.append(f"{I}{i}SC(I,J,K)={region_values['le_local_sc']}")
                                if "le_local_k" in region_values:
                                    f90_lines.append(f"{I}{i}GAM(I,J,K)={region_values['le_local_k']}")
                                f90_lines.append(f"{I}ENDDO")
                                f90_lines.append(f"{i}{i}ENDDO")
                                f90_lines.append(f"{i}ENDDO")
                            else:
                                if not added_if:
                                    f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                                    added_if = True
                                f90_lines.append(f"{i}DO I=2,L2")
                                f90_lines.append(f"{i}{i}DO J=2,M2")
                                f90_lines.append(f"{I}DO K=2,2")
                                if "le_local_sc" in region_values:
                                    f90_lines.append(f"{I}{i}SC(I,J,K)={region_values['le_local_sc']}")
                                if "le_local_k" in region_values:
                                    f90_lines.append(f"{I}{i}GAM(I,J,K)={region_values['le_local_k']}")
                                f90_lines.append(f"{I}ENDDO")
                                f90_lines.append(f"{i}{i}ENDDO")
                                f90_lines.append(f"{i}ENDDO")

            #### KBC=chb_flux, FLXC=le_value y FLXP=le_tempamb
            for boundary, patches in bound.items():
                for patch, patch_values in patches.items():
                    # TODO 1
                    transversal_var, vertical_var, indexes = self.loop_mapping2[boundary]
                    if var in patch_values and "chb_flux" in patch_values[var] and patch_values[var]["chb_flux"] == 2:
                        if not added_if:
                            f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                            added_if = True
                        # TODO 2
                        phi_var, loop_var_1, loop_limit_1, loop_var_2, loop_limit_2, _ = self.loop_mapping[boundary]
                        transversal_start = patch_values.get("le_transversal_start", 1)
                        transversal_end = patch_values.get("le_transversal_end", None)
                        vertical_start = patch_values.get("le_vertical_start", 1)
                        vertical_end = patch_values.get("le_vertical_end", None)
                        transversal_start, transversal_end, vertical_start, vertical_end = self.adjust_border_limits(
                            transversal_start, transversal_end, vertical_start, vertical_end, boundary
                        )
                        f90_lines.extend(
                            [
                                f"{i}DO {transversal_var}={transversal_start},{transversal_end}",
                                f"{i}{i}DO {vertical_var}={vertical_start},{vertical_end}",
                            ]
                        )
                        f90_lines.append(f"{I}KBC{phi_var}({transversal_var},{vertical_var})=2")
                        if "le_value" in patch_values[var]:
                            le_value = patch_values[var]["le_value"]
                            f90_lines.append(f"{I}FLXC{phi_var}({transversal_var},{vertical_var})={le_value}")
                        if "le_tempamb" in patch_values[var]:
                            le_tempamb = patch_values[var]["le_tempamb"]
                            f90_lines.append(f"{I}FLXP{phi_var}({transversal_var},{vertical_var})={le_tempamb}")
                        f90_lines.extend(
                            [
                                f"{i}{i}ENDDO",
                                f"{i}ENDDO",
                            ]
                        )
            if added_if:
                f90_lines.append("ENDIF")
                added_if = False

        f90_lines.append("RETURN")
        f90_lines.append("END")
        return f90_lines

    ################################################################################
    ##
    ## Funciones auxiliares
    ##
    ################################################################################

    def adjust_border_limits(self, transversal_start, transversal_end, vertical_start, vertical_end, boundary):
        """Ajusta los valores de inicio y fin según las condiciones especificadas."""
        valid_values = {"1", "2", "3", "L1", "L2", "L3", "M1", "M2", "M3", "N1", "N2", "N3"}
        valid_ends_x = {"L1", "L2", "L3", "1", "2", "3"}
        valid_ends_y = {"M1", "M2", "M3", "1", "2", "3"}
        valid_ends_z = {"N1", "N2", "N3", "1", "2", "3"}

        if "X" in boundary:
            transversal_end = transversal_end if transversal_end in valid_ends_y else "M1"
            vertical_end = vertical_end if vertical_end in valid_ends_z else "N1"
        elif "Y" in boundary:
            transversal_end = transversal_end if transversal_end in valid_ends_x else "L1"
            vertical_end = vertical_end if vertical_end in valid_ends_z else "N1"
        else:  # Z in boundary
            transversal_end = transversal_end if transversal_end in valid_ends_x else "L1"
            vertical_end = vertical_end if vertical_end in valid_ends_y else "M1"
        transversal_start = transversal_start if transversal_start in valid_values else "1"
        vertical_start = vertical_start if vertical_start in valid_values else "1"
        return transversal_start, transversal_end, vertical_start, vertical_end

    def adjust_volume_limits(self, volume_values):
        """
        Ajusta los valores de inicio y fin según las condiciones especificadas para los tres ejes (x, y, z).

        :param volume_values: Diccionario con los valores de los volúmenes.
        :return: Tupla con los valores de inicio y fin ajustados para x, y, z.
        """
        valid_starts = {"1", "2", "3", "L1", "L2", "L3", "M1", "M2", "M3", "N1", "N2", "N3"}
        valid_ends_x = {"L1", "L2", "L3", "1", "2", "3"}
        valid_ends_y = {"M1", "M2", "M3", "1", "2", "3"}
        valid_ends_z = {"N1", "N2", "N3", "1", "2", "3"}

        x_start = volume_values.get("le_x_start", "1")
        x_end = volume_values.get("le_x_end", "L1")
        y_start = volume_values.get("le_y_start", "1")
        y_end = volume_values.get("le_y_end", "M1")
        z_start = volume_values.get("le_z_start", "1")
        z_end = volume_values.get("le_z_end", "N1")

        x_start = x_start if x_start in valid_starts else "1"
        y_start = y_start if y_start in valid_starts else "1"
        z_start = z_start if z_start in valid_starts else "1"

        x_end = x_end if x_end in valid_ends_x else "L1"
        y_end = y_end if y_end in valid_ends_y else "M1"
        z_end = z_end if z_end in valid_ends_z else "N1"

        return x_start, x_end, y_start, y_end, z_start, z_end

    def generate_f90(self, config_manager):
        self.extend_f90(["SUBROUTINE ADAPT"])
        self.extend_f90(["INCLUDE '3DCOMMON.F90'", self.dimensionless_common])
        if "checkBox_4" in config_manager.output and config_manager.output["checkBox_4"] == 2:
            self.extend_f90([self.dimensionless])

        # HEADER y GRID section - Usando la función definida anteriormente
        grid_section_lines = self.translate_grid_section(config_manager.grid, config_manager.header)
        self.extend_f90(grid_section_lines)

        begin_section_lines = self.translate_begin_section(
            config_manager.grid,
            config_manager.variables,
            config_manager.bound,
            config_manager.values,
            config_manager.output,
        )
        self.extend_f90(begin_section_lines)

        dense_section_lines = self.translate_dense_section("")
        self.extend_f90(dense_section_lines)

        bound_section_lines = self.translate_bound_section(
            config_manager.bound,
        )
        self.extend_f90(bound_section_lines)

        output_section_lines = self.translate_output_section(config_manager.output)
        self.extend_f90(output_section_lines)

        phi_section_lines = self.translate_phi_section(config_manager.bound, config_manager.values)
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
    translator = F90Translator()
    f90_code = translator.generate_f90(json_data)
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
