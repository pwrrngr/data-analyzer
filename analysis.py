import pandas as pd

# Social media influencer engagement dataset
data = {
    'username': ['influencer_01', 'influencer_02', 'influencer_03', 
                 'influencer_04', 'influencer_05', 'influencer_06', 
                 'influencer_07', 'influencer_08', 'influencer_09', 
                 'influencer_10'],
    'platform': ['Instagram', 'TikTok', 'Instagram', 'YouTube', 
                 'TikTok', 'Instagram', 'YouTube', 'TikTok', 
                 'Instagram', 'YouTube'],
    'followers': [15000, 34000, 8900, 22000, 51000,
                  7800, 31000, 45000, 9200, 6700],
    'engagement_rate': [8.5, 4.2, 6.7, 9.1, 2.3,
                        5.8, 9.8, 3.4, 7.2, 5.1]
}

# Load into DataFrame
df = pd.DataFrame(data)
print("Dataset loaded:")
print(df)
print()

# Filter high follower accounts (over 10,000)
high_followers = df[df['followers'] > 10000]
print("High follower accounts:")
print(high_followers)
print()

# Sort by engagement rate highest to lowest
top_engagement = df.sort_values('engagement_rate', ascending=False)
print("Top engagement rates:")
print(top_engagement[['username', 'platform', 'engagement_rate']])
print()

# Group by platform - count influencers per platform
platform_summary = df.groupby('platform')['username'].count().reset_index()
platform_summary.columns = ['platform', 'influencer_count']
print("Influencers by platform:")
print(platform_summary.sort_values('influencer_count', ascending=False))
print()

# Flag high engagement accounts
df['engagement_level'] = df['engagement_rate'].apply(
    lambda x: 'HIGH' if x >= 7.0 else 'LOW'
)
print("Engagement level flags:")
print(df[['username', 'platform', 'engagement_rate', 'engagement_level']])
print()

# Export clean report
df.to_csv('influencer_report.csv', index=False)
print("Report exported to influencer_report.csv")
