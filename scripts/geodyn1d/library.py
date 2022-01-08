
#
# lithospheres
#

# =============================================================================
lith125_thick_hot_crust = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [15e3,10e3,15e3,85e3,0.0e0,475e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "rho": 2850.0e0,
        "temp_top": 0.0e0,
        "H": 1.2e-6
        },
"matMC": {
        "rho": 2850.0e0,
        "H": 1.2e-6
        },
"matLC": {
        "rho": 2850.0e0,
        "H": 1.2e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 16.2793e-3
        }
}


# =============================================================================
paper = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [17.5e3,0e0,17.5e3,85e3,0e0,480e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.3e-6,
        "alpha": 2.4e-5,
        "k": 2.1,
        "rho": 2750
        },
"matMC": {
        "rho": 2750
        },
"matLC": {
        "H": 0.2e-6,
        "alpha": 2.4e-5,
        "k": 2.5,
        "rho": 2850
        },
"matLM1": {
        "H": 0.0,
        "alpha": 3.0e-5,
        "k": 3.3,
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "H": 0.0,
        "k": 3.3,
        "temp_bottom": 1765.15e0,
        "temp_potential": 1525.15e0,
        "q_bottom": 28.3242187e-3
        }
}
# =============================================================================
lith60 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,25e3,0e0,0.0e0,540e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 39.6503906e-3
        }
}


# =============================================================================
lith200 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,45e3,45e3,75e3,400e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}
# =============================================================================
lith250 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,55e3,160e3,0.0e0,350e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
         },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}

# =============================================================================
lith240 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,55e3,150e3,0.0e0,360e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
         },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}
# =============================================================================
lith280 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,80e3,10e3,155e3,320e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
         },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}

# =============================================================================
lith160 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,55e3,70e3,0.0e0,440e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}

# =============================================================================
lith180 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,45e3,45e3,55e3,420e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}
# =============================================================================
lith180_LMdepl24 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [15e3,10e3,10e3,55e3,90e3,420e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3276
        },
"matLM2": {
        "rho": 3276
        },
"matSLM": {
        "rho": 3760
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}
# =============================================================================
lith180_LMdepl44 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [15e3,10e3,10e3,55e3,90e3,420e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3256
        },
"matLM2": {
        "rho": 3256
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}
# =============================================================================
lith180_LMdepl63 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [15e3,10e3,10e3,55e3,90e3,420e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.78e-6
        },
"matMC": {
        "H": 1.78e-6
        },
"matLC": {
        "H": 0.82e-6
        },
"matLM1": {
        "rho": 3237
        },
"matLM2": {
        "rho": 3237
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 12.4460937e-3
        }
}
# =============================================================================
lith120 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [15e3,10e3,10e3,85.0e3,0.0e0,480e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.2e-6
        },
"matMC": {
        "H": 1.2e-6
        },
"matLC": {
        "H": 0.473e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 20.59375e-3
        }
}
# =============================================================================
lith125_40km = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,15e3,10e3,85e3,0.0e0,0.0e0,475e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.299e-6
        },
"matMC": {
        "H": 1.299e-6
        },
"matLC": {
        "H": 0.498e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 19.5e-3
        }
}
# =============================================================================
lith130_40km = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,15e3,10e3,90e3,0.0e0,0.0e0,470e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.299e-6
        },
"matMC": {
        "H": 1.299e-6
        },
"matLC": {
        "H": 0.498e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 19.5e-3
        }
}
# =============================================================================
lith167_40km = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,15e3,10e3,127e3,0.0e0,0.0e0,433e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.299e-6
        },
"matMC": {
        "H": 1.299e-6
        },
"matLC": {
        "H": 0.498e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 19.5e-3
        }
}
# =============================================================================
lith192_65km = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [27.5e3,27.5e3,10e3,127e3,0.0e0,0.0e0,408e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.299e-6
        },
"matMC": {
        "H": 1.299e-6
        },
"matLC": {
        "H": 0.498e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 19.5e-3
        }
}




# =============================================================================
lith125 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matLM3','matSLM'],
"thicknesses": [15e3,10e3,10e3,90e3,0.0e0,0.0e0,475e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcLM3','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 1.299e-6
        },
"matMC": {
        "H": 1.299e-6
        },
"matLC": {
        "H": 0.498e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 19.5e-3
        }
}
# =============================================================================
lith40_CC10_LM30 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [4.3e3,2.85e3,2.85e3,0.0e0,30e3,560e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 13.e-6  # this gives apparent moho temperature of 540.2
        },
"matMC": {
        "H": 13.e-6
        },
"matLC": {
        "H": 13.e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 56.6875e-3
        }
}
# =============================================================================
lith35_CC5_LM30 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [2.15e3,1.425e3,1.425e3,0.0e0,30e3,565e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 60.e-6  # this gives apparent moho temperature of 469.4
        },
"matMC": {
        "H": 60.e-6
        },
"matLC": {
        "H": 60.e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 61.8437500e-3
        }
}
# =============================================================================
lith10_CC10_LM0 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [4.3e3,2.85e3,2.85e3,0.0e0,0.0e0,590e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 13.e-6  # this gives apparent moho temperature of 540.2
        },
"matMC": {
        "H": 13.e-6
        },
"matLC": {
        "H": 13.e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 224.0312500e-3
        }
}
# =============================================================================
lith5_CC5_LM0 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [2.15e3,1.425e3,1.425e3,0.0e0,0.0e0,595e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H": 60.e-6  # this gives apparent moho temperature of 469.4
        },
"matMC": {
        "H": 60.e-6
        },
"matLC": {
        "H": 60.e-6
        },
"matLM1": {
        "rho": 3300
        },
"matLM2": {
        "rho": 3300
        },
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 427.5312500e-3
        }
}
# =============================================================================
ridge_NoOc_NoDiffLayer = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [0.0e0,0.0e0,0.0e0,0e0,0.0e0,600e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "H": 0.0e0
        },
"matMC": {
        "H": 0.0e0
        },
"matLC": {
        "H": 0.0e0
        },
"matLM1": {
        "rho": 3300,
        "H": 0.0e0
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        }, 
"thermBcSLM": {
        "temp_top": 0.0e0,
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 19.5e-3
        }
}
# =============================================================================
ridge_Oc_DiffLayer6 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [6.0e3,0.0e0,0.0e0,0e0,0.0e0,594e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H"  : 0.0e0,
        "rho": 2900.
        },
"matMC": {
        "H": 0.0e0
        },
"matLC": {
        "H": 0.0e0
        },
"matLM1": {
        "rho": 3300,
        "H": 0.0e0
        },
"matLM2": {
        "rho": 3300
        },
"matSLM": {
        "rho": 3300
        }, 
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 480.875e-3
        }
}
# =============================================================================
ridge_Oc6_5_DiffLayer26_TECMOD = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLMd','matSLM'],
"thicknesses": [6.5e3,0.0e0,0.0e0,0e0,19.5e3,99.0e3,475e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLMd','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H"  : 0.0e0,
        "rho": 2900.e0
        },
"matMC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLM1": {
        "rho": 3288,
        "H": 0.0e0
        },
"matLM2": {
        "rho": 3288,
        "H": 0.0e0
        },
"matSLMd": {
        "rho": 3288,
        "H": 0.0e0
        },
"matSLM": {
        "rho": 3300,
        "H": 0.0e0
        },
'thermBcSLMd': {
        'temp_bottom': 1573.15,
        'temp_potential': 1523.15e0,
        'q_bottom': 109.0781250e-3
        },
"thermBcSLM": {
        "temp_bottom": 1763.15e0,
        "temp_potential": 1523.15e0,
        "q_bottom": 109.0781250e-3
        }
}
# =============================================================================
ridge_Oc6_5_DiffLayer26_TECMOD180 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLMd','matSLM'],
"thicknesses": [6.5e3,0.0e0,0.0e0,0e0,19.5e3,99.0e3,475e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLMd','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H"  : 0.0e0,
        "rho": 2900.e0
        },
"matMC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLM1": {
        "rho": 3288,
        "H": 0.0e0
        },
"matLM2": {
        "rho": 3288,
        "H": 0.0e0
        },
"matSLMd": {
        "rho": 3288,
        "H": 0.0e0
        },
"matSLM": {
        "rho": 3300,
        "H": 0.0e0
        },
'thermBcSLMd': {
        'temp_bottom': 1551e0,    #1813.15e0,
        'temp_potential': 1501e0, #1510.0e0
        'q_bottom': 109.8679625e-3
    },
'thermBcSLM': {
        'temp_bottom': 1741e0,    #1813.15e0,
        'temp_potential': 1501e0, #1510.0e0
        'q_bottom': 109.8679625e-3
    }
}
# =============================================================================
ridge_Oc6_5_DiffLayer26_TECMOD240 = {
"numlayers": 7,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLMd','matSLM'],
"thicknesses": [6.5e3,0.0e0,0.0e0,0e0,19.5e3,99.0e3,475e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLMd','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H"  : 0.0e0,
        "rho": 2900.e0
        },
"matMC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLM1": {
        "rho": 3288,
        "H": 0.0e0
        },
"matLM2": {
        "rho": 3288,
        "H": 0.0e0
        },
"matSLMd": {
        "rho": 3288,
        "H": 0.0e0
        },
"matSLM": {
        "rho": 3300,
        "H": 0.0e0
        },
'thermBcSLMd': {
        'temp_bottom': 1527e0,    #1813.15e0,
        'temp_potential': 1477e0, #1510.0e0
        'q_bottom': 105.0710875e-3
    },
'thermBcSLM': {
        'temp_bottom': 1717e0,    #1813.15e0,
        'temp_potential': 1477e0, #1510.0e0
        'q_bottom': 105.0710875e-3
    }
}



# =============================================================================
ridge_Oc6_5_DiffLayer26 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [6.5e3,0.0e0,0.0e0,0e0,19.5e3,574e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H"  : 0.0e0,
        "rho": 2900.e0
        },
"matMC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLM1": {
        "rho": 3300,
        "H": 0.0e0
        },
"matLM2": {
        "rho": 3300,
        "H": 0.0e0
        },
"matSLM": {
        "rho": 3300
        }, 
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 111.6718750e-3
        }
}

# =============================================================================
ridge_Oc_DiffLayer26 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [6.0e3,0.0e0,0.0e0,0e0,20.0e3,574e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "temp_top": 0.0e0,
        "H"  : 0.0e0,
        "rho": 2900.e0
        },
"matMC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLC": {
        "H": 0.0e0,
        "rho": 2900.e0
        },
"matLM1": {
        "rho": 3300,
        "H": 0.0e0
        },
"matLM2": {
        "rho": 3300,
        "H": 0.0e0
        },
"matSLM": {
        "rho": 3300
        }, 
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 111.6718750e-3
        }
}
# =============================================================================
ridge_NoOc_DiffLayer26 = {
"numlayers": 6,
"nature_layers": ['matUC','matMC','matLC','matLM1','matLM2','matSLM'],
"thicknesses": [0.0e0,0.0e0,0.0e0,0e0,26.0e3,574e3],
"thermalBc": ['thermBcUC','thermBcMC','thermBcLC','thermBcLM1','thermBcLM2','thermBcSLM'],
"matUC": {
        "H"  : 0.0e0,
        "rho": 2900.
        },
"matMC": {
        "H": 0.0e0
        },
"matLC": {
        "H": 0.0e0
        },
"matLM1": {
        "rho": 3300,
        "H": 0.0e0
        },
"matLM2": {
        "temp_top": 0.0e0,
        "rho": 3300,
        "H": 0.0e0
        },
"matSLM": {
        "rho": 3300
        }, 
"thermBcSLM": {
        "temp_bottom": 1793.15e0,
        "temp_potential": 1553.15e0,
        "q_bottom": 111.6718750e-3
        }
}
# =============================================================================


