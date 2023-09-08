# Introduction
This dataset is a collection of over 4,000 reviews of Dermalogica skincare products. Data source is from [Kaggle](https://www.kaggle.com/datasets/nenamalikah/nlp-ulta-skincare-reviews)

# Goals and Objectives
* What can the reviews tell us about the products?
* Do most buyers have common skincare issues?
* What issues did the products help solve or exacerbate?
* Create a wordcloud showing the words/phrases commonly associated with each product.
* Build a model that can predict whether a review is positive or negative.

# Featured Techniques
* Exploratory Analysis
* Word cloud
* Logistic Regression
* Random Forest Classifier
* Decision Tree Classifier

# Results
The most common products are daily superfoliant and microfoliant, suggesting that most customers have common skin issues.<br>
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/da481380-1f56-4e0c-9a97-b500f4741509)<br>

The sentiment analysis shows that Dermalogica has many benefits for its users, such as being a good face cleanser that exfoliates the face and makes the face smoother. Most users feel that Dermalogica products are great at solving skin problems.<br>
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/b0ca8b5f-eb1d-4565-bcf0-b016eac712f6)<br>

The data is a highly unbalanced dataset with 90% positive reviews.
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/06c67f12-0a84-4b46-8d0c-75c594af8676)<br>

After balancing the data with SMOTE, the model shows better performance with the balanced data than with the imbalanced data.<br>
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/b5a52fe2-a1b8-4a93-8a3d-186339085f0e)<br>
The **Random Forest Classifier** performed better with a higher accuracy score, while **Logistic Regression** gave a higher ROC score.<br>
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/77442454-f7af-46c1-96e3-8798ff200b1f)

# Conclusion
Most users feel that Dermalogica products are great at solving skin problems. But there are some users who don't like Dermalogica products.
