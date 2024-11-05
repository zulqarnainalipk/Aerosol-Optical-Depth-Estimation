# Dataset Documentation for Aerosol Optical Depth Estimation Project

This README file provides a comprehensive overview of the datasets used in the AOD (Aerosol Optical Depth) estimation project. This dataset combines Sentinel-2 satellite imagery with AERONET ground-based observations for accurate AOD estimation at a wavelength of 550 nm. Below, you’ll find details about the dataset files, structure, and data sources, along with a guide on how each component contributes to the project.

---

## Data Summary

The dataset consists of three main files:
1. **Training Images (`train_images.zip`)**: Contains 4,467 multispectral Sentinel-2 images for model training.
2. **Training Labels (`train_answer.csv`)**: Provides AOD annotations corresponding to the training images.
3. **Test Images (`test_images.zip`)**: Contains 1,489 Sentinel-2 images without labels, used for model evaluation.

---

## Dataset Details

### 1. `train_images.zip`
- **File Type**: ZIP Archive
- **File Count**: 4,467 images
- **Description**: Each file in `train_images.zip` is a Sentinel-2 satellite image containing multispectral data across 13 spectral bands. These bands capture diverse information that can help assess atmospheric and surface reflectance, essential for accurate AOD estimation.

#### Sentinel-2 Bands Overview

Each Sentinel-2 image consists of the following 13 spectral bands:

| Band Name | Wavelength (nm) | Description                    |
|-----------|-----------------|--------------------------------|
| B1        | 443             | Coastal aerosol                |
| B2        | 490             | Blue                           |
| B3        | 560             | Green                          |
| B4        | 665             | Red                            |
| B5        | 705             | Vegetation Red Edge            |
| B6        | 740             | Vegetation Red Edge            |
| B7        | 783             | Vegetation Red Edge            |
| B8        | 842             | Near Infrared (NIR)            |
| B8A       | 865             | Narrow NIR                     |
| B9        | 945             | Water vapor absorption         |
| B10       | 1375            | SWIR-Cirrus                    |
| B11       | 1610            | SWIR                           |
| B12       | 2190            | SWIR                           |

The data spans images captured from **2016/01/01** to **2024/05/01**. All images have undergone cloud masking to remove cloud cover, thereby improving the quality of the data for AOD analysis.

#### Use of Bands for AOD Estimation
- **Visible Bands (B2, B3, B4)**: Important for detecting aerosols due to their impact on visible light absorption and scattering.
- **NIR and SWIR Bands (B8, B11, B12)**: Useful for distinguishing aerosols from clouds and analyzing surface reflectance.
- **Vegetation Red Edge (B5, B6, B7)**: Captures fine changes in reflectance that may indicate surface details affected by aerosols.

More information on Sentinel-2 bands can be found on the [Google Earth Engine dataset page](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#bands).

---

### 2. `train_answer.csv`
- **File Type**: CSV
- **File Count**: 1 file
- **Description**: Contains AOD values (ground-truth annotations) for each training image in `train_images.zip`.

#### Structure of `train_answer.csv`
The CSV file has the following structure:

| Column         | Description                                      |
|----------------|--------------------------------------------------|
| `image_id`     | Unique identifier for each image in the training set |
| `aod_550nm`    | Aerosol Optical Depth value at 550nm              |
| `site_name`    | Location name corresponding to AERONET station    |

- **AOD at 550nm**: The `aod_550nm` values in this file are derived by interpolating AOD values from the AERONET dataset at 500nm and 675nm wavelengths using the Angstrom formula to compute the desired 550nm values.

#### AERONET Station Information
Each image’s `site_name` field specifies the AERONET location associated with that image. These locations span different geographical regions, offering a diverse set of aerosol data points.

---

### 3. `test_images.zip`
- **File Type**: ZIP Archive
- **File Count**: 1,489 images
- **Description**: Contains Sentinel-2 images with the same 13 bands as the training images, used for evaluating model predictions.

This dataset lacks ground-truth AOD values, making it suitable for model testing and submission. Once the model is trained, it predicts AOD values for each image in this dataset, which can then be submitted for scoring.

---

## Data Sources

### Sentinel-2 Imagery
Sentinel-2, part of the European Space Agency’s Copernicus Program, provides open-access satellite imagery with 13 spectral bands, offering crucial information across the visible, NIR, and SWIR regions. The multispectral nature of these images allows for diverse analysis, from atmospheric to surface-level data, essential for estimating AOD.

- **Image Processing**: Each image has been pre-processed for cloud masking to remove interference from clouds, ensuring that the features extracted from images are more accurate for AOD estimation.
  
For more details, refer to the [Google Earth Engine Sentinel-2 dataset documentation](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#bands).

### AERONET Data
AERONET (Aerosol Robotic Network) is a global ground-based network of sun photometers measuring aerosol optical depth, among other atmospheric parameters. The provided AERONET data includes AOD values at specific wavelengths (500nm and 675nm), and these values are interpolated to derive the AOD at 550nm required for this project.

- **Interpolation Using Angstrom Exponent**: The Angstrom exponent is used to interpolate between two known AOD values to estimate the value at a specific wavelength (550nm).
  
For more information on AERONET data, visit the [AERONET website](https://aeronet.gsfc.nasa.gov/).

---

## Dataset Preparation Workflow

The following workflow can be used to prepare and utilize the dataset for AOD estimation:

1. **Unzip and Load Sentinel-2 Images**: Extract and load multispectral images from `train_images.zip` and `test_images.zip`. Ensure that each image’s bands are accessible for feature extraction.

2. **Load Training Annotations**: Load `train_answer.csv` to retrieve AOD values for supervised training. Match each `image_id` in the CSV with its corresponding image in the training set.

3. **Feature Extraction**: Perform feature engineering on each Sentinel-2 image by calculating band ratios, statistical features, and other spatial characteristics to represent AOD-relevant information.

4. **Model Training**: Using the features extracted from the training images and their corresponding AOD values in `train_answer.csv`, train a regression model to predict AOD.

5. **Prediction on Test Set**: After training, predict AOD for each image in the `test_images.zip` set.

---

## Data Limitations and Considerations

1. **Temporal Variation**: AOD levels change over time due to factors like weather and human activities. While this dataset spans several years, any real-world deployment should consider the temporal dynamics of AOD.

2. **Geographical Bias**: Some regions may have more frequent data than others due to AERONET station distribution. Be mindful of potential biases toward heavily monitored areas.

3. **Cloud Masking Limitations**: Although the images are pre-processed for cloud removal, cloud shadow artifacts or partial cloud cover may still impact some images.

---
