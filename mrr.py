import json


def calculate_mrr_at_10(ranked_lists):
    #print(len(ranked_lists))
    #print('------')
    total_mrr = 0.0
    num_queries = len(ranked_lists)

    for ranked_list in ranked_lists:
        reciprocal_rank = 0.0

        for i, document in enumerate(ranked_list[:10], start=1):
            if document == 1:
                reciprocal_rank = 1.0 / i
                break

        total_mrr += reciprocal_rank

    # Calculate the mean MRR at 10
    mean_mrr_at_10 = total_mrr / num_queries

    return mean_mrr_at_10


def calculate_recalls(ranked_lists, max_rank=100):
    # Initialize an array to hold recall values for each rank from 1 to max_rank
    recalls = [0.0] * max_rank
    num_queries = len(ranked_lists)

    # Calculate recall for each rank
    for rank in range(1, max_rank + 1):
        all_found = 0
        for ranked_list in ranked_lists:
            # Check if the relevant document (marked as '1') is within the top 'rank' positions
            if 1 in ranked_list[:rank]:
                all_found += 1
        # Calculate recall for the current rank
        recall = all_found / num_queries
        recalls[rank - 1] = recall * 100

    return recalls


def calculate_recall_at_10(ranked_lists, rank):
    total_recall = 0.0
    num_queries = len(ranked_lists)
    #print(num_queries)
    all_found = 0
    for ranked_list in ranked_lists:
        #print(len(ranked_list))
        if 1 in ranked_list[:rank]:
            all_found += 1
        recall = all_found / num_queries

    # Calculate the mean Recall at 10

    return recall


def count_hit_num(ranked_lists):
    hit_num_list = []
    for ranked_list in ranked_lists:
        hit_num = 0
        if 1 in ranked_list[:100]:
            hit_num += 1
        hit_num_list.append(hit_num)

    return hit_num_list


# Example usage:
# Assuming you have a list of ranked documents for each query, each with a boolean 'is_relevant' field
# Replace this with your actual data structure


# UPR
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/baseline/NQ-UPR-DPR.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/baseline/NQ-UPR-MSS_DPR.json', 'r'))

# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/baseline/TQA-UPR-DPR.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/baseline/TQA-UPR-MSS.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/passage_rank_result/gpt_evaluate-v1-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/SQUAD/MSS-DPR/passage_rerank_result/SQUAD-v1-label-Prank.json','r'))


jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/baseline/SQUAD-UPR-MSS_DPR.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/MSS-DPR/passage_rerank_result/TQA-v1-label-Prank.json','r'))


# NQ
# bm25
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/bm25/NQ-bm25.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/bm25/bm25-evidence.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/bm25/passage_rank_result/test-v1-2-Prank.json','r'))

# contriever
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/contriever/test-passage-evidence.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/contriever/contriever-erank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/contriever/passage_rerank_result/my_evidence-Prank.json','r'))


# MSS
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS/NQ-mss.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS/mss-erank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/baseline/NQ-UPR-MSS.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS/passage_rank_result/my_evidence-Prank.json','r'))





#DPR
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/DPR/dpr.json','r'))
#DPR-ERANK
#jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/DPR/dpr-erank.json','r'))
#DPR-ERANK(my)
#jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/my-test/dpr-erank.json', 'r'))



#MSS-DPR
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/mss-dpr.json','r'))
#MSS-DPR-erank
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/mss-dpr-erank.json','r'))
#ours
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/passage_rank_result/gpt_result-A-label-3-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/mss-dpr-erank.json', 'r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/passage_rank_result/gpt_result-A-label-3-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/passage_rank_result/my_35t-com-v5-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/passage_rank_result/gpt_evaluate-v1-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/SQUAD/MSS-DPR/passage_rerank_result/SQUAD-v1-label-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/passage_rank_result/gpt_result-A-0-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/MSS-DPR/passage_rerank_result/TQA-v1-label-Prank.json','r'))


#DPR
#jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/1_my_work/dataset/NQ/dpr_nq-test_tag(1000).json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/DPR/passage_rerank_result/my_evidence-Prank.json', 'r'))


# TQA
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/bm25/TQA-bm25.json','r'))

# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/contriever/TQA-contriever.json','r'))

# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/mss/TQA-mss.json','r'))



# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/DPR/TQA-dpr.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/DPR/1-dpr_erank-test.json','r'))

# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/MSS-DPR/TQA.json','r'))

# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/MSS-DPR/TQA.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/MSS-DPR/passage_rerank_result/TQA-erank.json','r'))
# jfile = json.load(open('//mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/TQA/MSS-DPR/passage_rerank_result/TQA-v1-label-Prank.json','r'))


# SQUAD
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/SQUAD/MSS-DPR/passage_rerank_result/SQUAD-label-Prank.json','r'))
# jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/SQUAD/MSS-DPR/passage_rerank_result/SQUAD-label-1-Prank.json','r'))
jfile = json.load(open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/SQUAD/MSS-DPR/passage_rerank_result/SQUAD-add_evidence-Prank.json','r'))


ranked_lists = []
hit_list = []
write_list = []
label_list = []

for i, line in enumerate(jfile):

    ranked_list = []
    answers = line["answers"]
    try:
        line["ctxs"] = sorted(line["ctxs"], key=lambda x: x['score'], reverse=True)
    except:
        x = 1
    all_labels = 0

    hit_num = 0
    question = line["question"]
    # print(len(line["ctxs"]))
    for j, context in enumerate(line["ctxs"]):
        label = 0
        if "has_answer" not in context.keys():
            for answer in answers:
                if answer in context["text"]:
                    label = 1
                    all_labels += 1
                    if j < 100:
                        hit_num += 1
                    # hit_num += 1
        else:
            if context["has_answer"]:
                label = 1
                all_labels += 1

                if j < 100:
                    hit_num += 1
                # hit_num += 1
        ranked_list.append(label)

        if context["has_answer"] and label == 0:
            print(context["text"])
            print(answers)
            print('-----')

    hit_list.append(hit_num)
    label_list.append(all_labels)
    ranked_lists.append(ranked_list)

    # if hit_num == 0 and all_labels != 0:
    #     write_dic = {}
    #
    #     write_dic['id'] = i + 1
    #     write_dic['question'] = question
    #     write_dic['answers'] = line["answers"]
    #     evidence = ""
    #     if line["selected_evidences"]:
    #         evidence = next(iter(line["selected_evidences"]))
    #     write_dic['selected_evidences'] = evidence
    #     write_list.append(write_dic)

# with open('1test comparison results/no_hit-100(8967)-2.json', 'w') as f:
#     json.dump(write_list, f, indent=4)

# print(label_list)
print("所有段落不包含答案：", label_list.count(0))
print("前100个中不包含答案：", hit_list.count(0))
print("真未命中：", len(write_list))
mean_mrr_at_10 = calculate_mrr_at_10(ranked_lists)
recall_1 = calculate_recall_at_10(ranked_lists, 1)
recall_5 = calculate_recall_at_10(ranked_lists, 5)
recall_10 = calculate_recall_at_10(ranked_lists, 10)
recall_20 = calculate_recall_at_10(ranked_lists, 20)
recall_100 = calculate_recall_at_10(ranked_lists, 100)
recalls = calculate_recalls(ranked_lists)
#print(hit_list)

print(f"Mean Reciprocal Rank at 10: {mean_mrr_at_10:.4f}")
print(f"Recall at 1: {recall_1:.4f}")
print(f"Recall at 5: {recall_5:.4f}")
print(f"Recall at 10: {recall_10:.4f}")
print(f"Recall at 20: {recall_20:.4f}")
print(f"Recall at 100: {recall_100:.4f}")
# print(f"hit num: {count_hit_num(ranked_lists)}")


#print(recalls)
