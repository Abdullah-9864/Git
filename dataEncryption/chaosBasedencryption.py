import customtkinter as ctk
from tkinter import filedialog, messagebox
import numpy as np
from PIL import Image
import os
import threading

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

BG       = "#F4F6FA"
SURFACE  = "#FFFFFF"
CARD     = "#F0F2F8"
BORDER   = "#DDE1EC"
ACCENT   = "#F5A001"
ACCENT_H = "#A9DE18"
GREEN    = "#059669"
AMBER    = "#D97706"
RED      = "#DC2626"
TEXT     = "#0F172A"
TEXT2    = "#334155"
MUTED    = "#64748B"
SUBTLE   = "#94A3B8"
SIDEBAR  = "#1E293B"
SB_TEXT  = "#E2E8F0"
SB_MUTED = "#94A3B8"
SB_CARD  = "#273449"
SB_HOVER = "#334155"
SB_BORDER= "#334155"

# ── FAST ENCRYPTION using NumPy (no loops!) ──
def arnold_cat_map(arr, n):
    s = arr.shape[0]
    out = arr.copy()
    for _ in range(n):
        # create index grids
        x, y = np.meshgrid(np.arange(s), np.arange(s), indexing='ij')
        new_x = (x + y) % s
        new_y = (x + 2*y) % s
        tmp = np.zeros_like(out)
        tmp[new_x, new_y] = out[x, y]
        out = tmp
    return out

def arnold_inverse(arr, n):
    s = arr.shape[0]
    out = arr.copy()
    for _ in range(n):
        x, y = np.meshgrid(np.arange(s), np.arange(s), indexing='ij')
        new_x = (2*x - y) % s
        new_y = (-x + y) % s
        tmp = np.zeros_like(out)
        tmp[new_x, new_y] = out[x, y]
        out = tmp
    return out

def logistic_key(r, x0, size):
    key, x = [], x0
    for _ in range(size):
        x = r * x * (1 - x)
        key.append(int(x * 255))
    return np.array(key, dtype=np.uint8)

def do_encrypt(arr, iters, r, x0):
    # resize to 256x256 for fast processing
    img = Image.fromarray(arr.astype(np.uint8))
    img = img.resize((256, 256), Image.LANCZOS)
    arr256 = np.array(img)
    scrambled = arnold_cat_map(arr256, iters)
    ch = 3 if arr256.ndim == 3 else 1
    key = logistic_key(r, x0, 256*256*ch)
    flat = scrambled.flatten()
    return np.bitwise_xor(flat, np.resize(key, len(flat))).reshape(scrambled.shape)

def do_decrypt(arr, iters, r, x0):
    img = Image.fromarray(arr.astype(np.uint8))
    img = img.resize((256, 256), Image.LANCZOS)
    arr256 = np.array(img)
    ch = 3 if arr256.ndim == 3 else 1
    key = logistic_key(r, x0, 256*256*ch)
    flat = arr256.flatten()
    unxor = np.bitwise_xor(flat, np.resize(key, len(flat))).reshape(arr256.shape)
    return arnold_inverse(unxor, iters)

# ══════════════════════════════════════════════
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ChaosShield — Image Encryption")
        self.geometry("1300x780")
        self.minsize(1100, 700)
        self.configure(fg_color=BG)
        self.img_array    = None
        self.result_array = None
        self.mode = ctk.StringVar(value="encrypt")
        self._build()

    def _build(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        sidebar = ctk.CTkFrame(self, fg_color=SIDEBAR, corner_radius=0, width=300)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)
        sidebar.grid_rowconfigure(1, weight=1)
        self._build_sidebar(sidebar)

        content = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)
        content.grid(row=0, column=1, sticky="nsew")
        content.grid_rowconfigure(1, weight=1)
        content.grid_columnconfigure(0, weight=1)
        self._build_content(content)

    def _build_sidebar(self, sb):
        # LOGO
        logo = ctk.CTkFrame(sb, fg_color=ACCENT, corner_radius=0, height=72)
        logo.grid(row=0, column=0, sticky="ew")
        logo.pack_propagate(False)
        ctk.CTkLabel(logo, text="ChaosShield",
            font=ctk.CTkFont(size=20, weight="bold"), text_color="#FFFFFF"
        ).pack(pady=(16,0))
        ctk.CTkLabel(logo, text="Image Encryption Tool",
            font=ctk.CTkFont(size=11), text_color="#BFDBFE"
        ).pack(pady=(0,16))

        # PARAMS
        params = ctk.CTkFrame(sb, fg_color="transparent")
        params.grid(row=1, column=0, sticky="nsew")
        inner = ctk.CTkFrame(params, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=18, pady=16)

        # MODE
        self._sb_tag(inner, "MODE")
        mf = ctk.CTkFrame(inner, fg_color=SB_CARD, corner_radius=10)
        mf.pack(fill="x", pady=(4,12))
        for txt, val, col in [("Encrypt Image","encrypt",ACCENT),("Decrypt Image","decrypt","#10B981")]:
            ctk.CTkRadioButton(mf, text=txt, variable=self.mode, value=val,
                font=ctk.CTkFont(size=12), text_color=SB_TEXT,
                fg_color=col, hover_color=SB_HOVER
            ).pack(anchor="w", padx=14, pady=8)

        self._sb_sep(inner)

        # ITERATIONS
        self._sb_tag(inner, "ARNOLD CAT MAP")
        ic = ctk.CTkFrame(inner, fg_color=SB_CARD, corner_radius=10)
        ic.pack(fill="x", pady=(4,12))
        row = ctk.CTkFrame(ic, fg_color="transparent")
        row.pack(fill="x", padx=14, pady=(12,4))
        ctk.CTkLabel(row, text="Iterations", font=ctk.CTkFont(size=12), text_color=SB_MUTED).pack(side="left")
        self.iter_var = ctk.IntVar(value=10)
        self.iter_disp = ctk.CTkLabel(row, text="10",
            font=ctk.CTkFont(size=16, weight="bold"), text_color="#60A5FA")
        self.iter_disp.pack(side="right")
        ctk.CTkSlider(ic, from_=1, to=50, variable=self.iter_var,
            fg_color=SB_BORDER, progress_color="#3B82F6",
            button_color="#60A5FA", button_hover_color=ACCENT,
            command=self._on_iter
        ).pack(fill="x", padx=14, pady=(0,6))
        hint = ctk.CTkFrame(ic, fg_color="transparent")
        hint.pack(fill="x", padx=14, pady=(0,12))
        ctk.CTkLabel(hint, text="1 = faster", font=ctk.CTkFont(size=10), text_color=SB_BORDER).pack(side="left")
        ctk.CTkLabel(hint, text="50 = stronger", font=ctk.CTkFont(size=10), text_color=SB_BORDER).pack(side="right")

        self._sb_sep(inner)

        # KEY
        self._sb_tag(inner, "LOGISTIC MAP KEY")
        kc = ctk.CTkFrame(inner, fg_color=SB_CARD, corner_radius=10)
        kc.pack(fill="x", pady=(4,12))
        ctk.CTkLabel(kc, text="r  (3.57 – 4.0)", font=ctk.CTkFont(size=11), text_color=SB_MUTED).pack(anchor="w", padx=14, pady=(12,2))
        self.r_entry = ctk.CTkEntry(kc, fg_color=SIDEBAR, border_color=SB_BORDER,
            text_color=SB_TEXT, font=ctk.CTkFont(size=12), height=36)
        self.r_entry.insert(0, "3.99")
        self.r_entry.pack(fill="x", padx=14, pady=(0,8))
        ctk.CTkLabel(kc, text="x₀  (0.01 – 0.99)", font=ctk.CTkFont(size=11), text_color=SB_MUTED).pack(anchor="w", padx=14)
        self.x0_entry = ctk.CTkEntry(kc, fg_color=SIDEBAR, border_color=SB_BORDER,
            text_color=SB_TEXT, font=ctk.CTkFont(size=12), height=36)
        self.x0_entry.insert(0, "0.5")
        self.x0_entry.pack(fill="x", padx=14, pady=(2,12))

        self._sb_sep(inner)

        # STRENGTH
        self._sb_tag(inner, "ENCRYPTION STRENGTH")
        sc = ctk.CTkFrame(inner, fg_color=SB_CARD, corner_radius=10)
        sc.pack(fill="x", pady=(4,0))
        self.str_bar = ctk.CTkProgressBar(sc, fg_color=SB_BORDER,
            progress_color="#10B981", height=8, corner_radius=4)
        self.str_bar.pack(fill="x", padx=14, pady=(12,6))
        self.str_bar.set(0.2)
        self.str_lbl = ctk.CTkLabel(sc, text="Strong  ·  10 iterations",
            font=ctk.CTkFont(size=11), text_color="#6EE7B7")
        self.str_lbl.pack(pady=(0,12))

        # BUTTONS pinned at bottom
        btn_area = ctk.CTkFrame(sb, fg_color=SB_CARD, corner_radius=0)
        btn_area.grid(row=2, column=0, sticky="ew")
        ctk.CTkFrame(btn_area, fg_color=SB_BORDER, height=1).pack(fill="x")
        bi = ctk.CTkFrame(btn_area, fg_color="transparent")
        bi.pack(fill="x", padx=16, pady=14)

        ctk.CTkButton(bi, text="Load Image", height=40,
            fg_color="transparent", hover_color=SB_HOVER,
            text_color=SB_TEXT, font=ctk.CTkFont(size=12),
            border_width=1, border_color=SB_BORDER, corner_radius=8,
            command=self.load_image
        ).pack(fill="x", pady=(0,8))

        self.proc_btn = ctk.CTkButton(bi, text="Encrypt Image", height=44,
            fg_color=ACCENT, hover_color=ACCENT_H,
            text_color="#FFFFFF", font=ctk.CTkFont(size=13, weight="bold"),
            corner_radius=8, command=self.process
        )
        self.proc_btn.pack(fill="x", pady=(0,8))

        ctk.CTkButton(bi, text="Save Result", height=38,
            fg_color="transparent", hover_color=SB_HOVER,
            text_color="#6EE7B7", font=ctk.CTkFont(size=12),
            border_width=1, border_color="#10B981", corner_radius=8,
            command=self.save
        ).pack(fill="x", pady=(0,8))

        ctk.CTkButton(bi, text="Clear All", height=32,
            fg_color="transparent", hover_color=SB_HOVER,
            text_color=SB_MUTED, font=ctk.CTkFont(size=11),
            corner_radius=8, command=self.clear
        ).pack(fill="x")

        self.mode.trace_add("write", lambda *a: self.proc_btn.configure(
            text="Encrypt Image" if self.mode.get()=="encrypt" else "Decrypt Image",
            fg_color=ACCENT if self.mode.get()=="encrypt" else "#059669"
        ))

    def _build_content(self, p):
        # TOP BAR
        top = ctk.CTkFrame(p, fg_color=SURFACE, corner_radius=0, height=56)
        top.grid(row=0, column=0, sticky="ew")
        top.pack_propagate(False)
        ctk.CTkFrame(p, fg_color=BORDER, height=1, corner_radius=0).grid(row=0, column=0, sticky="sew")

        ctk.CTkLabel(top, text="Workspace",
            font=ctk.CTkFont(size=15, weight="bold"), text_color=TEXT
        ).pack(side="left", padx=20, pady=16)

        self.status_lbl = ctk.CTkLabel(top,
            text="Ready — load an image to begin",
            font=ctk.CTkFont(size=11), text_color=MUTED)
        self.status_lbl.pack(side="left", padx=4)

        self.info_lbl = ctk.CTkLabel(top, text="",
            font=ctk.CTkFont(size=11), text_color=MUTED,
            fg_color=CARD, corner_radius=6)
        self.info_lbl.pack(side="right", padx=16, pady=14)

        # IMAGES
        img_area = ctk.CTkFrame(p, fg_color="transparent")
        img_area.grid(row=1, column=0, sticky="nsew", padx=16, pady=12)
        img_area.grid_columnconfigure(0, weight=1)
        img_area.grid_columnconfigure(1, weight=1)
        img_area.grid_rowconfigure(0, weight=1)

        for col, lbl_attr, title_attr, ph, title in [
            (0,"orig_lbl","orig_title","No image loaded\n\nClick  Load Image  in the sidebar","ORIGINAL IMAGE"),
            (1,"res_lbl","res_title","Processed image will\nappear here","RESULT"),
        ]:
            card = ctk.CTkFrame(img_area, fg_color=SURFACE,
                corner_radius=12, border_width=1, border_color=BORDER)
            card.grid(row=0, column=col, sticky="nsew",
                padx=(0,8) if col==0 else (8,0))
            card.grid_rowconfigure(1, weight=1)
            card.grid_columnconfigure(0, weight=1)

            hdr = ctk.CTkFrame(card, fg_color=CARD, corner_radius=8, height=42)
            hdr.grid(row=0, column=0, sticky="ew", padx=12, pady=(12,6))
            hdr.pack_propagate(False)

            dot_col = ACCENT if col==0 else GREEN
            ctk.CTkFrame(hdr, fg_color=dot_col, width=8, height=8, corner_radius=4).pack(side="left", padx=(14,6), pady=17)
            t = ctk.CTkLabel(hdr, text=title,
                font=ctk.CTkFont(size=11, weight="bold"), text_color=TEXT2)
            t.pack(side="left", pady=12)
            setattr(self, title_attr, t)

            lbl = ctk.CTkLabel(card, text=ph,
                font=ctk.CTkFont(size=12), text_color=SUBTLE,
                fg_color=CARD, corner_radius=8)
            lbl.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0,12))
            setattr(self, lbl_attr, lbl)

        # PROGRESS BAR
        prog_frame = ctk.CTkFrame(p, fg_color=SURFACE, corner_radius=0, height=38)
        prog_frame.grid(row=2, column=0, sticky="ew")
        prog_frame.pack_propagate(False)
        ctk.CTkFrame(prog_frame, fg_color=BORDER, height=1).pack(fill="x", side="top")
        self.prog = ctk.CTkProgressBar(prog_frame, fg_color=BORDER,
            progress_color=ACCENT, height=3, corner_radius=0)
        self.prog.pack(fill="x", side="bottom")
        self.prog.set(0)
        self.prog_lbl = ctk.CTkLabel(prog_frame, text="",
            font=ctk.CTkFont(size=10), text_color=MUTED)
        self.prog_lbl.pack(side="left", padx=16, pady=8)

    def _sb_tag(self, p, text):
        ctk.CTkLabel(p, text=text,
            font=ctk.CTkFont(size=10, weight="bold"), text_color=SB_MUTED
        ).pack(anchor="w", pady=(0,2))

    def _sb_sep(self, p):
        ctk.CTkFrame(p, fg_color=SB_BORDER, height=1).pack(fill="x", pady=10)

    def _status(self, text, color=None):
        self.status_lbl.configure(text=text, text_color=color or MUTED)

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
            c, cl, t = "#F87171", RED, f"Weak  ·  {v} iterations"
        elif s < 0.6:
            c, cl, t = "#FCD34D", AMBER, f"Moderate  ·  {v} iterations"
        else:
            c, cl, t = "#6EE7B7", GREEN, f"Strong  ·  {v} iterations"
        self.str_bar.configure(progress_color=cl)
        self.str_lbl.configure(text=t, text_color=c)

    def load_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.tiff")])
        if not path: return
        img = Image.open(path).convert("RGB")
        self.img_array = np.array(img)
        self.after(100, lambda: self._show(self.orig_lbl, self.img_array))
        h, w = self.img_array.shape[:2]
        fname = os.path.basename(path)
        self.info_lbl.configure(text=f"  {w}×{h}  ·  {fname}  ")
        self._status(f"Image loaded  ·  {w}×{h}px", ACCENT)
        self.res_lbl.configure(image=None, text="Processed image will\nappear here")
        self.res_title.configure(text="RESULT")
        self.result_array = None
        self.prog.set(0)
        self.prog_lbl.configure(text="")

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
        self.prog.set(0.1)
        self.prog_lbl.configure(text="Applying Arnold Cat Map…")
        self._status("Processing image…", AMBER)

        def run():
            try:
                self.after(0, lambda: self.prog.set(0.4))
                self.after(0, lambda: self.prog_lbl.configure(text="Applying Logistic Map XOR…"))
                result = do_encrypt(self.img_array, iters, r, x0) \
                    if mode == "encrypt" else do_decrypt(self.img_array, iters, r, x0)
                self.after(0, lambda: self.prog.set(0.85))
                self.result_array = result
                res_title = "ENCRYPTED IMAGE" if mode=="encrypt" else "DECRYPTED IMAGE"
                done_txt  = "Encrypt Image"   if mode=="encrypt" else "Decrypt Image"
                status_txt = f"{'Encrypted' if mode=='encrypt' else 'Decrypted'} successfully  ·  {iters} iterations  ·  r={r}  x₀={x0}"
                self.after(400, lambda: [
                    self._show(self.res_lbl, result),
                    self.res_title.configure(text=res_title),
                    self.prog.set(1.0),
                    self.prog_lbl.configure(text="Done ✓"),
                    self._status(status_txt, GREEN),
                    self.proc_btn.configure(state="normal", text=done_txt)
                ])
            except Exception as e:
                self.after(0, lambda: [
                    messagebox.showerror("Error", str(e)),
                    self.proc_btn.configure(state="normal", text="Encrypt Image"),
                    self._status("An error occurred", RED),
                    self.prog.set(0)
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
            messagebox.showinfo("Saved", f"File saved successfully!\n{path}")

    def clear(self):
        self.img_array = self.result_array = None
        self.orig_lbl.configure(image=None,
            text="No image loaded\n\nClick  Load Image  in the sidebar")
        self.res_lbl.configure(image=None,
            text="Processed image will\nappear here")
        self.res_title.configure(text="RESULT")
        self.info_lbl.configure(text="")
        self.prog.set(0)
        self.prog_lbl.configure(text="")
        self._status("Ready — load an image to begin")

if __name__ == "__main__":
    App().mainloop()
