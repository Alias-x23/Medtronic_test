from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import random


class ImageSampler:
    def __init__(self, img_path=None):
        if img_path:
            self.img_path = img_path
        self.img_details = {}

    def read_image(self):
        """
        this reads in the image and provides some information to the user before returning the image as an array
        """
        img = io.imread(self.img_path)
        self.img_details["shape"] = np.shape(img)
        print(f"The target image has a resolution of "
              f"{self.img_details['shape'][0]}px by {self.img_details['shape'][1]}px")
        return img

    def sample_image(self, img, height=10, width=10, samples=3):
        """
        This takes the image and then generates samples based on the inputs
        """
        print(f"Generating {samples} {height}x{width} sample(s) from image now!")
        max_height = self.img_details["shape"][0] - height
        max_width = self.img_details["shape"][1] - width

        out_list = []

        for i in range(samples):
            rand_x = random.randint(0, max_height)
            rand_y = random.randint(0, max_width)
            out_list.append(img[rand_x:rand_x+height, rand_y:rand_y+width])

        return out_list

    def run_sampler(self):
        """
        this is the main method which will call the other methods in order
        it also checks that the user inputs are valid for sampling the image
        """
        img = self.read_image()

        error_count = 0
        while True:
            try:
                height = int(input(f"Please input an x (height) value for the samples:\n"))
                width = int(input(f"Please input a y (width) value for the samples:\n"))
                if height <= self.img_details["shape"][0] and width <= self.img_details["shape"][1]:
                    break
                print(f"The chosen height and width must be less than the size of the image\n"
                      f"max height = {self.img_details['shape'][0]}\nmax width = {self.img_details['shape'][1]}")
                continue
            except:
                print("\nERROR: Please input whole number values as digits only")
                error_count += 1
            if error_count > 2:
                print(f"Sorry too many incorrect attempts\nExiting program now")
                exit()

        sample_list = self.sample_image(img, height, width)
        for sample in sample_list:
            plt.imshow(sample)
            plt.show()

        return img, sample_list


def main():
    image_sampler = ImageSampler("cake_image.jpg")
    image_sampler.run_sampler()


if __name__ == '__main__':
    main()
