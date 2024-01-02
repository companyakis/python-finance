import yfinance as yf
import pandas as pd


#Turkiye Garanti Bankasi A.S. (GARAN.IS)

garanti = yf.download("GARAN.IS", start = "2000-01-01")
