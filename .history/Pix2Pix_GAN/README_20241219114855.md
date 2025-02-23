##  Pix2Pix: Image-to-Image Translation with Conditional GANs
**Pix2Pix** is a Conditional Generative Adversarial Network (CGAN) introduced by [Isola et al.](https://arxiv.org/abs/1611.07004) for image-to-image translation tasks. 

Pix2Pix is a type of Conditional Generative Adversarial Network (CGAN) introduced by Isola et al. in 2017 for image-to-image translation tasks. This model learns to translate one type of image into another by training on paired images (i.e., input-output pairs). The generator in Pix2Pix attempts to convert an input image into a target output image, while the discriminator learns to distinguish between real target images and the generated images from the generator.

## Key Features:

- **Conditional GAN**: Unlike standard GANs, the Pix2Pix model is conditional, meaning the generator is guided by an input image, and the discriminator evaluates the output based on both the input and generated image.
- **Paired Data**: The model requires paired training data (e.g., an image and its corresponding translated version) for tasks such as image colorization, edge-to-photo translation, and more.

## Applications:
- **Photo enhancement: Transforming low-quality images into high-quality ones.
- **Semantic segmentation: Mapping a segmentation mask (labels) to an image.
- **Image colorization: Turning grayscale images into color images.
- **Edge-to-image translation: Converting edge maps to full-color images.
- 
## Sample Output:

This is an example image of the Pix2Pix model output from the original paper:
![Pix2Pix Output](./Pix2Pix_Outputs.jpg)


