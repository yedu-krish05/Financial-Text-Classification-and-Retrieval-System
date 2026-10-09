# AI Case Study: Knowledge Base for Financial Article Analysis System

**Course:** Master of Computer Applications (MCA)  
**Topic:** Knowledge Representation in Artificial Intelligence   

---

## 1. Introduction
This case study outlines the foundational **Knowledge Base (KB)** for an AI-driven Financial Article Classifier & Q&A System. In Artificial Intelligence, building a robust knowledge base is critical for inference engines and expert systems. 

As per the project requirements, a knowledge base consisting of **25 core facts and rules** pertaining to financial markets and text classification algorithms has been established. These facts are represented using the **four primary Knowledge Representation techniques** in AI:
1. First-Order Predicate Logic (FOPL)
2. Semantic Networks
3. Frames
4. Production Rules (IF-THEN)

---

## 2. The Facts (Domain Knowledge)
The system's intelligence is built upon the following 25 facts spanning finance and natural language processing:
1. A stock represents ownership in a company.
2. A bond represents a debt instrument.
3. Inflation decreases purchasing power.
4. An increase in company earnings typically increases the stock price.
5. Rising interest rates cause bond prices to fall.
6. A bullish market indicates rising prices.
7. A bearish market indicates falling prices.
8. Dividends are paid to company shareholders.
9. High volatility implies high investment risk.
10. Diversification reduces portfolio risk.
11. A recession is defined as two consecutive quarters of negative GDP.
12. The central bank controls interest rates.
13. Mutual funds pool money from multiple investors.
14. Articles containing "revenue" and "earnings" are classified as Corporate Finance.
15. Articles containing "inflation" and "rates" are classified as Macroeconomics.
16. TF-IDF is used for feature extraction from text.
17. Naive Bayes is a probabilistic classification algorithm.
18. Cosine Similarity measures the semantic distance between vectors.
19. NLTK performs sentence tokenization.
20. Trafilatura is used for web scraping and text extraction.
21. Streamlit provides the web-based graphical user interface.
22. A cosine similarity score > 0.5 indicates high passage relevance.
23. An IPO (Initial Public Offering) makes a private company public.
24. GDP measures total economic output.
25. Unstructured HTML is cleaned using Regular Expressions.

---

## 3. Representation 1: First-Order Predicate Logic (FOPL)
*Logic representation allows the system to use formal mathematical logic to deduce new truths.*

1. `Represents(Stock, Ownership)`
2. `IsA(Bond, DebtInstrument)`
3. `Decreases(Inflation, PurchasingPower)`
4. `∀x (Company(x) ∧ Increases(Earnings, x) → Increases(StockPrice, x))`
5. `∀x (InterestRates(x) ∧ Rising(x) → Falling(BondPrices))`
6. `Indicates(BullMarket, RisingPrices)`
7. `Indicates(BearMarket, FallingPrices)`
8. `PaidTo(Dividends, Shareholders)`
9. `Implies(HighVolatility, HighRisk)`
10. `Reduces(Diversification, PortfolioRisk)`
11. `∀x (NegativeGDP(x, 2_Quarters) → IsRecession(x))`
12. `Controls(CentralBank, InterestRates)`
13. `Pools(MutualFund, InvestorMoney)`
14. `∀a (Article(a) ∧ Contains(a, "revenue") → Classify(a, CorporateFinance))`
15. `∀a (Article(a) ∧ Contains(a, "inflation") → Classify(a, Macroeconomics))`
16. `UsedFor(TF_IDF, FeatureExtraction)`
17. `IsA(NaiveBayes, ClassificationAlgorithm)`
18. `Measures(CosineSimilarity, SemanticDistance)`
19. `Performs(NLTK, Tokenization)`
20. `GreaterThan(SimilarityScore, 0.5) → Relevant(Passage)`

---

## 4. Representation 2: Semantic Networks
*Semantic networks use nodes (objects/concepts) and directed edges (relationships) to build a graph of knowledge.*

- **Stock** `[is_a]` **Asset**
- **Stock** `[represents]` **Ownership**
- **Company** `[issues]` **Stock**
- **Company** `[reports]` **Earnings**
- **Shareholder** `[receives]` **Dividends**
- **Bond** `[is_a]` **DebtInstrument**
- **Inflation** `[decreases]` **PurchasingPower**
- **CentralBank** `[controls]` **InterestRates**
- **TF_IDF** `[used_for]` **FeatureExtraction**
- **TF_IDF** `[input_to]` **NaiveBayes**
- **CosineSimilarity** `[measures]` **SemanticDistance**
- **Streamlit** `[provides]` **WebUI**
- **NLTK** `[performs]` **SentenceTokenization**
- **MutualFund** `[pools]` **Money**
- **IPO** `[stands_for]` **InitialPublicOffering**

---

## 5. Representation 3: Frames (Object-Oriented Slots)
*Frames represent knowledge by grouping properties, behaviors, and attributes (slots) into structured entities.*

**Frame: Financial_Instrument**
- `Subclasses:` Stock, Bond

**Frame: Stock**
- `Is-A:` Financial_Instrument
- `Represents:` Corporate Ownership
- `Yields:` Dividends
- `Risk_Level:` Variable / High

**Frame: Bond**
- `Is-A:` Financial_Instrument
- `Represents:` Corporate/Government Debt
- `Yields:` Fixed Interest
- `Risk_Level:` Low

**Frame: Market_State**
- `Instances:` BullMarket, BearMarket

**Frame: BullMarket**
- `Is-A:` Market_State
- `Trend:` Rising
- `Sentiment:` Positive

**Frame: Article_Classifier_Model**
- `Type:` Multinomial Naive Bayes
- `Input_Format:` TF-IDF Vector Matrix
- `Output_Format:` Category Label
- `Libraries_Used:` Scikit-Learn

**Frame: RAG_Engine**
- `Similarity_Metric:` Cosine Similarity
- `Tokenizer:` NLTK Punkt
- `Relevance_Threshold:` > 0.5

---

## 6. Representation 4: Production Rules (IF-THEN)
*Production rules form the basis of expert system inference engines using conditional logic.*

- **R1:** IF `asset_type == "Stock"` THEN `asset_represents = "Ownership"`
- **R2:** IF `asset_type == "Bond"` THEN `asset_represents = "Debt"`
- **R3:** IF `market_trend == "Rising"` THEN `market_state = "Bullish"`
- **R4:** IF `market_trend == "Falling"` THEN `market_state = "Bearish"`
- **R5:** IF `company_earnings == "Increasing"` THEN `stock_price_prediction = "Up"`
- **R6:** IF `interest_rates == "Rising"` THEN `bond_prices = "Falling"`
- **R7:** IF `article_keywords` INCLUDE ("earnings", "revenue") THEN `category = "Corporate Finance"`
- **R8:** IF `article_keywords` INCLUDE ("interest rates", "inflation") THEN `category = "Macroeconomics"`
- **R9:** IF `algorithm == "Naive Bayes"` THEN `task = "Classification"`
- **R10:** IF `algorithm == "Cosine Similarity"` THEN `task = "Semantic Matching"`
- **R11:** IF `similarity_score > 0.5` THEN `passage_relevance = "High"`
- **R12:** IF `similarity_score <= 0.5` THEN `passage_relevance = "Low"`
- **R13:** IF `text_source == "URL"` THEN `preprocessing = "Trafilatura Web Scraping"`
- **R14:** IF `gdp_growth < 0` FOR `2_quarters` THEN `economic_state = "Recession"`
- **R15:** IF `risk_tolerance == "Low"` THEN `recommend = "Bonds"`
- **R16:** IF `risk_tolerance == "High"` THEN `recommend = "Stocks"`
- **R17:** IF `strategy == "Diversification"` THEN `portfolio_risk = "Reduced"`
- **R18:** IF `ui_framework == "Streamlit"` THEN `application_type = "Web App"`

---

## 7. Conclusion
By organizing 25 distinct facts into Logic, Semantic Networks, Frames, and Production Rules, we establish a rigid knowledge base. This allows the AI application not only to classify articles mathematically via Machine Learning but also lays the groundwork for adding a rule-based Expert System capable of symbolic reasoning in the financial domain.
