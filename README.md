# Indian Politics: Mann Ki Baat Sentiment Analysis and Topic Modeling

### Project Overview

This project aims to analyze textual data and perform sentiment analysis on the public relations campaign "Mann Ki Baat." Launched by Indian Prime Minister Narendra Modi, this radio program has been a significant part of Indian media since October 3, 2014. We use Natural Language Processing (NLP) techniques to gain insights into the content and public opinion surrounding this campaign.

## Components

1. **Data Extraction**
   - **Speeches**: Scraped from [government website - PM India](https://www.pmindia.gov.in/en/mann-ki-baat/) using Beautiful Soup and Selenium.
   - **Tweets**: Extracted with `snscrape` for the hashtag `#MannKiBaat`.

2. **Data Pre-processing**
   - Techniques for cleaning and preparing data, including handling missing values and noise.

3. **Topic Modeling**
   - **LDA**: Used to identify topics in speeches with Gensim and Mallet models.
   - **Improvements**: Frequency Filter, POS Tag Filter, and Batch Wise LDA.
   <img width="650" alt="image" src="https://github.com/user-attachments/assets/ed4787f7-b101-46c1-a203-9d1beb9af62c">


4. **Sentiment Analysis**
   - **SentiWordNet**: Lexicon-based approach for sentiment scoring.
   - **Naive Bayes & SVM**: Supervised algorithms for classifying tweet sentiments.
   <img width="675" alt="image" src="https://github.com/user-attachments/assets/944eecd8-2e47-41ae-ba6c-e088776d4c99">


5. **Results Interpretation**
   - Visualization and analysis of topics and sentiment distribution.
  

## Methodology

1. **Data Extraction**:
   - Web scraping for speeches and `snscrape` for tweets.
2. **Data Pre-processing**:
   - Clean and prepare data for analysis.
3. **Topic Modeling**:
   - Apply LDA to extract topics.
4. **Sentiment Analysis**:
   - Use SentiWordNet and machine learning algorithms to analyze sentiments.
5. **Results Interpretation**:
   - Visualize and analyze topic and sentiment data.

<img width="553" alt="image" src="https://github.com/user-attachments/assets/48eb2aa3-c428-4d04-a4d7-5fd15c4459be">

## Visualizations 
<img width="500" alt="image" src="https://github.com/user-attachments/assets/6f369735-3894-4bcb-80ab-d79d88de59f4">  <img width="500" alt="image" src="https://github.com/user-attachments/assets/792375f7-fe61-4885-badf-877a0a34f2e3">
<img width="688" alt="image" src="https://github.com/user-attachments/assets/fada8c76-baad-4815-b532-9de786fb6314">
<img width="688" alt="image" src="https://github.com/user-attachments/assets/36d0d8d6-3133-41c9-a746-d413adcc2f51">



## Conclusion

The combined use of LDA for topic modeling and sentiment analysis provides valuable insights into the "Mann Ki Baat" campaign. The analysis shows a broad range of topics covered and public perception. Overall, the campaign has been successful, offering a platform for citizen feedback and improving government-public interaction.



<br><br>
### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Anushree176/IndianPolitics_TopicModelling_SentimentAnalysis.git

2. Install dependencies:
    ```bash
    pip install beautifulsoup4 selenium snscrape nltk gensim mallet scikit-learn matplotlib pandas

3. Download and configure the web driver for Selenium (e.g., ChromeDriver).

### Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
- Beautiful Soup, Selenium
- snscrape
- Gensim Mallet
- Scikit-learn , NLTK
- SIES Graduate School of Technology
