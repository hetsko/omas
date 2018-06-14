# This file contains the list of automatic COCOS transformations
# COCOS signals candidates are generated by running utilities/generate_cocos_signals.py
# Running this script is useful to keep track of new signals that IMAS adds in new data structure releases
#
# In this file you are only allowed to edit/add entries to the `cocos_signals` dictionary
# The comments indicate `#[ADD_OR_DELETE_SUGGESTION]# MATCHING_SCORE # RATIONALE_FOR_ADD_OR_DELETE`
#
# Proceed as follows:
# 1. Edit transformations in this file (if a signal is missing, it can be added here)
# 2. Run `utilities/generate_cocos_signals.py` (which will update this same file)
# 3. Commit changes

cocos_signals = {}

# CORE_PROFILES
cocos_signals['core_profiles.profiles_1d.:.e_field_parallel']='IP'                                              # 3.000000 # e_field  parallel  [V.m^-1]
cocos_signals['core_profiles.profiles_1d.:.electrons.velocity_pol']='BP'                                        # 3.000000 # velocity  _pol  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.electrons.velocity_tor']='BT'                                        # 3.000000 # velocity  _tor  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.velocity_pol']='BP'                                            # 3.000000 # velocity  _pol  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.velocity_tor']='BT'                                            # 3.000000 # velocity  _tor  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.j_tor']='IP'                                                         # 3.000000 # j  _tor  [A/m^2]
cocos_signals['core_profiles.profiles_1d.:.momentum_tor']='BT'                                                  # 3.000000 # momentum  _tor  [kg.m^-1.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.state.:.velocity.parallel']='BT'                               # 2.875000 # velocity  parallel  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.state.:.velocity.poloidal']='BP'                               # 2.875000 # velocity  poloidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.state.:.velocity.toroidal']='BT'                               # 2.875000 # velocity  toroidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.state.:.velocity.parallel']='BT'                           # 2.875000 # velocity  parallel  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.state.:.velocity.poloidal']='BP'                           # 2.875000 # velocity  poloidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.state.:.velocity.toroidal']='BT'                           # 2.875000 # velocity  toroidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.velocity.parallel']='BT'                                       # 2.833333 # velocity  parallel  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.velocity.poloidal']='BP'                                       # 2.833333 # velocity  poloidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.velocity.toroidal']='BT'                                       # 2.833333 # velocity  toroidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.velocity.parallel']='BT'                                   # 2.833333 # velocity  parallel  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.velocity.poloidal']='BP'                                   # 2.833333 # velocity  poloidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.velocity.toroidal']='BT'                                   # 2.833333 # velocity  toroidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.electrons.velocity.parallel']='BT'                                   # 2.800000 # velocity  parallel  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.electrons.velocity.poloidal']='BP'                                   # 2.800000 # velocity  poloidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.electrons.velocity.toroidal']='BT'                                   # 2.800000 # velocity  toroidal  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.e_field.parallel']='IP'                                              # 2.750000 # e_field  parallel  [V.m^-1]
cocos_signals['core_profiles.profiles_1d.:.e_field.poloidal']='BP'                                              # 2.750000 # e_field  poloidal  [V.m^-1]
cocos_signals['core_profiles.profiles_1d.:.e_field.toroidal']='IP'                                              # 2.750000 # e_field  toroidal  [V.m^-1]
cocos_signals['core_profiles.global_quantities.current_bootstrap']='IP'                                         # 2.000000 # current  [A]
cocos_signals['core_profiles.global_quantities.current_non_inductive']='IP'                                     # 2.000000 # current  [A]
cocos_signals['core_profiles.global_quantities.ip']='IP'                                                        # 2.000000 # ip  [A]
cocos_signals['core_profiles.global_quantities.v_loop']='IP'                                                    # 2.000000 # v  [V]
cocos_signals['core_profiles.profiles_1d.:.current_parallel_inside']='?'                                 #[ADD?]# 2.000000 # current  [A]
cocos_signals['core_profiles.profiles_1d.:.grid.psi']='PSI'                                                     # 2.000000 # psi  [Wb]
cocos_signals['core_profiles.profiles_1d.:.j_bootstrap']='IP'                                                   # 2.000000 # j  [A/m^2]
cocos_signals['core_profiles.profiles_1d.:.j_non_inductive']='IP'                                               # 2.000000 # j  [A/m^2]
cocos_signals['core_profiles.profiles_1d.:.j_ohmic']='IP'                                                       # 2.000000 # j  [A/m^2]
cocos_signals['core_profiles.profiles_1d.:.j_total']='IP'                                                       # 2.000000 # j  [A/m^2]
cocos_signals['core_profiles.profiles_1d.:.q']='Q'                                                              # 2.000000 # q  [-]
cocos_signals['core_profiles.vacuum_toroidal_field.b0']='BT'                                                    # 2.000000 # b0  [T]
cocos_signals['core_profiles.profiles_1d.:.ion.:.state.:.velocity.diamagnetic']='BT'                            # 1.875000 # velocity  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.state.:.velocity.diamagnetic']='BT'                        # 1.875000 # velocity  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.ion.:.velocity.diamagnetic']='BT'                                    # 1.833333 # velocity  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.neutral.:.velocity.diamagnetic']='BT'                                # 1.833333 # velocity  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.electrons.velocity.diamagnetic']='BT'                                # 1.800000 # velocity  [m.s^-1]
cocos_signals['core_profiles.profiles_1d.:.e_field.diamagnetic']='IP'                                           # 1.750000 # e_field  [V.m^-1]

# CORE_SOURCES
cocos_signals['core_sources.source.:.global_quantities.:.current_parallel']='IP'                                           # 3.000000 # current  parallel  [A.m]
cocos_signals['core_sources.source.:.global_quantities.:.torque_tor']='BT'                                                 # 3.000000 # torque  _tor  [kg.m^2.s^-2]
cocos_signals['core_sources.source.:.profiles_1d.:.j_parallel']='IP'                                                       # 3.000000 # j  parallel  [A.m^-2]
cocos_signals['core_sources.source.:.profiles_1d.:.momentum_tor']='BT'                                                     # 3.000000 # momentum  _tor  [kg.m^-1.s^-2]
cocos_signals['core_sources.source.:.profiles_1d.:.ion.:.momentum.parallel']='?'                                    #[ADD?]# 2.875000 # momentum  parallel  [kg.m^-1.s^-2]
cocos_signals['core_sources.source.:.profiles_1d.:.ion.:.momentum.poloidal']='?'                                    #[ADD?]# 2.875000 # momentum  poloidal  [kg.m^-1.s^-2]
cocos_signals['core_sources.source.:.profiles_1d.:.ion.:.momentum.toroidal']='?'                                    #[ADD?]# 2.875000 # momentum  toroidal  [kg.m^-1.s^-2]
cocos_signals['core_sources.source.:.profiles_1d.:.ion.:.momentum.toroidal_decomposed.explicit_part']='?'           #[ADD?]# 2.666667 # momentum  toroidal  [W.m^-3]
cocos_signals['core_sources.source.:.profiles_1d.:.ion.:.momentum.toroidal_decomposed.implicit_part']='?'           #[ADD?]# 2.666667 # momentum  toroidal  [s^-1]
cocos_signals['core_sources.source.:.profiles_1d.:.current_parallel_inside']='IP'                                          # 2.000000 # current  [A]
cocos_signals['core_sources.source.:.profiles_1d.:.grid.psi']='PSI'                                                        # 2.000000 # psi  [Wb]
cocos_signals['core_sources.source.:.profiles_1d.:.torque_tor_inside']='BT'                                                # 2.000000 # torque  [kg.m^2.s^-2]
cocos_signals['core_sources.vacuum_toroidal_field.b0']='BT'                                                                # 2.000000 # b0  [T]
cocos_signals['core_sources.source.:.profiles_1d.:.ion.:.momentum.diamagnetic']='?'                                 #[ADD?]# 1.875000 # momentum  [kg.m^-1.s^-2]

# EQUILIBRIUM
cocos_signals['equilibrium.time_slice.:.global_quantities.magnetic_axis.b_field_tor']='BT'                                        # 4.000000 # b  b_field  _tor  [T]
cocos_signals['equilibrium.time_slice.:.profiles_2d.:.b_field_tor']='BT'                                                          # 4.000000 # b  b_field  _tor  [T]
cocos_signals['equilibrium.time_slice.:.ggd.:.b_field_tor.:.values']='BT'                                                         # 3.142857 # b  b_field  _tor  [T]
cocos_signals['equilibrium.time_slice.:.global_quantities.magnetic_axis.b_tor']='BT'                                              # 3.000000 # b  _tor  [T]
cocos_signals['equilibrium.time_slice.:.profiles_1d.f_df_dpsi']='F_FPRIME'                                                        # 3.000000 # f  _dpsi  [T^2.m^2/Wb]
cocos_signals['equilibrium.time_slice.:.profiles_1d.j_parallel']='IP'                                                             # 3.000000 # j  parallel  [A/m^2]
cocos_signals['equilibrium.time_slice.:.profiles_1d.j_tor']='IP'                                                                  # 3.000000 # j  _tor  [A/m^2]
cocos_signals['equilibrium.time_slice.:.profiles_2d.:.b_tor']='BT'                                                                # 3.000000 # b  _tor  [T]
cocos_signals['equilibrium.time_slice.:.profiles_2d.:.j_parallel']='IP'                                                           # 3.000000 # j  parallel  [A.m^-2]
cocos_signals['equilibrium.time_slice.:.profiles_2d.:.j_tor']='IP'                                                                # 3.000000 # j  _tor  [A.m^-2]
cocos_signals['equilibrium.time_slice.:.constraints.b_field_tor_vacuum_r.measured']='BT'                                          # 2.600000 # b  b_field  [T.m]
cocos_signals['equilibrium.time_slice.:.constraints.b_field_tor_vacuum_r.reconstructed']='BT'                                     # 2.600000 # b  b_field  [T.m]
cocos_signals['equilibrium.time_slice.:.constraints.q.:.position.phi']='?'                                                 #[ADD?]# 2.571429 # q  phi  [rad]
cocos_signals['equilibrium.time_slice.:.ggd.:.j_parallel.:.values']='IP'                                                          # 2.428571 # j  parallel  [A.m^-2]
cocos_signals['equilibrium.time_slice.:.ggd.:.j_tor.:.values']='IP'                                                               # 2.428571 # j  _tor  [A.m^-2]
cocos_signals['equilibrium.time_slice.:.boundary.b_flux_pol_norm']='?'                                                     #[ADD?]# 2.000000 # b  [-]
cocos_signals['equilibrium.time_slice.:.boundary.psi']='?'                                                                 #[ADD?]# 2.000000 # psi  [Wb]
cocos_signals['equilibrium.time_slice.:.boundary_separatrix.psi']='?'                                                      #[ADD?]# 2.000000 # psi  [Wb]
cocos_signals['equilibrium.time_slice.:.global_quantities.ip']='IP'                                                               # 2.000000 # ip  [A]
cocos_signals['equilibrium.time_slice.:.global_quantities.psi_axis']='PSI'                                                        # 2.000000 # psi  [Wb]
cocos_signals['equilibrium.time_slice.:.global_quantities.psi_boundary']='PSI'                                                    # 2.000000 # psi  [Wb]
cocos_signals['equilibrium.time_slice.:.global_quantities.q_95']='Q'                                                              # 2.000000 # q  [-]
cocos_signals['equilibrium.time_slice.:.global_quantities.q_axis']='Q'                                                            # 2.000000 # q  [-]
cocos_signals['equilibrium.time_slice.:.profiles_1d.b_average']='BT'                                                              # 2.000000 # b  [T]
cocos_signals['equilibrium.time_slice.:.profiles_1d.b_max']='BT'                                                                  # 2.000000 # b  [T]
cocos_signals['equilibrium.time_slice.:.profiles_1d.b_min']='BT'                                                                  # 2.000000 # b  [T]
cocos_signals['equilibrium.time_slice.:.profiles_1d.darea_dpsi']='dPSI'                                                           # 2.000000 # _dpsi  [m^2.Wb^-1]
cocos_signals['equilibrium.time_slice.:.profiles_1d.dpressure_dpsi']='dPSI'                                                       # 2.000000 # _dpsi  [Pa.Wb^-1]
cocos_signals['equilibrium.time_slice.:.profiles_1d.dpsi_drho_tor']='PSI'                                                         # 2.000000 # _tor  [Wb/m]
cocos_signals['equilibrium.time_slice.:.profiles_1d.dvolume_dpsi']='dPSI'                                                         # 2.000000 # _dpsi  [m^3.Wb^-1]
cocos_signals['equilibrium.time_slice.:.profiles_1d.f']='F'                                                                       # 2.000000 # f  [T.m]
cocos_signals['equilibrium.time_slice.:.profiles_1d.phi']='BT'                                                                    # 2.000000 # phi  [Wb]
cocos_signals['equilibrium.time_slice.:.profiles_1d.psi']='PSI'                                                                   # 2.000000 # psi  [Wb]
cocos_signals['equilibrium.time_slice.:.profiles_1d.q']='Q'                                                                       # 2.000000 # q  [-]
cocos_signals['equilibrium.time_slice.:.profiles_2d.:.phi']='BT'                                                                  # 2.000000 # phi  [Wb]
cocos_signals['equilibrium.time_slice.:.profiles_2d.:.psi']='PSI'                                                                 # 2.000000 # psi  [Wb]
cocos_signals['equilibrium.vacuum_toroidal_field.b0']='BT'                                                                        # 2.000000 # b0  [T]
cocos_signals['equilibrium.time_slice.:.constraints.ip.measured']='IP'                                                            # 1.800000 # ip  [A]
cocos_signals['equilibrium.time_slice.:.constraints.ip.reconstructed']='IP'                                                       # 1.800000 # ip  [A]
cocos_signals['equilibrium.time_slice.:.global_quantities.q_min.value']='Q'                                                       # 1.800000 # q  [-]
cocos_signals['equilibrium.time_slice.:.ggd.:.phi.:.values']='BT'                                                                 # 1.714286 # phi  [Wb]
cocos_signals['equilibrium.time_slice.:.ggd.:.psi.:.values']='PSI'                                                                # 1.714286 # psi  [Wb]
cocos_signals['equilibrium.time_slice.:.constraints.pf_current.:.measured']='?'                                            #[ADD?]# 1.666667 # current  [A]
cocos_signals['equilibrium.time_slice.:.constraints.pf_current.:.reconstructed']='?'                                       #[ADD?]# 1.666667 # current  [A]
cocos_signals['equilibrium.time_slice.:.constraints.q.:.measured']='Q'                                                            # 1.666667 # q  [-]
cocos_signals['equilibrium.time_slice.:.constraints.q.:.reconstructed']='Q'                                                       # 1.666667 # q  [-]
cocos_signals['equilibrium.time_slice.:.constraints.b_field_tor_vacuum_r.standard_deviation']='BT'                         #[DEL?]# -1.000000 # standard_deviation
cocos_signals['equilibrium.time_slice.:.constraints.ip.standard_deviation']='IP'                                           #[DEL?]# -1.000000 # standard_deviation
cocos_signals['equilibrium.time_slice.:.constraints.q.:.standard_deviation']='Q'                                           #[DEL?]# -1.000000 # standard_deviation

# INFO

# WALL
cocos_signals['wall.description_2d.:.vessel.unit.:.element.:.j_tor.data']='?'                   #[ADD?]# 2.777778 # j  _tor  [A]