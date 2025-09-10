import qrcode

while True:
    print("\n---- QR Code Generator ----")
    website_link = input("Enter the website link: ")

    note = """
+--------------------------------------------------------------+
|                          NOTE                                |
+--------------------------------------------------------------+
| Version = Size of QR matrix (1 = smallest, 40 = largest).    |
|   Higher version = can store more data.                      |
|                                                              |
| Box size = Pixel size of each square (module).               |
|   Larger value = Bigger image (e.g., 5 = small,              |
|   10 = medium, 20 = large).                                  |
|                                                              |
| Border = White margin around QR (in modules).                |
|   Minimum recommended = 4 for best scanning.                 |
+--------------------------------------------------------------+
"""
    print(note)

    version = int(input("Enter version (1-40, or just type 1 for small QR): "))
    box_size = int(input("Enter box size (e.g., 5, 10, 20): "))
    border = int(input("Enter border size (e.g., 4, 5, 10): "))

    qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
    qr.add_data(website_link)
    qr.make(fit=True)

    fill = input("\nEnter the fill color (e.g., black, blue, red): ")
    back = input("Enter the background color (e.g., white, yellow, green): ")
    img = qr.make_image(fill_color=fill, back_color=back)

    file_name = input("\nEnter the file name to save (without extension): ") + ".png"
    img.save(file_name)

    print(f"QR code saved as {file_name}")

    again = input("\nDo you want to generate another QR code? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("👋 Exiting QR Code Generator. Goodbye!")
        break
