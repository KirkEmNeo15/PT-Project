"""Topic 1: FCFS, SJF, SRTF, and Priority Scheduling."""

import tkinter as tk
from tkinter import ttk

import customtkinter as ctk

from cpu_core import INPUT_ORDER, MAX_JOBS, PROCESS_ID, common_schedules, parse_workload
from priority import HIGH_FIRST, LOW_FIRST, NON_PREEMPTIVE, PREEMPTIVE, priority_schedule
from theme import C, CFONT, FONT, P, px, setup_fonts, style_tables

EXAMPLE_ROWS = "P1   0   7   4\nP2   2   4   1\nP3   4   1   3\nP4   5   4   2"
PROCESS_COLORS = ("#16665e", "#245797", "#7c4a9b", "#a14c32",
                  "#42673d", "#865519", "#385975", "#9b3c71")


def make_tabs(parent):
    return ctk.CTkTabview(
        parent, fg_color=C("card"), anchor="nw", border_width=1, border_color=C("border"),
        segmented_button_font=FONT.bold, segmented_button_fg_color=C("segment"),
        segmented_button_unselected_color=C("segment"),
        segmented_button_unselected_hover_color=C("accent_hover"),
        segmented_button_selected_color=C("accent"),
        segmented_button_selected_hover_color=C("accent_hover"), text_color="white",
    )


def make_menu(parent, values, **kwargs):
    return ctk.CTkOptionMenu(
        parent, values=list(values), font=FONT.ui, dropdown_font=FONT.ui,
        fg_color=C("accent"), button_color=C("accent_hover"),
        button_hover_color=C("accent"), text_color="white",
        dropdown_fg_color=C("card"), dropdown_hover_color=C("accent_soft"),
        dropdown_text_color=C("text"), height=32, **kwargs,
    )


def make_table(parent, headings, widths):
    frame = ctk.CTkFrame(parent, fg_color=C("card"))
    frame.pack(fill="both", expand=True, padx=6, pady=6)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    tree = ttk.Treeview(frame, columns=headings, show="headings", style="Result.Treeview", height=5)
    for name, width in zip(headings, widths, strict=True):
        width = max(px(width), CFONT.bold.measure(name) + px(16))
        tree.heading(name, text=name)
        tree.column(name, width=width, minwidth=width, stretch=False, anchor="center")
    tree.tag_configure("alternate", background=P()["soft"])

    vertical = ctk.CTkScrollbar(frame, command=tree.yview)
    horizontal = ctk.CTkScrollbar(frame, orientation="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)
    tree.grid(row=0, column=0, sticky="nsew")
    vertical.grid(row=0, column=1, sticky="ns")
    horizontal.grid(row=1, column=0, sticky="ew")
    return tree


def fill_table(tree, rows):
    tree.delete(*tree.get_children())
    for index, row in enumerate(rows):
        tree.insert("", "end", values=row, tags=("alternate",) if index % 2 else ())
    for index, name in enumerate(tree["columns"]):
        widest = max((CFONT.ui.measure(str(row[index])) for row in rows), default=0)
        width = max(tree.column(name, "minwidth"), widest + px(16))
        tree.column(name, width=width)
    tree.xview_moveto(0)
    tree.yview_moveto(0)


