# Nmap Scanner GUI

## Description
Nmap Scanner GUI is a Python-based tool using Tkinter for an intuitive interface to run Nmap scans. Features include full-screen mode, keyboard shortcuts, scan type selection, real-time output display, and automatic input focus. Customizable for Nmap's file path, it supports both IP and domain scanning.

## Features
- **GUI Interface:** Simple interface for selecting scan types and entering targets (IP or domain).
- **Scan Types:** 
  - SYN Scan (-sS)
  - Service Version Detection (-sV)
  - OS Detection (-O)
  - Aggressive Scan (-A)
  - Quick Scan (-T4 -F)
- **Full-Screen Mode:** Retro aesthetic with black background and bright green text.
- **Keyboard Shortcuts:** Press **Esc** to exit the program.
- **Clear Screen Option:** Option to reset the display after each scan.
- **Real-Time Output:** View Nmap scan results directly within the GUI.
- **Automatic Focus:** Cursor returns to the first input field after a scan.

## Requirements
- **Operating System:** Windows (Nmap installation required)
- **Software:**
  - Python 3.x
  - Nmap (Download from [nmap.org](https://nmap.org/download.html))
- **Python Libraries:**
  - `tkinter` (bundled with Python)
  - `subprocess` (standard Python library)

## Installation

1. **Install Python** from [python.org](https://www.python.org/).
2. **Install Nmap** from [nmap.org](https://nmap.org/download.html).
3. **Locate Nmap:** Find the installation path (e.g., `C:\Program Files (x86)\Nmap\nmap.exe`).
4. **Clone/Download the repository:**
   ```bash
   git clone https://github.com/yourusername/Nmap-Scanner-GUI.git
5. Update Nmap Path: Open main.py and update the Nmap path to match your system:
    python, copy the path from where your nmap.exe file is stored, usually its in C:// >> Program Files >> Nmap >> nmap.exe

paste the path here:
result = subprocess.run(
            ["PASTE_PATH_HERE"] + scan_type.split() + [target],
            text=True,
            capture_output=True
        )
6. Run the script: python main.py
