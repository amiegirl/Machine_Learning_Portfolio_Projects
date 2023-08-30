# Introduction
This app is designed to make ordering meals from local restaurants in Lagos, Nigeria, easy for the user.
This app recommends products to users and estimates the real-time delivery of products.

# Problem Statement
An inaccurate delivery time and the absence of product suggestions can lead to customer dissatisfaction and to low sales for businesses.

# Objectives
This app aim to provide a potential solution to estimate delivery in real time and offer tailored meal recommendations to enhace user satisfaction.

The restaurant and product information was gotten by web scraping. other information were generated randomly. The data was scrutinized to ensure it made logical sense.

# Featured Techniques
* EDA
* Linear Regression
* Random Forest Regression
* Decision Tree Regression

# Findings 
### **The count of place type shows that restaurants are more than cafe**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/2413b0f7-5a90-4efe-bbcb-5e94436fd4ed)


### **The count of product type shows that *snacks* are the most ordered product type**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/efd0dbfc-e7b0-4dbe-a7cc-f0b8bbf92454)


### **The order count shows the ten most common ordered products. *Chin Chin* had the highest order, followed by *Chicken Shawarma* and *Pound Cake*.**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/59d79e0f-9e0f-41ea-8dc3-dafbba1eed12)


### **Below shows the product types with the highest rating and the place they can be got. *Drinks from Rehobort restaurant* had the highest rating, followed by *Cuisine African Restaurant drinks* and *snacks from home cooking restaurant*.**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/cd267b1f-bc96-4ad8-9530-f0ab354a5024)


### **From the chart of places with the highest reviews. *Cafe One Yaba* got the highest reviews, followed by *La Pointe Cafe* and *My Coffee*.**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/125e1188-d306-4840-a870-a34bebfbe1aa)


### **Orders were highest in *december* which is a festive period**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/a266949e-c0e9-4c6c-8f4e-fbd57e2c17b6)


### **The scatter plot shows a positive relationship between distance and time taken, ie the longer the user distance to the restarant, the longer the estimated delivery time taken.**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/f86e6903-e28b-4220-b3cd-6c863613b2e5)


# Modelling
### **We develop models for predicting real time delivery of an order from different places. Three distinct machine learning models *Linear Regression*, *Random Forest Regression* and *Decision Tree Regression* were utilized to estimate delivery time**.

## Estimated Delivery Time Results
### **The model with the lowest *rmse* and best *accuracy* is *Linear Regression*.**
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/8814336d-b5c2-448d-bfcb-f35902f5e08a)

## Meal Recommendation
### **We used cosine similarity from *product description* and *product type* to recommend product to existing and new users. Used *product rating* to recommend best products and places to users.**

## Sample Result of a new user
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/aacde60f-76e1-434a-a27d-84c2e9aecec4)


## Sample Result of an existing user
![image](https://github.com/amiegirl/Machine_Learning_Portfolio_Projects/assets/81017006/634591b4-fad2-46e8-94bd-733a47adcc9c)
