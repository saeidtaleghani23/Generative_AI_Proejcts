# Generative AI Projects

This repository contains implementations of various Generative Adversarial Networks (GANs), showcasing different architectures used for image synthesis and translation tasks. Each project demonstrates key techniques in generative AI, including conditional image generation, style transfer, and domain adaptation.

## Projects Included

### 1. Conditional GAN (CGAN)  
A Conditional GAN extends the traditional GAN framework by conditioning both the generator and discriminator on auxiliary information, such as class labels, to generate specific types of images.  

- **Key Features:**
  - Conditional inputs guide image generation.
  - Uses additional label information in training.
  - Applications: Image-to-image translation, domain adaptation.  
- **Paper:** [Conditional Generative Adversarial Nets (Mirza & Osindero, 2014)](https://arxiv.org/abs/1411.1784)


### 2. Deep Convolutional GAN (DCGAN)  
DCGAN is an improved version of the vanilla GAN that incorporates deep convolutional networks for more stable training and high-quality image generation.  

- **Key Features:**
  - Uses convolutional layers instead of fully connected layers.
  - Batch normalization for stability.
  - Applications: Generating realistic images from noise.  
- **Paper:** [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks (Radford et al., 2015)](https://arxiv.org/abs/1511.06434)

### 3. CycleGAN  
CycleGAN enables unpaired image-to-image translation by learning to map images between two domains while preserving style and content.  

- **Key Features:**
  - Unpaired image translation.
  - Uses cycle consistency loss.
  - Applications: Style transfer, domain conversion (e.g., horse↔zebra, summer↔winter).  
- **Paper:** [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks (Zhu et al., 2017)](https://arxiv.org/abs/1703.10593)

### 4. Pix2Pix GAN  
Pix2Pix is a paired image-to-image translation GAN that learns a mapping from an input image to an output image using a supervised learning approach.  

- **Key Features:**
  - Requires paired training data.
  - Uses U-Net-based generator and PatchGAN discriminator.
  - Applications: Edge-to-photo, sketch-to-image, satellite-to-map transformations.  
- **Paper:** [Image-to-Image Translation with Conditional Adversarial Networks (Isola et al., 2017)](https://arxiv.org/abs/1611.07004)

## Installation

Clone the repository and install the required dependencies of each project:

```bash
git clone https://github.com/saeidtaleghani23/Generative_AI.git
cd Generative_AI
```