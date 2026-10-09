import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('assets', exist_ok=True)

FONT_PATH = "C:\\Windows\\Fonts\\consola.ttf"
FONT_BOLD_PATH = "C:\\Windows\\Fonts\\consolab.ttf"
TITLE_FONT_PATH = "C:\\Windows\\Fonts\\arial.ttf"

def create_terminal_window(title: str, lines_with_colors: list, output_path: str, width: int = 860):
    padding_x = 28
    padding_top = 48
    padding_bottom = 28
    line_height = 20

    font = ImageFont.truetype(FONT_PATH, 14)
    title_font = ImageFont.truetype(TITLE_FONT_PATH, 12)

    total_lines = len(lines_with_colors)
    height = padding_top + (total_lines * line_height) + padding_bottom

    # Canvas with outer shadow margin
    margin = 20
    img = Image.new("RGBA", (width + 2 * margin, height + 2 * margin), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Shadow
    for i in range(margin):
        alpha = int(25 * (1 - i / margin))
        draw.rounded_rectangle(
            [margin - i, margin - i, margin + width + i, margin + height + i],
            radius=12 + i,
            fill=(0, 0, 0, alpha)
        )

    # Window background
    box = [margin, margin, margin + width, margin + height]
    draw.rounded_rectangle(box, radius=10, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255), width=1)

    # Title bar
    title_bar_height = 36
    draw.rounded_rectangle(
        [margin, margin, margin + width, margin + title_bar_height],
        radius=10,
        fill=(30, 41, 59, 255)
    )
    draw.rectangle(
        [margin, margin + title_bar_height - 6, margin + width, margin + title_bar_height],
        fill=(30, 41, 59, 255)
    )

    # Window control dots
    dot_y = margin + 18
    draw.ellipse([margin + 16, dot_y - 5, margin + 26, dot_y + 5], fill=(239, 68, 68, 255))
    draw.ellipse([margin + 34, dot_y - 5, margin + 44, dot_y + 5], fill=(245, 158, 11, 255))
    draw.ellipse([margin + 52, dot_y - 5, margin + 62, dot_y + 5], fill=(34, 197, 94, 255))

    # Window title
    draw.text((margin + (width // 2) - 60, margin + 11), title, font=title_font, fill=(148, 163, 184, 255))

    # Render lines
    y = margin + padding_top
    for line_segments in lines_with_colors:
        x = margin + padding_x
        for text, color in line_segments:
            draw.text((x, y), text, font=font, fill=color)
            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]
            x += text_width
        y += line_height

    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")


# Colors
C_CYAN = (56, 189, 248, 255)
C_GREEN = (74, 222, 128, 255)
C_YELLOW = (250, 204, 21, 255)
C_RED = (248, 113, 113, 255)
C_WHITE = (241, 245, 249, 255)
C_GRAY = (148, 163, 184, 255)
C_DARKGRAY = (100, 116, 139, 255)

# --- 1. Start Screen ---
start_lines = [
    [("$$$$$$$\\            $$$$$$$$\\ $$\\   $$\\           $$\\      $$\\ ", C_CYAN)],
    [("$$  __$$\\           \\____$$  |$$$\\  $$ |          $$$\\    $$$ |", C_CYAN)],
    [("$$ |  $$ | $$$$$$\\      $$  / $$$$\\ $$ |$$\\   $$\\ $$$$\\  $$$$ |", C_CYAN)],
    [("$$$$$$$  |$$  __$$\\    $$  /  $$ $$\\$$ |$$ |  $$ |$$\\$$\\$$ $$ |", C_CYAN)],
    [("$$  __$$< $$$$$$$$ |  $$  /   $$ \\$$$$ |$$ |  $$ |$$ \\$$$  $$ |", C_CYAN)],
    [("$$ |  $$ |$$   ____| $$  /    $$ |\\$$$ |$$ |  $$ |$$ |\\$  /$$ |", C_CYAN)],
    [("$$ |  $$ |\\$$$$$$$\\ $$$$$$$$\\ $$ | \\$$ |\\$$$$$$  |$$ | \\_/ $$ |", C_CYAN)],
    [("\\__|  \\__| \\_______|\\________|\\__|  \\__| \\______/ \\__|     \\__|", C_CYAN)],
    [("", C_WHITE)],
    [("    ReZNuM's Tool to get API Hash and API ID of Telegram account", C_YELLOW)],
    [("", C_WHITE)],
    [("Telegram: @ItsReZNuM | Instagram: ReZ.NuM | GitHub: https://github.com/ItsReZNuM", C_GREEN)],
    [("", C_WHITE)],
    [("[", C_RED), ("+", C_GREEN), ("] ", C_RED), ("Enter your number along with country code [Ex: +98XXXXXXXXX]: ", C_GREEN), ("+989123456789", C_YELLOW)],
    [("", C_WHITE)],
    [("[*] Requesting confirmation code from Telegram...", C_CYAN)],
    [("[+] Confirmation code sent to your Telegram app!", C_GREEN)],
    [("", C_WHITE)],
    [("[", C_RED), ("+", C_GREEN), ("] ", C_RED), ("Enter the code sent to your Telegram account: ", C_GREEN), ("tG59bKz", C_YELLOW)],
]

create_terminal_window("TelApiIDHash - Session Start", start_lines, "assets/start_screen.png")


# --- 2. Success Screen ---
success_lines = [
    [("[*] Logging in to my.telegram.org...", C_CYAN)],
    [("[+] Login successful!", C_GREEN)],
    [("[*] Fetching API configuration page...", C_CYAN)],
    [("", C_WHITE)],
    [("$$$$$$$\\   $$$$$$\\   $$$$$$\\  $$\\      $$\\ $$\\ ", C_GREEN)],
    [("$$  __$$\\ $$  __$$\\ $$  __$$\\ $$$\\    $$$ |$$ |", C_GREEN)],
    [("$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$\\  $$$$ |$$ |", C_GREEN)],
    [("$$$$$$$\\ |$$ |  $$ |$$ |  $$ |$$\\$$\\$$ $$ |$$ |", C_GREEN)],
    [("$$  __$$\\ $$ |  $$ |$$ |  $$ |$$ \\$$$  $$ |\\__|", C_GREEN)],
    [("$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\\$  /$$ |    ", C_GREEN)],
    [("$$$$$$$  | $$$$$$  | $$$$$$  |$$ | \\_/ $$ |$$\\ ", C_GREEN)],
    [("\\_______/  \\______/  \\______/ \\__|     \\__|\\__|", C_GREEN)],
    [("", C_WHITE)],
    [("    APIs successfully received:", C_CYAN)],
    [("", C_WHITE)],
    [("        [", C_RED), ("+", C_GREEN), ("] ", C_RED), ("Api ID: ", C_GREEN), ("24981734", C_YELLOW)],
    [("        [", C_RED), ("+", C_GREEN), ("] ", C_RED), ("Api HASH: ", C_GREEN), ("e2f4a180c59b7201d4a8ef38a0bc931f", C_YELLOW)],
    [("", C_WHITE)],
    [("        [", C_RED), ("~", C_GREEN), ("] ", C_RED), ("Public Key: ", C_GREEN), ("-----BEGIN RSA PUBLIC KEY-----...", C_YELLOW)],
    [("        [", C_RED), ("~", C_GREEN), ("] ", C_RED), ("Production configuration: ", C_GREEN), ("149.154.167.50:443", C_YELLOW)],
    [("", C_WHITE)],
    [("[+] Done! You can now use your Telegram API credentials in your projects.", C_GREEN)],
]

create_terminal_window("TelApiIDHash - Credentials Obtained", success_lines, "assets/success_screen.png")


# --- 3. Error Screen ---
error_lines = [
    [(" $$$$$$\\   $$$$$$\\  $$$$$$$\\  $$$$$$$\\ $$\\     $$\\       $$\\ ", C_RED)],
    [("$$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\$$\\   $$  |      $$ |", C_RED)],
    [("$$ /  \\__|$$ /  $$ |$$ |  $$ |$$ |  $$ |\\$$\\ $$  /       $$ |", C_RED)],
    [("\\$$$$$$\\  $$ |  $$ |$$$$$$$  |$$$$$$$  | \\$$$$  /        $$ |", C_RED)],
    [(" \\____$$\\ $$ |  $$ |$$  __$$< $$  __$$<   \\$$  /         \\__|", C_RED)],
    [("$$\\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |              ", C_RED)],
    [("\\$$$$$$  | $$$$$$  |$$ |  $$ |$$ |  $$ |   $$ |          $$\\ ", C_RED)],
    [(" \\______/  \\______/ \\__|  \\__|\\__|  \\__|   \\__|          \\__|", C_RED)],
    [("", C_WHITE)],
    [("    [!] Error: ", C_RED), ("Login failed: Invalid confirmation code!", C_YELLOW)],
    [("    Details: Make sure the code entered is correct and has not expired.", C_DARKGRAY)],
    [("", C_WHITE)],
    [("    [!] Troubleshooting tips:", C_CYAN)],
    [("      - Ensure your confirmation code was copied without spaces.", C_GRAY)],
    [("      - Telegram web login codes are case-sensitive.", C_GRAY)],
    [("      - If rate-limited, wait 8 to 24 hours before retrying.", C_GRAY)],
]

create_terminal_window("TelApiIDHash - Error Handling", error_lines, "assets/error_screen.png")


# --- 4. Banner ---
def create_project_banner(output_path: str, width: int = 860, height: int = 240):
    img = Image.new("RGBA", (width, height), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)

    # Decorative gradient lines / grid
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(30, 41, 59, 80), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(30, 41, 59, 80), width=1)

    # Border
    draw.rectangle([0, 0, width - 1, height - 1], outline=(51, 65, 85, 255), width=2)

    # Title & Subtitles
    font_large = ImageFont.truetype(FONT_BOLD_PATH, 34)
    font_sub = ImageFont.truetype(FONT_PATH, 15)
    font_badge = ImageFont.truetype(FONT_PATH, 13)

    draw.text((45, 40), "Telegram API ID & Hash Tool", font=font_large, fill=(56, 189, 248, 255))
    draw.text((45, 88), "Fast, resilient CLI extractor for Telegram MTProto API Credentials", font=font_sub, fill=(203, 213, 225, 255))

    # Badges
    badges = [
        ("Python 3.8+", (34, 197, 94, 255), (20, 83, 45, 255)),
        ("my.telegram.org", (56, 189, 248, 255), (12, 74, 110, 255)),
        ("Auto App Creation", (250, 204, 21, 255), (113, 63, 18, 255)),
        ("Multi-Layer Scraping", (168, 85, 247, 255), (88, 28, 135, 255)),
    ]

    bx = 45
    by = 132
    for text, text_col, bg_col in badges:
        bbox = font_badge.getbbox(text)
        bw = (bbox[2] - bbox[0]) + 18
        bh = 26
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=6, fill=bg_col, outline=text_col, width=1)
        draw.text((bx + 9, by + 5), text, font=font_badge, fill=text_col)
        bx += bw + 12

    # Author watermark
    draw.text((45, 188), "Created by ReZNuM | Telegram: @ItsReZNuM | GitHub: @ItsReZNuM", font=font_badge, fill=(148, 163, 184, 255))

    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

create_project_banner("assets/banner.png")
