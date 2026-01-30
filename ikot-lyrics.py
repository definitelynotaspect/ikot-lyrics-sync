import time
import sys

# Formatted for the Bridge/Outro of "Ikot" by Over October
lyrics = [
    ("Ikaw lang at ikaw ang sinisigaw", 1.5, 0.12),
    ("Ng puso kong 'di mapakali", 1.8, 0.12),
    ("Ikaw lang at ikaw ang sinisigaw", 1.5, 0.12),
    ("Pag-ibig ko'y sana mapansin", 2.0, 0.12),
    ("Ikaw lang at ikaw ang sinisigaw", 1.5, 0.12),
    ("Ng puso kong 'di mapakali", 1.8, 0.12),
    ("Ikaw lang at ikaw ang sinisigaw", 1.5, 0.12),
    ("Pag-ibig ko'y sana mapansin...", 3.0, 0.12),
]

def type_out(text, char_delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics_list):
    print("--- Playing: Ikot (Bridge/Outro) ---")
    time.sleep(1) # Short pause before starting
    for line, line_delay, char_delay in lyrics_list:
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    play_lyrics(lyrics)