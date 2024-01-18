# Leaderboard

| Model Name | Score | Date Tested |
|------------|-------|-------------|
| gpt-4 | 85.71% | 2024-01-15 |
| agronomYi-hermes-34b | 79.05% | 2024-01-15 |
| mistral-medium | 77.14% | 2024-01-15 |
| nous-hermes-yi-34b | 76.19% | 2024-01-15 |
| mixtral-8x7b-instruct | 72.38% | 2024-01-15 |
| claude-2 | 72.38% | 2024-01-15 |
| yi-34b-chat | 71.43% | 2024-01-15 |
| norm | 69.52% | 2024-01-17 |
| openhermes-2.5-mistral-7b | 69.52% | 2024-01-15 |
| gpt-3.5-turbo | 67.62% | 2024-01-15 |
| mistral-7b-instruct | 61.9% | 2024-01-15 |



# What is this?
We are benchmarking the ability for different models to give correct answers to Agronomy questions. This is a simple, 98 multiple-choice question benchmark today, and I plan to make it more complete and challenging in the future.

# Why?
When building new models for agriculture, it's important to know if your model is getting better or worse. This is a simple benchmark to help us determine if we are improving the agronomic ability of new models and by how much.

# Roadmap
1. Make it harder! These are fairly basic questions. We should add short and long answer questions (to be evaluated against example correct answers)
2. Add questions for international regions
3. Add more models to the leaderboard


# Updates
## 2024-01-17
1. Updated benchmark questions to remove incorrectly formed questions (for eaxample, the most missed question across all models was "e. both symptoms occur across the field and stunted roots", which is clearly not a properly formed question). 

2. Included chat prompt templates for models that require chat templates. 

3. Reran benchmark against all models after fixes in place and updated leaderboard.

