import argparse
import os
from PIL import Image, ImageDraw, ImageFont

def generate_certificate(name, course, date, template_path, output_path, font_path="arial.ttf"):
    try:
        # Load the certificate template
        template = Image.open(template_path)
    except Exception as e:
        print(f"Error loading template image: {e}")
        return

    draw = ImageDraw.Draw(template)

    # Define fonts and positions (customize these values based on your template)
    try:
        font = ImageFont.truetype(font_path, 60)
    except IOError:
        print(f"Font file not found: {font_path}")
        return

    # Example positions (you'll need to adjust these based on your template)
    name_position = (500, 300)
    course_position = (500, 400)
    date_position = (500, 500)

    # Draw the text on the template
    draw.text(name_position, name, font=font, fill="black")
    draw.text(course_position, course, font=font, fill="black")
    draw.text(date_position, date, font=font, fill="black")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the generated certificate
    try:
        template.save(output_path)
        print(f"Certificate saved to {output_path}")
    except Exception as e:
        print(f"Error saving certificate: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generate digital certificates")
    parser.add_argument("name", help="Name of the recipient")
    parser.add_argument("course", help="Course name")
    parser.add_argument("date", help="Date of completion")
    parser.add_argument("template_path", help="Path to the certificate template image")
    parser.add_argument("output_path", help="Path to save the generated certificate")
    parser.add_argument("--font", default="arial.ttf", help="Path to the font file (default: arial.ttf)")

    args = parser.parse_args()

    generate_certificate(args.name, args.course, args.date, args.template_path, args.output_path, args.font)

if __name__ == "__main__":
    main()



