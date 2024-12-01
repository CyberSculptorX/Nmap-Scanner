import subprocess
import tkinter as tk

def nmap_scan(scan_type, target, output_text):
    try:
        output_text.insert(tk.END, f"\nRunning {scan_type} scan on {target}...\n")
        output_text.insert(tk.END, "Scan in progress...\n")
        output_text.update()
        # Run the Nmap scan using subprocess and capture output
        result = subprocess.run(
            ["PASTE_PATH_HERE"] + scan_type.split() + [target],
            text=True,
            capture_output=True
        )
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        output_text.insert(tk.END, f"An error occurred: {e}\n")

def handle_choice(choice, target, output_text, root):
    if choice == '6':  # Clear Screen
        output_text.delete("1.0", tk.END)
        return
    elif not target and choice != '6':
        output_text.insert(tk.END, "Error: Please enter a target (IP or domain).\n")
        return

    if choice == '1':
        nmap_scan("-sS", target, output_text)
    elif choice == '2':
        nmap_scan("-sV", target, output_text)
    elif choice == '3':
        nmap_scan("-O", target, output_text)
    elif choice == '4':
        nmap_scan("-A", target, output_text)
    elif choice == '5':
        nmap_scan("-T4 -F", target, output_text)
    else:
        output_text.insert(tk.END, "Invalid choice. Please try again.\n")
    output_text.insert(tk.END, "\n" + "="*25 + "\n")
    output_text.see(tk.END)

def main():
    # Create the Tkinter root window
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Make the window full screen
    root.configure(background="black")    # Set black background
    root.overrideredirect(True)           # Remove the window frame

    # Add a keybinding to close the program with the Esc key
    root.bind("<Escape>", lambda event: root.destroy())

    # Create and place widgets
    title_label = tk.Label(root, text="Nmap Scanner Program", font=("Courier", 24), fg="lime", bg="black")
    title_label.pack(pady=20)

    menu_text = ("Select a scan type:\n"
                 "1. SYN Scan (Default)\n"
                 "2. Service Version Detection\n"
                 "3. OS Detection\n"
                 "4. Aggressive Scan\n"
                 "5. Quick Scan\n"
                 "6. Clear Screen\n"
                 "Esc. Press Escape On Keyboard To Exit")
    menu_label = tk.Label(root, text=menu_text, font=("Courier", 16), fg="lime", bg="black", justify="left")
    menu_label.pack(pady=10)

    scan_choice_entry = tk.Entry(root, font=("Courier", 16), fg="lime", bg="black", insertbackground="lime", width=30)
    scan_choice_entry.pack(pady=10)

    target_label = tk.Label(root, text="Enter target (IP or domain):", font=("Courier", 16), fg="lime", bg="black")
    target_label.pack(pady=10)

    target_entry = tk.Entry(root, font=("Courier", 16), fg="lime", bg="black", insertbackground="lime", width=30)
    target_entry.pack(pady=10)

    output_text = tk.Text(root, font=("Courier", 14), fg="lime", bg="black", insertbackground="lime", height=15, wrap="word")
    output_text.pack(pady=10)

    def submit_choice():
        choice = scan_choice_entry.get().strip()
        target = target_entry.get().strip()
        scan_choice_entry.delete(0, tk.END)  # Clear the entry after retrieving input
        target_entry.delete(0, tk.END)  # Clear the target entry after retrieving input
        handle_choice(choice, target, output_text, root)
        scan_choice_entry.focus_set()  # Move the cursor back to the choice input box

    submit_button = tk.Button(root, text="Submit", command=submit_choice, font=("Courier", 16), fg="black", bg="lime")
    submit_button.pack(pady=20)

    # Set initial focus on the scan choice entry box
    scan_choice_entry.focus_set()

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
