import customtkinter as ctk
from tkinter import filedialog, messagebox
import numpy as np
from PIL import Image
import os
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG      = "#0F1117"
SURFACE = "#171B26"
CARD    = "#1E2433"
BORDER  = "#2A3145"
ACCENT  = "#4F8EF7"
GREEN   = "#34C77B"
AMBER   = "#F5A623"
RED     = "#E05252"
TEXT    = "#EEF0F6"
MUTED   = "#7A8499"
SUBTLE  = "#3A4560"

# ── ENCRYPTION ──
def arnold_cat_map(arr, n):
    s = arr.shape[0]
    out = arr.copy()
    for _ in range(n):
        tmp = np.zeros_like(out)
        for x in range(s):
            for y in range(s):
                tmp[(x+y)%s][(x+2*y)%s] = out[x][y]
        out = tmp
    return out

def arnold_inverse(arr, n):
    s = arr.shape[0]
    out = arr.copy()
    for _ in range(n):
        tmp = np.zeros_like(out)
        for x in range(s):
            for y in range(s):
                tmp[(2*x-y)%s][(-x+y)%s] = out[x][y]
        out = tmp
    return out

def logistic_key(r, x0, size):
    key, x = [], x0
    for _ in range(size):
        x = r * x * (1 - x)
        key.append(int(x * 255))
    return np.array(key, dtype=np.uint8)

def do_encrypt(arr, iters, r, x0):
    s = min(arr.shape[:2])
    sq = arr[:s, :s].copy()
    scrambled = arnold_cat_map(sq, iters)
    ch = 3 if arr.ndim == 3 else 1
    key = logistic_key(r, x0, s*s*ch)
    flat = scrambled.flatten()
    return np.bitwise_xor(flat, np.resize(key, len(flat))).reshape(scrambled.shape)

def do_decrypt(arr, iters, r, x0):
    s = min(arr.shape[:2])
    sq = arr[:s, :s].copy()
    ch = 3 if arr.ndim == 3 else 1
    key = logistic_key(r, x0, s*s*ch)
    flat = sq.flatten()
    unxor = np.bitwise_xor(flat, np.resize(key, len(flat))).reshape(sq.shape)
    return arnold_inverse(unxor, iters)

# ══════════════════════════════════════════════
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ChaosShield — Image Encryption")
        self.geometry("1280x760")
        self.minsize(1100, 680)
        self.configure(fg_color=BG)
        self.img_array    = None
        self.result_array = None
        self.mode = ctk.StringVar(value="encrypt")
        self._build()

    def _build(self):
        # TOP BAR
        top = ctk.CTkFrame(self, fg_color=SURFACE, corner_radius=0, height=54)
        top.pack(fill="x")
        top.pack_propagate(False)
        ctk.CTkFrame(self, fg_color=BORDER, height=1, corner_radius=0).pack(fill="x")

        ctk.CTkLabel(top, text="ChaosShield",
            font=ctk.CTkFont(size=17, weight="bold"), text_color=TEXT
        ).pack(side="left", padx=20)
        ctk.CTkLabel(top, text="Arnold Cat Map  ·  Logistic Map  ·  Chaos-Based Encryption",
            font=ctk.CTkFont(size=11), text_color=MUTED
        ).pack(side="left", padx=4)

        self.status_chip = ctk.CTkLabel(top,
            text="● Ready",
            font=ctk.CTkFont(size=11), text_color=MUTED,
            fg_color=CARD, corner_radius=6
        )
        self.status_chip.pack(side="right", padx=16)
        ctk.CTkLabel(top, text="BSIT · v1.0",
            font=ctk.CTkFont(size=10), text_color=SUBTLE
        ).pack(side="right", padx=4)

        # BODY
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=14, pady=12)

        # SIDEBAR — uses place() for pinned buttons
        sidebar = ctk.CTkFrame(body, fg_color=SURFACE, corner_radius=12, width=284)
        sidebar.pack(side="left", fill="y", padx=(0,10))
        sidebar.pack_propagate(False)
        self._build_sidebar(sidebar)

        # RIGHT
        right = ctk.CTkFrame(body, fg_color="transparent")
        right.pack(side="left", fill="both", expand=True)
        self._build_right(right)

    # ─────────────────────────────────────────
    def _build_sidebar(self, sidebar):
        # TOP SECTION — scrollable params
        params = ctk.CTkFrame(sidebar, fg_color="transparent")
        params.place(relx=0, rely=0, relwidth=1, rely=0, y=0, x=0,
                     anchor="nw", width=284, height=430)
        params.pack_propagate(False)

        inner = ctk.CTkFrame(params, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=16, pady=14)

        # MODE
        self._tag(inner, "MODE")
        mf = ctk.CTkFrame(inner, fg_color=CARD, corner_radius=8)
        mf.pack(fill="x", pady=(3,8))
        for txt, val, col in [("Encrypt", "encrypt", ACCENT), ("Decrypt", "decrypt", GREEN)]:
            ctk.CTkRadioButton(mf, text=txt, variable=self.mode, value=val,
                font=ctk.CTkFont(size=12), text_color=TEXT,
                fg_color=col, hover_color=SUBTLE
            ).pack(anchor="w", padx=12, pady=6)

        self._sep(inner)

        # ITERATIONS
        self._tag(inner, "ARNOLD ITERATIONS")
        ic = ctk.CTkFrame(inner, fg_color=CARD, corner_radius=8)
        ic.pack(fill="x", pady=(3,8))

        rw = ctk.CTkFrame(ic, fg_color="transparent")
        rw.pack(fill="x", padx=12, pady=(10,3))
        ctk.CTkLabel(rw, text="Passes", font=ctk.CTkFont(size=11), text_color=MUTED).pack(side="left")
        self.iter_var = ctk.IntVar(value=10)
        self.iter_disp = ctk.CTkLabel(rw, text="10",
            font=ctk.CTkFont(size=14, weight="bold"), text_color=ACCENT)
        self.iter_disp.pack(side="right")

        ctk.CTkSlider(ic, from_=1, to=50, variable=self.iter_var,
            fg_color=BORDER, progress_color=ACCENT,
            button_color=ACCENT, button_hover_color="#6BA3FF",
            command=self._on_iter
        ).pack(fill="x", padx=12, pady=(0,8))

        self._sep(inner)

        # KEY
        self._tag(inner, "SECRET KEY — LOGISTIC MAP")
        kc = ctk.CTkFrame(inner, fg_color=CARD, corner_radius=8)
        kc.pack(fill="x", pady=(3,8))

        ctk.CTkLabel(kc, text="r  (3.57 – 4.0)", font=ctk.CTkFont(size=11), text_color=MUTED
        ).pack(anchor="w", padx=12, pady=(10,2))
        self.r_entry = ctk.CTkEntry(kc, fg_color=SURFACE, border_color=BORDER,
            text_color=TEXT, font=ctk.CTkFont(size=12), height=34)
        self.r_entry.insert(0, "3.99")
        self.r_entry.pack(fill="x", padx=12, pady=(0,8))

        ctk.CTkLabel(kc, text="x₀  (0.01 – 0.99)", font=ctk.CTkFont(size=11), text_color=MUTED
        ).pack(anchor="w", padx=12)
        self.x0_entry = ctk.CTkEntry(kc, fg_color=SURFACE, border_color=BORDER,
            text_color=TEXT, font=ctk.CTkFont(size=12), height=34)
        self.x0_entry.insert(0, "0.5")
        self.x0_entry.pack(fill="x", padx=12, pady=(2,10))

        self._sep(inner)

        # STRENGTH
        self._tag(inner, "STRENGTH")
        sc = ctk.CTkFrame(inner, fg_color=CARD, corner_radius=8)
        sc.pack(fill="x", pady=(3,0))
        self.str_bar = ctk.CTkProgressBar(sc, fg_color=BORDER,
            progress_color=GREEN, height=6, corner_radius=3)
        self.str_bar.pack(fill="x", padx=12, pady=(10,4))
        self.str_bar.set(0.2)
        self.str_lbl = ctk.CTkLabel(sc, text="Strong  ·  10 passes",
            font=ctk.CTkFont(size=11), text_color=GREEN)
        self.str_lbl.pack(pady=(0,10))

        # BOTTOM BUTTONS — pinned to bottom with place()
        btn_frame = ctk.CTkFrame(sidebar, fg_color=SURFACE, corner_radius=0)
        btn_frame.place(relx=0, rely=1.0, anchor="sw", relwidth=1)

        ctk.CTkFrame(btn_frame, fg_color=BORDER, height=1).pack(fill="x")

        inner_btn = ctk.CTkFrame(btn_frame, fg_color="transparent")
        inner_btn.pack(fill="x", padx=16, pady=14)

        ctk.CTkButton(inner_btn, text="📂  Load Image", height=38,
            fg_color=CARD, hover_color=BORDER,
            text_color=TEXT, font=ctk.CTkFont(size=12),
            border_width=1, border_color=BORDER, corner_radius=8,
            command=self.load_image
        ).pack(fill="x", pady=(0,6))

        self.proc_btn = ctk.CTkButton(inner_btn,
            text="Encrypt Image", height=42,
            fg_color=ACCENT, hover_color="#3A7AE0",
            text_color="#FFFFFF", font=ctk.CTkFont(size=13, weight="bold"),
            corner_radius=8, command=self.process
        )
        self.proc_btn.pack(fill="x", pady=(0,6))

        ctk.CTkButton(inner_btn, text="Save Result", height=36,
            fg_color="transparent", hover_color=CARD,
            text_color=GREEN, font=ctk.CTkFont(size=12),
            border_width=1, border_color=GREEN, corner_radius=8,
            command=self.save
        ).pack(fill="x", pady=(0,6))

        ctk.CTkButton(inner_btn, text="Clear", height=30,
            fg_color="transparent", hover_color=CARD,
            text_color=MUTED, font=ctk.CTkFont(size=11),
            corner_radius=8, command=self.clear
        ).pack(fill="x")

        self.mode.trace_add("write", lambda *a: self.proc_btn.configure(
            text="Encrypt Image" if self.mode.get()=="encrypt" else "Decrypt Image",
            fg_color=ACCENT if self.mode.get()=="encrypt" else "#2A6044"
        ))

    # ─────────────────────────────────────────
    def _build_right(self, p):
        # Image panels
        panels = ctk.CTkFrame(p, fg_color="transparent")
        panels.pack(fill="both", expand=True)
        panels.columnconfigure(0, weight=1)
        panels.columnconfigure(1, weight=1)
        panels.rowconfigure(0, weight=1)

        for col, lbl_attr, title_attr, placeholder, title in [
            (0, "orig_lbl", "orig_title", "No image loaded\n\nClick Load Image", "ORIGINAL"),
            (1, "res_lbl",  "res_title",  "Result will appear here\nafter processing", "RESULT"),
        ]:
            card = ctk.CTkFrame(panels, fg_color=SURFACE, corner_radius=12)
            card.grid(row=0, column=col, sticky="nsew",
                      padx=(0,6) if col==0 else (6,0))
            card.rowconfigure(1, weight=1)
            card.columnconfigure(0, weight=1)

            hdr = ctk.CTkFrame(card, fg_color=CARD, corner_radius=8, height=36)
            hdr.grid(row=0, column=0, sticky="ew", padx=12, pady=(12,6))
            hdr.pack_propagate(False)
            t = ctk.CTkLabel(hdr, text=title,
                font=ctk.CTkFont(size=11, weight="bold"), text_color=MUTED)
            t.pack(side="left", padx=14, pady=8)
            setattr(self, title_attr, t)

            lbl = ctk.CTkLabel(card, text=placeholder,
                font=ctk.CTkFont(size=12), text_color=MUTED,
                fg_color=CARD, corner_radius=8)
            lbl.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0,12))
            setattr(self, lbl_attr, lbl)

        # Bottom info bar
        bot = ctk.CTkFrame(p, fg_color=SURFACE, corner_radius=8, height=36)
        bot.pack(fill="x", pady=(8,0))
        bot.pack_propagate(False)

        self.info_lbl = ctk.CTkLabel(bot, text="",
            font=ctk.CTkFont(size=11), text_color=MUTED)
        self.info_lbl.pack(side="left", padx=14)

        self.prog = ctk.CTkProgressBar(bot, fg_color=BORDER,
            progress_color=ACCENT, height=4, corner_radius=2, width=150)
        self.prog.pack(side="right", padx=14, pady=16)
        self.prog.set(0)

    # ─────────────────────────────────────────
    def _tag(self, p, text):
        ctk.CTkLabel(p, text=text,
            font=ctk.CTkFont(size=10, weight="bold"), text_color=MUTED
        ).pack(anchor="w", pady=(0,2))

    def _sep(self, p):
        ctk.CTkFrame(p, fg_color=BORDER, height=1).pack(fill="x", pady=8)

    def _status(self, text, color=None):
        self.status_chip.configure(text=f"● {text}", text_color=color or MUTED)

    def _show(self, widget, arr):
        img = Image.fromarray(arr.astype(np.uint8))
        w = max(widget.winfo_width()-20, 300)
        h = max(widget.winfo_height()-20, 300)
        img.thumbnail((w, h), Image.LANCZOS)
        photo = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
        widget.configure(image=photo, text="")
        widget._img = photo

    def _on_iter(self, val):
        v = int(float(val))
        self.iter_disp.configure(text=str(v))
        s = v / 50
        self.str_bar.set(s)
        if s < 0.3:
            c, t = RED, f"Weak  ·  {v} passes"
        elif s < 0.6:
            c, t = AMBER, f"Moderate  ·  {v} passes"
        else:
            c, t = GREEN, f"Strong  ·  {v} passes"
        self.str_bar.configure(progress_color=c)
        self.str_lbl.configure(text=t, text_color=c)

    def load_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.tiff")])
        if not path: return
        img = Image.open(path).convert("RGB")
        self.img_array = np.array(img)
        self.after(100, lambda: self._show(self.orig_lbl, self.img_array))
        h, w = self.img_array.shape[:2]
        self.info_lbl.configure(text=f"{w}×{h}  ·  {os.path.basename(path)}")
        self._status(f"Loaded  ·  {w}×{h}px", TEXT)
        self.res_lbl.configure(image=None,
            text="Result will appear here\nafter processing")
        self.result_array = None
        self.prog.set(0)

    def process(self):
        if self.img_array is None:
            messagebox.showwarning("No Image", "Please load an image first!")
            return
        try:
            r  = float(self.r_entry.get())
            x0 = float(self.x0_entry.get())
            if not (3.57 <= r <= 4.0):
                messagebox.showerror("Invalid Key", "r must be between 3.57 and 4.0")
                return
            if not (0.01 <= x0 <= 0.99):
                messagebox.showerror("Invalid Key", "x₀ must be between 0.01 and 0.99")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid numbers for r and x₀")
            return

        iters = self.iter_var.get()
        mode  = self.mode.get()
        self.proc_btn.configure(state="disabled", text="Processing…")
        self.prog.set(0.15)
        self._status("Processing…", AMBER)

        def run():
            try:
                self.after(0, lambda: self.prog.set(0.45))
                result = do_encrypt(self.img_array, iters, r, x0) \
                    if mode == "encrypt" else do_decrypt(self.img_array, iters, r, x0)
                self.after(0, lambda: self.prog.set(0.85))
                self.result_array = result
                lbl = "ENCRYPTED" if mode == "encrypt" else "DECRYPTED"
                done_text = "Encrypt Image" if mode == "encrypt" else "Decrypt Image"
                self.after(300, lambda: [
                    self._show(self.res_lbl, result),
                    self.res_title.configure(text=lbl),
                    self.prog.set(1.0),
                    self._status(
                        ("Encrypted" if mode=="encrypt" else "Decrypted")
                        + f"  ·  {iters} passes  ·  r={r}  x₀={x0}", GREEN),
                    self.proc_btn.configure(state="normal", text=done_text)
                ])
            except Exception as e:
                self.after(0, lambda: [
                    messagebox.showerror("Error", str(e)),
                    self.proc_btn.configure(state="normal", text="Encrypt Image"),
                    self._status("Error occurred", RED)
                ])

        threading.Thread(target=run, daemon=True).start()

    def save(self):
        if self.result_array is None:
            messagebox.showwarning("Nothing to Save", "Process an image first!")
            return
        default = "encrypted.png" if self.mode.get()=="encrypt" else "decrypted.png"
        path = filedialog.asksaveasfilename(
            defaultextension=".png", initialfile=default,
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if path:
            Image.fromarray(self.result_array.astype(np.uint8)).save(path)
            self._status(f"Saved  ·  {os.path.basename(path)}", GREEN)
            messagebox.showinfo("Saved", f"File saved!\n{path}")

    def clear(self):
        self.img_array = self.result_array = None
        self.orig_lbl.configure(image=None,
            text="No image loaded\n\nClick Load Image")
        self.res_lbl.configure(image=None,
            text="Result will appear here\nafter processing")
        self.res_title.configure(text="RESULT")
        self.info_lbl.configure(text="")
        self.prog.set(0)
        self._status("Ready")

if __name__ == "__main__":
    App().mainloop()
