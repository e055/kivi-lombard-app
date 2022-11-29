import dearpygui.dearpygui as dpg
from body import *

dpg.create_context()


def ad_person():
    run("add")


def gui():
    with dpg.window(tag="Primary Window"):
        dpg.add_text("Lombard APP")
        dpg.add_button(label="Add Person", callback=ad_person)

    dpg.create_viewport(title='Custom Title', width=800, height=800)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


gui()