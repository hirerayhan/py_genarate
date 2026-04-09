import os
import time
import sys
import webbrowser
import ctypes

# Windows CMD color support
os.system('color')

# Color codes
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner():
    # Fixed alignment and replaced special unicode characters for CMD compatibility
    banner = f"""{GREEN}
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║                 {BOLD}Tool Made By RAYHAN BISWAS{RESET}{GREEN}                 ║
    ║                                                            ║
    ║    Contact: https://www.facebook.com/rayhanbiswasbd.v2/    ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝{RESET}
"""
    print(banner)
    print(f"{CYAN}[INFO] Tool Initialized successfully...{RESET}\n")
    time.sleep(2)

# Prefix list
prefixes = ['13', '14', '15', '16', '17', '18', '19']

def show_popup_and_redirect():
    url = "https://www.facebook.com/rayhanbiswasbd.v2/"
    print(f"\n{YELLOW}[INFO] Redirecting to Facebook...{RESET}")
    
    # Show popup for Windows
    if sys.platform.startswith('win'):
        # 0x40 is MB_ICONINFORMATION (Information icon with OK button)
        ctypes.windll.user32.MessageBoxW(0, "কাজ শেষ হয়েছে! দয়া করে আমার ফেসবুক পেজটি ফলো করুন।\n\nTask Completed! Please follow my Facebook page.", "Follow My Page", 0x40)
    else:
        print(f"{CYAN}কাজ শেষ হয়েছে! দয়া করে আমার ফেসবুক পেজটি ফলো করুন।{RESET}")
        
    # Open URL in default browser
    webbrowser.open(url)

def generate_numbers():
    print_banner()
    print(f"{BOLD}Starting Generation Process...{RESET}")
    print("This involves handling large data, please wait.\n")

    # Folder and number limits
    total_numbers = 100000000  # 10 koti number
    numbers_per_folder = 100000 # Proti folder e 1 lokkho
    total_folders = total_numbers // numbers_per_folder # Mot 1000 folder hobe

    # Animation frames and colors
    animation_frames = ['|', '/', '-', '\\']
    animation_colors = [GREEN, CYAN, YELLOW, MAGENTA, RED, BLUE, WHITE]

    for prefix in prefixes:
        print(f"{GREEN}Processing Prefix {prefix}...{RESET}")

        # Create main folder (e.g., '13')
        if not os.path.exists(prefix):
            os.makedirs(prefix)

        start_time = time.time()

        try:
            for folder_num in range(1, total_folders + 1):
                # Create subfolder (e.g., '13/Folder_1')
                subfolder_path = os.path.join(prefix, f"Folder_{folder_num}")
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)

                file_path = os.path.join(subfolder_path, f"{prefix}_part_{folder_num}.csv")

                with open(file_path, "w", buffering=1024*1024) as f:
                    f.write("PhoneNumber\n")

                    buffer = []
                    start_index = (folder_num - 1) * numbers_per_folder
                    end_index = folder_num * numbers_per_folder

                    # Generate exactly 1 Lakh numbers for this specific folder
                    for idx, i in enumerate(range(start_index, end_index)):
                        full_number = f"{prefix}{i:08d}"
                        buffer.append(full_number)

                        # Show colored animation every 5000 numbers
                        if idx % 5000 == 0:
                            step = idx // 5000
                            frame = animation_frames[step % len(animation_frames)]
                            color = animation_colors[step % len(animation_colors)]
                            sys.stdout.write(f"\r  {color}[{frame}]{RESET} Generating numbers for Folder_{folder_num}...")
                            sys.stdout.flush()

                    # Write all 1 Lakh numbers at once
                    f.write("\n".join(buffer) + "\n")
                    
                    sys.stdout.write(f"\r  {GREEN}[✓]{RESET} Created {file_path} with {numbers_per_folder} numbers       \n")
                    sys.stdout.flush()

            print(f"\n{GREEN}✅ Completed {prefix}{RESET}")
            print(f"Time taken: {round((time.time() - start_time)/60, 2)} minutes\n")

        except KeyboardInterrupt:
            print(f"\n{BOLD}Process stopped by user!{RESET}")
            sys.exit()

        except Exception as e:
            print(f"\nError: {e}")

    print(f"{GREEN}╔══════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║        ALL TASKS COMPLETED!          ║{RESET}")
    print(f"{GREEN}╚══════════════════════════════════════╝{RESET}")

    # Show popup and open facebook page
    show_popup_and_redirect()

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    generate_numbers()
