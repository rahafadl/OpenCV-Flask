from flask import Flask, render_template, send_from_directory
import cv2

app = Flask(__name__)

# دالة لمعالجة الصورة الأصلية واستخراج الحواف
def process_image():
    image_path = "image.jpg"  # تأكد أن الصورة الأصلية موجودة هنا
    output_path = "static/edges.jpg"  # يتم حفظ الصورة الناتجة هنا

    # قراءة الصورة
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError("الصورة الأصلية غير موجودة أو لا يمكن قراءتها.")

    # تطبيق فلتر كشف الحواف
    edges = cv2.Canny(image, 100, 200)

    # حفظ الصورة الناتجة
    cv2.imwrite(output_path, edges)

# نقطة البداية للتطبيق
@app.route("/")
def index():
    # معالجة الصورة قبل عرض الصفحة
    process_image()
    return render_template("index.html")

# تقديم الصورة الناتجة
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
