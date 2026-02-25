# Computer Vision

## Overview

Computer Vision (CV) enables machines to interpret and understand visual information from the world — images, videos, and real-time camera feeds. While NLP is the primary modality for most AI agents, CV is essential for multimodal agents that process visual data.

## Core CV Tasks

| Task | Description | Applications |
|------|------------|-------------|
| **Image Classification** | Assign a label to an entire image | "This is a cat", medical diagnosis |
| **Object Detection** | Locate and classify objects within an image | Autonomous driving, security cameras |
| **Semantic Segmentation** | Classify every pixel in an image | Medical imaging, satellite analysis |
| **Instance Segmentation** | Detect + segment individual object instances | Robotics, AR/VR |
| **Image Generation** | Create new images from descriptions or noise | DALL-E, Stable Diffusion, Midjourney |
| **OCR** | Extract text from images | Document processing, receipt scanning |
| **Face Recognition** | Identify or verify people from facial features | Security, authentication |
| **Pose Estimation** | Detect body positions and movements | Fitness apps, gaming, robotics |

## Key Architectures

### CNNs (Convolutional Neural Networks)
The foundational architecture for CV. Uses convolutional filters to detect features (edges, textures, shapes) at multiple scales.
- **LeNet** (1998): Handwritten digit recognition
- **AlexNet** (2012): ImageNet breakthrough — started the deep learning revolution
- **VGG** (2014): Deeper networks with small 3x3 filters
- **ResNet** (2015): Skip connections enabling very deep networks (152+ layers)
- **EfficientNet** (2019): Optimal scaling of width, depth, and resolution

### Vision Transformers (ViT)
Applies the Transformer architecture (from NLP) to images by splitting them into patches.
- Treats image patches like tokens
- Self-attention across all patches
- Often matches or exceeds CNNs with enough data

### Multimodal Models
- **CLIP** (OpenAI): Connects images and text in a shared embedding space
- **GPT-4V / GPT-4o**: Processes both text and images
- **LLaVA**: Open-source multimodal model
- **Gemini**: Google's multimodal foundation model

## CV for Agentic AI

- **Multimodal agents** can see and understand images, screenshots, documents
- **Document processing agents** use OCR to extract information from PDFs and images
- **Web agents** use CV to understand and navigate web pages
- **Robotic agents** rely on CV for perception and navigation
- **Quality inspection agents** use CV for manufacturing defect detection

## Tools and Frameworks
- **OpenCV**: Open-source computer vision library
- **PyTorch / torchvision**: Deep learning framework with CV models
- **Hugging Face**: Pre-trained vision models and pipelines
- **YOLO**: Real-time object detection
- **Detectron2**: Facebook's object detection platform
