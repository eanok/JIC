from itertools import combinations
import math
import psutil
import statistics
import time

start_time = time.time()
# STEP------------- 1
min_support_count =  4065

with open("onlineretail.txt", "r") as f:
    transactions = [line.strip().split() for line in f]

# find the count of each item in the transactions
item_counts = {}
for transaction in transactions:
    for item in transaction:
        item_counts[item] = item_counts.get(item, 0) + 1


# find the frequent items whose count is higher or equal to the minimum support count
frequent_items_counts = {item: count for item, count in item_counts.items() if count >= min_support_count}



# find the Infrequent items whose count is lower than the minimum support count
Infrequent_items_counts = {item: count for item, count in item_counts.items() if count < min_support_count}



# iterate over transactions and remove infrequent items
for i in range(len(transactions)):
    transactions[i] = [item for item in transactions[i] if item in frequent_items_counts]



#STEP------2
support_count_dict = {}
median_transactions=[]


for transaction in transactions:
    if len(transaction) <= 4:
        # Transactions with length less than or equal to 4
        for i in range(2, len(transaction) + 1):
            subsets = list(combinations(transaction, i))
            # Store the subsets with key value in the dictionary
            for subset in subsets:
                if subset in support_count_dict:
                    support_count_dict[subset] += 1
                else:
                    support_count_dict[subset] = 1
                        
    else:
        # Transactions with length greater than 4
        n = len(transaction)

        #medaianTransactions
        median_transactions.append(transaction)  

        
        median = math.ceil(len(transaction)/2)
        front_part = transaction[:median]
        for j in range(2,median+1):
            subsets = list(combinations(front_part, j))
            # Store the subsets with key value in the dictionary
            for subset in subsets:
                if subset in support_count_dict:
                    support_count_dict[subset] += 1
                else:
                    support_count_dict[subset] = 1
# print(median_transactions)        
                   

# Create a new dictionary to store the unique subsets and their support counts
unique_subsets = {}
for subset, count in support_count_dict.items():
    if subset not in unique_subsets:
        unique_subsets[subset] = count
# print('Unique subsets with support counts:')
# print(unique_subsets)




frequent_itemsets={}
for subset, count in unique_subsets.items():
    if count >= min_support_count:
        frequent_itemsets[subset] = count      


infrequent_itemsets={}
for subset, count in unique_subsets.items():
    if count < min_support_count:
        infrequent_itemsets[subset] = count 


#step-------------------- 4
current = []

for i in range(len(median_transactions)):
    for subset in combinations(median_transactions[i], len(median_transactions[i])-1):
        if not any(set(itemset).issubset(set(subset)) for itemset in infrequent_itemsets):
            current.append(median_transactions[i])
            break
for i in current:
    if tuple(i) in frequent_itemsets:
        frequent_itemsets[tuple(i)] += 1
    else:
        frequent_itemsets[tuple(i)] = 1

#part 1
for i in range(len(median_transactions)):
    n = len(median_transactions[i])
    m = math.ceil(len(median_transactions[i])/2)
    for subset in combinations(median_transactions[i], len(median_transactions[i])-1):
        is_subset = False
        for item_set in infrequent_itemsets:
            if set(item_set).issubset(set(subset)):
                is_subset = True
                break
        if not is_subset:
            if subset in frequent_itemsets:
                frequent_itemsets[subset] += 1
            else:
                frequent_itemsets[subset] = 1            
#part 2
            if len(subset) != 2:
                # print('subset', subset)
                for subset_2 in combinations(subset, len(subset)-1):
                    if not any(set(itemset).issubset(set(subset_2)) for itemset in infrequent_itemsets):
                        if subset_2 in frequent_itemsets:
                            frequent_itemsets[subset_2] += 1
                        else:
                            frequent_itemsets[subset_2] = 1
                        
#part 3 
                        if len(subset_2) != 2:
                            for subset_3 in combinations(subset_2, len(subset_2)-1):
                                if not any(set(itemset).issubset(set(subset_3)) for itemset in infrequent_itemsets):
                                    if subset_3 in frequent_itemsets:
                                        frequent_itemsets[subset_3] += 1
                                    else:
                                        frequent_itemsets[subset_3] = 1
#part 4
                                    if len(subset_3) != 2:
                                        for subset_4 in combinations(subset_3, len(subset_3)-1):
                                            if not any(set(itemset).issubset(set(subset_4)) for itemset in infrequent_itemsets):
                        
                                                if subset_4 in frequent_itemsets:
                                                    frequent_itemsets[subset_4] += 1
                                                else:
                                                    frequent_itemsets[subset_4] = 1
#part 5
                                                if len(subset_4) != 2:
                                                    for subset_5 in combinations(subset_4, len(subset_4)-1):
                                                        if not any(set(itemset).issubset(set(subset_5)) for itemset in infrequent_itemsets):
                                                            
                                                            if subset_5 in frequent_itemsets:
                                                                frequent_itemsets[subset_5] += 1
                                                            else:
                                                                frequent_itemsets[subset_5] = 1
#part 6 
                                                            if len(subset_5) != 2:
                                                                for subset_6 in combinations(subset_5, len(subset_5)-1):
                                                                    if not any(set(itemset).issubset(set(subset_6)) for itemset in infrequent_itemsets):
                                                            
                                                                        if subset_6 in frequent_itemsets:
                                                                            frequent_itemsets[subset_6] += 1
                                                                        else:
                                                                            frequent_itemsets[subset_6] = 1
                                        


#if the maximum length of the transaction is greater than 8 increase part 4 
                    
#part 4 (if needed)
final_freq_itemsets={}
for subset, count in frequent_itemsets.items():
    if count >= min_support_count: 
        final_freq_itemsets[subset] = 'FI'


# for subset, count in frequent_itemsets.items():
#     if count < min_support_count:
#         if subset in infrequent_itemsets:
#             infrequent_itemsets[subset] += count
#         else:
#             infrequent_itemsets[subset] = count

# for subset, count in infrequent_itemsets.items():
#     if count >= min_support_count: 
#         final_freq_itemsets[subset] = count

print('----------------------------Frequent items------------------------------')
print(frequent_items_counts)
# print('------------------------------------------------------------------------')
print(final_freq_itemsets)
print('----------------------------Frequent itemsets---------------------------')

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")










