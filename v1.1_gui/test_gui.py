import tkinter as tk
import pytest
import v1_1_gui.SimpleInsulinCalc_GUI_Refactored_Accessible as gui

def test_gui_calculation(monkeypatch):
    gui.input_display.set("breakfast")
    gui.carbs_display.set("50")
    gui.correctional_question.set("yes")
    gui.correction_display.set("2")
    gui.calculate()
    assert "units" in gui.result_display.get().lower()
