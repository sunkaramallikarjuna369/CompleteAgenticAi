"""
Speech Recognition
==================
Section 02

Demonstrates speech processing concepts: audio signals,
frequency analysis, and voice activity detection.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math

print("=" * 60)
print("1. AUDIO SIGNAL GENERATION")
print("=" * 60)

def generate_tone(freq, duration=0.01, sample_rate=1000):
    n_samples = int(duration * sample_rate)
    return [math.sin(2 * math.pi * freq * t / sample_rate) for t in range(n_samples)]

signal_440 = generate_tone(440, 0.01)
signal_880 = generate_tone(880, 0.01)
print(f"  440 Hz tone (first 10): {[f'{s:.2f}' for s in signal_440[:10]]}")
print(f"  880 Hz tone (first 10): {[f'{s:.2f}' for s in signal_880[:10]]}")

print("\n" + "=" * 60)
print("2. FREQUENCY ANALYSIS (DFT)")
print("=" * 60)

def dft(signal, sample_rate=1000):
    N = len(signal)
    freqs = []
    for k in range(N // 2):
        real = sum(signal[n] * math.cos(2*math.pi*k*n/N) for n in range(N))
        imag = sum(signal[n] * math.sin(2*math.pi*k*n/N) for n in range(N))
        magnitude = math.sqrt(real**2 + imag**2) / N
        freq = k * sample_rate / N
        freqs.append((freq, magnitude))
    return freqs

mixed = [s1 + s2 for s1, s2 in zip(signal_440, signal_880)]
spectrum = dft(mixed)
top_freqs = sorted(spectrum, key=lambda x: -x[1])[:5]
print("  Top frequencies:")
for freq, mag in top_freqs:
    bar = "#" * int(mag * 40)
    print(f"    {freq:6.0f} Hz: {bar} ({mag:.3f})")

print("\n" + "=" * 60)
print("3. VOICE ACTIVITY DETECTION")
print("=" * 60)

import random
random.seed(42)
frames = [random.gauss(0, 0.01) for _ in range(5)]  # silence
frames += [random.gauss(0, 0.3) for _ in range(10)]  # speech
frames += [random.gauss(0, 0.01) for _ in range(5)]  # silence

threshold = 0.05
for i, energy in enumerate(frames):
    status = "SPEECH" if abs(energy) > threshold else "SILENT"
    bar = "#" * int(abs(energy) * 50)
    print(f"  Frame {i:2d}: {bar:20s} [{status}]")

print("\nDone!")
