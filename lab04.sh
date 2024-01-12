import subprocess

def simulate_yes():
    try:
        # Use subprocess.Popen to run the 'yes' command
        yes_process = subprocess.Popen(['yes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Read the output of the 'yes' command
        output, _ = yes_process.communicate()
        
        # Print or process the output as needed
        print(output)
        
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) gracefully
        print("\nInterrupted. Exiting...")

if __name__ == "__main__":
    simulate_yes()


