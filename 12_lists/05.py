## 05 - Filter
scores = [96, 47, 113, 89, 100, 102]
# count = 0
# for score in scores:
#     if score >= 100:
#         count += 1

high_scores = [score for score in scores if score >= 100]
count = len(high_scores)
        
print(count)
