from rich.console import Console
import time
import os

console = Console()

def typewriter(lines, default_char_delay=0.08, default_line_delay=0.5):
    
    for line in lines:
        if isinstance(line, list):  
            line_delay = default_line_delay
            for segment in line:
                if len(segment) == 2:
                    text, color = segment
                    char_delay = default_char_delay
                elif len(segment) == 3:
                    text, color, char_delay = segment
                else:
                    raise ValueError()

                for ch in text:
                    console.print(ch, style=color, end="")
                    console.file.flush()
                    time.sleep(char_delay)
            console.print()
            time.sleep(line_delay)
        else:  
            text, char_delay, line_delay, color = line
            for ch in text:
                console.print(ch, style=color, end="")
                console.file.flush()
                time.sleep(char_delay)
            console.print()
            time.sleep(line_delay)

os.system("cls")
if __name__ == "__main__":
 linhas = [

        ("", 0.01, 0.10, "#E4E4E4"),

        ("Enter, Caroline..", 0.07, 2.50, "#166A8B"),
        
        [
            ("- Just trust me, ", "#4E1515", 0.09),
            ("you'll be fine", "#4E1515", 0.12),
        ],

        ("", 0.02, 1.75, "#E4E4E4"),

        [
            ("And when I'm back in ", "#E4E4E4", 0.10),
            ("Chicago, ", "bold italic #166A8B", 0.07),
        ],

        ("I feel it", 0.115, 1.30, "#166A8B"),
        
        ("", 0.01, 0.01, "#E4E4E4"),
        
        [
            ("Another version of ", "#E4E4E4", 0.11),
            ("me ", "italic #166A8B", 0.07),
        ],

        ("I was in it..", 0.13, 1.75, "#166A8B"),

        ("", 0.01, 0.01, "#E4E4E4"),

        [
            ("I wave goodbye to the ", "#E4E4E4", 0.098),
            ("end of beginning", "bold italic #F0D88A", 0.09),
        ],

        ("(goodbye)", 0.10, 0.50, "#454545"),
        ("(goodbye)", 0.10, 0.70, "#454545"),
        ("(goodbye)", 0.10, 0.70, "#454545"),
        ("(goodbye)", 0.10, 2.00, "#454545"),

        (".", 1, 0.015, "#454545"),
        (".", 1, 0.015, "#454545"),

        ("___", 5, 2, "#1F1F1F"),
    ]
typewriter(linhas)
