from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1280, 720
OUTPUT_DIR = 'screenshots'


def load_font(size):
    candidates = [
        'C:/Windows/Fonts/arial.ttf',
        'C:/Windows/Fonts/Arial.ttf',
        'C:/Windows/Fonts/segoeui.ttf',
        'C:/Windows/Fonts/Segoe UI.ttf',
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_gradient_background(img, top_color, bottom_color):
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    return draw


def draw_card(draw, x1, y1, x2, y2, color, radius=26):
    draw.rounded_rectangle((x1, y1, x2, y2), radius=radius, fill=color)


def create_main_page():
    img = Image.new('RGBA', (WIDTH, HEIGHT), (17, 24, 39, 255))
    draw = draw_gradient_background(img, (17, 24, 39), (88, 28, 135))

    draw_card(draw, 60, 70, 1220, 650, (255, 255, 255, 245), radius=32)
    draw_card(draw, 90, 110, 1190, 620, (248, 250, 252, 255), radius=28)

    title_font = load_font(54)
    subtitle_font = load_font(24)
    body_font = load_font(20)
    small_font = load_font(18)

    draw.text((110, 150), '🎬 MovieVerse', fill=(109, 40, 217), font=title_font)
    draw.text((110, 220), 'Search your favorite movies and view details instantly.', fill=(71, 85, 105), font=subtitle_font)
    draw.text((110, 255), 'Discover movies from around the world with smart suggestions.', fill=(107, 114, 128), font=body_font)

    search_bar = (110, 320, 900, 370)
    draw.rounded_rectangle(search_bar, radius=20, fill=(255, 255, 255), outline=(209, 213, 219), width=2)
    draw.text((140, 332), 'Search for a movie...', fill=(148, 163, 184), font=body_font)

    draw.rounded_rectangle((920, 320, 1040, 370), radius=20, fill=(229, 9, 20), outline=(229, 9, 20), width=2)
    draw.text((958, 333), 'Search', fill=(255, 255, 255), font=body_font)

    draw.rounded_rectangle((110, 420, 360, 580), radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    draw.text((140, 450), 'Trending Now', fill=(30, 41, 59), font=load_font(24))
    draw.text((140, 490), '• Inception', fill=(100, 116, 139), font=body_font)
    draw.text((140, 525), '• Interstellar', fill=(100, 116, 139), font=body_font)
    draw.text((140, 560), '• The Matrix', fill=(100, 116, 139), font=body_font)

    draw.rounded_rectangle((400, 420, 760, 580), radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    draw.text((430, 450), 'Popular Picks', fill=(30, 41, 59), font=load_font(24))
    draw.text((430, 490), 'Movie details, ratings, genre and plot in one click.', fill=(100, 116, 139), font=body_font)
    draw.text((430, 525), 'Fast and simple movie discovery experience.', fill=(100, 116, 139), font=body_font)

    draw.rounded_rectangle((790, 420, 1080, 580), radius=24, fill=(109, 40, 217), outline=(109, 40, 217), width=2)
    draw.text((820, 450), 'Live Search', fill=(255, 255, 255), font=load_font(24))
    draw.text((820, 490), 'Enter a movie name to see', fill=(237, 233, 254), font=body_font)
    draw.text((820, 525), 'instant suggestions.', fill=(237, 233, 254), font=body_font)

    img.save(os.path.join(OUTPUT_DIR, 'mainpage.png'))


def create_suggestion_page():
    img = Image.new('RGBA', (WIDTH, HEIGHT), (17, 24, 39, 255))
    draw = draw_gradient_background(img, (17, 24, 39), (15, 118, 110))

    draw_card(draw, 50, 60, 1230, 660, (255, 255, 255, 245), radius=32)
    draw_card(draw, 80, 90, 1200, 630, (248, 250, 252, 255), radius=28)

    title_font = load_font(36)
    body_font = load_font(20)
    small_font = load_font(17)

    draw.text((110, 120), 'Movie Suggestions', fill=(109, 40, 217), font=title_font)
    draw.text((110, 175), 'Showing results for: Inception', fill=(71, 85, 105), font=body_font)

    search_bar = (110, 210, 920, 270)
    draw.rounded_rectangle(search_bar, radius=20, fill=(255, 255, 255), outline=(209, 213, 219), width=2)
    draw.text((140, 224), 'Search again...', fill=(148, 163, 184), font=body_font)
    draw.rounded_rectangle((940, 210, 1040, 270), radius=20, fill=(229, 9, 20), outline=(229, 9, 20), width=2)
    draw.text((970, 224), 'Search', fill=(255, 255, 255), font=body_font)

    cards = [
        ((110, 320), 'Inception', 'Sci-Fi / Thriller', '2010', '⭐ 8.8'),
        ((430, 320), 'Interstellar', 'Sci-Fi / Adventure', '2014', '⭐ 8.7'),
        ((750, 320), 'The Matrix', 'Action / Sci-Fi', '1999', '⭐ 8.7'),
    ]

    for (x, y), title, genre, year, rating in cards:
        draw_card(draw, x, y, x + 280, y + 240, (255, 255, 255, 255), radius=24)
        draw.rounded_rectangle((x + 20, y + 20, x + 260, y + 150), radius=20, fill=(15, 118, 110, 30))
        draw.text((x + 30, y + 170), title, fill=(30, 41, 59), font=load_font(24))
        draw.text((x + 30, y + 205), genre, fill=(100, 116, 139), font=small_font)
        draw.text((x + 30, y + 230), f'Year: {year}   {rating}', fill=(109, 40, 217), font=small_font)

    draw_card(draw, 1060, 320, 1160, 560, (109, 40, 217, 255), radius=24)
    draw.text((1088, 350), 'Details', fill=(255, 255, 255), font=load_font(22))
    draw.text((1088, 390), 'A skilled thief', fill=(237, 233, 254), font=small_font)
    draw.text((1088, 420), 'enters people\'s dreams', fill=(237, 233, 254), font=small_font)
    draw.text((1088, 455), 'to steal secrets.', fill=(237, 233, 254), font=small_font)
    draw.text((1088, 505), 'IMDb: 8.8', fill=(255, 255, 255), font=small_font)

    img.save(os.path.join(OUTPUT_DIR, 'movie-suggestion-page.png'))


os.makedirs(OUTPUT_DIR, exist_ok=True)
create_main_page()
create_suggestion_page()

print('created', os.path.getsize(os.path.join(OUTPUT_DIR, 'mainpage.png')), os.path.getsize(os.path.join(OUTPUT_DIR, 'movie-suggestion-page.png')))
