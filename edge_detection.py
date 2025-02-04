import cv2  # استيراد مكتبة OpenCV

# تحميل الصورة
image_path = 'image.jpg'  # ضع مسار الصورة هنا
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# تحويل الصورة إلى تدرجات الرمادي
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# تطبيق خوارزمية اكتشاف الحواف Canny
edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

# عرض النتائج
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)

# الانتظار حتى يتم الضغط على أي مفتاح لإغلاق النوافذ
cv2.waitKey(0)
cv2.destroyAllWindows()
