# Job Role Recommendation Engine

## 🧠 Approach
- Represented each job role as a set of skills.
- Converted these sets into a binary matrix using `MultiLabelBinarizer`.
- Calculated similarity using Jaccard similarity.
- Returned top 3 most similar roles based on overlapping skillsets.

## 🔍 Why Jaccard Similarity?
- Perfect for comparing sets.
- Measures intersection over union.
- Simple, interpretable, and effective for this context.

## 📦 Tools Used
- Python
- Pandas, Scikit-learn
- Streamlit

## 🔄 Example Output
**Input**: Data Scientist  
**Recommendations**:
1. Data Analyst – 0.60  
2. Machine Learning Engineer – 0.40  
3. Business Analyst – 0.20
