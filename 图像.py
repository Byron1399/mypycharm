import cv2
import matplotlib.pyplot as plt

# 读取图片
image = cv2.imread(r'C:\Users\lll13\Pictures\1.jpg', cv2.IMREAD_GRAYSCALE)

# 对图像进行自适应阈值二值化处理
binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# 画出直方图
plt.figure(figsize=(10, 5))

# 原始灰度图像的直方图
plt.subplot(1, 2, 1)
plt.hist(image.ravel(), 256, [0, 256], color='blue')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# 二值化后的图像的直方图
plt.subplot(1, 2, 2)
plt.hist(binary_image.ravel(), 2, [0, 256], color='red')  # 二值图像只有两个像素值
plt.title('Binary Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

