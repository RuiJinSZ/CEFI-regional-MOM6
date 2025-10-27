import argparse


def parse_args() -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("count", type=int)
    return arg_parser.parse_args()


def generate_data_table(year: int):
    result = (
        f' "ATM", "p_surf",   "psl",    "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/psl_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010000-{year}12312100.padded.nc",      "bilinear",   1.0\n'
        f' "ATM", "p_bot",    "psl",    "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/psl_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010000-{year}12312100.padded.nc",      "bilinear",   1.0\n'
        f' "ATM", "t_bot",              "tas",      "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/tas_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010000-{year}12312100.padded.nc",      "bilinear",   1.0\n'
        f' "ATM", "sphum_bot",          "huss",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/huss_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010000-{year}12312100.padded.nc",     "bilinear",   1.0\n'
        f' "ATM", "u_bot",              "uas",      "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/uas_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010000-{year}12312100.padded.nc",      "bicubic",    1.0\n'
        f' "ATM", "v_bot",              "vas",      "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/vas_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010000-{year}12312100.padded.nc",      "bicubic",    1.0\n'
        f' "ATM", "z_bot",              "",         "",                        "bilinear",  10.0\n'
        f' "ATM", "gust",               "",         "",                        "bilinear",   1.0e-4\n'
        f' "ICE", "lw_flux_dn",         "rlds",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/rlds_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010130-{year}12312230.padded.nc",     "bilinear",   1.0\n'
        f' "ICE", "sw_flux_vis_dir_dn", "rsds",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/rsds_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010130-{year}12312230.padded.nc",     "bilinear",   0.285\n'
        f' "ICE", "sw_flux_vis_dif_dn", "rsds",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/rsds_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010130-{year}12312230.padded.nc",     "bilinear",   0.285\n'
        f' "ICE", "sw_flux_nir_dir_dn", "rsds",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/rsds_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010130-{year}12312230.padded.nc",     "bilinear",   0.215\n'
        f' "ICE", "sw_flux_nir_dif_dn", "rsds",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/rsds_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010130-{year}12312230.padded.nc",     "bilinear",   0.215\n'
        f' "ICE", "lprec",              "prra",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/prra_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010130-{year}12312230.padded.nc",     "bilinear",   1.0\n'
        f' "ICE", "fprec",              "prsn",     "/glade/work/rui/MOM6_global_forcing/JRA55-do_v1.5.0_padded/prsn_input4MIPs_atmosphericState_OMIP_MRI-JRA55-do-1-5-0_gr_{year}01010130-{year}12312230.padded.nc",     "bilinear",   1.0\n'
        f' "ICE", "calving",            "",         "",                        "none",       0.0\n'
        f' "ICE", "dhdt",               "",         "",                        "none",      80.0\n'
        f' "ICE", "dedt",               "",         "",                        "none",       2.0e-6\n'
        f' "ICE", "drdt",               "",         "",                        "none",      10.0\n'
        f' "LND", "t_surf",             "",         "",                        "none",     273.0\n'
        f' "LND", "t_ca",               "",         "",                        "none",     273.0\n'
        f' "LND", "q_ca",               "",         "",                        "none",       0.0\n'
        f' "LND", "rough_mom",          "",         "",                        "none",       0.01\n'
        f' "LND", "rough_heat",         "",         "",                        "none",       0.1\n'
        f' "LND", "albedo",             "",         "",                        "none",       0.1\n'
        f' "LND", "sphum_surf",         "",         "",                        "none",       0.0\n'
        f' "LND", "sphum_ca",           "",         "",                        "none",       0.0\n'
        f' "LND", "t_flux",             "",         "",                        "none",       0.0\n'
        f' "LND", "sphum_flux",         "",         "",                        "none",       0.0\n'
        f' "LND", "lw_flux",            "",         "",                        "none",       0.0\n'
        f' "LND", "sw_flux",            "",         "",                        "none",       0.0\n'
        f' "LND", "lprec",              "",         "",                        "none",       0.0\n'
        f' "LND", "fprec",              "",         "",                        "none",       0.0\n'
        f' "LND", "dhdt",               "",         "",                        "none",       5.0\n'
        f' "LND", "dedt",               "",         "",                        "none",       2e-6\n'
        f' "LND", "dedq",               "",         "",                        "none",       0.0\n'
        f' "LND", "drdt",               "",         "",                        "none",       5.0\n'
        f' "LND", "drag_q",             "",         "",                        "none",       0.0\n'
        f' "LND", "p_surf",             "",         "",                        "none",       1.e5\n'
        f'"ICE", "runoff",             "runoff",    "/glade/work/rui/MOM6_global_forcing/runoff.daitren.clim.1440x1080.v20180328.nc",   "none",       1.0\n'
        f'"OCN", "runoff_no3_flux_ice_ocn",   "NO3_CONC",   "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_ldon_flux_ice_ocn",  "LDON_CONC",  "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_sldon_flux_ice_ocn", "SLDON_CONC", "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_srdon_flux_ice_ocn", "SRDON_CONC", "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_ndet_flux_ice_ocn",  "NDET_CONC",  "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_po4_flux_ice_ocn",   "PO4_CONC",   "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_ldop_flux_ice_ocn",  "LDOP_CONC",  "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_sldop_flux_ice_ocn", "SLDOP_CONC", "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_srdop_flux_ice_ocn", "SRDOP_CONC", "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_pdet_flux_ice_ocn",  "PDET_CONC",  "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_fed_flux_ice_ocn",   "FED_CONC",   "/glade/work/rui/MOM6_global_forcing/RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc","none",1.0e-3\n'
        f'"OCN", "runoff_alk_flux_ice_ocn",   "",  "",                         "none", 0.42e-3\n'
        f'"OCN", "runoff_dic_flux_ice_ocn",   "",  "",                         "none", 0.32e-3\n'
        f'"OCN", "runoff_lith_flux_ice_ocn",  "",  "",                         "none", 13.0e-3\n'
        f'#\n'
        f'# jgj data table for o2 gas exchange\n'
        f'#\n'
        f'"ATM", "o2_flux_pcair_atm",  ""     , ""               , "none", 0.214\n'
        f'#\n'
        f'"ATM", "co2_flux_pcair_atm", "mole_fraction_of_carbon_dioxide_in_air", "/glade/work/rui/MOM6_global_forcing/mole_fraction_of_co2_extended_ssp245.nc", "bilinear", 1.0e-06\n'
        f'"ATM", "co2_bot",            "mole_fraction_of_carbon_dioxide_in_air", "/glade/work/rui/MOM6_global_forcing/mole_fraction_of_co2_extended_ssp245.nc", "bilinear", 1.0e-06\n'
        f'"ATM", "co2_dvmr_restore",   "mole_fraction_of_carbon_dioxide_in_air", "/glade/work/rui/MOM6_global_forcing/mole_fraction_of_co2_extended_ssp245.nc", "bilinear", 1.0e-06\n'
        f'#ocean-ice specific\n'
        f'"OCN", "dry_dep_fed_flux_ice_ocn",  "FLUX", "/glade/work/rui/MOM6_global_forcing/Soluble_Fe_Flux_AM4.nc", "bilinear", -1.0\n'
        f'"OCN", "dry_dep_lith_flux_ice_ocn", "FLUX_MINERAL", "/glade/work/rui/MOM6_global_forcing/Mineral_Flux_AM4.nc", "bilinear", -1.0\n'
        f'"OCN", "dry_dep_po4_flux_ice_ocn",  "FLUX_MINERAL", "/glade/work/rui/MOM6_global_forcing/Mineral_Flux_AM4.nc",  "bilinear", -4.0e-6\n'
        f'#"OCN", "wet_dep_no3_flux_ice_ocn",  "NO3_WET_DEP",  "./INPUT/depflux_total.mean.1860.nc",                "bilinear",  -1.0\n'
        f'#"OCN", "dry_dep_no3_flux_ice_ocn",  "NO3_DRY_DEP",  "./INPUT/depflux_total.mean.1860.nc",                "bilinear",  -1.0\n'
        f'#"OCN", "wet_dep_nh4_flux_ice_ocn",  "NH4_WET_DEP",  "./INPUT/depflux_total.mean.1860.nc",                "bilinear",  -1.0\n'
        f'#"OCN", "dry_dep_nh4_flux_ice_ocn",  "NH4_DRY_DEP",  "./INPUT/depflux_total.mean.1860.nc",                "bilinear",  -1.0\n'
        f'"OCN", "wet_dep_no3_flux_ice_ocn",  "wetnoy",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_wetnoy_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "dry_dep_no3_flux_ice_ocn",  "drynoy",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_drynoy_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "wet_dep_nh4_flux_ice_ocn",  "wetnh4",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_wetnh4_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "dry_dep_nh4_flux_ice_ocn",  "drynh4",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_drynh4_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "wet_dep_fe_flux_ice_ocn",  "wetfe",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_wetfe_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "dry_dep_fe_flux_ice_ocn",  "dryfe",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_dryfe_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "wet_dep_nh3_flux_ice_ocn",  "wetnh3",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_wetnh3_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "dry_dep_nh3_flux_ice_ocn",  "drynh3",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_drynh3_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "wet_dep_dust_flux_ice_ocn",  "wetdust",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_wetdust_climo_1993-2014.nc",                "bilinear",  -1.0\n'
        f'"OCN", "dry_dep_dust_flux_ice_ocn",  "drydust",    "/glade/work/rui/MOM6_global_forcing/esm4_deposition/esm4_drydust_climo_1993-2014.nc",                "bilinear",  -1.0\n'
    )
    with open("data_table", 'w') as f:
        print(result, end="", file=f)


def generate_diag_table(year: int):
    result = (
        'OM4_025_COBALTv3_jra55_const\n'
        f'{year} 1 1 0 0 0\n'
        '      # MOM6 ocean diagnostics files\n'
        '"ocean_daily",            1, "days",   1, "days", "time"\n'
        '"ocean_month",            1, "months", 1, "days", "time"\n'
        '"ocean_month_z",          1, "months", 1, "days", "time"\n'
        '"ocean_annual",          12, "months", 1, "days", "time"\n'
        '"ocean_annual_z",        12, "months", 1, "days", "time"\n'
        '"ocean_static",          -1, "months", 1, "days", "time"\n'
        '# ocean static information\n'
        '"ocean_model", "areacello",   "areacello",   "ocean_static", "all", "none", "none", 2 # Ocean Grid-Cell Area\n'
        '"ocean_model", "deptho",      "deptho",      "ocean_static", "all", "none", "none", 2 # Sea Floor Depth\n'
        '"ocean_model", "sftof",       "sftof",       "ocean_static", "all", "none", "none", 2 # Sea Area Fraction\n'
        '"ocean_model", "Coriolis",    "Coriolis",    "ocean_static", "all", "none", "none", 2 # Coriolis parameter at corner (Bu) points\n'
        '"ocean_model", "geolon",      "geolon",      "ocean_static", "all", "none", "none", 2 # Longitude of tracer (T) points\n'
        '"ocean_model", "geolat",      "geolat",      "ocean_static", "all", "none", "none", 2 # Latitude of tracer (T) points\n'
        '"ocean_model", "geolon_c",    "geolon_c",    "ocean_static", "all", "none", "none", 2 # Longitude of corner (Bu) points\n'
        '"ocean_model", "geolat_c",    "geolat_c",    "ocean_static", "all", "none", "none", 2 # Latitude of corner (Bu) points\n'
        '"ocean_model", "geolon_u",    "geolon_u",    "ocean_static", "all", "none", "none", 2 # Longitude of zonal velocity (Cu) points\n'
        '"ocean_model", "geolat_u",    "geolat_u",    "ocean_static", "all", "none", "none", 2 # Latitude of zonal velocity (Cu) points\n'
        '"ocean_model", "geolon_v",    "geolon_v",    "ocean_static", "all", "none", "none", 2 # Longitude of meridional velocity (Cv) points\n'
        '"ocean_model", "geolat_v",    "geolat_v",    "ocean_static", "all", "none", "none", 2 # Latitude of meridional velocity (Cv) points\n'
        '"ocean_model", "wet",         "wet",         "ocean_static", "all", "none", "none", 2 # 0 if land, 1 if ocean at tracer points\n'
        '"ocean_model", "wet_c",       "wet_c",       "ocean_static", "all", "none", "none", 2 # 0 if land, 1 if ocean at corner (Bu) points\n'
        '"ocean_model", "wet_u",       "wet_u",       "ocean_static", "all", "none", "none", 2 # 0 if land, 1 if ocean at zonal velocity (Cu) points\n'
        '"ocean_model", "wet_v",       "wet_v",       "ocean_static", "all", "none", "none", 2 # 0 if land, 1 if ocean at meridional velocity (Cv) points\n'
        '"ocean_model", "dxt",         "dxt",         "ocean_static", "all", "none", "none", 2 # Delta(x) at thickness/tracer points (meter)\n'
        '"ocean_model", "dyt",         "dyt",         "ocean_static", "all", "none", "none", 2 # Delta(y) at thickness/tracer points (meter)\n'
        '"ocean_model", "dxCu",        "dxCu",        "ocean_static", "all", "none", "none", 2 # Delta(x) at u points (meter)\n'
        '"ocean_model", "dyCu",        "dyCu",        "ocean_static", "all", "none", "none", 2 # Delta(y) at u points (meter)\n'
        '"ocean_model", "dxCv",        "dxCv",        "ocean_static", "all", "none", "none", 2 # Delta(x) at v points (meter)\n'
        '"ocean_model", "dyCv",        "dyCv",        "ocean_static", "all", "none", "none", 2 # Delta(y) at v points (meter)\n'
        '"ocean_model", "areacello_cu","areacello_cu","ocean_static", "all", "none", "none", 2 # Ocean Grid-Cell Area\n'
        '"ocean_model", "areacello_cv","areacello_cv","ocean_static", "all", "none", "none", 2 # Ocean Grid-Cell Area\n'
        '"ocean_model", "areacello_bu","areacello_bu","ocean_static", "all", "none", "none", 2 # Ocean Grid-Cell Area\n'
        '# Daily ocean\n'
        '"ocean_model",   "ssh",          "ssh",              "ocean_daily",         "all", "mean", "none",2 # Sea Surface Height\n'
        '"ocean_model",   "ssh",          "sshmin",           "ocean_daily",         "all", "min",  "none",2 # Sea Surface Height\n'
        '"ocean_model",   "ssh",          "sshmax",           "ocean_daily",         "all", "max",  "none",2 # Sea Surface Height\n'
        '"ocean_model",   "tos",          "tos",              "ocean_daily",         "all", "mean", "none",2 # Sea Surface Temperature\n'
        '"ocean_model",   "tos",          "tosmin",           "ocean_daily",         "all", "min" , "none",2 # Sea Surface Temperature\n'
        '"ocean_model",   "tos",          "tosmax",           "ocean_daily",         "all", "max" , "none",2 # Sea Surface Temperature\n'
        '"ocean_model",   "tossq",        "tossq",            "ocean_daily",         "all", "mean", "none",2 # Square of Sea Surface Temperature\n'
        '"ocean_model",   "tob",          "tob",              "ocean_daily",         "all", "mean", "none",2 # Sea Water Potential Temperature at Sea Floor\n'
        '"ocean_model",   "sos",          "sos",              "ocean_daily",         "all", "mean", "none",2 # Sea Surface Salinity\n'
        '"ocean_model",   "sossq",        "sossq",            "ocean_daily",         "all", "mean", "none",2 # Square of Sea Surface Salinity\n'
        '"ocean_model",   "sob",          "sob",              "ocean_daily",         "all", "mean", "none",2 # Sea Water Salinity at Sea Floor\n'
        '"ocean_model",   "SSU",          "ssu",              "ocean_daily",         "all", "mean", "none",2 # Sea Surface Zonal Velocity\n'
        '"ocean_model",   "SSV",          "ssv",              "ocean_daily",         "all", "mean", "none",2 # Sea Surface Meridional Velocity\n'
        '"ocean_model",   "ePBL_h_ML",    "omldamax",         "ocean_daily",         "all", "max",  "none",2 # Surface boundary layer depth\n'
        '# Monthly ocean in z* coordinates\n'
        '"ocean_model_z", "volcello",     "volcello",         "ocean_month_z",       "all", "mean", "none",2 # Ocean grid-cell volume\n'
        '"ocean_model_z", "thetao",       "thetao",           "ocean_month_z",       "all", "mean", "none",2 # Sea Water Potential Temperature\n'
        '"ocean_model_z", "so",           "so",               "ocean_month_z",       "all", "mean", "none",2 # Sea Water Salinity\n'
        '"ocean_model_z", "uo",           "uo",               "ocean_month_z",       "all", "mean", "none",2 # Sea Water X Velocity\n'
        '"ocean_model_z", "vo",           "vo",               "ocean_month_z",       "all", "mean", "none",2 # Sea Water Y Velocity\n'
        '"ocean_model_z", "umo",          "umo",              "ocean_month_z",       "all", "mean", "none",2 # Ocean Mass X Transport\n'
        '"ocean_model_z", "vmo",          "vmo",              "ocean_month_z",       "all", "mean", "none",2 # Ocean Mass Y Transport\n'
        '"ocean_model_z", "uhml",         "uhml",             "ocean_month_z",       "all", "mean", "none",2 # Zonal Thickness Flux to Restratify Mixed Layer\n'
        '"ocean_model_z", "vhml",         "vhml",             "ocean_month_z",       "all", "mean", "none",2 # Meridional Thickness Flux to Restratify Mixed Layer\n'
        '"ocean_model_z", "rhopot0",      "rhopot0",          "ocean_month_z",       "all", "mean", "none",2 # Potential density referenced to surface\n'
        '"ocean_model_z", "rhoinsitu",    "rhoinsitu",        "ocean_month_z",       "all", "mean", "none",2 # In situ density\n'
        '# Monthly ocean\n'
        '"ocean_model",   "pbo",          "pbo",              "ocean_month",         "all", "mean", "none",2 # Sea Water Pressure at Sea Floor\n'
        '"ocean_model",   "zos",          "zos",              "ocean_month",         "all", "mean", "none",2 # Sea surface height above geoid\n'
        '"ocean_model",   "ssh",          "ssh",              "ocean_month",         "all", "mean", "none",2 # Sea Surface Height\n'
        '"ocean_model",   "zossq",        "zossq",            "ocean_month",         "all", "mean", "none",2 # Square of sea surface height above geoid\n'
        '"ocean_model",   "tos",          "tos",              "ocean_month",         "all", "mean", "none",2 # Sea Surface Temperature\n'
        '"ocean_model",   "tossq",        "tossq",            "ocean_month",         "all", "mean", "none",2 # Square of Sea Surface Temperature\n'
        '"ocean_model",   "tob",          "tob",              "ocean_month",         "all", "mean", "none",2 # Sea Water Potential Temperature at Sea Floor\n'
        '"ocean_model",   "sos",          "sos",              "ocean_month",         "all", "mean", "none",2 # Sea Surface Salinity\n'
        '"ocean_model",   "sossq",        "sossq",            "ocean_month",         "all", "mean", "none",2 # Square of Sea Surface Salinity\n'
        '"ocean_model",   "sob",          "sob",              "ocean_month",         "all", "mean", "none",2 # Sea Water Salinity at Sea Floor\n'
        '# Annual ocean in z* coordinates\n'
        '"ocean_model_z", "volcello",     "volcello",         "ocean_annual_z",      "all", "mean", "none",2 # Ocean grid-cell volume\n'
        '"ocean_model_z", "thetao",       "thetao",           "ocean_annual_z",      "all", "mean", "none",2 # Sea Water Potential Temperature\n'
        '"ocean_model_z", "thetao_xyave", "thetao_xyave",     "ocean_annual_z",      "all", "mean", "none",2 # Sea Water Potential Temperature\n'
        '"ocean_model_z", "so",           "so",               "ocean_annual_z",      "all", "mean", "none",2 # Sea Water Salinity\n'
        '"ocean_model_z", "so_xyave",     "so_xyave",         "ocean_annual_z",      "all", "mean", "none",2 # Sea Water Salinity\n'
        '"ocean_model_z", "uo",           "uo",               "ocean_annual_z",      "all", "mean", "none",2 # Sea Water X Velocity\n'
        '"ocean_model_z", "vo",           "vo",               "ocean_annual_z",      "all", "mean", "none",2 # Sea Water Y Velocity\n'
        '# Annual ocean\n'
        '"ocean_model",   "thetao",       "thetao",           "ocean_annual",        "all", "mean", "none",2 # Sea Water Potential Temperature\n'
        '"ocean_model",   "tos",          "tos",              "ocean_annual",        "all", "mean", "none",2 # Sea Surface Temperature\n'
        '"ocean_model",   "tossq",        "tossq",            "ocean_annual",        "all", "mean", "none",2 # Square of Sea Surface Temperature\n'
        '"ocean_model",   "tob",          "tob",              "ocean_annual",        "all", "mean", "none",2 # Sea Water Potential Temperature at Sea Floor\n'
        '"ocean_model",   "so",           "so",               "ocean_annual",        "all", "mean", "none",2 # Sea Water Salinity\n'
        '"ocean_model",   "sos",          "sos",              "ocean_annual",        "all", "mean", "none",2 # Sea Surface Salinity\n'
        '"ocean_model",   "sossq",        "sossq",            "ocean_annual",        "all", "mean", "none",2 # Square of Sea Surface Salinity\n'
        '"ocean_model",   "sob",          "sob",              "ocean_annual",        "all", "mean", "none",2 # Sea Water Salinity at Sea Floor\n'
        '"ocean_model",   "tos",              "tos_max",      "ocean_annual",        "all", "max",  "none",2 # Sea Surface Temperature\n'
        '"ocean_model",   "tos",              "tos_min",      "ocean_annual",        "all", "min",  "none",2 # Sea Surface Temperature\n'
        '# CEFI OBGC/COBALT diagnostics files \n'
        '"ocean_cobalt_sfc",             1, "months", 1, "days", "time"\n'
        '"ocean_cobalt_btm",             1, "months", 1, "days", "time"\n'
        '"ocean_cobalt_tracers_int",     1, "months", 1, "days", "time"\n'
        '"ocean_cobalt_fluxes_int",      1, "months", 1, "days", "time"\n'
        '"ocean_cobalt_fdet_100",        1, "months", 1, "days", "time"\n'
        '"ocean_cobalt_tracers_month_z", 1, "months", 1, "days", "time"\n'
        '"ocean_cobalt_daily_2d",       24, "hours",  1, "days", "time"\n'
        '"ocean_cobalt_omip_sfc",             1, "months", 1, "days", "time"\n'
        '"ocean_cobalt_omip_2d",              1, "months", 1, "days", "time"\n'
        '# Daily COBALT 2D fileds\n'
        '"generic_cobalt", "phos",             "phos",             "ocean_cobalt_daily_2d","all","mean","none",2 # Surface pH\n'
        '"generic_cobalt", "no3os",            "no3os",            "ocean_cobalt_daily_2d","all","mean","none",2 # Surface Dissolved Nitrate Concentration\n'
        '"generic_cobalt", "pco2surf",         "pco2surf",         "ocean_cobalt_daily_2d","all","mean","none",2 # Oceanic pCO2\n'
        '"generic_cobalt", "mesozoo_200",      "mesozoo_200",      "ocean_cobalt_daily_2d","all","mean","none",2 # Mesozooplankton biomass, 200m integral\n'
        '"generic_cobalt", "btm_o2",           "btm_o2",           "ocean_cobalt_daily_2d","all","mean","none",2 # Bottom Oxygen\n'
        '"generic_cobalt", "btm_co3_sol_arag", "btm_co3_sol_arag", "ocean_cobalt_daily_2d","all","mean","none",2 # Bottom Aragonite Solubility\n'
        '"generic_cobalt", "btm_co3_sol_calc", "btm_co3_sol_calc", "ocean_cobalt_daily_2d","all","mean","none",2 # Bottom Calcite Solubility\n'
        '"generic_cobalt", "btm_co3_ion",      "btm_co3_ion",      "ocean_cobalt_daily_2d","all","mean","none",2 # Bottom Carbonate Ion\n'
        '"generic_cobalt", "btm_htotal",       "btm_htotal",       "ocean_cobalt_daily_2d","all","mean","none",2 # Bottom Htotal\n'
        '"generic_cobalt","chlos",             "chlos",            "ocean_cobalt_daily_2d","all","mean","none",2 # Surface Mass Concentration of Total Phytoplankton expressed as Chlorophyll in sea water\n'
        '"generic_cobalt","phycos",            "phycos",           "ocean_cobalt_daily_2d","all","mean","none",2 # Surface Phytoplankton Carbon Concentration\n'
        '# Monthly COBALT surface fields (2D)\n'
        '"generic_cobalt","dic_csurf",         "dic_csurf",        "ocean_cobalt_sfc","all","mean","none",2 # Ocean surface gas concentration of dic\n'
        '"generic_cobalt","dic_deltap",        "dic_deltap",       "ocean_cobalt_sfc","all","mean","none",2 # Ocn minus Atm pressure of dic\n'
        '"generic_cobalt","dic_kw",            "dic_kw",           "ocean_cobalt_sfc","all","mean","none",2 # Gas Exchange piston velocity for dic\n'
        '"generic_cobalt","dic_sc_no",         "dic_sc_no",        "ocean_cobalt_sfc","all","mean","none",2 # Ocean surface Schmidt Number for dic\n'
        '"generic_cobalt","pco2surf",          "pco2surf",         "ocean_cobalt_sfc","all","mean","none",2 # Oceanic pCO2\n'
        '"generic_cobalt","o2_alpha",          "o2_alpha",         "ocean_cobalt_sfc","all","mean","none",2 # Atmospheric saturation for o2\n'
        '"generic_cobalt","o2_csurf",          "o2_csurf",         "ocean_cobalt_sfc","all","mean","none",2 # Ocean surface gas concentration of o2\n'
        '"generic_cobalt","o2_deltap",         "o2_deltap",        "ocean_cobalt_sfc","all","mean","none",2 # Ocn minus Atm pressure of o2\n'
        '"generic_cobalt","o2_kw",             "o2_kw",            "ocean_cobalt_sfc","all","mean","none",2 # Gas Exchange piston velocity for o2\n'
        '"generic_cobalt","o2_sc_no",          "o2_sc_no",         "ocean_cobalt_sfc","all","mean","none",2 # Ocean surface Schmidt Number for o2\n'
        '"generic_cobalt","dic_stf_gas",       "dic_stf_gas",      "ocean_cobalt_sfc","all","mean","none",2 # Gas exchange flux of dic into Ocean Surface\n'
        '"generic_cobalt","o2_stf_gas",        "o2_stf_gas",       "ocean_cobalt_sfc","all","mean","none",2 # Gas exchange flux of o2 into Ocean Surface\n'
        '"generic_cobalt","dep_dry_fed",       "dep_dry_fed",      "ocean_cobalt_sfc","all","mean","none",2 # Dry Deposition of Iron to the ocean\n'
        '"generic_cobalt","dep_dry_nh4",       "dep_dry_nh4",      "ocean_cobalt_sfc","all","mean","none",2 # Dry Deposition of Ammonia to the ocean\n'
        '"generic_cobalt","dep_dry_no3",       "dep_dry_no3",      "ocean_cobalt_sfc","all","mean","none",2 # Dry Deposition of Nitrate to the ocean\n'
        '"generic_cobalt","dep_dry_po4",       "dep_dry_po4",      "ocean_cobalt_sfc","all","mean","none",2 # Dry Deposition of Phosphate to the ocean\n'
        '"generic_cobalt","dep_dry_lith",      "dep_dry_lith",     "ocean_cobalt_sfc","all","mean","none",2 # Dry Deposition of Lithogenic Material\n'
        '"generic_cobalt","dep_wet_fed",       "dep_wet_fed",      "ocean_cobalt_sfc","all","mean","none",2 # Wet Deposition of Iron to the ocean\n'
        '"generic_cobalt","dep_wet_nh4",       "dep_wet_nh4",      "ocean_cobalt_sfc","all","mean","none",2 # Wet Deposition of Ammonia to the ocean\n'
        '"generic_cobalt","dep_wet_no3",       "dep_wet_no3",      "ocean_cobalt_sfc","all","mean","none",2 # Wet Deposition of Nitrate to the ocean\n'
        '"generic_cobalt","dep_wet_lith",      "dep_wet_lith",     "ocean_cobalt_sfc","all","mean","none",2 # Wet Deposition of Lithogenic Material\n'
        '"generic_cobalt","runoff_flux_alk",   "runoff_flux_alk",  "ocean_cobalt_sfc","all","mean","none",2 # Alkalinity runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_dic",   "runoff_flux_dic",  "ocean_cobalt_sfc","all","mean","none",2 # Dissolved Inorganic Carbon runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_fed",   "runoff_flux_fed",  "ocean_cobalt_sfc","all","mean","none",2 # Iron runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_lith",  "runoff_flux_lith", "ocean_cobalt_sfc","all","mean","none",2 # Lithogenic runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_no3",   "runoff_flux_no3",  "ocean_cobalt_sfc","all","mean","none",2 # Nitrate runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_ldon",  "runoff_flux_ldon", "ocean_cobalt_sfc","all","mean","none",2 # LDON runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_sldon", "runoff_flux_sldon","ocean_cobalt_sfc","all","mean","none",2 # SLDON runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_srdon", "runoff_flux_srdon","ocean_cobalt_sfc","all","mean","none",2 # SRDON runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_ndet",  "runoff_flux_ndet", "ocean_cobalt_sfc","all","mean","none",2 # NDET runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_pdet",  "runoff_flux_pdet", "ocean_cobalt_sfc","all","mean","none",2 # PDET runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_po4",   "runoff_flux_po4",  "ocean_cobalt_sfc","all","mean","none",2 # PO4 runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_ldop",  "runoff_flux_ldop", "ocean_cobalt_sfc","all","mean","none",2 # LDOP runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_sldop", "runoff_flux_sldop","ocean_cobalt_sfc","all","mean","none",2 # SLDOP runoff flux to the ocean\n'
        '"generic_cobalt","runoff_flux_srdop", "runoff_flux_srdop","ocean_cobalt_sfc","all","mean","none",2 # SRDOP runoff flux to the ocean\n'
        '"generic_cobalt","sfc_def_fe_di",     "sfc_def_fe_di",    "ocean_cobalt_sfc","all","mean","none",2 # Surface diazotroph iron deficiency\n'
        '"generic_cobalt","sfc_def_fe_lgp",    "sfc_def_fe_lgp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. iron deficiency\n'
        '"generic_cobalt","sfc_def_fe_mdp",    "sfc_def_fe_mdp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. iron deficiency\n'
        '"generic_cobalt","sfc_def_fe_smp",    "sfc_def_fe_smp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. iron deficiency\n'
        '"generic_cobalt","sfc_felim_di",      "sfc_felim_di",     "ocean_cobalt_sfc","all","mean","none",2 # Surface diazotroph iron uptake limitation\n'
        '"generic_cobalt","sfc_felim_lgp",     "sfc_felim_lgp",    "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. iron uptake limitation\n'
        '"generic_cobalt","sfc_felim_mdp",     "sfc_felim_mdp",    "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. iron uptake limitation\n'
        '"generic_cobalt","sfc_felim_smp",     "sfc_felim_smp",    "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. iron uptake limitation\n'
        '"generic_cobalt","sfc_irrlim_di",     "sfc_irrlim_di",    "ocean_cobalt_sfc","all","mean","none",2 # Surface diazotroph light limitation\n'
        '"generic_cobalt","sfc_irrlim_lgp",    "sfc_irrlim_lgp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. light limitation\n'
        '"generic_cobalt","sfc_irrlim_mdp",    "sfc_irrlim_mdp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. light limitation\n'
        '"generic_cobalt","sfc_irrlim_smp",    "sfc_irrlim_smp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. light limitation\n'
        '"generic_cobalt","sfc_theta_di",      "sfc_theta_di",     "ocean_cobalt_sfc","all","mean","none",2 # Surface diazotroph Chl:C\n'
        '"generic_cobalt","sfc_theta_lgp",     "sfc_theta_lgp",    "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. Chl:C\n'
        '"generic_cobalt","sfc_theta_mdp",     "sfc_theta_mdp",    "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. Chl:C\n'
        '"generic_cobalt","sfc_theta_smp",     "sfc_theta_smp",    "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. Chl:C\n'
        '"generic_cobalt","sfc_mu_di",         "sfc_mu_di",        "ocean_cobalt_sfc","all","mean","none",2 # Surface diazotroph growth rate\n'
        '"generic_cobalt","sfc_mu_lgp",        "sfc_mu_lgp",       "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. Chl:C\n'
        '"generic_cobalt","sfc_mu_mdp",        "sfc_mu_mdp",       "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. Chl:C\n'
        '"generic_cobalt","sfc_mu_smp",        "sfc_mu_smp",       "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. Chl:C\n'
        '"generic_cobalt","sfc_nh4lim_lgp",    "sfc_nh4lim_lgp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. ammonia limitation\n'
        '"generic_cobalt","sfc_nh4lim_mdp",    "sfc_nh4lim_mdp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. ammonia limitation\n'
        '"generic_cobalt","sfc_nh4lim_smp",    "sfc_nh4lim_smp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. ammonia limitation\n'
        '"generic_cobalt","sfc_no3lim_lgp",    "sfc_no3lim_lgp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. nitrate limitation\n'
        '"generic_cobalt","sfc_no3lim_mdp",    "sfc_no3lim_mdp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. nitrate limitation\n'
        '"generic_cobalt","sfc_no3lim_smp",    "sfc_no3lim_smp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. nitrate limitation\n'
        '"generic_cobalt","sfc_po4lim_di",     "sfc_po4lim_di",    "ocean_cobalt_sfc","all","mean","none",2 # Surface diazotroph phosphate limitation\n'
        '"generic_cobalt","sfc_po4lim_lgp",    "sfc_po4lim_lgp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. phosphate limitation\n'
        '"generic_cobalt","sfc_po4lim_mdp",    "sfc_po4lim_mdp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. phosphate limitation\n'
        '"generic_cobalt","sfc_po4lim_smp",    "sfc_po4lim_smp",   "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. phosphate limitation\n'
        '"generic_cobalt","sfc_q_fe_2_n_di",   "sfc_q_fe_2_n_di",  "ocean_cobalt_sfc","all","mean","none",2 # Surface diazotroph iron:nitrogen\n'
        '"generic_cobalt","sfc_q_fe_2_n_lgp",  "sfc_q_fe_2_n_lgp", "ocean_cobalt_sfc","all","mean","none",2 # Surface large phyto. iron:nitrogen\n'
        '"generic_cobalt","sfc_q_fe_2_n_mdp",  "sfc_q_fe_2_n_mdp", "ocean_cobalt_sfc","all","mean","none",2 # Surface medium phyto. iron:nitrogen\n'
        '"generic_cobalt","sfc_q_fe_2_n_smp",  "sfc_q_fe_2_n_smp", "ocean_cobalt_sfc","all","mean","none",2 # Surface small phyto. iron:nitrogen\n'
        '"generic_cobalt","nh4_stf",           "nh4_stf",          "ocean_cobalt_sfc","all","mean","none",2 # Total flux of nh4 into Ocean Surface\n'
        '"generic_cobalt","sfc_no3",           "sfc_no3",           "ocean_cobalt_sfc","all","mean","none",2 # Surface NO3\n'
        '"generic_cobalt","sfc_po4",           "sfc_po4",           "ocean_cobalt_sfc","all","mean","none",2 # Surface PO4\n'
        '"generic_cobalt","sfc_sio4",          "sfc_sio4",          "ocean_cobalt_sfc","all","mean","none",2 # Surface SiO4\n'
        '"generic_cobalt","sfc_co3_sol_arag",  "sfc_co3_sol_arag",  "ocean_cobalt_sfc","all","mean","none",2 # Surface Carbonate Ion Solubility for Aragonite\n'
        '"generic_cobalt","sfc_co3_sol_calc",  "sfc_co3_sol_calc",  "ocean_cobalt_sfc","all","mean","none",2 # Surface Carbonate Ion Solubility for Calcite\n'
        '"generic_cobalt","sfc_co3_ion",       "sfc_co3_ion",       "ocean_cobalt_sfc","all","mean","none",2 # Surface Carbonate Ion\n'
        '# Monthly COBALT bottom fields (2D)\n'
        '"generic_cobalt","btm_temp",         "btm_temp",        "ocean_cobalt_btm","all","mean","none",2 # Bottom Temperature\n'
        '"generic_cobalt","btm_o2",           "btm_o2",          "ocean_cobalt_btm","all","mean","none",2 # Bottom Oxygen\n'
        '"generic_cobalt","ffedet_btm",       "ffedet_btm",      "ocean_cobalt_btm","all","mean","none",2 # fedet sinking flux burial\n'
        '"generic_cobalt","ffedi_btm",        "ffedi_btm",       "ocean_cobalt_btm","all","mean","none",2 # diazo Fe sinking flux to bottom\n'
        '"generic_cobalt","ffetot_btm",       "ffetot_btm",       "ocean_cobalt_btm","all","mean","none",2 # Total Fe sinking flux to bottom\n'
        '"generic_cobalt","ffemd_btm",        "ffemd_btm",       "ocean_cobalt_btm","all","mean","none",2 # medium phyto Fe sinking flux to bottom\n'
        '"generic_cobalt","ffelg_btm",        "ffelg_btm",       "ocean_cobalt_btm","all","mean","none",2 # large phyto Fe sinking flux to bottom\n'
        '"generic_cobalt","ffe_sed",          "ffe_sed",         "ocean_cobalt_btm","all","mean","none",2 # Sediment iron efflux\n'
        '"generic_cobalt","flithdet_btm",     "flithdet_btm",    "ocean_cobalt_btm","all","mean","none",2 # Lithogenic detrital sinking flux burial\n'
        '"generic_cobalt","fndet_btm",        "fndet_btm",       "ocean_cobalt_btm","all","mean","none",2 # ndet sinking flux to bottom\n'
        '"generic_cobalt","fndi_btm",         "fndi_btm",        "ocean_cobalt_btm","all","mean","none",2 # diazo N sinking flux to bottom\n'
        '"generic_cobalt","fntot_btm",        "fntot_btm",        "ocean_cobalt_btm","all","mean","none",2 # Total N sinking flux to bottom\n'
        '"generic_cobalt","fnmd_btm",         "fnmd_btm",        "ocean_cobalt_btm","all","mean","none",2 # medium phyto N sinking flux to bottom\n'
        '"generic_cobalt","fnlg_btm",         "fnlg_btm",        "ocean_cobalt_btm","all","mean","none",2 # large phyto N sinking flux to bottom\n'
        '"generic_cobalt","fpdet_btm",        "fpdet_btm",       "ocean_cobalt_btm","all","mean","none",2 # pdet sinking flux to bottom\n'
        '"generic_cobalt","fpdi_btm",         "fpdi_btm",        "ocean_cobalt_btm","all","mean","none",2 # diazo P sinking flux to bottom\n'
        '"generic_cobalt","fptot_btm",        "fptot_btm",        "ocean_cobalt_btm","all","mean","none",2 # Total P sinking flux to bottom\n'
        '"generic_cobalt","fpmd_btm",         "fpmd_btm",        "ocean_cobalt_btm","all","mean","none",2 # medium phyto P sinking flux to bottom\n'
        '"generic_cobalt","fplg_btm",         "fplg_btm",        "ocean_cobalt_btm","all","mean","none",2 # large phyto P sinking flux to bottom\n'
        '"generic_cobalt","fsidet_btm",       "fsidet_btm",      "ocean_cobalt_btm","all","mean","none",2 # sidet sinking flux to bottom\n'
        '"generic_cobalt","fsimd_btm",        "fsimd_btm",       "ocean_cobalt_btm","all","mean","none",2 # medium phyto Si sinking flux to bottom\n'
        '"generic_cobalt","fsilg_btm",        "fsilg_btm",       "ocean_cobalt_btm","all","mean","none",2 # large phyto Si sinking flux to bottom\n'
        '"generic_cobalt","fcadet_arag_btm",  "fcadet_arag_btm", "ocean_cobalt_btm","all","mean","none",2 # Aragonite sinking flux at bottom\n'
        '"generic_cobalt","fcadet_calc_btm",  "fcadet_calc_btm", "ocean_cobalt_btm","all","mean","none",2 # Calcite sinking flux at bottom\n'
        '"generic_cobalt","fcased_burial",    "fcased_burial",   "ocean_cobalt_btm","all","mean","none",2 # Calcite permanent burial flux\n'
        '"generic_cobalt","fcased_redis",     "fcased_redis",    "ocean_cobalt_btm","all","mean","none",2 # Calcite redissolution from sediments\n'
        '"generic_cobalt","fnfeso4red_sed",   "fnfeso4red_sed",  "ocean_cobalt_btm","all","mean","none",2 # Sediment Ndet Fe and SO4 reduction flux\n'
        '"generic_cobalt","fno3denit_sed",    "fno3denit_sed",   "ocean_cobalt_btm","all","mean","none",2 # Sediment denitrification flux\n'
        '"generic_cobalt","fnoxic_sed",       "fnoxic_sed",      "ocean_cobalt_btm","all","mean","none",2 # Sediment oxic Ndet remineralization flux\n'
        '"generic_cobalt","cased_2d",         "cased",           "ocean_cobalt_btm","all","mean","none",2 # calcium carbonate in sediment\n'
        '"generic_cobalt","btm_co3_sol_arag", "btm_co3_sol_arag","ocean_cobalt_btm","all","mean","none",2 # Bottom Aragonite Solubility\n'
        '"generic_cobalt","btm_co3_sol_calc", "btm_co3_sol_calc","ocean_cobalt_btm","all","mean","none",2 # Bottom Calcite Solubility\n'
        '"generic_cobalt","btm_co3_ion",      "btm_co3_ion",     "ocean_cobalt_btm","all","mean","none",2 # Bottom Carbonate Ion\n'
        '"generic_cobalt","btm_htotal",       "btm_htotal",      "ocean_cobalt_btm","all","mean","none",2 # Bottom Htotal\n'
        '"generic_cobalt","fcased_redis_surfresp","fcased_redis_surfresp","ocean_cobalt_btm","all","mean","none",2 # Calcite redissolution rom sediments, surfresp\n'
        '"generic_cobalt","cased_redis_coef",     "cased_redis_coef",     "ocean_cobalt_btm","all","mean","none",2 # Calcite redissolution from sediments, deepresp coefficient,\n'
        '"generic_cobalt","cased_redis_delz",     "cased_redis_delz",     "ocean_cobalt_btm","all","mean","none",2 # Calcite redissolution from sediments, effective depth\n'
        '# COBALT downward fluxes at 100 meters\n'
        '"generic_cobalt","fndet_100",        "fndet_100",        "ocean_cobalt_fdet_100","all","mean","none",2 # Nitrogen detritus sinking flux @ 100m\n'
        '"generic_cobalt","fntot_100",        "fntot_100",        "ocean_cobalt_fdet_100","all","mean","none",2 # total nitrogen sinking flux @ 100m\n'
        '"generic_cobalt","fpdet_100",        "fpdet_100",        "ocean_cobalt_fdet_100","all","mean","none",2 # Phosphorous detritus sinking flux @ 100m\n'
        '"generic_cobalt","fptot_100",        "fptot_100",        "ocean_cobalt_fdet_100","all","mean","none",2 # total phosphorous sinking flux @ 100m\n'
        '"generic_cobalt","ffedet_100",       "ffedet_100",       "ocean_cobalt_fdet_100","all","mean","none",2 # Iron detritus sinking flux @ 100m\n'
        '"generic_cobalt","fsidet_100",       "fsidet_100",       "ocean_cobalt_fdet_100","all","mean","none",2 # Silicon detritus sinking flux @ 100m\n'
        '"generic_cobalt","fcadet_calc_100",  "fcadet_calc_100",  "ocean_cobalt_fdet_100","all","mean","none",2 # Calcite detritus sinking flux @ 100m\n'
        '"generic_cobalt","fcadet_arag_100",  "fcadet_arag_100",  "ocean_cobalt_fdet_100","all","mean","none",2 # Aragonite detritus sinking flux @ 100m\n'
        '"generic_cobalt","flithdet_100",     "flithdet_100",     "ocean_cobalt_fdet_100","all","mean","none",2 # Lithogenic detritus sinking flux @ 100m\n'
        '# COBALT integrated tracer variables at 100 meters\n'
        '"generic_cobalt","nsmp_100",         "nsmp_100",        "ocean_cobalt_tracers_int","all","mean","none",2 # Small phytoplankton nitrogen biomass in upper 100m\n'
        '"generic_cobalt","nmdp_100",         "nmdp_100",        "ocean_cobalt_tracers_int","all","mean","none",2 # Medium phytoplankton nitrogen biomass in upper 100m\n'
        '"generic_cobalt","nlgp_100",         "nlgp_100",        "ocean_cobalt_tracers_int","all","mean","none",2 # Large phytoplankton nitrogen biomass in upper 100m\n'
        '"generic_cobalt","ndi_100",          "ndi_100",         "ocean_cobalt_tracers_int","all","mean","none",2 # Diazotroph nitrogen biomass in upper 100m\n'
        '"generic_cobalt","silgp_100",        "silgp_100",       "ocean_cobalt_tracers_int","all","mean","none",2 # Large phytoplankton silicon biomass in upper 100m\n'
        '"generic_cobalt","simdp_100",        "simdp_100",       "ocean_cobalt_tracers_int","all","mean","none",2 # Medium phytoplankton silicon biomass in upper 100m\n'
        '"generic_cobalt","nsmz_100",         "nsmz_100",        "ocean_cobalt_tracers_int","all","mean","none",2 # Small zooplankton nitrogen biomass in upper 100m\n'
        '"generic_cobalt","nmdz_100",         "nmdz_100",        "ocean_cobalt_tracers_int","all","mean","none",2 # Medium zooplankton nitrogen biomass in upper 100m\n'
        '"generic_cobalt","nlgz_100",         "nlgz_100",        "ocean_cobalt_tracers_int","all","mean","none",2 # Large zooplankton nitrogen biomass in upper 100m\n'
        '"generic_cobalt","nbact_100",        "nbact_100",       "ocean_cobalt_tracers_int","all","mean","none",2 # Bacterial nitrogen biomass in upper 100m\n'
        '"generic_cobalt","don_100",          "don_100",         "ocean_cobalt_tracers_int","all","mean","none",2 # Dissolved organic nitrogen (sr+sl+l) in upper 100m\n'
        '"generic_cobalt","ndet_100",         "ndet_100",        "ocean_cobalt_tracers_int","all","mean","none",2 # Nitrogen detritus biomass in upper 100m\n'
        '"generic_cobalt","mesozoo_200",      "mesozoo_200",     "ocean_cobalt_tracers_int","all","mean","none",2 # Mesozooplankton biomass, 200m integral\n'
        '# Generic COBALT integrated flux variables\n'
        '"generic_cobalt","jprod_nsmp_100",          "jprod_nsmp_100",           "ocean_cobalt_fluxes_int","all","mean","none",2 # Small phyto. nitrogen  prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nmdp_100",          "jprod_nmdp_100",           "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium phyto. nitrogen  prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nlgp_100",          "jprod_nlgp_100",           "ocean_cobalt_fluxes_int","all","mean","none",2 # Large phyto. nitrogen  prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_ndi_100",           "jprod_ndi_100",            "ocean_cobalt_fluxes_int","all","mean","none",2 # Diazotroph nitrogen prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nsmp_new_100",      "jprod_nsmp_new_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Small phyto. new (NO3-based) prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nmdp_new_100",      "jprod_nmdp_new_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium phyto. new (NO3-based) prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nlgp_new_100",      "jprod_nlgp_new_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Large phyto. new (NO3-based) prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_ndi_new_100",       "jprod_ndi_new_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Diazotroph new (NO3-based) prim. prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_ndi_n2_100",        "jprod_ndi_n2_100",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Diazotroph nitrogen fixation in upper 100m\n'
        '"generic_cobalt","jprod_nsmz_100",          "jprod_nsmz_100",           "ocean_cobalt_fluxes_int","all","mean","none",2 # Small zooplankton nitrogen prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nmdz_100",          "jprod_nmdz_100",           "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium zooplankton nitrogen prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nlgz_100",          "jprod_nlgz_100",           "ocean_cobalt_fluxes_int","all","mean","none",2 # Large zooplankton nitrogen prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_nbact_100",         "jprod_nbact_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Bacteria nitrogen prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_mesozoo_200",       "jprod_mesozoo_200",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Mesozooplankton Production, 200m integration\n'
        '"generic_cobalt","jzloss_nsmp_100",         "jzloss_nsmp_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Small phyto. nitrogen loss to zooplankton integral in upper 100m\n'
        '"generic_cobalt","jzloss_nmdp_100",         "jzloss_nmdp_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium phyto. nitrogen loss to zooplankton integral in upper 100m\n'
        '"generic_cobalt","jzloss_nlgp_100",         "jzloss_nlgp_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Large phyto. nitrogen loss to zooplankton integral in upper 100m\n'
        '"generic_cobalt","jzloss_ndi_100",          "jzloss_ndi_100",           "ocean_cobalt_fluxes_int","all","mean","none",2 # Diazotroph nitrogen loss to zooplankton integral in upper 100m\n'
        '"generic_cobalt","jaggloss_nsmp_100",       "jaggloss_nsmp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Small phyto. nitrogen aggregation loss integral in upper 100m\n'
        '"generic_cobalt","jaggloss_nmdp_100",       "jaggloss_nmdp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium phyto. nitrogen aggregation loss integral in upper 100m\n'
        '"generic_cobalt","jaggloss_nlgp_100",       "jaggloss_nlgp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Large phyto. nitrogen aggregation loss integral in upper 100m\n'
        '"generic_cobalt","jvirloss_nsmp_100",       "jvirloss_nsmp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Small phyto. nitrogen virus loss integral in upper 100m\n'
        '"generic_cobalt","jvirloss_nmdp_100",       "jvirloss_nmdp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium phyto. nitrogen virus loss integral in upper 100m\n'
        '"generic_cobalt","jvirloss_nlgp_100",       "jvirloss_nlgp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Large phyto. nitrogen virus loss integral in upper 100m\n'
        '"generic_cobalt","jmortloss_nsmp_100",      "jmortloss_nsmp_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Small phyto. nitrogen mortality loss integral in upper 100m\n'
        '"generic_cobalt","jmortloss_nmdp_100",      "jmortloss_nmdp_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium phyto. nitrogen mortality loss integral in upper 100m\n'
        '"generic_cobalt","jmortloss_nlgp_100",      "jmortloss_nlgp_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Large phyto. nitrogen mortality loss integral in upper 100m\n'
        '"generic_cobalt","jmortloss_ndi_100",       "jmortloss_ndi_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Diazotroph nitrogen mortality loss integral in upper 100m\n'
        '"generic_cobalt","jexuloss_nsmp_100",       "jexuloss_nsmp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Small phyto. nitrogen exudation loss integral in upper 100m\n'
        '"generic_cobalt","jexuloss_nmdp_100",       "jexuloss_nmdp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium phyto. nitrogen exudation loss integral in upper 100m\n'
        '"generic_cobalt","jexuloss_nlgp_100",       "jexuloss_nlgp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Large phyto. nitrogen exudation loss integral in upper 100m\n'
        '"generic_cobalt","jexuloss_ndi_100",        "jexuloss_ndi_100",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Diazotroph nitrogen exudation loss integral in upper 100m\n'
        '"generic_cobalt","jingest_n_nsmz_100",      "jingest_n_nsmz_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Small zooplankton nitrogen ingestion integral in upper 100m\n'
        '"generic_cobalt","jingest_n_nmdz_100",      "jingest_n_nmdz_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium zooplankton nitrogen ingestion integral in upper 100m\n'
        '"generic_cobalt","jingest_n_nlgz_100",      "jingest_n_nlgz_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Large zooplankton nitrogen ingestion integral in upper 100m\n'
        '"generic_cobalt","jingest_n_hp_100",        "jingest_n_hp_100",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Higher predator ingestion of nitrogen integral in upper 100m\n'
        '"generic_cobalt","jzloss_nsmz_100",         "jzloss_nsmz_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Small zooplankton nitrogen loss to zooplankton integral in upper 100m\n'
        '"generic_cobalt","jzloss_nmdz_100",         "jzloss_nmdz_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium zooplankton nitrogen loss to zooplankton integral in upper 100m\n'
        '"generic_cobalt","jhploss_nmdz_100",        "jhploss_nmdz_100",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium zooplankton nitrogen loss to higher preds. integral in upper 100m\n'
        '"generic_cobalt","jhploss_nlgz_100",        "jhploss_nlgz_100",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Large zooplankton nitrogen loss to higher preds. integral in upper 100m\n'
        '"generic_cobalt","jprod_ndet_nmdz_100",     "jprod_ndet_nmdz_100",      "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium zooplankton nitrogen detritus prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_ndet_nlgz_100",     "jprod_ndet_nlgz_100",      "ocean_cobalt_fluxes_int","all","mean","none",2 # Large zooplankton nitrogen detritus prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_ndet_hp_100",       "jprod_ndet_hp_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Higher predator nitrogen detritus prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_don_nsmz_100",      "jprod_don_nsmz_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Small zooplankton dissolved org. nitrogen prod. integral in upper 100m\n'
        '"generic_cobalt","jprod_don_nmdz_100",      "jprod_don_nmdz_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium zooplankton dissolved org. nitrogen prod. integral in upper 100m\n'
        '"generic_cobalt","jremin_n_nsmz_100",       "jremin_n_nsmz_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Small zooplankton nitrogen remineralization integral in upper 100m\n'
        '"generic_cobalt","jremin_n_nmdz_100",       "jremin_n_nmdz_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Medium zooplankton nitrogen remineralization integral in upper 100m\n'
        '"generic_cobalt","jremin_n_nlgz_100",       "jremin_n_nlgz_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Large zooplankton nitrogen remineralization integral in upper 100m\n'
        '"generic_cobalt","jremin_n_hp_100",         "jremin_n_hp_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Higher predator nitrogen remineralization integral in upper 100m\n'
        '"generic_cobalt","juptake_ldon_nbact_100",  "juptake_ldon_nbact_100",   "ocean_cobalt_fluxes_int","all","mean","none",2 # Bacterial uptake of labile dissolved org. nitrogen in upper 100m\n'
        '"generic_cobalt","jvirloss_nbact_100",      "jvirloss_nbact_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Bacteria nitrogen loss to viruses integral in upper 100m\n'
        '"generic_cobalt","jzloss_nbact_100",        "jzloss_nbact_100",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Bacteria nitrogen loss to zooplankton integral in upper 100m\n'
        '"generic_cobalt","jremin_n_nbact_100",      "jremin_n_nbact_100",       "ocean_cobalt_fluxes_int","all","mean","none",2 # Bacteria nitrogen remineralization integral in upper 100m\n'
        '"generic_cobalt","jprod_lithdet_100",       "jprod_lithdet_100",        "ocean_cobalt_fluxes_int","all","mean","none",2 # Lithogenic detritus production integral in upper 100m\n'
        '"generic_cobalt","jprod_sidet_100",         "jprod_sidet_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Silica detritus production integral in upper 100m\n'
        '"generic_cobalt","jprod_cadet_calc_100",    "jprod_cadet_calc_100",     "ocean_cobalt_fluxes_int","all","mean","none",2 # Calcite detritus production integral in upper 100m\n'
        '"generic_cobalt","jprod_cadet_arag_100",    "jprod_cadet_arag_100",     "ocean_cobalt_fluxes_int","all","mean","none",2 # Aragonite detritus production integral in upper 100m\n'
        '"generic_cobalt ","jremin_ndet_100",        "jremin_ndet_100",          "ocean_cobalt_fluxes_int","all","mean","none",2 # Remineralization of nitrogen detritus integral in upper 100m\n'
        '"generic_cobalt ","wc_vert_int_jdiss_sidet","wc_vert_int_jdiss_sidet",  "ocean_cobalt_fluxes_int","all","mean","none",2 # Water column silica dissolution vertical integral\n'
        '"generic_cobalt ","wc_vert_int_jdiss_cadet","wc_vert_int_jdiss_cadet",  "ocean_cobalt_fluxes_int","all","mean","none",2 # Water column calcium carbonate dissolution vertical integral\n'
        '"generic_cobalt ","wc_vert_int_jo2resp",    "wc_vert_int_jo2resp",      "ocean_cobalt_fluxes_int","all","mean","none",2 # Water column oxygen respired vertical integral\n'
        '"generic_cobalt ","wc_vert_int_jprod_cadet","wc_vert_int_jprod_cadet",  "ocean_cobalt_fluxes_int","all","mean","none",2 # Water column calcium carbonate production vertical integral\n'
        '"generic_cobalt ","wc_vert_int_jno3denit",  "wc_vert_int_jno3denit",    "ocean_cobalt_fluxes_int","all","mean","none",2 # Water column denitrification vertical integral\n'
        '"generic_cobalt ","wc_vert_int_jprod_no3nitrif","wc_vert_int_jprod_no3nitrif","ocean_cobalt_fluxes_int","all","mean","none",2 # Water column nitrification vertical integral\n'
        '"generic_cobalt ","wc_vert_int_juptake_nh4","wc_vert_int_juptake_nh4",  "ocean_cobalt_fluxes_int","all","mean","none",2 #  Water column ammonia based NPP vertical integral\n'
        '"generic_cobalt ","wc_vert_int_juptake_no3","wc_vert_int_juptake_no3",  "ocean_cobalt_fluxes_int","all","mean","none",2 # Water column nitrate based NPP, vertical integral\n'
        '"generic_cobalt ","wc_vert_int_nfix",       "wc_vert_int_nfix",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Nitrogen fixation vertical integral\n'
        '"generic_cobalt ","wc_vert_int_jprod_nh4",  "wc_vert_int_jprod_nh4",    "ocean_cobalt_fluxes_int","all","mean","none",2 #  Water column ammonia production vertical integral\n'
        '"generic_cobalt ","wc_vert_int_npp",         "wc_vert_int_npp",         "ocean_cobalt_fluxes_int","all","mean","none",2 # Water column net primary production vertical integral\n'
        '"generic_cobalt","jdiss_cadet_arag_plus_btm", "jdiss_cadet_arag_plus_btm","ocean_cobalt_fluxes_int","all","mean","none",2 # CaCO3 detritus dissolution plus bottom dissolution, layer integral\n'
        '"generic_cobalt","jdiss_cadet_arag",         "jdiss_cadet_arag",        "ocean_cobalt_fluxes_int","all","mean","none",2 # CaCO3 detritus dissolution, layer integral	     "generic_cobalt","jdiss_cadet_calc",	  "jdiss_cadet_calc",	     "ocean_cobalt_fluxes_int","all","mean","none",2 # CaCO3 detritus dissolution, layer integral\n'
        '"generic_cobalt","jdiss_cadet_calc_plus_btm", "jdiss_cadet_calc_plus_btm", "ocean_cobalt_fluxes_int","all","mean","none",2 # CaCO3 detritus dissolution plus bottom dissolution, layer integral												                                                                  "generic_cobalt","juptake_no3_Di",	            "juptake_no3_Di",	             "ocean_cobalt_fluxes_int",  "all",   "mean", "none", 2 # Diaz. phyto. NO3 uptake layer integral																		\n'
        '"generic_cobalt","juptake_no3_Lg",	          "juptake_no3_Lg",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Large phyto. NO3 uptake layer integral																		\n'
        '"generic_cobalt","juptake_no3_Md",	          "juptake_no3_Md",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Medium phyto. NO3 uptake layer integral																		\n'
        '"generic_cobalt","juptake_no3_Sm",	          "juptake_no3_Sm",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Small phyto. NO3 uptake layer integral																		\n'
        '"generic_cobalt","jo2resp_wc",	                  "jo2resp_wc",	                   "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Water column aerobic respiration layer integral																		\n'
        '"generic_cobalt","juptake_nh4nitrif",	          "juptake_nh4nitrif",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # NH4 uptake via Nitrification layer integral																		\n'
        '"generic_cobalt","jno3denit_wc",	          "jno3denit_wc",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Water column Denitrification layer integral																		\n'
        '"generic_cobalt","juptake_nh4amx",	          "juptake_nh4amx",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # NH4 uptake via Anammox layer integral																		\n'
        '"generic_cobalt","juptake_nh4_Di",	          "juptake_nh4_Di",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Diaz. phyto. NH4 uptake layer integral																		\n'
        '"generic_cobalt","juptake_nh4_Lg",	          "juptake_nh4_Lg",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Large phyto. NH4 uptake layer integral																		\n'
        '"generic_cobalt","juptake_nh4_Md",	          "juptake_nh4_Md",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Medium phyto. NH4 uptake layer integral																		\n'
        '"generic_cobalt","juptake_nh4_Sm",	          "juptake_nh4_Sm",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Small phyto. NH4 uptake layer integral																					  "generic_cobalt","jprod_nh4",	                    "jprod_nh4",	             "ocean_cobalt_fluxes_int",   "all",  "mean", "none", 2 # NH4 production layer integral																		\n'
        '"generic_cobalt","jprod_nh4_plus_btm",	          "jprod_nh4_plus_btm",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # NH4 production layer integral plus bottom fluxes																		\n'
        '"generic_cobalt","juptake_n2_Di",	          "juptake_n2_Di",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Nitrogen fixation layer integral																		\n'
        '"generic_cobalt","jprod_cadet_arag",	          "jprod_cadet_arag",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Aragonite CaCO3 production layer integral																		\n'
        '"generic_cobalt","jprod_cadet_calc",	          "jprod_cadet_calc",	           "ocean_cobalt_fluxes_int",	"all",	"mean",	"none",	2 # Calcite CaCO3 production layer integral																					  # Monthly cobalt tracers in z* coordinates\n'
        '"generic_cobalt_z","htotal",             "htotal",             "ocean_cobalt_tracers_month_z","all","mean","none",2 # H+ ion concentration\n'
        '"ocean_model_z","volcello",              "volcello",           "ocean_cobalt_tracers_month_z","all","mean","none",2 # Ocean grid-cell volume\n'
        '"generic_cobalt_z","no3",                "no3",               "ocean_cobalt_tracers_month_z","all","mean","none",2 # Nitrate\n'
        '"generic_cobalt_z","o2",                 "o2",                "ocean_cobalt_tracers_month_z","all","mean","none",2 # Oxygen\n'
        '"generic_cobalt_z","o2",                 "o2min",             "ocean_cobalt_tracers_month_z","all","min","none",2 # Oxygen\n'
        '"generic_cobalt_z","o2",                 "o2max",             "ocean_cobalt_tracers_month_z","all","max","none",2 # Oxygen\n'
        '"generic_cobalt_z","omega_arag",         "omega_arag",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Carbonate Ion Saturation State for Aragonite\n'
        '"generic_cobalt_z","omega_calc",         "omega_calc",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Carbonate Ion Saturation State for Calcite\n'
        '"generic_cobalt_z","ndi",                "ndi",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Diazotroph Nitrogen\n'
        '"generic_cobalt_z","nlg",                "nlg",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Large Phytoplankton Nitrogen\n'
        '"generic_cobalt_z","nmd",                "nmd",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium Phytoplankton Nitrogen\n'
        '"generic_cobalt_z","nsm",                "nsm",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Small Phytoplankton Nitrogen\n'
        '"generic_cobalt_z","pdi",                "pdi",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Diazotroph Phosphorus\n'
        '"generic_cobalt_z","plg",                "plg",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Large Phytoplankton Phosphorus\n'
        '"generic_cobalt_z","pmd",                "pmd",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium Phytoplankton Phosphorus\n'
        '"generic_cobalt_z","psm",                "psm",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Small Phytoplankton Phosphorus\n'
        '"generic_cobalt_z","q_p_2_n_Sm",         "q_p_2_n_Sm",   "ocean_cobalt_tracers_month_z","all","mean","none",2 # P:N ratio of Small Phyto\n'
        '"generic_cobalt_z","q_p_2_n_Md",         "q_p_2_n_Md",   "ocean_cobalt_tracers_month_z","all","mean","none",2 # P:N ratio of Medium Phyto\n'
        '"generic_cobalt_z","q_p_2_n_Lg",         "q_p_2_n_Lg",   "ocean_cobalt_tracers_month_z","all","mean","none",2 # P:N ratio of Large Phyto\n'
        '"generic_cobalt_z","q_p_2_n_Di",         "q_p_2_n_Di",   "ocean_cobalt_tracers_month_z","all","mean","none",2 # P:N ratio of Diaz. Phyto\n'
        '"generic_cobalt_z","silg",               "silg",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # Large Phytoplankton Silicon\n'
        '"generic_cobalt_z","simd",               "simd",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium Phytoplankton Silicon\n'
        '"generic_cobalt_z","chl",                "chl",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Chlorophyll\n'
        '"generic_cobalt_z","chl_Lg",             "chl_Lg",       "ocean_cobalt_tracers_month_z","all","mean","none",2 # Large Phyto. Chlorophyll\n'
        '"generic_cobalt_z","chl_Md",             "chl_Md",       "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium Phyto. Chlorophyll\n'
        '"generic_cobalt_z","chl_Sm",             "chl_Sm",       "ocean_cobalt_tracers_month_z","all","mean","none",2 # Small Phyto. Chlorophyll\n'
        '"generic_cobalt_z","chl_Di",             "chl_Di",       "ocean_cobalt_tracers_month_z","all","mean","none",2 # Diaz. Phyto. Chlorophyll\n'
        '"generic_cobalt_z","mu_Lg",              "mu_Lg",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Large Phyto. Overall Growth Rate\n'
        '"generic_cobalt_z","mu_Md",              "mu_Md",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium Phyto. Overall Growth Rate\n'
        '"generic_cobalt_z","mu_Sm",              "mu_Sm",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Small Phyto. Growth Rate\n'
        '"generic_cobalt_z","mu_Di",              "mu_Di",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Diaz. Phyto. Overall Growth Rate\n'
        '"generic_cobalt_z","irrlim_Lg",          "irrlim_Lg",    "ocean_cobalt_tracers_month_z","all","mean","none",2 # Large Phyto. Light Limitation\n'
        '"generic_cobalt_z","irrlim_Md",          "irrlim_Md",    "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium Phyto. Light Limitation\n'
        '"generic_cobalt_z","irrlim_Sm",          "irrlim_Sm",    "ocean_cobalt_tracers_month_z","all","mean","none",2 # Small Phyto. Light Limitation\n'
        '"generic_cobalt_z","irrlim_Di",          "irrlim_Di",    "ocean_cobalt_tracers_month_z","all","mean","none",2 # Diaz. Phyto. Light Limitation\n'
        '"generic_cobalt_z","nbact",              "nbact",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # bacterial\n'
        '"generic_cobalt_z","nsmz",               "nsmz",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # Small Zooplankton Nitrogen\n'
        '"generic_cobalt_z","nmdz",               "nmdz",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium-sized zooplankton Nitrogen\n'
        '"generic_cobalt_z","nlgz",               "nlgz",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # large Zooplankton Nitrogen\n'
        '"generic_cobalt_z","po4",                "po4",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Phosphate\n'
        '"generic_cobalt_z","nh4",                "nh4",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Ammonia\n'
        '"generic_cobalt_z","fed",                "fed",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Dissolved Iron\n'
        '"generic_cobalt_z","fedet",              "fedet",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Detrital Iron\n'
        '"generic_cobalt_z","ndet",               "ndet",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # ndet\n'
        '"generic_cobalt_z","feprime",            "feprime",      "ocean_cobalt_tracers_month_z","all","mean","none",2 # Free iron concentration\n'
        '"generic_cobalt_z","theta_Lg",           "theta_Lg",     "ocean_cobalt_tracers_month_z","all","mean","none",2 # Large Phyto. Chl:C\n'
        '"generic_cobalt_z","theta_Md",           "theta_Md",     "ocean_cobalt_tracers_month_z","all","mean","none",2 # Medium Phyto. Chl:C\n'
        '"generic_cobalt_z","theta_Sm",           "theta_Sm",     "ocean_cobalt_tracers_month_z","all","mean","none",2 # Small Phyto. Chl:C\n'
        '"generic_cobalt_z","theta_Di",           "theta_Di",     "ocean_cobalt_tracers_month_z","all","mean","none",2 # Diaz. Phyto. Chl:C\n'
        '"generic_cobalt_z","irr_mix",            "irr_mix",      "ocean_cobalt_tracers_month_z","all","mean","none",2 # Instantaneous light, avg over mixing layer\n'
        '"generic_cobalt_z","irr_inst",           "irr_inst",     "ocean_cobalt_tracers_month_z","all","mean","none",2 # Instantaneous Light\n'
        '"generic_cobalt_z","dissic",             "dissic",       "ocean_cobalt_tracers_month_z","all","mean","none",2 # Dissolved Inorganic Carbon Concentration\n'
        '"generic_cobalt_z","dissoc",             "dissoc",       "ocean_cobalt_tracers_month_z","all","mean","none",2 # Dissolved Organic Carbon Concentration\n'
        '"generic_cobalt_z","talk",               "talk",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # Total Alkalinity\n'
        '"generic_cobalt_z","si",                 "si",           "ocean_cobalt_tracers_month_z","all","mean","none",2 # Total Dissolved Inorganic Silicon Concentration\n'
        '"generic_cobalt_z","co3",                "co3",          "ocean_cobalt_tracers_month_z","all","mean","none",2 # Carbonate Ion Concentration\n'
        '"generic_cobalt_z","calc",               "calc",         "ocean_cobalt_tracers_month_z","all","mean","none",2 # Calcite Concentration\n'
        '"generic_cobalt_z","zmeso",              "zmeso",        "ocean_cobalt_tracers_month_z","all","mean","none",2 # Mole Concentration of Mesozooplankton expressed as Carbon in sea water\n'
        '"generic_cobalt_z","zmicro",             "zmicro",       "ocean_cobalt_tracers_month_z","all","mean","none",2 # Mole Concentration of Microzooplankton expressed as Carbon in sea water\n'
        '# 2-D Monthly Marine Biogeochemical Surface Tracer Fields\n'
        '"generic_cobalt","dissicos",       "dissicos",             "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Dissolved Inorganic Carbon Concentration\n'
        '"generic_cobalt","dissocos",       "dissocos",             "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Dissolved Organic Carbon Concentration\n'
        '"generic_cobalt","phycos",         "phycos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Phytoplankton Carbon Concentration\n'
        '"generic_cobalt","zoocos",         "zoocos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Zooplankton Carbon Concentration\n'
        '"generic_cobalt","baccos",         "baccos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Bacterial Carbon Concentration\n'
        '"generic_cobalt","detocos",        "detocos",              "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Detrital Organic Carbon Concentration\n'
        '"generic_cobalt","calcos",         "calcos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Calcite Concentration\n'
        '"generic_cobalt","aragos",         "aragos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Aragonite Concentration\n'
        '"generic_cobalt","phydiatos",      "phydiatos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Diatoms expressed as Carbon in sea water\n'
        '"generic_cobalt","phydiazos",      "phydiazos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Diazotrophs expressed as Carbon in sea water\n'
        '"generic_cobalt","phypicoos",      "phypicoos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Picophytoplankton expressed as Carbon in sea water\n'
        '"generic_cobalt","phymiscos",      "phymiscos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Miscellaneous Phytoplankton expressed as Carbon in sea water\n'
        '"generic_cobalt","zmicroos",       "zmicroos",             "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Microzooplankton expressed as Carbon in sea water\n'
        '"generic_cobalt","zmesoos",        "zmesoos",              "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Mesozooplankton expressed as Carbon in sea water\n'
        '"generic_cobalt","talkos",         "talkos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Total Alkalinity\n'
        '"generic_cobalt","phos",           "phos",                 "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface pH\n'
        '"generic_cobalt","o2os",           "o2os",                 "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Dissolved Oxygen Concentration\n'
        '"generic_cobalt","o2satos",        "o2satos",              "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Dissolved Oxygen Concentration at Saturation\n'
        '"generic_cobalt","no3os",          "no3os",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Dissolved Nitrate Concentration\n'
        '"generic_cobalt","nh4os",          "nh4os",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Dissolved Ammonium Concentration\n'
        '"generic_cobalt","po4os",          "po4os",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Total Dissolved Inorganic Phosphorus Concentration\n'
        '"generic_cobalt","dfeos",          "dfeos",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Dissolved Iron Concentration\n'
        '"generic_cobalt","sios",           "sios",                 "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Total Dissolved Inorganic Silicon Concentration\n'
        '"generic_cobalt","chlos",          "chlos",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mass Concentration of Total Phytoplankton expressed as Chlorophyll in sea water\n'
        '"generic_cobalt","chldiatos",      "chldiatos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mass Concentration of Diatoms expressed as Chlorophyll in sea water\n'
        '"generic_cobalt","chldiazos",      "chldiazos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mass Concentration of Diazotrophs expressed as Chlorophyll in sea water\n'
        '"generic_cobalt","chlpicoos",      "chlpicoos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mass Concentration of Picophytoplankton expressed as Chlorophyll in sea water\n'
        '"generic_cobalt","chlmiscos",      "chlmiscos",            "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mass Concentration of Other Phytoplankton expressed as Chlorophyll in sea water\n'
        '"generic_cobalt","ponos",          "ponos",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Particulate Organic Matter expressed as Nitrogen in sea water\n'
        '"generic_cobalt","popos",          "popos",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Particulate Organic Matter expressed as Phosphorus in sea water\n'
        '"generic_cobalt","bfeos",          "bfeos",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Particulate Organic Matter expressed as Iron in sea water\n'
        '"generic_cobalt","bsios",          "bsios",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Particulate Organic Matter expressed as Silicon in sea water\n'
        '"generic_cobalt","phynos",         "phynos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Phytoplankton Nitrogen in sea water\n'
        '"generic_cobalt","phypos",         "phypos",               "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Total Phytoplankton expressed as Phosphorus in sea water\n'
        '"generic_cobalt","phyfeos",        "phyfeos",              "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Total Phytoplankton expressed as Iron in sea water\n'
        '"generic_cobalt","physios",        "physios",              "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Total Phytoplankton expressed as Silicon in sea water\n'
        '"generic_cobalt","co3os",          "co3os",                "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Carbonate Ion Concentration\n'
        '"generic_cobalt","co3satcalcos",   "co3satcalcos",         "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Carbonate Ion in Equilibrium with Pure Calcite in sea water\n'
        '"generic_cobalt","co3sataragos",   "co3sataragos",         "ocean_cobalt_omip_sfc","all","mean","none",2 # Surface Mole Concentration of Carbonate Ion in Equilibrium with Pure Aragonite in sea water\n'
        '# Additional 2-D monthly Marine Biogeochemical Fields (e.g. vertically integrated, 100m, etc)\n'
        '"generic_cobalt","limndiat",        "limndiat",            "ocean_cobalt_omip_2d","all","mean","none",2 # Nitrogen Limitation of Diatoms\n'
        '"generic_cobalt","limnpico",        "limnpico",            "ocean_cobalt_omip_2d","all","mean","none",2 # Nitrogen Limitation of Picophytoplankton\n'
        '"generic_cobalt","limnmisc",        "limnmisc",            "ocean_cobalt_omip_2d","all","mean","none",2 # Nitrogen Limitation of Other Phytoplankton\n'
        '"generic_cobalt","limirrdiat",      "limirrdiat",          "ocean_cobalt_omip_2d","all","mean","none",2 # Irradiance Limitation of Diatoms\n'
        '"generic_cobalt","limirrdiaz",      "limirrdiaz",          "ocean_cobalt_omip_2d","all","mean","none",2 # Irradiance Limitation of Diazotrophs\n'
        '"generic_cobalt","limirrpico",      "limirrpico",          "ocean_cobalt_omip_2d","all","mean","none",2 # Irradiance Limitation of Picophytoplankton\n'
        '"generic_cobalt","limirrmisc",      "limirrmisc",          "ocean_cobalt_omip_2d","all","mean","none",2 # Irradiance Limitation of Other Phytoplankton\n'
        '"generic_cobalt","limfediat",       "limfediat",           "ocean_cobalt_omip_2d","all","mean","none",2 # Iron Limitation of Diatoms\n'
        '"generic_cobalt","limfediaz",       "limfediaz",           "ocean_cobalt_omip_2d","all","mean","none",2 # Iron Limitation of Diazotrophs\n'
        '"generic_cobalt","limfepico",       "limfepico",           "ocean_cobalt_omip_2d","all","mean","none",2 # Iron Limitation of Picophytoplankton\n'
        '"generic_cobalt","limfemisc",       "limfemisc",           "ocean_cobalt_omip_2d","all","mean","none",2 # Iron Limitation of Other Phytoplankton\n'
        '"generic_cobalt","limpdiat",        "limpdiat",            "ocean_cobalt_omip_2d","all","mean","none",2 # Phosphorus Limitation of Diatoms\n'
        '"generic_cobalt","limpdiaz",        "limpdiaz",            "ocean_cobalt_omip_2d","all","mean","none",2 # Phosphorus Limitation of Diazotrophs\n'
        '"generic_cobalt","limppico",        "limppico",            "ocean_cobalt_omip_2d","all","mean","none",2 # Phosphorus Limitation of Picophytoplankton\n'
        '"generic_cobalt","limpmisc",        "limpmisc",            "ocean_cobalt_omip_2d","all","mean","none",2 # Phosphorus Limitation of Other Phytoplankton\n'
        '"generic_cobalt","intpp",           "intpp",               "ocean_cobalt_omip_2d","all","mean","none",2 # Primary Organic Carbon Production by All Types of Phytoplankton\n'
        '"generic_cobalt","intppnitrate",    "intppnitrate",        "ocean_cobalt_omip_2d","all","mean","none",2 # Primary Organic Carbon Production by Phytoplankton Based on Nitrate Uptake Alone\n'
        '"generic_cobalt","intppdiat",       "intppdiat",           "ocean_cobalt_omip_2d","all","mean","none",2 # Net Primary Organic Carbon Production by Diatoms\n'
        '"generic_cobalt","intppdiaz",       "intppdiaz",           "ocean_cobalt_omip_2d","all","mean","none",2 # Net Primary Mole Productivity of Carbon by Diazotrophs\n'
        '"generic_cobalt","intpppico",       "intpppico",           "ocean_cobalt_omip_2d","all","mean","none",2 # Net Primary Mole Productivity of Carbon by Picophytoplankton\n'
        '"generic_cobalt","intppmisc",       "intppmisc",           "ocean_cobalt_omip_2d","all","mean","none",2 # Net Primary Organic Carbon Production by Other Phytoplankton\n'
        '"generic_cobalt","intpbn",          "intpbn",              "ocean_cobalt_omip_2d","all","mean","none",2 # Nitrogen Production\n'
        '"generic_cobalt","intpbp",          "intpbp",              "ocean_cobalt_omip_2d","all","mean","none",2 # Phosphorus Production\n'
        '"generic_cobalt","intpbfe",         "intpbfe",             "ocean_cobalt_omip_2d","all","mean","none",2 # Iron Production\n'
        '"generic_cobalt","intpbsi",         "intpbsi",             "ocean_cobalt_omip_2d","all","mean","none",2 # Silicon Production\n'
        '"generic_cobalt","intpcalcite",     "intpcalcite",         "ocean_cobalt_omip_2d","all","mean","none",2 # Calcite Production\n'
        '"generic_cobalt","intparag",        "intparag",            "ocean_cobalt_omip_2d","all","mean","none",2 # Aragonite Production\n'
        '"generic_cobalt","epc100",          "epc100",              "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Flux of Particulate Organic Carbon\n'
        '"generic_cobalt","epn100",          "epn100",              "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Flux of Particulate Nitrogen\n'
        '"generic_cobalt","epp100",          "epp100",              "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Flux of Particulate Phosphorus\n'
        '"generic_cobalt","epfe100",         "epfe100",             "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Flux of Particulate Iron\n'
        '"generic_cobalt","epsi100",         "epsi100",             "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Flux of Particulate Silicon\n'
        '"generic_cobalt","epcalc100",       "epcalc100",           "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Flux of Calcite\n'
        '"generic_cobalt","eparag100",       "eparag100",           "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Flux of Aragonite\n'
        '"generic_cobalt","intdic",          "intdic",              "ocean_cobalt_omip_2d","all","mean","none",2 # Dissolved Inorganic Carbon Content\n'
        '"generic_cobalt","intdoc",          "intdoc",              "ocean_cobalt_omip_2d","all","mean","none",2 # Dissolved Organic Carbon Content\n'
        '"generic_cobalt","intpoc",          "intpoc",              "ocean_cobalt_omip_2d","all","mean","none",2 # Particulate Organic Carbon Content\n'
        '"generic_cobalt","spco2",           "spco2",               "ocean_cobalt_omip_2d","all","mean","none",2 # Surface Aqueous Partial Pressure of CO2\n'
        '"generic_cobalt","dpco2",           "dpco2",               "ocean_cobalt_omip_2d","all","mean","none",2 # Delta PCO2\n'
        '"generic_cobalt","dpo2",            "dpo2",                "ocean_cobalt_omip_2d","all","mean","none",2 # Delta PO2\n'
        '"generic_cobalt","fgco2",           "fgco2",               "ocean_cobalt_omip_2d","all","mean","none",2 # Surface Downward Flux of Total CO2\n'
        '"generic_cobalt","fgo2",            "fgo2",                "ocean_cobalt_omip_2d","all","mean","none",2 # Surface Downward Flux of O2\n'
        '"generic_cobalt","icfriver",        "icfriver",            "ocean_cobalt_omip_2d","all","mean","none",2 # Flux of Inorganic Carbon Into Ocean Surface by Runoff\n'
        '"generic_cobalt","fric",            "fric",                "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Inorganic Carbon Flux at Ocean Bottom\n'
        '"generic_cobalt","ocfriver",        "ocfriver",            "ocean_cobalt_omip_2d","all","mean","none",2 # Flux of Organic Carbon Into Ocean Surface by Runoff\n'
        '"generic_cobalt","froc",            "froc",                "ocean_cobalt_omip_2d","all","mean","none",2 # Downward Organic Carbon Flux at Ocean Bottom\n'
        '"generic_cobalt","intpn2",          "intpn2",              "ocean_cobalt_omip_2d","all","mean","none",2 # Nitrogen Fixation Rate in Ocean\n'
        '"generic_cobalt","fsn",             "fsn",                 "ocean_cobalt_omip_2d","all","mean","none",2 # Surface Downward Net Flux of Nitrogen\n'
        '"generic_cobalt","frn",             "frn",                 "ocean_cobalt_omip_2d","all","mean","none",2 # Nitrogen Loss to Sediments and through Denitrification\n'
        '"generic_cobalt","fsfe",            "fsfe",                "ocean_cobalt_omip_2d","all","mean","none",2 # Surface Downward Net Flux of Iron\n'
        '"generic_cobalt","frfe",            "frfe",                "ocean_cobalt_omip_2d","all","mean","none",2 # Iron Loss to Sediments\n'
        '# MOM6 ocean diagnostics only used in a CORE/OMIP (no interactive atmos). \n'
        '# These terms provide diagnostics for the surface salinity / fresh water restoring. \n'
        '"ocean_model", "vprec",        "vprec",        "ocean_annual", "all", "mean", "none",2\n'
        '"ocean_model", "salt_flux_added",  "salt_flux_added",  "ocean_annual", "all", "mean", "none",2\n'
        '"ocean_model", "vprec",        "vprec",        "ocean_month", "all", "mean", "none",2\n'
        '"ocean_model", "salt_flux_added",  "salt_flux_added",  "ocean_month", "all", "mean", "none",2\n'
        '#\n'
        '"ocean_model_z", "opottemppmdiff", "opottemppmdiff", "ocean_annual_z", "all", "mean", "none",2\n'
    )
    with open("diag_table", 'w') as f:
        print(result, end="", file=f)


def generate_input_nml(year: int):
    restart = "r" if year >= 1959 else "n"
    result = (
        " &MOM_input_nml\n"
        "        output_directory = './',\n"
        f"        input_filename = '{restart}'\n"
        "        restart_input_dir = 'INPUT/',\n"
        "        restart_output_dir = 'RESTART/',\n"
        "        parameter_filename = 'INPUT/MOM_input','INPUT/MOM_layout','INPUT/MOM_saltrestore','INPUT/MOM_override'\n"
        "/\n"
        "\n"
        " &SIS_input_nml\n"
        "        output_directory = './',\n"
        f"        input_filename = '{restart}'\n"
        "        restart_input_dir = 'INPUT/',\n"
        "        restart_output_dir = 'RESTART/',\n"
        "        parameter_filename = 'INPUT/SIS_input','INPUT/SIS_layout','INPUT/SIS_override'\n"
        "/\n"
        "\n"
        " &atmos_model_nml\n"
        "        layout= 0, 0\n"
        "/\n"
        "\n"
        " &cobalt_input_nml\n"
        "        parameter_filename = 'INPUT/COBALT_input','INPUT/COBALT_override'\n"
        "/\n"
        "\n"
        " &coupler_nml\n"
        "        months = 12,\n"
        "        days   = 0,\n"
        f"        current_date = {year},1,1,0,0,0,\n"
        "        hours = 0\n"
        "        minutes = 0\n"
        "        seconds = 0\n"
        "        calendar = 'gregorian',\n"
        "        dt_cpld  = 3600,   \n"
        "        dt_atmos = 3600,  \n"
        "        do_atmos = .false.,\n"
        "        do_land = .false.,\n"
        "        do_ice = .true.,\n"
        "        do_ocean = .true.,\n"
        "        atmos_npes = 0,\n"
        "        ocean_npes = 0,\n"
        "        concurrent = .false.\n"
        "        use_lag_fluxes=.false.\n"
        "        atmos_nthreads = 1\n"
        "        ocean_nthreads = 1\n"
        "/\n"
        "\n"
        " &diag_manager_nml\n"
        "        max_files = 400\n"
        "        flush_nc_files=.true.\n"
        "        max_axes = 400,\n"
        "        max_num_axis_sets = 400,\n"
        "        max_input_fields = 2000 \n"
        "        max_output_fields = 5000 \n"
        "        mix_snapshot_average_fields=.false.\n"
        "/\n"
        "\n"
        " &flux_exchange_nml\n"
        "            debug_stocks = .FALSE.\n"
        "            divert_stocks_report = .TRUE.            \n"
        "            do_area_weighted_flux = .FALSE.\n"
        "/\n"
        "\n"
        " &fms_io_nml\n"
        "        fms_netcdf_restart=.true.\n"
        "        threading_read='multi'\n"
        "        max_files_r = 800\n"
        "        max_files_w = 800\n"
        "/\n"
        "\n"
        " &fms_nml\n"
        "        clock_grain='ROUTINE'\n"
        "        clock_flags='NONE'\n"
        "        domains_stack_size = 8000000\n"
        "        stack_size =0\n"
        "/\n"
        "\n"
        " &generic_COBALT_nml\n"
        "        co2_calc = 'mocsy'\n"
        "	debug = .false.\n"
        "	imbalance_tolerance = 1.0e-9\n"
        "/\n"
        "\n"
        " &generic_tracer_nml\n"
        "        do_generic_tracer=.true.\n"
        "        do_generic_COBALT=.true.\n"
        "        force_update_fluxes=.true.\n"
        "        do_vertfill_post=.true.\n"
        "/\n"
        "\n"
        " &ice_albedo_nml\n"
        "            t_range = 10.\n"
        "/\n"
        "\n"
        " &ice_model_nml\n"
        "\n"
        "/\n"
        "\n"
        " &icebergs_nml\n"
        "        verbose=.false.\n"
        "        verbose_hrs=24\n"
        "        traj_sample_hrs=0\n"
        "        debug=.false.\n"
        "        really_debug=.false.\n"
        "        use_slow_find=.true.\n"
        "        add_weight_to_ocean=.false.\n"
        "        passive_mode=.false.\n"
        "        generate_test_icebergs=.false.\n"
        "        speed_limit=0.\n"
        "        use_roundoff_fix=.true.\n"
        "        make_calving_reproduce=.true.\n"
        "        old_bug_bilin=.false.\n"
        "        tidal_drift=0.005\n"
        "        use_updated_rolling_scheme=.true.\n"
        "/\n"
        "\n"
        " &monin_obukhov_nml\n"
        "            neutral = .true.\n"
        "/\n"
        "\n"
        " &ocean_albedo_nml\n"
        "            ocean_albedo_option = 2\n"
        "/\n"
        "\n"
        " &ocean_rough_nml\n"
        "            rough_scheme = 'beljaars'\n"
        "/\n"
        "\n"
        " &sat_vapor_pres_nml\n"
        "        construct_table_wrt_liq = .true.,\n"
        "        construct_table_wrt_liq_and_ice = .true.,\n"
        "/\n"
        "\n"
        " &surface_flux_nml\n"
        "            ncar_ocean_flux = .true.\n"
        "	    raoult_sat_vap = .true.\n"
        "/\n"
        "\n"
        " &topography_nml\n"
        "            topog_file = 'INPUT/navy_topography.data.nc'\n"
        "/\n"
        "\n"
        " &xgrid_nml\n"
        "        make_exchange_reproduce = .true.\n"
        "        interp_method = 'second_order'\n"
        "/\n"
    )
    with open("input.nml", 'w') as f:
        print(result, end="", file=f)


if __name__ == "__main__":
    args = parse_args()
    count = args.count
    year = 1958 + count
    generate_data_table(year)
    generate_diag_table(year)
    generate_input_nml(year)