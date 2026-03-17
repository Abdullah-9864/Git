from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# --- Load and FORCE square ---
img = Image.open("C:\Git\dataEncryption\photo.jpg").convert("RGB")
size = min(img.size)
img = img.crop((0, 0, size, size))   # crop to square ✅
pixels = np.array(img)

# --- Arnold Cat Map (confusion) ---
def arnold_cat_map(pixels, iterations=10):
    h, w = pixels.shape[:2]
    result = pixels.copy()
    for _ in range(iterations):
        new = np.zeros_like(result)
        for y in range(h):
            for x in range(w):
                nx = (x + y) % w
                ny = (x + 2*y) % h
                new[ny, nx] = result[y, x]
        result = new
    return result

# --- Inverse Arnold Cat Map (correct decryption) ---
def inverse_arnold_cat_map(pixels, iterations=10):
    h, w = pixels.shape[:2]
    result = pixels.copy()
    for _ in range(iterations):
        new = np.zeros_like(result)
        for y in range(h):
            for x in range(w):
                ox = (2*x - y) % w      # ✅ true inverse
                oy = (-x + y) % h       # ✅ true inverse
                new[oy, ox] = result[y, x]
        result = new
    return result

# --- Logistic Map key stream ---
def logistic_stream(x0, length, r=3.99):
    x = x0
    stream = []
    for _ in range(length):
        x = r * x * (1 - x)
        stream.append(int(x * 256))
    return np.array(stream, dtype=np.uint8)

# --- XOR ---
def xor_pixels(pixels, stream):
    flat = pixels.flatten()
    stream_tiled = np.tile(stream, len(flat) // len(stream) + 1)[:len(flat)]
    return np.bitwise_xor(flat, stream_tiled).reshape(pixels.shape)

# --- ENCRYPT ---
SECRET_KEY = 0.583726
ITERATIONS = 10

shuffled  = arnold_cat_map(pixels, ITERATIONS)
stream    = logistic_stream(SECRET_KEY, shuffled.size)
encrypted = xor_pixels(shuffled, stream)

# --- DECRYPT ---
unxored   = xor_pixels(encrypted, stream)                    # undo diffusion
decrypted = inverse_arnold_cat_map(unxored, ITERATIONS)      # undo confusion ✅

# --- Show ---
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(pixels);      axes[0].set_title("Original")
axes[1].imshow(encrypted);   axes[1].set_title("Encrypted")
axes[2].imshow(decrypted);   axes[2].set_title("Decrypted")
plt.tight_layout()
plt.show()