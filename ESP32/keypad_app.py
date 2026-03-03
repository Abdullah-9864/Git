import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import csv
import os
from datetime import datetime

# ─── CONFIG ──────────────────────────────────────────────────────────────────
SAVE_FILE = "esp32_data.csv"
BAUD_RATE = 115200

# ─── COLORS ──────────────────────────────────────────────────────────────────
BG        = "#0d1117"
PANEL     = "#161b22"
ACCENT    = "#00ff88"
ACCENT2   = "#00ccff"
BTN_NUM   = "#21262d"
BTN_HOVER = "#30363d"
BTN_ACT   = "#00ff88"
TEXT      = "#e6edf3"
MUTED     = "#8b949e"
RED       = "#ff4444"
ORANGE    = "#ff8c00"

class KeypadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ESP32 Keypad Controller")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.serial_conn = None
        self.current_input = ""
        self.history = []  # list of (timestamp, number, sum, product, avg)

        self.setup_csv()
        self.build_ui()

    # ─── CSV SETUP ────────────────────────────────────────────────────────────
    def setup_csv(self):
        if not os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Number Entered", "Running Sum", "Running Product", "Running Average"])

    def save_to_csv(self, number, sum_val, product_val, avg_val):
        with open(SAVE_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                number, sum_val, product_val, avg_val
            ])

    # ─── UI ───────────────────────────────────────────────────────────────────
    def build_ui(self):
        self.root.geometry("660x720")

        # ── Title Bar
        title_frame = tk.Frame(self.root, bg=BG, pady=12)
        title_frame.pack(fill="x", padx=20)
        tk.Label(title_frame, text="ESP32", font=("Courier New", 11, "bold"),
                 fg=ACCENT, bg=BG).pack(side="left")
        tk.Label(title_frame, text=" KEYPAD CONTROLLER", font=("Courier New", 11),
                 fg=MUTED, bg=BG).pack(side="left")

        save_btn = tk.Button(title_frame, text="📂 Open Data File",
                             font=("Courier New", 9), fg=ACCENT2, bg=PANEL,
                             bd=0, relief="flat", cursor="hand2",
                             command=lambda: os.startfile(SAVE_FILE) if os.name=="nt" else os.system(f"open {SAVE_FILE}"))
        save_btn.pack(side="right")

        # ── Serial Connection Bar
        conn_frame = tk.Frame(self.root, bg=PANEL, pady=8, padx=14)
        conn_frame.pack(fill="x", padx=20, pady=(0, 10))

        tk.Label(conn_frame, text="PORT:", font=("Courier New", 9),
                 fg=MUTED, bg=PANEL).pack(side="left")

        self.port_var = tk.StringVar()
        self.port_combo = ttk.Combobox(conn_frame, textvariable=self.port_var,
                                        width=12, font=("Courier New", 9))
        self.port_combo.pack(side="left", padx=6)
        self.refresh_ports()

        tk.Button(conn_frame, text="⟳", font=("Courier New", 10), fg=MUTED,
                  bg=PANEL, bd=0, cursor="hand2",
                  command=self.refresh_ports).pack(side="left")

        self.conn_btn = tk.Button(conn_frame, text="CONNECT",
                                   font=("Courier New", 9, "bold"),
                                   fg=BG, bg=ACCENT, bd=0, relief="flat",
                                   padx=10, cursor="hand2",
                                   command=self.toggle_connect)
        self.conn_btn.pack(side="left", padx=10)

        self.conn_status = tk.Label(conn_frame, text="● DISCONNECTED",
                                     font=("Courier New", 9), fg=RED, bg=PANEL)
        self.conn_status.pack(side="left")

        # ── Display Screen
        screen_frame = tk.Frame(self.root, bg=PANEL, pady=10, padx=14)
        screen_frame.pack(fill="x", padx=20, pady=(0, 8))

        tk.Label(screen_frame, text="INPUT", font=("Courier New", 8),
                 fg=MUTED, bg=PANEL).pack(anchor="w")
        self.display = tk.Label(screen_frame, text="0",
                                 font=("Courier New", 32, "bold"),
                                 fg=ACCENT, bg=PANEL, anchor="e")
        self.display.pack(fill="x")

        # ── Results Panel
        results_frame = tk.Frame(self.root, bg=PANEL, pady=8, padx=14)
        results_frame.pack(fill="x", padx=20, pady=(0, 8))

        tk.Label(results_frame, text="ESP32 RESULTS", font=("Courier New", 8),
                 fg=MUTED, bg=PANEL).pack(anchor="w")

        res_grid = tk.Frame(results_frame, bg=PANEL)
        res_grid.pack(fill="x", pady=4)

        self.result_labels = {}
        stats = [("COUNT", ACCENT), ("SUM", ACCENT2), ("PRODUCT", ORANGE), ("AVG", "#ff88cc")]
        for i, (label, color) in enumerate(stats):
            col_frame = tk.Frame(res_grid, bg=BTN_NUM, padx=10, pady=6)
            col_frame.grid(row=0, column=i, padx=3, sticky="nsew")
            res_grid.columnconfigure(i, weight=1)
            tk.Label(col_frame, text=label, font=("Courier New", 7),
                     fg=MUTED, bg=BTN_NUM).pack()
            lbl = tk.Label(col_frame, text="—", font=("Courier New", 13, "bold"),
                            fg=color, bg=BTN_NUM)
            lbl.pack()
            self.result_labels[label] = lbl

        # ── Keypad
        pad_frame = tk.Frame(self.root, bg=BG)
        pad_frame.pack(padx=20, pady=(0, 8))

        buttons = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [".", "0", "⌫"],
        ]
        for r, row in enumerate(buttons):
            for c, key in enumerate(row):
                self.make_btn(pad_frame, key, r, c)

        # Bottom row: Clear + Send
        clear_btn = tk.Button(pad_frame, text="CLEAR ALL",
                               font=("Courier New", 11, "bold"),
                               fg=RED, bg=BTN_NUM, bd=0, relief="flat",
                               width=8, height=2, cursor="hand2",
                               command=self.clear_all)
        clear_btn.grid(row=4, column=0, columnspan=1, padx=4, pady=4, sticky="nsew")
        self.bind_hover(clear_btn, BTN_NUM, BTN_HOVER)

        send_btn = tk.Button(pad_frame, text="SEND  →",
                              font=("Courier New", 11, "bold"),
                              fg=BG, bg=ACCENT, bd=0, relief="flat",
                              width=12, height=2, cursor="hand2",
                              command=self.send_number)
        send_btn.grid(row=4, column=1, columnspan=2, padx=4, pady=4, sticky="nsew")

        # ── Log
        log_frame = tk.Frame(self.root, bg=PANEL, pady=6, padx=10)
        log_frame.pack(fill="both", expand=True, padx=20, pady=(0, 16))
        tk.Label(log_frame, text="LOG", font=("Courier New", 8),
                 fg=MUTED, bg=PANEL).pack(anchor="w")
        self.log_box = tk.Text(log_frame, height=5, bg=BG, fg=MUTED,
                                font=("Courier New", 9), bd=0, relief="flat",
                                state="disabled", wrap="word")
        self.log_box.pack(fill="both", expand=True)

    def make_btn(self, parent, text, row, col):
        btn = tk.Button(parent, text=text,
                         font=("Courier New", 16, "bold"),
                         fg=TEXT, bg=BTN_NUM, bd=0, relief="flat",
                         width=5, height=2, cursor="hand2",
                         command=lambda t=text: self.key_press(t))
        btn.grid(row=row, column=col, padx=4, pady=4)
        self.bind_hover(btn, BTN_NUM, BTN_HOVER)
        return btn

    def bind_hover(self, widget, normal, hover):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover))
        widget.bind("<Leave>", lambda e: widget.config(bg=normal))

    # ─── LOGIC ────────────────────────────────────────────────────────────────
    def refresh_ports(self):
        ports = [p.device for p in serial.tools.list_ports.comports()]
        self.port_combo["values"] = ports
        if ports:
            self.port_combo.set(ports[0])

    def toggle_connect(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            self.serial_conn = None
            self.conn_btn.config(text="CONNECT", fg=BG, bg=ACCENT)
            self.conn_status.config(text="● DISCONNECTED", fg=RED)
            self.log("Disconnected from ESP32")
        else:
            try:
                port = self.port_var.get()
                self.serial_conn = serial.Serial(port, BAUD_RATE, timeout=1)
                self.conn_btn.config(text="DISCONNECT", fg=BG, bg=RED)
                self.conn_status.config(text="● CONNECTED", fg=ACCENT)
                self.log(f"Connected to {port} at {BAUD_RATE} baud")
                self.root.after(500, self.read_serial)
            except Exception as e:
                messagebox.showerror("Connection Error", str(e))

    def key_press(self, key):
        if key == "⌫":
            self.current_input = self.current_input[:-1]
        else:
            if key == "." and "." in self.current_input:
                return
            self.current_input += key

        self.display.config(text=self.current_input if self.current_input else "0")

    def send_number(self):
        if not self.current_input:
            self.log("Nothing to send!")
            return
        if not (self.serial_conn and self.serial_conn.is_open):
            self.log("Not connected to ESP32!")
            return
        try:
            num = self.current_input
            self.serial_conn.write((num + "\n").encode())
            self.log(f"Sent: {num}")
            self.current_input = ""
            self.display.config(text="0")
        except Exception as e:
            self.log(f"Send error: {e}")

    def clear_all(self):
        self.current_input = ""
        self.display.config(text="0")
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.write(b"CLEAR\n")
            self.log("Sent CLEAR to ESP32")
        for lbl in self.result_labels.values():
            lbl.config(text="—")

    def read_serial(self):
        if self.serial_conn and self.serial_conn.is_open:
            try:
                while self.serial_conn.in_waiting:
                    line = self.serial_conn.readline().decode().strip()
                    if line:
                        self.parse_response(line)
            except:
                pass
            self.root.after(100, self.read_serial)

    def parse_response(self, line):
        self.log(f"ESP32: {line}")
        if line.startswith("COUNT:"):
            try:
                parts = dict(p.split(":") for p in line.split("|"))
                count   = parts["COUNT"]
                sum_v   = parts["SUM"]
                prod_v  = parts["PRODUCT"]
                avg_v   = parts["AVG"]

                self.result_labels["COUNT"].config(text=count)
                self.result_labels["SUM"].config(text=sum_v)
                self.result_labels["PRODUCT"].config(text=prod_v)
                self.result_labels["AVG"].config(text=avg_v)

                # Save to CSV
                # figure out what number was just entered
                self.save_to_csv("(sent)", sum_v, prod_v, avg_v)
            except Exception as e:
                self.log(f"Parse error: {e}")

    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_box.config(state="normal")
        self.log_box.insert("end", f"[{timestamp}] {msg}\n")
        self.log_box.see("end")
        self.log_box.config(state="disabled")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = KeypadApp(root)
    root.mainloop()
