# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the Cherry Leaves project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. In your newly created repo click on the green Code button. 

1. Then, from the Codespaces tab, click Create codespace on main.

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. Open the jupyter_notebooks directory, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.12.1 as it inherits from the workspace, so it will be Python-3.12.1 as installed by Codespaces. To confirm this, you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, then you can create a new one with _Regenerate API Key_.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- List here your project hypothesis(es) and how you envision validating it (them).

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.












Project Considerations
In case you want to use a spreadsheet to list your variables for the data-cleaning and feature-engineering steps, you may download the template in this link. This file will not be assessed and it will not be marked as part of your final grade, it is just an auxiliary file you can use in your workflow.

In this file, you should list the variables of your chosen dataset.

Requirements:

You have to set at least 2 business requirements, where one should be answered using conventional data analysis and the other should be answered using ML.
You should deliver at least one ML system that is capable of meeting a given business requirement. In that case, you may either use conventional ML or Neural Networks to predict the desired behaviour. We suggest you consider the ML tasks we covered in the course: Regression, Classification and Clustering.
Dashboard Expectations
Your dashboard should contain:

A project summary page, showing the project dataset summary and the client's requirements.
A page (or a set of pages) displaying how you used data analytics and/or ML to solve the business requirements.
A page indicating your project hypothesis and how you validated it across the project.
A technical page displaying your model performance, assuming you used ML to solve a business requirement. If you deployed an ML pipeline, you have to display your pipeline steps.


What are the business objectives?

Is there any business objective that can be answered with conventional data analysis?

Does the client need a dashboard or an API endpoint?

What does the client consider as a successful project outcome?

Can you break down the project into Epics and User Stories?

Ethical or Privacy concerns?

Does the data suggest a particular model?

What are the model’s inputs and intended outputs?

What are the criteria for the performance goal of the predictions?

How will the client benefit?




Quality and Feasibility Review
Feasibility Assessment:

Data Availability: ✔️ Tumor/no-tumor labels exist (4,154 tumor, 1,586 no-tumor, 72.4%/27.6% split). Imbalanced dataset; oversample no-tumor class using imblearn and augment with rotation/flipping via keras.preprocessing.image.ImageDataGenerator to balance and diversify.  
Technical Risk: Low (ResNet50 proven for medical imaging).  
Time Estimate: 40 hours (data prep: 10h, modeling: 20h, dashboard: 10h).





To align the provided project summary points with the primary and secondary business objectives (automating tumor detection in CT scans using a custom-built CNN and enabling visual interpretability via intuitive visualizations and a dashboard), I’ll review and edit the points for consistency. The primary objective focuses on automation through a custom CNN, and the secondary objective emphasizes visual interpretability for differentiating tumor vs. non-tumor CT scans. Any points that deviate from these objectives or introduce inconsistencies will be revised or removed.

### Review of Inconsistencies
After analyzing the provided summary, most points align well with the objectives, but a few areas need adjustment:
1. **Conventional Data Analysis (Q2)**: The statement that cost/time savings can be demonstrated using standard analytics is partially misaligned. While analytics can support the secondary objective (visual interpretability), the primary focus should remain on the CNN’s automation. This section needs clarification to tie analytics directly to visualization for interpretability.
2. **Efficiency Analytics Epic (Q5)**: The epic includes “Simulate time/cost savings,” which, while useful, is not explicitly tied to the secondary objective of visual interpretability. This needs rephrasing to focus on visualizations that support differentiation of tumor vs. non-tumor scans.
3. **Client Benefits (Q10)**: The cost/time savings are mentioned but not explicitly linked to the dashboard’s role in interpretability. This section should emphasize how the dashboard visualizes predictions to aid manual comparison, aligning with the secondary objective.
4. **Risk Mitigation**: The mitigation strategies are relevant but don’t explicitly address risks related to visual interpretability (e.g., unclear visualizations). This needs a minor addition.
5. **Final Deliverables**: The deliverables mention a “validation metrics report” but don’t clarify its role in interpretability. This should be tied to the secondary objective.

### Revised Project Summary
Below is the edited project summary, with changes to ensure consistency with the primary (automate tumor detection with a custom CNN) and secondary (enable visual interpretability) objectives. I’ve kept the structure intact and only modified the inconsistent points, ensuring clarity and alignment.

---

#  Project Summary: Tumor Detection in CT Scans (Custom CNN, No Pre-trained Models)

## ✅ Business Objectives

### **Primary Objective**:
> **Automate tumor detection** in CT scans using a custom-built convolutional neural network (CNN), trained from scratch.

### **Secondary Objective**:
> **Enable visual interpretability** to help the client and their team differentiate between tumor and non-tumor CT scans using intuitive visualizations and a dashboard.

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
* **Primary**: Train a custom CNN to detect tumors from CT scans automatically.
* **Secondary**: Provide intuitive visualizations and a dashboard for manual comparison of tumor vs. non-tumor images.
  Notebook: `DataVisualization.ipynb`

---

### 2. **Any objective addressable with conventional data analysis?**
Yes — visualizations for interpretability (e.g., class distribution, prediction confidence) can be created using standard analytics to support the secondary objective.
Notebook: `DataVisualization.ipynb`
Libraries: `numpy`, `seaborn`, `plotly`

---

### 3. **Dashboard or API endpoint?**
**Dashboard only** — used to:
* Display real-time predictions with visual explanations (e.g., heatmaps, confidence scores).
* Enable manual comparison of tumor vs. non-tumor scans.
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
| **Visualization & Dashboard** | 3.1 Create visualizations for tumor vs. non-tumor differentiation<br>3.2 Build Streamlit dashboard<br>3.3 Deploy on Heroku | `DataVisualization.ipynb`     |

---

### 6. **Ethical/Privacy Considerations**
* **Privacy**: All data is anonymized —  compliant.
* **Bias**: Use oversampling + augmentation to reduce false negatives (especially no-tumor cases).
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
* Streamlit dashboard for predictions, visual interpretability (e.g., heatmaps), and ROI calculator (Heroku-hosted)
* Validation metrics report with visualizations to support tumor vs. non-tumor differentiation

---

