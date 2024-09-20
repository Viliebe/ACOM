import cv2
import numpy as np
def gauss(x, y, omega, a, b):
    first = 1/(2*np.pi * (omega ** 2))
    second = np.exp(-((x-a) ** 2 + (y-b) ** 2) / (2*(omega**2)))

    return first * second

def gausianBlur(img,kernelSize,devation):
    kernel=np.ones((kernelSize,kernelSize))
    a=b=(kernelSize+1)//2
    for i in range(kernelSize):
        for j in range(kernelSize):
            kernel[i,j]=gauss(i,j,devation,a,b)
    print(kernel)
    sum=kernel.sum()
    kernel/=sum
    print(kernel)

    blured=img.copy()
    Start = kernelSize // 2

    for i in range(Start, blured.shape[0] - Start):
        for j in range(Start, blured.shape[1] - Start):
            val=0
            for k in range(-Start, Start + 1):
                for l in range(-Start, Start + 1):
                    val += img[i + k, j + l] * kernel[k + Start, l + Start]
            blured[i, j] = val
    return blured

img=cv2.imread("pic1.jpg",cv2.IMREAD_GRAYSCALE)
# blured1=gausianBlur(img,5,100)
# blured2=gausianBlur(img,7,100)
# blured3=gausianBlur(img,5,10)
# blured4=gausianBlur(img,7,10)
blured5=gausianBlur(img,11,50)

# cv2.imshow("blured 5 100",blured1)
# cv2.imshow("blured 7 100",blured2)
# cv2.imshow("blured 5 10",blured3)
# cv2.imshow("blured 7 10",blured4)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2blured=cv2.GaussianBlur(img,(5,5),100)
# cv2.imshow("blured 5 100",blured1)
# cv2.imshow("opencv blur",cv2blured)
cv2.imshow("blured 7 100",blured5)

cv2.waitKey(0)
cv2.destroyAllWindows()