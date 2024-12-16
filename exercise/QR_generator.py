import os
import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path, "JPEG")

    print(f"QR code saved as {file_path}")

if __name__ == "__main__":
    data = input("Enter data for QR code: ")
    file_name = input("Enter file name for QR code image (without extension): ")

    # Get the current working directory
    current_dir = os.getcwd()

    # Specify a file path for the saved QR code image in the current directory
    file_path = os.path.join(current_dir, file_name + ".jpg")

    generate_qr_code(data, file_path)
