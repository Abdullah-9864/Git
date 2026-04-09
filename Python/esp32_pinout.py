import tkinter as tk
from tkinter import font as tkfont
import math

# ─── Helpers ──────────────────────────────────────────────────────────────────

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f'#{int(r):02x}{int(g):02x}{int(b):02x}'

def lighten(hex_color, factor=0.35):
    r, g, b = hex_to_rgb(hex_color)
    return rgb_to_hex(r + (255-r)*factor, g + (255-g)*factor, b + (255-b)*factor)

def dim(hex_color, factor=0.4):
    r, g, b = hex_to_rgb(hex_color)
    return rgb_to_hex(r*factor, g*factor, b*factor)

def lerp_color(c1, c2, t):
    r1,g1,b1 = hex_to_rgb(c1)
    r2,g2,b2 = hex_to_rgb(c2)
    return rgb_to_hex(r1+(r2-r1)*t, g1+(g2-g1)*t, b1+(b2-b1)*t)

# ─── Data ─────────────────────────────────────────────────────────────────────

PIN_COLORS = {
    'power':   '#E24B4A',
    'adc':     '#3B8BD4',
    'dac':     '#1D9E75',
    'touch':   '#9F77DD',
    'uart':    '#639922',
    'i2c':     '#0F6E56',
    'spi':     '#D85A30',
    'special': '#EF9F27',
    'gnd':     '#4a4a4a',
}

LEFT_PINS = [
    ('EN',        'special'),
    ('VP (36)',   'adc'),
    ('VN (39)',   'adc'),
    ('34',        'adc'),
    ('35',        'adc'),
    ('32',        'touch'),
    ('33',        'touch'),
    ('25 (DAC)', 'dac'),
    ('26 (DAC)', 'dac'),
    ('27',        'touch'),
    ('14',        'touch'),
    ('12',        'touch'),
    ('GND',       'gnd'),
    ('13',        'touch'),
    ('5V',        'power'),
]

RIGHT_PINS = [
    ('3.3V',      'power'),
    ('GND',       'gnd'),
    ('15',        'touch'),
    ('2 (Boot)',  'special'),
    ('4',         'touch'),
    ('16 (RX2)', 'uart'),
    ('17 (TX2)', 'uart'),
    ('5 (CS)',   'spi'),
    ('18 (SCK)', 'spi'),
    ('19 (MISO)','spi'),
    ('21 (SDA)', 'i2c'),
    ('RX0 (3)',  'uart'),
    ('TX0 (1)',  'uart'),
    ('22 (SCL)', 'i2c'),
    ('23 (MOSI)','spi'),
]

INFO = {
    'power': {
        'title': '⚡  Power Pins',
        'pins':  '3.3V, 5V (VIN), GND',
        'lines': [
            "These supply electricity to the ESP32 and connected",
            "components. Key things to know:",
            "",
            "  3.3V  →  Output from onboard regulator. Powers sensors.",
            "  5V    →  Input from USB. Do NOT feed into GPIO pins!",
            "  GND   →  Common ground. Every component must share GND.",
            "",
            "⚠  ESP32 GPIO pins are 3.3V only. Connecting 5V directly",
            "   to a GPIO pin will permanently damage the chip!",
        ]
    },
    'adc': {
        'title': '📊  ADC — Analog to Digital Converter',
        'pins':  'GPIO 32–39, 25, 26',
        'lines': [
            "The real world is analog — temperature, light, sound are",
            "all varying voltages. ADC pins read 0–3.3V and convert",
            "it to a number from 0 to 4095.",
            "",
            "  Perfect for: potentiometers, LDR light sensors,",
            "  soil moisture, analog temperature sensors (NTC).",
            "",
            "⚠  ADC2 pins stop working when Wi-Fi is active!",
            "   Use ADC1 (GPIO 32–39) for reliable readings.",
        ]
    },
    'dac': {
        'title': '🔊  DAC — Digital to Analog Converter',
        'pins':  'GPIO 25 and GPIO 26 only',
        'lines': [
            "The reverse of ADC — converts a number into a real",
            "analog voltage between 0V and 3.3V.",
            "",
            "Only 2 pins on the entire ESP32 have this feature!",
            "",
            "  Use for: audio tones, smooth control signals,",
            "  waveform generation (sine, triangle, sawtooth).",
            "",
            "  If you want the ESP32 to play a sound, these",
            "  are the pins to use with a small amplifier.",
        ]
    },
    'touch': {
        'title': '👆  Touch Pins — Capacitive Sensor',
        'pins':  'GPIO 0, 2, 4, 12–15, 27, 32, 33',
        'lines': [
            "These pins detect human touch — no button needed!",
            "They sense capacitance changes when your finger",
            "gets close, just like a smartphone screen.",
            "",
            "  Attach a wire or piece of aluminum foil to a pin",
            "  and it becomes an instant touch button!",
            "",
            "  Great for: lamps, interactive art, secret switches,",
            "  DIY musical instruments, touch keyboards.",
        ]
    },
    'uart': {
        'title': '📡  UART — Serial Communication',
        'pins':  'TX0(1), RX0(3), TX2(17), RX2(16)',
        'lines': [
            "UART lets devices talk using simple TX/RX wire pairs.",
            "TX = Transmit, RX = Receive. Always cross-connect!",
            "(ESP TX → device RX, ESP RX → device TX)",
            "",
            "  UART0 (TX0/RX0): Connected to the USB chip.",
            "  This is how Serial Monitor works and how",
            "  you upload code from your computer!",
            "",
            "  UART2 (TX2/RX2): Free port for GPS, Bluetooth",
            "  modules, or other microcontrollers.",
        ]
    },
    'i2c': {
        'title': '🔗  I2C — Inter-Integrated Circuit',
        'pins':  'GPIO 21 (SDA), GPIO 22 (SCL)',
        'lines': [
            "I2C connects many devices with just 2 wires!",
            "",
            "  SDA (GPIO 21) — carries the actual data",
            "  SCL (GPIO 22) — clock that keeps both sides in sync",
            "",
            "You used I2C in your smart home project for the",
            "LCD display (address 0x27). Each device has a unique",
            "address, so many devices can share the same 2 wires.",
            "",
            "  Popular I2C devices: OLED, BME280, MPU6050, RTC.",
        ]
    },
    'spi': {
        'title': '⚡  SPI — Serial Peripheral Interface',
        'pins':  'MOSI(23), MISO(19), SCK(18), CS(5)',
        'lines': [
            "SPI is faster than I2C and uses 4 wires:",
            "",
            "  MOSI (23) — Data from ESP32 to device",
            "  MISO (19) — Data from device to ESP32",
            "  SCK  (18) — Clock signal",
            "  CS   (5)  — Chip Select (activate a device)",
            "",
            "  Used for: SD cards, TFT color displays,",
            "  NRF24L01 RF modules, LoRa, SPI Flash chips.",
            "",
            "  Speed: up to 80 MHz — much faster than I2C!",
        ]
    },
    'special': {
        'title': '⚠  Special Purpose Pins',
        'pins':  'EN, GPIO 0 (Boot), GPIO 2',
        'lines': [
            "These pins control chip behavior at startup.",
            "",
            "  EN  →  Pull LOW to reset the chip (like a",
            "         restart button). Connected to RST button.",
            "",
            "  GPIO 0  →  Boot mode control.",
            "    HIGH at boot = normal run mode",
            "    LOW  at boot = flash / upload mode",
            "",
            "  GPIO 2  →  Has the onboard LED. Also affects boot.",
            "",
            "⚠  Accidentally pulling these LOW causes boot failures!",
        ]
    },
}

CATEGORIES = [
    ('power',   '⚡ Power',   '#E24B4A'),
    ('adc',     '📊 ADC',     '#3B8BD4'),
    ('dac',     '🔊 DAC',     '#1D9E75'),
    ('touch',   '👆 Touch',   '#9F77DD'),
    ('uart',    '📡 UART',    '#639922'),
    ('i2c',     '🔗 I2C',     '#0F6E56'),
    ('spi',     '⚙ SPI',     '#D85A30'),
    ('special', '⚠ Special', '#EF9F27'),
]

# ─── Board layout constants ────────────────────────────────────────────────────
CVS_W, CVS_H = 500, 440
BOARD_X1, BOARD_Y1 = 155, 18
BOARD_X2, BOARD_Y2 = 345, 420
PIN_W, PIN_H = 22, 13
N_PINS = 15
PIN_Y_START = 38
PIN_Y_STEP  = (393 - PIN_Y_START) / (N_PINS - 1)   # ≈ 25.4
LEFT_PIN_X  = BOARD_X1 - PIN_W          # 133
RIGHT_PIN_X = BOARD_X2                  # 345


# ─── Application ──────────────────────────────────────────────────────────────

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ESP32 Pinout Guide")
        self.root.resizable(False, False)
        self.root.configure(bg='#0f0f1a')

        self.selected_cat = None
        self.pulse_step   = 0
        self.pulse_job    = None
        self.hover_job    = None

        # pin_id → (label, category, base_color)
        self.pin_data   = {}
        # category → [pin_ids]
        self.cat_pins   = {k: [] for k in PIN_COLORS}

        self._build_ui()
        self._draw_board()
        self._draw_pins()
        self._show_welcome()
        self.root.mainloop()

    # ── UI Construction ───────────────────────────────────────────────────────

    def _build_ui(self):
        FONT_TITLE  = ('Consolas', 13, 'bold')
        FONT_LABEL  = ('Consolas', 9)
        FONT_BTN    = ('Consolas', 9)
        FONT_INFO_T = ('Consolas', 13, 'bold')
        FONT_INFO_S = ('Consolas', 10)
        FONT_INFO_B = ('Consolas', 10)

        # ── Top title ─────────────────────────────────────────────────────────
        title_fr = tk.Frame(self.root, bg='#0f0f1a')
        title_fr.pack(fill='x', padx=20, pady=(14, 4))
        tk.Label(title_fr, text='ESP32 DevKit  —  Pinout Guide',
                 font=('Consolas', 15, 'bold'), fg='#e0e0e0', bg='#0f0f1a').pack(side='left')
        tk.Label(title_fr, text='click a pin or category to explore',
                 font=('Consolas', 9), fg='#555', bg='#0f0f1a').pack(side='left', padx=12)

        # ── Main area ─────────────────────────────────────────────────────────
        main_fr = tk.Frame(self.root, bg='#0f0f1a')
        main_fr.pack(fill='both', padx=12, pady=4)

        # Canvas
        self.canvas = tk.Canvas(main_fr, width=CVS_W, height=CVS_H,
                                bg='#0f0f1a', highlightthickness=0)
        self.canvas.pack(side='left', padx=(0, 12))

        # Right info panel
        right_fr = tk.Frame(main_fr, bg='#0f0f1a')
        right_fr.pack(side='left', fill='both', expand=True)

        # Info card frame
        self.info_card = tk.Frame(right_fr, bg='#1a1a2e',
                                  highlightthickness=1,
                                  highlightbackground='#2a2a45')
        self.info_card.pack(fill='both', expand=True, pady=(0, 10))

        pad = dict(padx=16, pady=0)

        # Category color bar
        self.cat_bar = tk.Frame(self.info_card, bg='#E24B4A', height=4)
        self.cat_bar.pack(fill='x')

        tk.Frame(self.info_card, bg='#1a1a2e', height=12).pack()

        # Title
        self.lbl_title = tk.Label(self.info_card, text='',
                                   font=('Consolas', 13, 'bold'),
                                   fg='#e0e0e0', bg='#1a1a2e', anchor='w')
        self.lbl_title.pack(fill='x', **pad)

        # Pins subtitle
        self.lbl_pins = tk.Label(self.info_card, text='',
                                  font=('Consolas', 9),
                                  fg='#888', bg='#1a1a2e', anchor='w')
        # self.lbl_pins.pack(fill='x', **pad, pady=(2, 8))
        self.lbl_pins.pack(fill='x', **pad)

        # Separator
        sep = tk.Frame(self.info_card, bg='#2a2a45', height=1)
        sep.pack(fill='x', padx=16, pady=(0, 10))

        # Description text widget
        self.txt = tk.Text(self.info_card, font=('Consolas', 10),
                           fg='#c8c8d8', bg='#1a1a2e',
                           relief='flat', bd=0,
                           wrap='word', state='disabled',
                           cursor='arrow',
                           width=34, height=14,
                           selectbackground='#1a1a2e',
                           inactiveselectbackground='#1a1a2e')
        self.txt.pack(fill='both', expand=True, padx=16, pady=(0, 16))
        self.txt.tag_config('warn', foreground='#EF9F27')
        self.txt.tag_config('em',   foreground='#e0e0e0', font=('Consolas', 10, 'bold'))

        # ── Category buttons ──────────────────────────────────────────────────
        btn_fr = tk.Frame(right_fr, bg='#0f0f1a')
        btn_fr.pack(fill='x')
        self.cat_buttons = {}
        for i, (cat, label, color) in enumerate(CATEGORIES):
            btn = tk.Button(btn_fr, text=label,
                            font=('Consolas', 9),
                            fg='#bbb', bg='#1a1a2e',
                            activeforeground='#fff',
                            activebackground='#252540',
                            relief='flat', bd=0,
                            padx=8, pady=5,
                            cursor='hand2',
                            command=lambda c=cat: self.select_cat(c))
            btn.grid(row=i//4, column=i%4, padx=3, pady=3, sticky='ew')
            btn_fr.columnconfigure(i%4, weight=1)
            self.cat_buttons[cat] = (btn, color)

        # Reset button
        reset_btn = tk.Button(right_fr, text='↺  Show all pins',
                              font=('Consolas', 9),
                              fg='#888', bg='#151525',
                              activeforeground='#ccc',
                              activebackground='#1e1e35',
                              relief='flat', bd=0,
                              pady=6, cursor='hand2',
                              command=self.reset_selection)
        reset_btn.pack(fill='x', pady=(6, 0))

    # ── Board Drawing ─────────────────────────────────────────────────────────

    def _draw_board(self):
        c = self.canvas
        bx1, by1, bx2, by2 = BOARD_X1, BOARD_Y1, BOARD_X2, BOARD_Y2

        # PCB shadow
        c.create_rectangle(bx1+4, by1+4, bx2+4, by2+4,
                           fill='#050508', outline='', tags='board')

        # PCB body
        c.create_rectangle(bx1, by1, bx2, by2,
                           fill='#1a2e1a', outline='#2d4a2d',
                           width=2, tags='board')

        # Antenna area
        c.create_rectangle(bx1+22, by1+8, bx2-22, by1+48,
                           fill='#0d1f0d', outline='#1a3a1a', width=1)
        c.create_text((bx1+bx2)//2, by1+32, text='Wi-Fi + BT Antenna',
                      font=('Consolas', 7), fill='#3a5c3a')

        # Antenna stripes
        for i in range(5):
            cx = bx1 + 36 + i * 18
            c.create_rectangle(cx, by1+14, cx+10, by1+42,
                               fill='#152a15', outline='#1e401e', width=0)

        # Main chip
        cx1 = bx1 + 36
        cy1 = by1 + 138
        cx2 = bx2 - 36
        cy2 = by2 - 130
        c.create_rectangle(cx1, cy1, cx2, cy2,
                           fill='#111111', outline='#2a2a2a', width=1)
        c.create_text((cx1+cx2)//2, (cy1+cy2)//2 - 8,
                      text='ESP32', font=('Consolas', 9, 'bold'), fill='#444')
        c.create_text((cx1+cx2)//2, (cy1+cy2)//2 + 8,
                      text='WROOM-32', font=('Consolas', 7), fill='#333')

        # Chip pin dots
        for i in range(8):
            dot_y = cy1 + 10 + i * (cy2 - cy1 - 20) / 7
            c.create_oval(cx1-4, dot_y-2, cx1, dot_y+2, fill='#2a2a2a', outline='')
            c.create_oval(cx2, dot_y-2, cx2+4, dot_y+2, fill='#2a2a2a', outline='')

        # LED indicator
        c.create_oval(bx1+16, by2-80, bx1+26, by2-70,
                      fill='#003300', outline='#005500', width=1)
        c.create_text(bx1+21, by2-62, text='LED', font=('Consolas', 6), fill='#334433')

        # USB connector
        usb_x1 = (bx1+bx2)//2 - 28
        usb_x2 = (bx1+bx2)//2 + 28
        c.create_rectangle(usb_x1, by2-2, usb_x2, by2+20,
                           fill='#2a2a2a', outline='#444', width=1)
        c.create_text((usb_x1+usb_x2)//2, by2+9,
                      text='USB', font=('Consolas', 7), fill='#666')

        # Small capacitors/components
        for bx, by in [(bx1+8, by2-110), (bx2-14, by2-110)]:
            c.create_rectangle(bx, by, bx+6, by+12,
                               fill='#333', outline='#444')

        # Label "LEFT" / "RIGHT"
        c.create_text(bx1-30, (by1+by2)//2, text='←  L', angle=0,
                      font=('Consolas', 7), fill='#333')
        c.create_text(bx2+30, (by1+by2)//2, text='R  →', angle=0,
                      font=('Consolas', 7), fill='#333')

    def _pin_y(self, index):
        return int(PIN_Y_START + index * PIN_Y_STEP)

    def _draw_pins(self):
        c = self.canvas

        for i, (label, cat) in enumerate(LEFT_PINS):
            y = self._pin_y(i)
            color = PIN_COLORS.get(cat, '#888')

            # Connector wire stub
            c.create_line(LEFT_PIN_X-6, y + PIN_H//2,
                          LEFT_PIN_X, y + PIN_H//2,
                          fill='#2a2a2a', width=2)

            # Pin rectangle
            pid = c.create_rectangle(LEFT_PIN_X, y, LEFT_PIN_X+PIN_W, y+PIN_H,
                                     fill=color, outline=lighten(color, 0.2), width=1)
            # Label
            c.create_text(LEFT_PIN_X - 9, y + PIN_H//2,
                          text=label, anchor='e',
                          font=('Consolas', 8), fill='#aaaaaa')

            self.pin_data[pid] = (label, cat, color)
            self.cat_pins[cat].append(pid)

            c.tag_bind(pid, '<Enter>',   lambda e, p=pid: self._on_hover(p, True))
            c.tag_bind(pid, '<Leave>',   lambda e, p=pid: self._on_hover(p, False))
            c.tag_bind(pid, '<Button-1>',lambda e, p=pid: self._on_click(p))

        for i, (label, cat) in enumerate(RIGHT_PINS):
            y = self._pin_y(i)
            color = PIN_COLORS.get(cat, '#888')

            # Connector wire stub
            c.create_line(RIGHT_PIN_X+PIN_W, y + PIN_H//2,
                          RIGHT_PIN_X+PIN_W+6, y + PIN_H//2,
                          fill='#2a2a2a', width=2)

            pid = c.create_rectangle(RIGHT_PIN_X, y, RIGHT_PIN_X+PIN_W, y+PIN_H,
                                     fill=color, outline=lighten(color, 0.2), width=1)
            c.create_text(RIGHT_PIN_X + PIN_W + 9, y + PIN_H//2,
                          text=label, anchor='w',
                          font=('Consolas', 8), fill='#aaaaaa')

            self.pin_data[pid] = (label, cat, color)
            self.cat_pins[cat].append(pid)

            c.tag_bind(pid, '<Enter>',   lambda e, p=pid: self._on_hover(p, True))
            c.tag_bind(pid, '<Leave>',   lambda e, p=pid: self._on_hover(p, False))
            c.tag_bind(pid, '<Button-1>',lambda e, p=pid: self._on_click(p))

    # ── Interactions ──────────────────────────────────────────────────────────

    def _on_hover(self, pid, entering):
        label, cat, base_color = self.pin_data[pid]
        if entering:
            self.canvas.configure(cursor='hand2')
            self.canvas.itemconfig(pid, fill=lighten(base_color, 0.45))
        else:
            self.canvas.configure(cursor='')
            # restore correct color depending on selection state
            if self.selected_cat and cat != self.selected_cat:
                self.canvas.itemconfig(pid, fill=dim(base_color, 0.3))
            else:
                self.canvas.itemconfig(pid, fill=base_color)

    def _on_click(self, pid):
        label, cat, base_color = self.pin_data[pid]
        self.select_cat(cat)

    def select_cat(self, cat):
        self.selected_cat = cat

        # Update button styles
        for c_key, (btn, color) in self.cat_buttons.items():
            if c_key == cat:
                btn.config(fg='#fff', bg='#252540',
                           relief='solid', bd=1,
                           highlightbackground=color,
                           highlightcolor=color,
                           highlightthickness=1)
            else:
                btn.config(fg='#bbb', bg='#1a1a2e',
                           relief='flat', bd=0)

        # Dim non-selected pins, highlight selected
        for pid, (label, p_cat, base_color) in self.pin_data.items():
            if p_cat == cat:
                self.canvas.itemconfig(pid, fill=base_color)
            else:
                self.canvas.itemconfig(pid, fill=dim(base_color, 0.25))

        # Start pulse animation
        self._stop_pulse()
        self._pulse(cat, 0)

        # Update info panel
        self._show_info(cat)

    def reset_selection(self):
        self.selected_cat = None
        self._stop_pulse()

        for btn_key, (btn, _) in self.cat_buttons.items():
            btn.config(fg='#bbb', bg='#1a1a2e', relief='flat', bd=0)

        for pid, (label, cat, base_color) in self.pin_data.items():
            self.canvas.itemconfig(pid, fill=base_color)

        self._show_welcome()

    def _stop_pulse(self):
        if self.pulse_job:
            self.root.after_cancel(self.pulse_job)
            self.pulse_job = None
        self.pulse_step = 0

    def _pulse(self, cat, step):
        if self.selected_cat != cat:
            return
        pins = self.cat_pins.get(cat, [])
        # sine wave 0..1
        t = (math.sin(step * 0.12) + 1) / 2
        for pid in pins:
            _, _, base_color = self.pin_data[pid]
            c = lerp_color(base_color, lighten(base_color, 0.5), t * 0.6)
            self.canvas.itemconfig(pid, fill=c)
        self.pulse_job = self.root.after(30, lambda: self._pulse(cat, step+1))

    # ── Info Panel ────────────────────────────────────────────────────────────

    def _show_welcome(self):
        self.lbl_title.config(text='ESP32 Pinout Guide', fg='#e0e0e0')
        self.lbl_pins.config(text='Click a pin on the board or a category button')
        self.cat_bar.config(bg='#2a2a45')
        self._set_text([
            "The ESP32 is a powerful microcontroller with:",
            "",
            "  • Dual-core 240 MHz CPU",
            "  • Built-in Wi-Fi (2.4 GHz)",
            "  • Built-in Bluetooth (Classic + BLE)",
            "  • 4 MB Flash storage (your code)",
            "  • 520 KB SRAM (runtime memory)",
            "  • 38 pins with many functions",
            "",
            "Pins are color-coded by function:",
            "  Red    → Power (3.3V, 5V, GND)",
            "  Blue   → ADC (read analog sensors)",
            "  Green  → DAC (output analog signal)",
            "  Purple → Touch (capacitive sensing)",
            "  Lime   → UART (serial communication)",
            "  Teal   → I2C (multi-device protocol)",
            "  Orange → SPI (high-speed protocol)",
            "  Amber  → Special (EN, Boot, LED)",
        ])

    def _show_info(self, cat):
        data = INFO.get(cat)
        if not data:
            return

        # Find category color
        cat_color = PIN_COLORS.get(cat, '#888')

        self.cat_bar.config(bg=cat_color)
        self.lbl_title.config(text=data['title'], fg=cat_color)
        self.lbl_pins.config(text='Pins: ' + data['pins'])

        self._set_text(data['lines'])

    def _set_text(self, lines):
        self.txt.config(state='normal')
        self.txt.delete('1.0', 'end')
        for line in lines:
            if line.startswith('⚠'):
                self.txt.insert('end', line + '\n', 'warn')
            elif line.startswith('  •') or (line and line[0] not in (' ', '')):
                self.txt.insert('end', line + '\n')
            else:
                self.txt.insert('end', line + '\n')
        self.txt.config(state='disabled')


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    App()
