import os
import time
import sys

# Windows CMD color support
os.system('color')

# Color codes
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner():
    banner = f"""
{GREEN}
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║    {BOLD}Tool Made By 𝐑𝐀𝐘𝐇𝐀𝐍 𝐁𝐈𝐒𝐖𝐀𝐒   {RESET}{GREEN}     ║
    ║                                                            ║
    ║   Contact: https://www.facebook.com/rayhanbiswasbd.v2/     ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
{RESET}
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

    for prefix in prefixes:
        print(f"{GREEN}Processing Prefix {prefix}...{RESET}")

        # Create folder
        if not os.path.exists(prefix):
            os.makedirs(prefix)

        file_path = os.path.join(prefix, f"{prefix}.csv")

        try:
            with open(file_path, "w", buffering=1024*1024) as f:
                f.write("PhoneNumber\n")

                batch_size = 1000000
                buffer = []

                start_time = time.time()

                # 10 Crore loop
                for i in range(100000000):
                    full_number = f"{prefix}{i:08d}"
                    buffer.append(full_number)

                    if len(buffer) == batch_size:
                        f.write("\n".join(buffer) + "\n")
                        buffer = []

                        sys.stdout.write(f"\r  - Written batch ending with {full_number}")
                        sys.stdout.flush()

                if buffer:
                    f.write("\n".join(buffer) + "\n")

            print(f"\n{GREEN}✅ Completed {file_path}{RESET}")
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
