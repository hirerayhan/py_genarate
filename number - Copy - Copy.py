import os
import time
import sys

# Windows CMD color support
os.system('color')

# Color codes
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
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


def generate_numbers():
    print_banner()
    print(f"{BOLD}Starting Generation Process...{RESET}")
    print("This involves handling large data, please wait.\n")

    # Folder and number limits
    total_numbers = 100000000  # 10 koti number
    numbers_per_folder = 100000 # Proti folder e 1 lokkho
    total_folders = total_numbers // numbers_per_folder # Mot 1000 folder hobe

    # Animation frames
    animation_frames = ['|', '/', '-', '\\']

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

                        # Show animation every 5000 numbers
                        if idx % 5000 == 0:
                            frame = animation_frames[(idx // 5000) % len(animation_frames)]
                            sys.stdout.write(f"\r  {YELLOW}[{frame}]{RESET} Generating numbers for Folder_{folder_num}...")
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

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    generate_numbers()
