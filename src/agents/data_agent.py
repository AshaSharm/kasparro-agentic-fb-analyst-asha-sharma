"""
Data Agent for Kasparro Agentic FB Analyst
Handles all data loading, cleaning, standardization, and summary statistics.
Output is a clean DataFrame plus relevant summaries for downstream agents.
"""

import pandas as pd
import numpy as np
from pathlib import Path

class DataAgent:
    def __init__(self, config):
        self.config = config
        self.df = None
    
    def load_and_preprocess(self):
        """Main method: loads raw CSV and applies all preprocessing steps."""
        path = self.config['data_path']
        self.df = pd.read_csv(path)
        self._basic_cleaning()
        summary = self._summarize()
        return self.df, summary

    def _basic_cleaning(self):
        """Clean column types, names, and standardize all fields."""
        df = self.df

        # Standardize column names
        df.columns = [col.lower().strip() for col in df.columns]

        # Convert date column
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Standardize string/categorical columns
        cat_cols = ['campaign_name', 'adset_name', 'creative_type', 
                    'audience_type', 'platform', 'country']
        for col in cat_cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.lower().str.strip()

        # Clean numeric columns and handle errors
        num_cols = ['spend', 'impressions', 'clicks', 'purchases', 'revenue', 'ctr', 'roas']
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # Drop rows with null or zero-critical data
        df = df.dropna(subset=['spend', 'impressions', 'clicks', 'revenue'])
        df = df[(df['spend'] > 0) & (df['impressions'] > 0)]

        # Recalculate metrics for integrity
        df['ctr'] = df['clicks'] / df['impressions']
        df['roas'] = df['revenue'] / df['spend']

        # Drop or fill NaN and infinite values (after calculation)
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['ctr', 'roas'])

        # Update self.df
        self.df = df

    def _summarize(self):
        """Create summary: date stats, overall metrics, recent and low-CTR campaigns."""
        df = self.df
        # Define 7-day sliding windows
        max_date = df['date'].max()
        recent_7 = df[df['date'] >= max_date - pd.Timedelta(days=7)]
        prev_7 = df[(df['date'] < max_date - pd.Timedelta(days=7)) & 
                    (df['date'] >= max_date - pd.Timedelta(days=14))]

        # Calculate campaign-level CTR for low-CTR identification
        low_ctr_threshold = self.config.get('low_ctr_threshold', 0.01)
        campaign_agg = df.groupby('campaign_name').agg(
            mean_ctr=('ctr', 'mean'),
            total_spend=('spend', 'sum'),
            creative_message=('creative_message', lambda x: x.mode()[0] if len(x) else "")
        ).reset_index()
        low_ctr_campaigns = campaign_agg[campaign_agg['mean_ctr'] < low_ctr_threshold].copy()

        summary = {
            'total_rows': len(df),
            'date_range': {
                'start': df['date'].min().strftime('%Y-%m-%d'),
                'end': df['date'].max().strftime('%Y-%m-%d')
            },
            'overall_metrics': {
                'total_spend': float(df['spend'].sum()),
                'total_revenue': float(df['revenue'].sum()),
                'mean_roas': float(df['roas'].mean()),
                'mean_ctr': float(df['ctr'].mean()),
                'total_purchases': int(df['purchases'].sum())
            },
            'recent_7_days': {
                'mean_roas': float(recent_7['roas'].mean()) if len(recent_7) else 0,
                'mean_ctr': float(recent_7['ctr'].mean()) if len(recent_7) else 0,
                'total_spend': float(recent_7['spend'].sum()) if len(recent_7) else 0
            },
            'previous_7_days': {
                'mean_roas': float(prev_7['roas'].mean()) if len(prev_7) else 0,
                'mean_ctr': float(prev_7['ctr'].mean()) if len(prev_7) else 0
            },
            'campaigns_count': df['campaign_name'].nunique(),
            'creative_types_dist': df['creative_type'].value_counts().to_dict(),
            'platforms_dist': df['platform'].value_counts().to_dict(),
            'low_ctr_campaigns': low_ctr_campaigns.to_dict('records')
        }
        return summary

# ---- LangChain Integration ---- #
from langchain_core.runnables import RunnableLambda

def get_data_agent(config):
    agent = DataAgent(config)
    def summarize(plan):
        # plan param is unused—kept for pattern compatibility
        df, summary = agent.load_and_preprocess()
        return summary
    return RunnableLambda(summarize)
