
#  Project Summary: Tumor Detection in CT Scans (Custom CNN, No Pre-trained Models)

## ✅ Business Objectives

### **Primary Objective**:
> **Automate tumor detection** in CT scans using a custom-built convolutional neural network (CNN), trained from scratch.

### **Secondary Objective**:
> **Enable visual interpretability** to help the client and their team differentiate between tumor and non-tumor CT scans using intuitive visualizations, an interactive image montage, and a dashboard.


---

## Feasibility Assessment

* **Data Availability**: ✔️ Yes. Dataset has **4,154 tumor** and **1,586 no-tumor** images (imbalanced: 72.4% / 27.6%).
  **Mitigation**: Use `imblearn` for oversampling and `ImageDataGenerator` (rotation, flipping) for augmentation.
* **Technical Risk**: Medium. No use of pre-trained models increases training complexity, but it’s feasible with proper tuning.
* **Time Estimate**: ~40 hours
  * Data preparation: 10h
  * Model development (from scratch): 20h
  * Dashboard development: 10h

---

##  Business Q&A (Revised)

### 1. **What are the business objectives?**
* **Primary**: Train a custom CNN to detect tumors from CT scans automatically. **Achieved**: 89.66% test accuracy (0.34% short of >90% target)
* **Secondary**: Provide intuitive visualizations and a dashboard for manual comparison of tumor vs. non-tumor images.
  Notebook: `DataVisualization.ipynb`

---

### 2. **Any objective addressable with conventional data analysis?**
Yes — visualizations for interpretability (e.g., class distribution, prediction confidence) can be created using standard analytics to support the secondary objective. **Achieved**: Generated confidence score analysis, precision-recall curves, and confusion matrices.
Notebook: `DataVisualization.ipynb`
Libraries: `numpy`, `seaborn`, `plotly`

---

### 3. **Dashboard or API endpoint?**
**Dashboard only** — used to:
* Display real-time predictions with visual explanations (e.g., heatmaps, confidence scores).
* Enable manual comparison of tumor vs. non-tumor scans.
**Status**: Dashboard integration artifacts generated (test_predictions.csv, evaluation_metrics.json, confusion_matrices.json)
  Tool: **Streamlit**, hosted on **Heroku**
  Notebook: `ModelingAndEvaluating.ipynb`

---

### 4. **Success Criteria (Custom Model)?**
| Component | Goal                                                            |
| --------- | --------------------------------------------------------------- |
| Model     | >90% accuracy, >88% recall, <1.5 sec/inference                  |
| Dashboard | Real-time predictions + intuitive visualizations (e.g., heatmaps) for tumor vs. non-tumor differentiation + ROI calculator |

---

### 5. **Project Epics and User Stories**
| Epic                     | User Stories                                                                                                                 | Notebook                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **Data Prep**            | 1.1 Merge tumor classes<br>1.2 Resize images (224x224)<br>1.3 Analyze class imbalance<br>1.4 Augment minority class          | `DataCollection.ipynb`        |
| **Model Dev**            | 2.1 Build CNN from scratch<br>2.2 Train on tumor/no-tumor<br>2.3 Tune hyperparameters<br>2.4 Monitor recall & inference time | `ModelingAndEvaluating.ipynb` |
<!-- Add to Project Epics and User Stories -->
| **Visualization & Dashboard** | 3.1 Create visualizations for tumor vs. no-tumor differentiation<br>3.2 Build Streamlit dashboard<br>3.3 Add interactive image montage for label exploration<br>3.4 Deploy on Heroku | `DataVisualization.ipynb`     |

### 6. **Ethical/Privacy Considerations**
* **Privacy**: All data is anonymized —  compliant.
* **Bias**: Data is well balanced in final splits (imbalance ratio >0.8) - no class weights needed.
  Notebook: `DataCollection.ipynb`

---

### 7. **Does the data suggest a model?**
Yes — **custom CNN** (from scratch).
* 3-5 convolutional blocks + max pooling
* Flatten → dense layers → sigmoid
  Notebook: `ModelingAndEvaluating.ipynb`
  Framework: `TensorFlow`, `Keras`

---

### 8. **Inputs and Outputs**
* **Input**: 224x224 RGB (converted from grayscale), normalized
* **Output**: Tumor probability (0-1) + binary class (Tumor / No Tumor) + visual explanations (e.g., heatmaps)
  Libraries: `opencv`, `tensorflow`

---

### 9. **Performance Goals**
| Metric         | Target   | Validated via              |
| -------------- | -------- | -------------------------- |
| Accuracy       | >90%     | Test set                   |
| Recall         | >88%     | Confusion matrix           |
| Inference Time | <1.5 sec | Measured on unseen samples |

---

### 10. **Client Benefits**
* **Automation**: Reduces scan screening time from ~15 mins to ~2 mins via custom CNN.
* **Interpretability**: Dashboard provides intuitive visualizations (e.g., heatmaps, confidence scores) to aid manual differentiation of tumor vs. non-tumor scans.
* **Cost Savings**: Up to 85% reduction per 1,000 scans (~$42,400), visualized via dashboard sliders (Streamlit + Plotly).
  Notebook: `DataVisualization.ipynb`

---

##  Notebook Workflow Summary
| Notebook                      | Tasks                                                                                             | Libraries                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `DataCollection.ipynb`        | - Merge classes<br>- Resize + normalize<br>- Balance classes via oversampling<br>- Augment images | `opencv`, `imblearn`, `keras`                  |
| `DataVisualization.ipynb`     | - Visualize class distribution<br>- Create heatmaps for interpretability<br>- Build ROI calculator | `matplotlib`, `seaborn`, `plotly`, `streamlit` |
| `ModelingAndEvaluating.ipynb` | - Custom CNN<br>- Training & tuning<br>- Streamlit dashboard with prediction visualizations       | `tensorflow`, `sklearn`, `streamlit`           |

---

##  Risk Mitigation (Custom Training & Visualization Focus)
| Risk                        | Mitigation                                        |
| --------------------------- | ------------------------------------------------- |
| Class imbalance             | Oversample & augment minority class               |
| Model underfitting          | Use deeper CNN + batch norm + dropout             |
| Slow inference              | Keep model compact (limit parameters)             |
| Overfitting                 | Use early stopping + validation loss monitoring   |
| Unclear dashboard visualizations | Test heatmap clarity and user interaction locally before deploying to Heroku |

---

## Final Deliverables
* 3 Jupyter notebooks
* Fully custom CNN model (trained from scratch)
* Streamlit dashboard for predictions, visual interpretability (e.g., heatmaps), interactive image montage, and ROI calculator (Heroku-hosted)

* Validation metrics report with visualizations to support tumor vs. non-tumor differentiation

---




Class Imbalance Handling: Analyze class distribution and apply techniques like oversampling or data augmentation to balance the dataset.

Data Augmentation: Apply transformations (rotation, flipping, etc.) to increase dataset diversity, especially for minority classes.

Metadata Creation: Generate a CSV or DataFrame with image paths and labels for easy access during modeling.

Data Storage: Save the processed images and metadata in a structured directory for downstream tasks.

Documentation: Record all preprocessing steps for reproducibility and transparency.