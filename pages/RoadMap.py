import streamlit as st
st.set_page_config(
    page_title="Roadmap",
    page_icon="🎯",      
)

st.title("🎯Roadmap")

#Sidebar 
with st.sidebar:
    if st.button("Log Out"):
        st.switch_page("main.py")       
    st.title("What to do")    
    st.page_link("pages/Home.py", label = "Home", icon = "🏠")
    st.page_link("pages/Resources.py", label = "Resources", icon = "📑")
    st.page_link("pages/RoadMap.py", label = "RoadMap", icon = "🎯",)
    st.markdown("---")
    st.link_button("📌Visit my GitHub to view the source code!👈","https://github.com/FlorinMilu/Streamlit-Dev")




st.markdown("""
### 1. Data Collection and Preprocessing:
Dataset: Obtain a labeled dataset of medical images with annotated tumor regions. Datasets like The Cancer Imaging Archive (TCIA) or other publicly available medical imaging datasets can be useful.

Data Preprocessing: Preprocess the images to ensure uniformity in terms of resolution and format. Normalize pixel values and consider augmentations to increase the diversity of the training data.

### 2. Model Development:
Choose a Segmentation Architecture: Select a suitable deep learning architecture for image segmentation. Popular choices include U-Net, DeepLab, or Mask R-CNN.

Data Splitting: Split your dataset into training, validation, and test sets.

Model Training: Train the chosen segmentation model using the training set. Use the validation set to monitor and fine-tune hyperparameters to avoid overfitting.

Post-processing: Implement post-processing steps to refine the segmentation results, such as removing small isolated regions or smoothing the boundaries.

### 3. Tumor Volume Estimation:
Voxel-to-Millimeter Conversion: Since medical images often have voxel dimensions, convert the segmented regions into real-world millimeter dimensions using the metadata associated with the images.

Volume Calculation: Use the segmented regions to calculate the volume of the tumor. This can be done by summing up the volumes of individual voxels or employing numerical integration techniques.

### 4. Streamlit App Integration:
Create a Streamlit App Script: Develop a Streamlit app script where users can upload medical images. Use the trained model to perform segmentation and volume estimation.

Display Results: Present the segmented images and the calculated tumor volume in the Streamlit app. You can also include additional visualizations or metrics to enhance the user experience.

### 5. Deployment:
Deploy on a Platform: Deploy your Streamlit app on platforms like Heroku, Streamlit Sharing, or AWS. Ensure that you handle the deployment of the deep learning model appropriately, considering any necessary dependencies.
            
### 6. Continuous Improvement:
Iterate and Fine-tune: Collect user feedback, analyze model performance, and iteratively improve your app. Fine-tune the model as needed based on additional labeled data or improved algorithms.
""")