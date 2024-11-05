# Aerosol Optical Depth Estimation using Sentinel-2 Imagery

## Project Overview

Aerosol Optical Depth (AOD) is a key measure used in atmospheric sciences to quantify the concentration of aerosols in the atmosphere. Accurate AOD estimation is critical for monitoring air quality, assessing environmental health, and understanding climate change. This project aims to estimate AOD by extracting relevant features from high-resolution Sentinel-2 satellite imagery, which contains 13 spectral bands, and then applying a CatBoost regression model to make predictions.

This solution is part of a competitive effort to enhance AOD estimation accuracy, contributing to better environmental monitoring and decision-making.

---

## Solution Architecture

The solution is divided into the following stages:

1. **Data Processing & Feature Extraction**: Using multispectral Sentinel-2 images, we extract custom features that capture relevant spatial and spectral information.
2. **Modeling with CatBoost**: We apply a CatBoost regression model with a cross-validation approach to predict AOD values.
3. **Evaluation & Cross-Validation**: Using K-Fold cross-validation, we assess model performance and output predictions for the test set.

Each stage involves multiple steps, as detailed below.

---

## Data Description

### 1. Sentinel-2 Satellite Images
Sentinel-2 imagery is multispectral, offering high-resolution data across 13 bands (from visible to shortwave infrared regions). The available bands for each image are as follows:
- B1 to B12, including a specific 8A band for improved vegetation and water mapping.

These bands enable the analysis of various land and atmospheric properties, which are essential for extracting AOD-related features.

### 2. AERONET Dataset
The AERONET (Aerosol Robotic Network) dataset provides ground-truth AOD values at specific wavelengths, particularly at 500nm and 675nm. Using Angstrom interpolation, we compute AOD at the target 550nm wavelength for alignment with satellite data.

---

## Methodology

### Step 1: Feature Extraction

To effectively capture the spectral and spatial characteristics related to AOD, we designed custom features from Sentinel-2 bands based on domain insights. These features are derived using statistical calculations, band ratios, texture, and wavelet transformations.

#### Feature Engineering

1. **Band Ratios**: Ratios between bands are calculated to capture relative spectral intensities, revealing information about aerosols' influence on different wavelengths. Band ratios are valuable because they:
   - Enhance contrast by highlighting differences between spectral bands.
   - Mitigate the effect of varying light conditions by normalizing reflectance values.

   Example features:
   - `ratio_band_1_8_mean_max_ratio`: Mean-to-max ratio between Band 1 and Band 8.
   - `ratio_band_3_5_mean`: Mean of the ratio between Band 3 and Band 5.

2. **Statistical Features**: We calculate statistics such as mean, min, max, and standard deviation across bands to capture general reflectance behavior. These can reveal how aerosol presence impacts the spread and distribution of reflectance values in the image.
   - `min_max_ratio_3`: Minimum-to-maximum ratio in Band 3.
   - `band_6_13_std_ratio`: Ratio of standard deviations between Band 6 and Band 13.

3. **Local Binary Pattern (LBP)**: LBP is used to quantify texture in Band 1, capturing fine spatial variations that could indicate aerosol distribution patterns. 
   - `band_1_window_3_lbp_entropy`: Entropy of LBP histogram for Band 1.

4. **Wavelet Transform Features**: We applied a wavelet decomposition on selected bands to capture spatial frequency details across multiple scales. Specifically, Haar wavelets were used for their simplicity and efficiency in capturing high-frequency changes.
   - `band_1_wavelet_haar_cD3_min`: Minimum coefficient in the detail component of the third level for Band 1.

Each of these features is carefully constructed to capture different properties of aerosols' interaction with atmospheric and surface reflectance.

### Step 2: Data Aggregation and Preprocessing

For training, the extracted features are compiled alongside AERONET’s AOD values, which serve as the ground truth labels. We processed training and testing datasets by saving features in `.npz` format, facilitating efficient loading and handling.

### Step 3: Model Training with CatBoost

#### Why CatBoost?
CatBoost is a gradient boosting algorithm optimized for handling categorical features and mitigating overfitting. It also provides efficient GPU support, which accelerates the training process significantly.

#### Model Configuration
We optimized the model using a custom parameter set, which includes:
   - `learning_rate`, `l2_leaf_reg`, `depth`, and `iterations`: These parameters control the learning dynamics of the model.
   - `grow_policy` set to `'Lossguide'`: Helps the model choose splits that minimize prediction error, making it suitable for structured data.
   - `task_type='GPU'`: Ensures efficient processing.

#### Cross-Validation and Evaluation
Using 17-fold cross-validation, we evaluate model stability and performance. For each fold:
   - We split the data into training and validation sets, fit the model, and calculate the Pearson correlation between predictions and ground truth AOD values.
   - Average correlations across folds provide a robust measure of model reliability.

The cross-validation yielded a mean correlation of **0.9560 ± 0.0273**, indicating high predictive performance.

### Step 4: Prediction and Output

After training, we predict AOD values for test images using the trained CatBoost model. These predictions are saved to a CSV file for submission or further analysis.

---

## File Structure

The project consists of the following main files:

- **`extract_features()`**: Function for extracting features from Sentinel-2 images.
- **`process_csv()`**: Aggregates features and labels from the training data.
- **`process_folder()`**: Extracts features from the test data and saves them for prediction.
- **`perform_cross_validation_and_predict()`**: Trains the CatBoost model using cross-validation and outputs predictions.
- **`C_PD_9F.csv`**: The final prediction file containing AOD estimates for test images.

---

## Results and Observations

1. **Cross-Validation Performance**: The model achieved a high Pearson correlation of **0.9560** on average across 17 folds, indicating that the features are well-suited for predicting AOD from Sentinel-2 imagery.
   
2. **Feature Importance**: Upon analysis, wavelet and ratio-based features showed strong predictive power, highlighting the value of spectral and spatial patterns in AOD estimation.

3. **Prediction Output**: Test predictions were saved successfully to `C_PD_9F.csv`, providing AOD estimates for each test image.

---

## Requirements

- **Python Libraries**:
  - `numpy`, `pandas`, `scipy`: For numerical computations and data handling.
  - `rasterio`: For reading Sentinel-2 images.
  - `scikit-image`: For LBP feature extraction.
  - `pywavelets`: For wavelet transform calculations.
  - `catboost`: For regression modeling.

- **Hardware**: GPU recommended for efficient CatBoost training.

---

## Conclusion and Future Work

This project demonstrates a robust methodology for AOD estimation from Sentinel-2 images by combining domain-specific feature engineering with CatBoost regression. The achieved correlation shows promise for deploying this model in real-world AOD monitoring applications.

### Future Directions
To further improve the model:
   - **Additional Features**: Explore more complex spatial patterns using GLCM (Gray Level Co-occurrence Matrix) or advanced CNN-based features.
   - **Temporal Analysis**: Incorporate time-series data for each location to capture temporal variations in aerosol levels.
   - **Hyperparameter Tuning**: Experiment with more advanced optimization techniques to fine-tune CatBoost parameters.

