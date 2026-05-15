import cadquery as cq
import os
import shutil

def convert_step(input_path, output_path, fmt):
    print(f"  {fmt}: {output_path}")
    try:
        part = cq.importers.importStep(input_path)
        assy = cq.Assembly()
        assy.add(part, name=os.path.basename(input_path))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        assy.save(output_path, exportType=fmt)
    except Exception as e:
        print(f"    ERROR: {e}")

MAPPINGS = [
    # (source_step, dest_name, dest_dir)

    # Voron Bodies
    ("Voron/goliath_chcXL_sherpa/sphinx_tLW_goliath_voron.step",         "body_goliath-chcxl_sherpa_voron",    "Configurator/Parts/Voron/Bodies"),
    ("Voron/rapidoUHF_sherpa/sphinx_tLW_rapidoUHF_voron.step",           "body_rapido-uhf_sherpa_voron",        "Configurator/Parts/Voron/Bodies"),
    ("Voron/tricorn_sherpa_voron/sphinx_tLW_tricorn_voron.step",          "body_tricorn_sherpa_voron",           "Configurator/Parts/Voron/Bodies"),

    # Voron Common (shared parts — sourced from goliath variant)
    ("Voron/goliath_chcXL_sherpa/sphinx_tLW_ middle_braket.step",        "mount_middle_bracket_voron",          "Configurator/Parts/Voron/Common"),
    ("Voron/goliath_chcXL_sherpa/sphinx_tLW_rear_duct.step",             "duct_rear_voron",                     "Configurator/Parts/Voron/Common"),
    ("Voron/goliath_chcXL_sherpa/sphinx_tLW_top_support_sherpa.step",    "support_top_sherpa_voron",            "Configurator/Parts/Voron/Common"),

    # Voron Accessory
    ("Voron/Apex clip sphinx_voron.step",                                 "mount_apex_clip_voron",               "Configurator/Parts/Voron/Common"),

    # Monolith Bodies
    ("Monolith/sphinx_tLW_dragonUHF_sherpa/sphinx_tLW_dragonUHF - main_body_dragonUHF.step", "body_dragon-uhf_sherpa_monolith",   "Configurator/Parts/Monolith/Bodies"),
    ("Monolith/sphinx_tLW_goliath_chcxl_sherpa/sphinx_tLW_goliath - main_body_goliath.step", "body_goliath-chcxl_sherpa_monolith","Configurator/Parts/Monolith/Bodies"),
    ("Monolith/sphinx_tLW_rapidoUHF_sherpa/sphinx_tLW_rapido - main_body_rapido.step",       "body_rapido-uhf_sherpa_monolith",   "Configurator/Parts/Monolith/Bodies"),
    ("Monolith/sphinx_tLW_tricorn_sherpa/sphinx_tLW_tricorn_main_body_tricorn.step",          "body_tricorn_sherpa_monolith",      "Configurator/Parts/Monolith/Bodies"),

    # Monolith Common (sourced from goliath variant)
    ("Monolith/sphinx_tLW_goliath_chcxl_sherpa/sphinx_tLW_ middle_braket.step",              "mount_middle_bracket_monolith",     "Configurator/Parts/Monolith/Common"),
    ("Monolith/sphinx_tLW_goliath_chcxl_sherpa/sphinx_tLW_rear_duct.step",                   "duct_rear_monolith",                "Configurator/Parts/Monolith/Common"),
    ("Monolith/sphinx_tLW_goliath_chcxl_sherpa/sphinx_tLW_top_support_sherpa.step",          "support_top_sherpa_monolith",       "Configurator/Parts/Monolith/Common"),

    # Monolith Accessory
    ("Monolith/Apex clip 9mm.step",                                       "mount_apex_clip_9mm_monolith",        "Configurator/Parts/Monolith/Common"),
]

STL_COPIES = [
    ("Voron/goliath_chcXL_sherpa/sphinx_tLW_top_support_sherpa_switch.stl",        "Configurator/Parts/Voron/Common/support_top_sherpa_switch_voron.stl"),
    ("Monolith/sphinx_tLW_goliath_chcxl_sherpa/sphinx_tLW_top_support_sherpa_switch.stl", "Configurator/Parts/Monolith/Common/support_top_sherpa_switch_monolith.stl"),
]

for src, name, dest_dir in MAPPINGS:
    print(f"\n{src}")
    for fmt in ("GLB", "STL"):
        convert_step(src, os.path.join(dest_dir, f"{name}.{fmt.lower()}"), fmt)

for src, dest in STL_COPIES:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(src, dest)
        print(f"\nCopied STL: {dest}")

print("\nDone.")
